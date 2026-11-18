"""tbdtrack_sphinx - TBD tracking with a summary table for Sphinx.

Sphinx counterpart of tbdtrack.sty (LaTeX). See tbdtrack_sphinx_README.md.

    :tbd:`word | details | target date | custom ID`   (details, date, ID optional)
    .. tbd:: word            (block form, body = details; options :date:, :id:)
    .. tbdtable::            (the TBD table)
"""

import csv
import json
import os

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

__version__ = "2026.11.17"
logger = logging.getLogger(__name__)

CSS = """<style>
.tbd-word {color: #c00; font-weight: bold;}
.tbd-id, .tbd-id:visited {color: #c00; font-size: 70%; font-family: monospace;}
</style>"""


class tbd_marker(nodes.Inline, nodes.TextElement):
    """Placeholder for a TBD in the text; resolved per builder."""


class tbdtable(nodes.General, nodes.Element):
    """Placeholder for the TBD table."""


def _tbd_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    parts = [p.strip() for p in text.split("|")]
    parts += [""] * (4 - len(parts))
    word, details, date, custom_id = parts[:4]
    return [_marker(word, details, date, custom_id)], []


def _marker(word, details, date, custom_id):
    node = tbd_marker(word, word)
    node["details"] = details
    node["date"] = date
    node["custom_id"] = custom_id
    return node


class TbdDirective(Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {"date": directives.unchanged, "id": directives.unchanged}

    def run(self):
        marker = _marker(
            self.arguments[0],
            " ".join(line.strip() for line in self.content).strip(),
            self.options.get("date", "").strip(),
            self.options.get("id", "").strip(),
        )
        return [nodes.paragraph("", "", marker)]


class TbdTableDirective(Directive):
    def run(self):
        env = self.state.document.settings.env
        env.tbd_table_doc = env.docname
        return [tbdtable()]


def _section(node):
    """(title, anchor id) of the section containing the node."""
    while node is not None:
        if isinstance(node, nodes.section):
            return node[0].astext(), (node["ids"] or [""])[0]
        node = node.parent
    return "", ""


def _collect(app, doctree):
    env = app.env
    if not hasattr(env, "tbd_items"):
        env.tbd_items = {}
    items = []
    for marker in doctree.findall(tbd_marker):
        title, anchor = _section(marker)
        items.append(
            {
                "word": marker.astext(),
                "details": marker["details"],
                "date": marker["date"],
                "custom_id": marker["custom_id"],
                "section": title,
                "anchor": anchor,
            }
        )
        marker["tbd_index"] = len(items) - 1
        marker["tbd_doc"] = env.docname
    env.tbd_items[env.docname] = items


def _purge(app, env, docname):
    getattr(env, "tbd_items", {}).pop(docname, None)


def _merge(app, env, docnames, other):
    if not hasattr(env, "tbd_items"):
        env.tbd_items = {}
    env.tbd_items.update(getattr(other, "tbd_items", {}))
    if getattr(other, "tbd_table_doc", None):
        env.tbd_table_doc = other.tbd_table_doc


def _outdated(app, env, added, changed, removed):
    """Running numbers and the table depend on all documents: re-write them."""
    if not (added or changed or removed):
        return []
    docs = set(getattr(env, "tbd_items", {}))
    if getattr(env, "tbd_table_doc", None):
        docs.add(env.tbd_table_doc)
    return list(docs - set(removed))


def _doc_order(env):
    order, seen = [], set()

    def walk(doc):
        if doc in seen:
            return
        seen.add(doc)
        order.append(doc)
        for child in env.toctree_includes.get(doc, []):
            walk(child)

    walk(env.config.root_doc)
    order += sorted(set(env.tbd_items) - seen)
    return order


def _numbered(env):
    """All items in document order with running number and final ID."""
    abbrev = env.config.tbd_doc_abbrev
    result, n = [], 0
    for doc in _doc_order(env):
        for index, item in enumerate(getattr(env, "tbd_items", {}).get(doc, [])):
            n += 1
            entry = dict(item, doc=doc, index=index, n=n)
            entry["id"] = item["custom_id"] or f"TBD_{abbrev}_{n}"
            result.append(entry)
    return result


def _location(env, e):
    """Section title prefixed with its number (needs :numbered: in the toctree)."""
    numbers = env.toc_secnumbers.get(e["doc"], {})
    number = numbers.get("#" + e["anchor"]) or numbers.get("")
    title = e["section"] or e["doc"]
    return ".".join(map(str, number)) + " " + title if number else title


def _uri(builder, fromdoc, doc, anchor):
    return builder.get_relative_uri(fromdoc, doc) + "#" + anchor


def _raw(latex):
    return nodes.raw("", latex, format="latex")


def _marker_nodes(app, fromdoc, entry, table_doc):
    builder, word = app.builder, entry["word"]
    ident = entry["id"]
    if builder.format == "html":
        text = nodes.inline(word, word, classes=["tbd-word"], ids=[f"tbd-{entry['n']}"])
        if not table_doc:
            return [text]
        ref = nodes.reference(
            "", ident, refuri=_uri(builder, fromdoc, table_doc, f"tbdrow-{entry['n']}"),
            classes=["tbd-id"],
        )
        return [text, nodes.superscript("", "", nodes.Text("["), ref, nodes.Text("]"))]
    if builder.format == "latex":
        out = [_raw(rf"\phantomsection\label{{tbd:src:{entry['n']}}}{{\color{{red}}"),
               nodes.Text(word), _raw("}")]
        if table_doc:
            out += [_raw(rf"\textsuperscript{{\hyperref[tbd:row:{entry['n']}]{{\textcolor{{red}}{{["),
                    nodes.literal(ident, ident), _raw("]}}}")]
        return out
    return [nodes.Text(f"{word} [{ident}]")]


def _cell(*children):
    return nodes.entry("", nodes.paragraph("", "", *children))


def _table(app, fromdoc, entries):
    builder, env = app.builder, app.env
    widths = [22, 38, 14, 26]
    tgroup = nodes.tgroup(cols=4)
    for w in widths:
        tgroup += nodes.colspec(colwidth=w)
    header = nodes.row("", *[_cell(nodes.strong("", t)) for t in
                             ("ID", "Details", "Target date", "Location")])
    tgroup += nodes.thead("", header)
    body = nodes.tbody()
    for e in entries:
        if builder.format == "html":
            idcell = _cell(nodes.inline("", "", nodes.reference(
                "", e["id"], refuri=_uri(builder, fromdoc, e["doc"], f"tbd-{e['n']}")),
                ids=[f"tbdrow-{e['n']}"]))
            loc = _cell(nodes.reference(
                "", _location(env, e),
                refuri=_uri(builder, fromdoc, e["doc"], f"tbd-{e['n']}")))
        elif builder.format == "latex":
            idcell = _cell(_raw(rf"\phantomsection\label{{tbd:row:{e['n']}}}"
                                rf"\hyperref[tbd:src:{e['n']}]{{"),
                           nodes.literal(e["id"], e["id"]), _raw("}"))
            loc = _cell(nodes.Text(_location(env, e)),
                        _raw(rf", p.~\pageref{{tbd:src:{e['n']}}}"))
        else:
            idcell = _cell(nodes.Text(e["id"]))
            loc = _cell(nodes.Text(_location(env, e)))
        shown = nodes.emphasis(e["word"], e["word"])
        details = _cell(shown, nodes.Text(f": {e['details']}")) if e["details"] else _cell(shown)
        body += nodes.row("", idcell, details, _cell(nodes.Text(e["date"])), loc)
    tgroup += body
    return nodes.table("", tgroup, classes=["colwidths-given"])


def _resolve(app, doctree, fromdoc):
    env = app.env
    final = app.config.tbd_final
    table_doc = getattr(env, "tbd_table_doc", None)
    entries = _numbered(env)
    lookup = {(e["doc"], e["index"]): e for e in entries}

    for marker in list(doctree.findall(tbd_marker)):
        if final:
            marker.replace_self(nodes.Text(marker.astext()))
            continue
        entry = lookup[(marker["tbd_doc"], marker["tbd_index"])]
        marker.replace_self(_marker_nodes(app, fromdoc, entry, table_doc))

    for placeholder in list(doctree.findall(tbdtable)):
        if final:
            placeholder.parent.remove(placeholder)
        elif not entries:
            placeholder.replace_self(nodes.paragraph("", "No open TBD items."))
        else:
            placeholder.replace_self(_table(app, fromdoc, entries))


def _export(app, exception):
    path = app.config.tbd_export
    if exception or not path or app.config.tbd_final:
        return
    rows = [
        {"id": e["id"], "document": app.config.tbd_doc_abbrev, "text": e["word"],
         "details": e["details"], "target_date": e["date"], "location": _location(app.env, e)}
        for e in _numbered(app.env)
    ]
    target = os.path.join(app.outdir, path)
    with open(target, "w", newline="", encoding="utf-8") as fh:
        if path.endswith(".csv"):
            writer = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else ["id"])
            writer.writeheader()
            writer.writerows(rows)
        else:
            json.dump(rows, fh, indent=2, ensure_ascii=False)


def _html_context(app, pagename, templatename, context, doctree):
    if not app.config.tbd_final:
        context["metatags"] = context.get("metatags", "") + CSS


def setup(app):
    app.add_config_value("tbd_doc_abbrev", "DOC", "env")
    app.add_config_value("tbd_final", False, "env")
    app.add_config_value("tbd_export", None, "html")
    app.add_node(tbd_marker)
    app.add_node(tbdtable)
    app.add_role("tbd", _tbd_role)
    app.add_directive("tbd", TbdDirective)
    app.add_directive("tbdtable", TbdTableDirective)
    app.connect("doctree-read", _collect)
    app.connect("env-purge-doc", _purge)
    app.connect("env-merge-info", _merge)
    app.connect("env-get-outdated", _outdated)
    app.connect("doctree-resolved", _resolve)
    app.connect("html-page-context", _html_context)
    app.connect("build-finished", _export)
    return {"version": __version__, "parallel_read_safe": True, "parallel_write_safe": True}

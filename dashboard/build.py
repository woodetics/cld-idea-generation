#!/usr/bin/env python3
"""Build the Idea Vault dashboard from the repo's markdown files.

Usage (from the repo root):
    pip install markdown
    python3 dashboard/build.py

Writes:
    dashboard.html               full page you open in a browser (works offline)
    dashboard/build/artifact.html  same page without <html>/<head>/<body>, for publishing as a claude.ai artifact

To add a new lesson, drop a .md file into money-maker/ or claude-lab/ (or add a folder to GROUPS),
add a log entry to dashboard/updates.md, and run the script again.
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
DASH = ROOT / "dashboard"

# Order of the course: (folder, group label, page-id prefix)
GROUPS = [
    ("claude-lab", "Claude Lab", "claude-lab"),
    ("money-maker", "Money Maker", "money-maker"),
]

# Short labels for the sidebar. Files not listed fall back to their H1.
NAV_LABELS = {
    "claude-lab/README.md": "Overview",
    "claude-lab/00-max-plan-facts-and-rules.md": "Max plan and the rules",
    "claude-lab/01-raw-research-how-people-use-claude.md": "Research: how people use Claude",
    "claude-lab/02-earning-projects.md": "Earning projects",
    "claude-lab/03-gray-zone-projects.md": "Gray zone projects",
    "claude-lab/04-learning-path.md": "Learning path",
    "claude-lab/05-jarvis-and-ai-office-parked.md": "Jarvis and AI office (parked)",
    "money-maker/README.md": "Overview",
    "money-maker/00-start-here-broke-playbook.md": "Broke playbook (30 days)",
    "money-maker/01-research-raw-notes.md": "Research notes",
    "money-maker/02-claude-code-agent-services.md": "Claude Code services",
    "money-maker/03-video-and-shorts.md": "Video and Shorts",
    "money-maker/04-upskilling-and-fast-cash.md": "Upskilling and fast cash",
    "money-maker/05-github-repos-toolbox.md": "GitHub toolbox",
    "money-maker/06-hidden-gems.md": "Hidden gems",
    "money-maker/07-gray-zone.md": "Gray zone",
    "money-maker/08-digital-products.md": "Digital products",
    "money-maker/09-outreach-scripts-and-pricing.md": "Outreach and pricing",
    "money-maker/10-tools-costs-payments.md": "Tools, costs, payments",
    "money-maker/11-idea-remix-engine.md": "Idea remix engine",
    "money-maker/12-agent-reach-setup.md": "Agent Reach setup",
}

MD_EXT = ["tables", "fenced_code", "sane_lists"]


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:80] or "section"


def page_id(prefix, path):
    if path.name == "README.md":
        return f"{prefix}-overview"
    m = re.match(r"(\d+)", path.name)
    return f"{prefix}-{m.group(1)}" if m else f"{prefix}-{slug(path.stem)}"


def preprocess(md):
    """Make GitHub-style markdown friendlier to Python-Markdown."""
    out, in_fence, prev = [], False, ""
    for line in md.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            prev = line
            continue
        if not in_fence:
            if line.strip() == "---":  # horizontal rules read as clutter in cards
                prev = ""
                out.append("")
                continue
            m = re.match(r"^( {1,3})([-*] |\d+\. )", line)
            if m:  # 2-space nested lists -> 4 spaces
                line = "    " + line.lstrip()
            is_item = bool(re.match(r"^\s*([-*] |\d+\. )", line))
            prev_item = bool(re.match(r"^\s*([-*] |\d+\. )", prev))
            is_table = line.lstrip().startswith("|")
            prev_table = prev.lstrip().startswith("|")
            if prev.strip() and ((is_item and not prev_item) or (is_table and not prev_table)):
                out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def split_sections(md):
    """Return (h1, intro_md, [(h2, body_md), ...])."""
    lines, h1, intro, sections, cur, in_fence = md.splitlines(), "", [], [], None, False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("# ") and not h1:
            h1 = line[2:].strip()
            continue
        if not in_fence and line.startswith("## "):
            cur = [line[3:].strip(), []]
            sections.append(cur)
            continue
        (cur[1] if cur else intro).append(line)
    return h1, "\n".join(intro), [(t, "\n".join(b)) for t, b in sections]


def render(md, ctx):
    h = markdown.markdown(preprocess(md), extensions=MD_EXT)
    h = re.sub(r"<table>", '<div class="table-wrap"><table>', h)
    h = h.replace("</table>", "</table></div>")
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    # "Label: text" paragraphs and list items get a styled label
    h = re.sub(r"<(p|li)>([A-Z][A-Za-z0-9 /'(),&+-]{1,48}):(\s)", r'<\1><span class="lbl">\2:</span>\3', h)
    # References to other lessons become links
    def xref(m):
        raw = html.unescape(m.group(1))
        name = raw.split("/")[-1]
        folder = None
        for f, _, _ in GROUPS:
            if f"{f}/" in raw:
                folder = f
        target = ctx["files"].get((folder or ctx["folder"], name)) or next(
            (v for (f, n), v in ctx["files"].items() if n == name), None
        )
        if not target:
            return m.group(0)
        return f'<a class="xref" href="#{target}"><code>{m.group(1)}</code></a>'

    h = re.sub(r"<code>((?:\.\./)?(?:[\w-]+/)?[\w-]+\.md)</code>", xref, h)
    return h


def tags_for(title, body):
    tags = []
    m = re.search(r"Speed (\d), difficulty (\d), fun (\d)", body)
    if m:
        tags += [("speed", f"Speed {m.group(1)}"), ("diff", f"Difficulty {m.group(2)}"), ("fun", f"Fun {m.group(3)}")]
    if re.search(r"Hidden gem rating: HIGH", body):
        tags.append(("gem", "Hidden gem"))
    if re.search(r"\(DON'T", title) or title.endswith("(DON'T)"):
        tags.append(("stop", "Avoid"))
    return tags


def code_of(title):
    m = re.match(r"^([A-Z]{1,2}\d{1,2})\.", title)
    return m.group(1).lower() if m else ""


def build_pages():
    files, pages = {}, []
    for folder, label, prefix in GROUPS:
        paths = sorted((ROOT / folder).glob("*.md"), key=lambda p: (p.name != "README.md", p.name))
        for p in paths:
            files[(folder, p.name)] = page_id(prefix, p)
            pages.append((folder, label, prefix, p))
    out = []
    for folder, label, prefix, p in pages:
        md = p.read_text(encoding="utf-8")
        h1, intro, sections = split_sections(md)
        pid = files[(folder, p.name)]
        ctx = {"files": files, "folder": folder}
        words = len(re.findall(r"\w+", md))
        out.append({
            "id": pid,
            "group": label,
            "nav": NAV_LABELS.get(f"{folder}/{p.name}", h1),
            "title": h1 or p.stem,
            "source": f"{folder}/{p.name}",
            "minutes": max(1, round(words / 220)),
            "intro": render(intro, ctx) if intro.strip() else "",
            "sections": [
                {"title": t, "id": f"{pid}--{slug(t)}", "code": code_of(t), "tags": tags_for(t, b), "html": render(b, ctx)}
                for t, b in sections
            ],
        })
    return out, files


def page_html(pg, idx, group_pages, prev_pg, next_pg):
    e = html.escape
    secs = pg["sections"]
    toc = "".join(
        f'<a class="chip" href="#{s["id"]}">{e(s["title"])}</a>' for s in secs
    ) if len(secs) > 1 else ""
    blocks = []
    for s in secs:
        tags = "".join(f'<span class="tag tag-{k}">{e(v)}</span>' for k, v in s["tags"])
        blocks.append(
            f'<details class="lesson" id="{s["id"]}" data-code="{s["code"]}">'
            f'<summary><span class="lesson-title">{e(s["title"])}</span>'
            f'{"<span class=tags>" + tags + "</span>" if tags else ""}</summary>'
            f'<div class="prose">{s["html"]}</div></details>'
        )
    pager = '<nav class="pager" aria-label="Lesson navigation">'
    pager += f'<a class="pager-prev" href="#{prev_pg["id"]}"><span>Previous</span>{e(prev_pg["nav"])}</a>' if prev_pg else "<span></span>"
    pager += f'<a class="pager-next" href="#{next_pg["id"]}"><span>Next</span>{e(next_pg["nav"])}</a>' if next_pg else "<span></span>"
    pager += "</nav>"
    return f'''
<section class="page" id="p-{pg["id"]}" data-id="{pg["id"]}" data-title="{e(pg["nav"])}" hidden>
  <header class="page-head">
    <p class="eyebrow">{e(pg["group"])} <span aria-hidden="true">/</span> Lesson {idx + 1} of {len(group_pages)}</p>
    <h1>{e(pg["title"])}</h1>
    <p class="meta">{len(secs)} sections <span aria-hidden="true">·</span> about {pg["minutes"]} min read <span aria-hidden="true">·</span> <code>{e(pg["source"])}</code></p>
    <div class="page-tools">
      <label class="done-toggle"><input type="checkbox" id="done-{pg["id"]}" data-page="{pg["id"]}"> Mark as done</label>
      {'<button type="button" class="btn-ghost expand-all" data-page="' + pg["id"] + '">Open all sections</button>' if secs else ''}
    </div>
  </header>
  {'<div class="prose intro">' + pg["intro"] + '</div>' if pg["intro"] else ''}
  {'<nav class="toc" aria-label="Sections in this lesson"><p class="toc-label">In this lesson</p><div class="chips">' + toc + '</div></nav>' if toc else ''}
  <div class="lessons">{"".join(blocks)}</div>
  {pager}
</section>'''


def updates_html():
    md = (DASH / "updates.md").read_text(encoding="utf-8")
    h1, intro, sections = split_sections(md)
    ctx = {"files": {}, "folder": ""}
    items = "".join(
        f'<article class="update"><h3>{html.escape(t)}</h3><div class="prose">{render(b, ctx)}</div></article>'
        for t, b in sections
    )
    latest = sections[0][0] if sections else ""
    return items, latest


def main():
    pages, files = build_pages()
    by_group = {}
    for pg in pages:
        by_group.setdefault(pg["group"], []).append(pg)

    nav, body = [], []
    flat = pages
    for i, pg in enumerate(flat):
        gp = by_group[pg["group"]]
        body.append(page_html(pg, gp.index(pg), gp, flat[i - 1] if i else None, flat[i + 1] if i + 1 < len(flat) else None))
    for group, gp in by_group.items():
        links = "".join(
            f'<li><a href="#{p["id"]}" data-page="{p["id"]}"><span class="dot" aria-hidden="true"></span>{html.escape(p["nav"])}</a></li>'
            for p in gp
        )
        gid = slug(group)
        nav.append(
            f'<div class="nav-group" data-group="{gid}"><p class="nav-group-label">{html.escape(group)}'
            f'<span class="nav-count" data-count="{gid}"></span></p><ul>{links}</ul></div>'
        )

    upd_items, latest = updates_html()
    home = (DASH / "home.html").read_text(encoding="utf-8").replace("{{LATEST_UPDATE}}", html.escape(latest))
    total = sum(len(p["sections"]) for p in pages)
    home = home.replace("{{LESSON_COUNT}}", str(len(pages))).replace("{{SECTION_COUNT}}", str(total))

    shell = (DASH / "shell.html").read_text(encoding="utf-8")
    fragment = (
        shell.replace("{{NAV}}", "\n".join(nav))
        .replace("{{HOME}}", home)
        .replace("{{UPDATES}}", upd_items)
        .replace("{{PAGES}}", "\n".join(body))
        .replace("{{LATEST_UPDATE}}", html.escape(latest))
    )
    (DASH / "build").mkdir(exist_ok=True)
    (DASH / "build" / "artifact.html").write_text(fragment, encoding="utf-8")
    full = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + fragment + "\n</body>\n</html>\n"
    )
    (ROOT / "dashboard.html").write_text(full, encoding="utf-8")
    print(f"Built {len(pages)} lessons, {total} sections -> dashboard.html ({len(full)//1024} KB)")


if __name__ == "__main__":
    main()

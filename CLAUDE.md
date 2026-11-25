# CLAUDE.md

This repo is Kent's knowledge base for money-making ideas and Claude projects. Folders: `money-maker/` (general money ideas) and `claude-lab/` (Claude Max usage, earning projects, learning path).

## Standing reminder (show this at the start of new sessions)

Kent asked to be reminded to come back and learn the Jarvis / AI office setup. At the start of a new conversation in this repo, briefly remind them that `claude-lab/05-jarvis-and-ai-office-parked.md` is waiting, and offer to start that deep dive. Keep the reminder to one or two lines and don't block whatever they asked for. Stop reminding once they say it's done or tell you to drop it, and update this section when that happens.

## How to work in this repo

- Keep information in full, organized markdown files. Don't summarize research away.
- Ideas should be remixes of building blocks, not copies of one person's business. Say where the building blocks came from.
- Target buyers: US, UK, EU, AU, CA. Budget is tight, so favor ideas with a fast first dollar.

## Dashboard (keep it updated, every time)

`dashboard.html` at the repo root is the clickable course view of everything in this repo, and it's also published as a private artifact: https://claude.ai/artifact/EcKzhX8qAGS7kcZbb4K8e1

Whenever new information lands (web research, new ideas, edits to any .md file in `money-maker/` or `claude-lab/`, or a new folder), keep the dashboard in sync in the same turn:

1. Put the information in the markdown files first (the dashboard is built from them, never edited by hand).
2. Add a dated entry at the top of `dashboard/updates.md` saying what changed.
3. New folder? Add it to `GROUPS` in `dashboard/build.py`. New file? Add a short sidebar label to `NAV_LABELS`.
4. Rebuild: `pip install markdown` (once), then `python3 dashboard/build.py`.
5. Republish `dashboard/build/artifact.html` to the artifact URL above (from a new conversation, pass it as `url` and read the artifact first).
6. Commit `dashboard.html` and the dashboard sources with the markdown changes.

Home page content (quick picks, start-here steps) lives in `dashboard/home.html`. Styles and behavior live in `dashboard/shell.html`.

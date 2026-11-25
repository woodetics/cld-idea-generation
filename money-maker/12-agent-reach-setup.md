# Agent-Reach Setup (on your own computer)

Repo: https://github.com/Panniantong/Agent-Reach (MIT, v1.6.1)

## What happened in the cloud session

- Agent-Reach was cloned and installed with uv, and `agent-reach setup` succeeded (5/5 default channels prepared: GitHub, YouTube, Bilibili, V2EX, web).
- But the cloud container's network policy blocked the sites it reads (YouTube, Reddit, the GitHub API, Exa, Jina). Every query returned "blocked by proxy".
- So the research for this folder used the built-in web search instead. On your own computer none of those blocks exist.

## Install on your machine (Mac / Linux)

Install uv first if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install Agent-Reach from GitHub (NOT from PyPI, the PyPI package with that name is a different project):

```bash
uv tool install https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip
```

```bash
agent-reach setup
```

Windows: install uv with

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

then run the same two commands.

If `agent-reach` isn't found after install:

```bash
uv tool update-shell
```

and open a new terminal.

Easiest way: just tell Claude Code on your machine "install Agent Reach: https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md" and it does everything. Setup also installs a Claude Code skill so Claude knows how to use it.

## Add optional channels

```bash
agent-reach add reddit
```

```bash
agent-reach add linkedin
```

```bash
agent-reach add xiaohongshu
```

```bash
agent-reach add twitter
```

Logins: it copies a site's login from your Chrome into its own private browser (doesn't read your password vault). Use a secondary/burner account for platforms that restrict automated access (X, Instagram, Xiaohongshu).

For YouTube transcription of videos without subtitles, add a Groq key (free tier) in your own terminal:

```bash
agent-reach configure groq-key
```

## Commands for money research

Every command prints JSON. Pattern: `agent-reach <channel> <action> [args]`.

```bash
agent-reach channels
```

```bash
agent-reach github search "faceless video generator"
```

```bash
agent-reach github read https://github.com/calesthio/OpenMontage
```

```bash
agent-reach youtube search "n8n automation agency first client"
```

```bash
agent-reach youtube subtitle https://www.youtube.com/watch?v=VIDEO_ID
```

```bash
agent-reach reddit search "I would pay for a tool that"
```

```bash
agent-reach reddit subreddit smallbusiness
```

```bash
agent-reach linkedin jobs "AI automation remote"
```

```bash
agent-reach bilibili hot
```

```bash
agent-reach xiaohongshu search "厨房神器"
```

```bash
agent-reach read https://any-link-here
```

## Prompts to give Claude Code once Agent-Reach is installed

- "Use agent-reach to search Reddit for posts in r/smallbusiness, r/Entrepreneur and r/sweatystartup from the last month where people say 'I'd pay for' or 'is there a tool'. Group the pains, rank by frequency, save to pains.md."
- "Use agent-reach to pull subtitles from the top 10 YouTube videos about 'AI automation agency'. Extract every concrete tactic, price and niche mentioned. Then invent 5 NEW offers that combine them with underserved audiences from 11-idea-remix-engine.md."
- "Use agent-reach to search GitHub for repos with 'self-hosted' in the topic and over 1,000 stars, then read their issues for 'hosted version' requests. List the top 10 with license type."
- "Use agent-reach on Xiaohongshu and Bilibili to find the 20 most-discussed kitchen/beauty/gadget products this week. Translate, then check if each exists on TikTok Shop US. Write a trend report."
- "Use agent-reach linkedin jobs to find remote AI training/annotation roles open internationally. Build a table with pay and country eligibility."

## Safety notes (from the repo)

- Read-only: never posts, comments, likes or DMs.
- Never logs in for you or asks for your password.
- Its private browser is only reachable from your own computer.
- Keys go in your own terminal, never pasted into chat.
- Uninstall: tell your agent "uninstall Agent Reach", it lists what it will delete and asks first.

# Learning Path: How to Actually Build These

The cards in `02-earning-projects.md` point at modules here. You don't need all of them before you start earning. Modules 1 to 4 cover the fastest ideas (E3, E8, E9, E13). Learn the rest WHILE you work on a paid project, that's honestly the only way it sticks.

How to learn any module: open Claude Code in an empty folder and say "teach me [module] by building [the tiny project listed]. Explain each step before you do it, and stop so I can try the next one myself." Claude Code is the best tutor for Claude Code.

Set up on: your Windows PC, the Claude mobile app, and later a $5 VPS if a project needs to be always on.

## Module 1. Claude Code basics on Windows (day 1 to 2)

What you learn:
- Install: PowerShell, `irm https://claude.ai/install.ps1 | iex`, plus Git for Windows (recommended, gives Claude the Bash tool).
- The Claude Desktop app too (Cowork, Dispatch, computer use live there).
- Starting a session in a folder, `/model`, `/clear`, `/usage`, permission modes, auto mode.
- Git basics: Claude commits for you, but you need to understand "save points" so you can undo when it breaks stuff.
- Plain markdown (everything in this course is markdown files).

Tiny project: make a folder called `sandbox`, ask Claude to build a one-page website about yourself, then change it 5 times and undo one change with git.

You're done when: you can start Claude Code, give it a task, review what it did, and roll back a mistake without panicking.

## Module 2. CLAUDE.md and Skills (day 3 to 5)

What you learn:
- `CLAUDE.md`: the file Claude reads at the start of every session in that folder. Your project's rules, goals and context. This is how you stop repeating yourself (and how you save usage).
- Skills: reusable instruction packs (a `SKILL.md` plus optional scripts) Claude loads when the task matches. Your "my-writing-style" is a skill, so you've already seen one.
- Slash commands and plugins (a bundle of skills, commands and settings you can share or sell).

Tiny project: write a skill called "airbnb-audit-checklist" that lists what a great listing has. Then ask Claude to audit one real listing using it.

You're done when: you can make a skill from scratch and Claude actually uses it without being told.

Where to look: davepoon/buildwithclaude and daymade/claude-code-skills to read good examples (READ them, don't just install them, that's the lesson).

## Module 3. Working with files and data (week 2)

What you learn:
- Getting Claude to read CSVs, PDFs, exports and photos, and write clean spreadsheets, reports and markdown.
- Building a knowledge vault: folders of markdown linked together (Obsidian is free and makes it visual).
- Keeping private client data private: work in a separate folder per client, delete after delivery.

Tiny project: export your own ChatGPT or Claude data and build a mini "about me" vault from it (this is E13's whole product, done on yourself first).

You're done when: you can hand Claude a messy pile of files and get a clean, organized result you'd show a client.

## Module 4. Subagents and parallel work (week 2 to 3)

What you learn:
- Subagents: helper agents with their own context and job (one audits photos, one audits pricing). Keeps your main chat small.
- Making your own subagents as files (`.claude/agents/`), each with a clear role and limited tools.
- The verifier pattern: one agent checks the others' work and throws out anything without evidence (straight from shopify-audit-agents).
- When NOT to go parallel: it burns usage fast.

Tiny project: turn your Module 2 audit into a swarm: 4 specialist subagents + 1 verifier + 1 editor that writes the final report.

You're done when: the swarm's report is clearly better than a single prompt's. That report is your E3 sample.

Where to look: oh-my-claudecode (41k stars) and agent-teams-lite (pure markdown, easy to read).

## Module 5. Scheduling and alerts (week 3)

What you learn:
- Routines: jobs that run on Anthropic's cloud on a schedule, even with your PC off. `/schedule` or claude.ai/code/routines.
- `/loop` and local scheduled tasks.
- Channels: talk to a running Claude Code session from Telegram or Discord (sender allowlist so only YOU can talk to it).
- Cowork Dispatch: text your PC from your phone.
- Connectors (Gmail, Calendar, Drive) so a routine can read your stuff.

Tiny project: side project S1, a 7am Telegram morning brief.

You're done when: something useful lands on your phone every morning without you touching your PC.

## Module 6. Overnight builds and specs (week 3 to 4)

What you learn:
- Writing a spec file Claude can follow alone: goal, what "done" looks like, how to test it, where to log progress.
- Auto mode and long runs, checking in the morning, reading the diff.
- Breaking big projects into tasks, a `PROGRESS.md` Claude updates as it goes.
- Planning with Fable, building with Sonnet.

Tiny project: write a spec for a small browser game (E12) before bed, let it run, play it in the morning.

You're done when: you wake up to something that works more often than not.

## Module 7. API keys, the Agent SDK and deploying a bot (month 2)

This is the module that turns "I do the work with Claude" into "I sell a product that runs by itself", the legit way.

What you learn:
- Why: products that serve other people must run on an API key, not your Max login (see `00-max-plan-facts-and-rules.md`).
- Claude Console, making an API key, using your $100/month Max API credit, setting a spending limit (DO this first).
- The Claude Agent SDK: the same engine as Claude Code, but inside your own program.
- A Telegram bot on a $5 VPS (Linux, systemd or PM2 to keep it running), secrets in environment variables, never in code.
- Prompt caching to make API calls cheaper.

Tiny project: a Telegram bot that takes a voice note and returns a tidy job log entry (the core of E1), running on your VPS with your API key.

You're done when: the bot keeps answering after you close your laptop, and you know what each message costs.

Where to look: kirie (Agent SDK, Telegram, memory), ClickHouse/nerve (Agent SDK runtime), claude-telegram-relay (minimal pattern).

## Module 8. Video tooling (month 2, only if you go the video route)

What you learn:
- ffmpeg basics (Claude writes the commands, you learn what they do).
- Whisper for transcripts (local, or Groq's free tier).
- Remotion: videos made from code, so templates are reusable.
- Picking clip moments with Claude and cutting on word boundaries.

Tiny project: take one podcast episode and make 3 captioned vertical clips.

You're done when: one long video turns into clips with one command.

Where to look: digitalsamba/claude-code-video-toolkit, zero-dollar-studio, clipper-skill, awesome-claude-video-skills (180 repos, security-graded).

## Module 9 (later). Jarvis and the AI office

Parked on purpose, you asked me to remind you later. Everything needed to start is waiting in `05-jarvis-and-ai-office-parked.md`. By the time you finish Modules 1 to 7, you'll honestly already know 80% of how to build one.

## A 30-day plan that pays while you learn

- Week 1: Modules 1 and 2. Make 2 free sample Airbnb audits (E3) by hand with your skill.
- Week 2: Modules 3 and 4. Turn the audit into a swarm. Post the samples, pitch 20 hosts or property managers. Do one E13 migration on yourself and record it as content.
- Week 3: Module 5. Set up your morning brief. Pitch E8 (AI Shelf Check) screenshots to 20 local businesses.
- Week 4: Module 6. First overnight build. Pick the ONE idea that got the most replies and go all in on it for month 2.

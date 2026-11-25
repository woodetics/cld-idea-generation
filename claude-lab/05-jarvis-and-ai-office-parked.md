# PARKED: Jarvis and the AI Office (come back to this)

You asked to focus on earning projects first and get reminded about this later. So this is a parking spot, not the full guide. The repo's `CLAUDE.md` tells future Claude sessions to remind you about it.

When you come back, start the session with: "Let's do the Jarvis / AI office deep dive from claude-lab/05." That gives the next session enough to go straight into building instead of researching from zero.

## What "Jarvis" means in practice

A personal assistant you talk to from your phone (text or voice), that remembers you, can act on your PC or in the cloud, and checks in on its own (morning brief, reminders, "your build finished").

The 4 parts every Jarvis has:
1. A door: Telegram, Discord, WhatsApp, voice, or iMessage.
2. A brain: Claude Code (on your login, for YOUR personal use) or the Agent SDK (on an API key, if anyone else uses it).
3. Memory: a folder of markdown files (an Obsidian vault) plus a CLAUDE.md.
4. A heartbeat: scheduled jobs (Routines, `/loop`, cron) so it does things without being asked.

Options found, from easiest to most DIY:
- Built-in Anthropic pieces: Channels (Telegram/Discord/iMessage into a running session), Cowork Dispatch (phone to desktop), Routines (cloud schedule), Remote Control. Least setup, fully allowed on Max.
- cc-connect (16k stars): bridges Claude Code to Telegram, Discord, Slack, LINE and more.
- NanoClaw (31k stars): always-on, each agent in its own container, agent swarms in chat.
- claude-telegram-relay: the minimal pattern, good for learning how it works.
- Voice: ethanplusai/jarvis (Mac only, but the idea ports to Windows), jarvis-voice-assistant (double-clap to launch).
- Memory: claude-obsidian (16k stars), obsidian-second-brain (shared logbook across agents), agentmemory (30k stars).

Watch out: Anthropic blocked third-party tools from using subscription logins in April 2026. Tools that run the REAL Claude Code for your own personal use are fine. Tools that take your Claude login and use it some other way are risky. Check each repo before trusting it with your account.

## What "AI office" means in practice

Several agents with job titles (CEO/planner, researcher, writer, reviewer, sales) sharing a task board, each with its own instructions, handing work to each other, with you as the boss who approves.

Options found:
- Paperclip: org charts, budgets, goals, task tracking, audit logs, many businesses in one install. Playbooks: paperclip-company-playbook, paperclip-plugin-company-wizard.
- oh-my-claudecode (41k stars): teams-first orchestration inside Claude Code.
- dontbemichael (594 stars): "run an office of agents" on your existing Claude Code subscription.
- GT-Office: desktop app for multi-agent work, Windows supported.
- agent-office: isometric office you WATCH agents work in (just fun to look at).
- AI Team OS (CronusL-1141/AI-company): meetings, task wall, React dashboard.
- OpenExecutive: 8 specialist agents behind one "executive" persona.

The cautionary tale to remember: someone built a 5-agent AI company that "sent 241 emails and got zero replies". Agents are great at DOING work, terrible at knowing if it's any good. Keep a human approval step (you) on anything that goes out the door.

## Variations to explore when you come back (my own ideas)

- Jarvis with a CFO: an assistant whose only job is your money. Tracks client invoices, chases late payments with drafts you approve, and tells you every Sunday how many weeks of runway you have.
- The night shift office: an office that only works while you sleep. You leave tasks on the board at 11pm, it hands you a "shift report" at 7am on Telegram.
- An office per client: each client from `02-earning-projects.md` E2 gets its own mini office with its own memory, so nothing leaks between clients.
- The two-Jarvis setup: a personal one on your Max (allowed, just for you) and a business one on an API key (for anything clients touch). Same skills, two brains.
- A Jarvis that runs your learning: quizzes you on the modules in `04-learning-path.md` every morning and tracks what you've actually built.

## Questions to answer at the start of that session

- Text or voice first?
- Always on (needs the $5 VPS or a PC that never sleeps) or "on when my PC is on"?
- Personal only, or will clients ever touch it? (decides Max login vs API key)
- What's the first boring job it should take off your plate?

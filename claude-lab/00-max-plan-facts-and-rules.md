# Claude Max: What You're Actually Buying (and How to Squeeze It)

Read this BEFORE you pay. Facts come from Anthropic's own pricing, support and legal pages, read on 2026-11-25 (full quotes are in `01-raw-research-how-people-use-claude.md`, Part A).

## The plan, in plain words

- Max is $100/month, monthly only. You get 5x Pro's usage every 5 hours AND every week.
- Ultra is $200/month, 10x Pro per week and no 5-hour limit (for verified accounts). Don't start here. Upgrade only once you KEEP hitting the Max weekly wall on work that earns.
- Max includes Claude Code, Cowork, Claude in Chrome, scheduled tasks, Opus, Sonnet, Haiku, and Fable (Anthropic's top model) for up to half your weekly limit.
- Max also gives you $100/month in API credits on the Claude Platform. This is the sleeper perk, more on it below.
- Usage does NOT roll over. "You receive your full weekly allowance each cycle." So a lazy week is literally money burned.

## The ONE rule that decides how you can make money with it

This is the part most YouTube "make money with Claude" videos skip (dramatic, I know, but it matters).

What's allowed with your Max login:
- You, personally, using the unmodified Claude Code, Claude Desktop, Cowork and claude.ai. For anything, including client work. You do the work with Claude, you sell the RESULT. That's normal use.
- A client signing in to the unmodified Claude Code with THEIR OWN subscription, even on a machine or server you set up for them. So you can sell "I'll set up Claude for you", as long as they log in with their own account.

What's NOT allowed:
- Building an app or bot for OTHER people that runs on your Max login. Anthropic's words: they don't permit developers "to route requests through Free, Pro, Max, or Ultra plan credentials on behalf of their users."
- Collecting or storing someone else's Claude login.
- Modifying the Claude Code program itself.
- Anything you build as a product for others, including on the Agent SDK, "should use API key authentication".
- Anthropic blocked third-party tools like OpenClaw from using subscription logins in April 2026 and says it can enforce "without prior notice". So don't build your income on a hack that might get your account shut.

What this means for you, in one line: USE Max to do work and build things, but anything that runs 24/7 serving paying customers should run on an API key. And that's exactly where the $100/month API credit comes in. It's free money to run your products' first customers on, the legit way.

## Where your usage goes (so you don't run out by Wednesday)

- Long chats eat more. Every message re-reads the whole conversation. Start fresh sessions often (`/clear`) and keep a `CLAUDE.md` so Claude doesn't need the history.
- Big files eat more. Point Claude at the exact file, not the whole folder.
- Fable is capped at half your weekly limit and costs the most. Use it for the HARD thinking (planning a business, architecture, tricky bugs), then let Sonnet or Haiku do the grunt work. Switch with `/model`.
- Subagents run in their own context, so they keep your main chat small. But 10 agents in parallel burn 10x as fast. Parallel is for when you're racing a deadline, not by default.
- Your weekly reset time is fixed per account. Check it in Settings > Usage, and plan your heavy builds for the 2 days AFTER a reset, not the night before.

## How to keep Max busy while you sleep (the actual "maximize" trick)

The people getting the most from Max aren't typing more. They're queuing work so Claude keeps going while they're away.

- Routines (cloud): saved Claude Code jobs that run on Anthropic's servers on a schedule, even with your laptop OFF. Create at claude.ai/code/routines or with `/schedule`. Good for: daily lead lists, competitor checks, research digests, drafting tomorrow's content.
- Cowork Dispatch: text your PC from your phone, it works on your desktop files and apps. Needs the PC awake with Claude Desktop open.
- Channels: message a running Claude Code session from Telegram or Discord. Perfect for "start this task" from the bus.
- `/loop` and local scheduled tasks: repeat a task inside a session every N minutes.
- Overnight build ritual: before bed, write a clear spec in a markdown file ("build X, test it, write what you did to PROGRESS.md"), start Claude Code in auto mode, go to sleep, review in the morning. This alone can double what you get from the plan.

## A weekly rhythm for someone with a day to spare

- Day 1 to 2 after reset: big builds (new project, new client deliverable). Fable for planning, Sonnet for building.
- Day 3 to 5: client work and content. Mostly Sonnet.
- Day 6 to 7: research, learning, cleanup, writing skills you'll reuse. Haiku or Sonnet. If you still have usage left the day before reset, dump it into a long research or overnight build. Leftover usage is wasted usage.

## Your setup (Windows + phone + maybe a $5 VPS)

- Install on Windows (PowerShell, no admin): `irm https://claude.ai/install.ps1 | iex`. Install Git for Windows too, it's "recommended" so Claude Code gets its Bash tool.
- Install the Claude Desktop app (for Cowork, Dispatch and computer use) and the Claude mobile app.
- Your laptop doesn't need to be on 24/7 for most of this, because Routines run in Anthropic's cloud.
- A $5 VPS only becomes worth it when you have something that must ALWAYS answer (a client bot, a Telegram assistant listening all day). And remember, that thing should run on an API key if it serves other people.

## Is Max worth it for you right now? (honest take)

- If you're going to use Claude Code at least 2 to 3 hours a day on things that can earn, yes. Pro at $20 runs out fast with Claude Code.
- If you're not sure yet, start with Pro for a week, get the Windows setup and your first `CLAUDE.md` working, THEN upgrade. Upgrading mid-month is easy. Paying $100 to spend the first week fighting an install is not.
- The $100 API credit only helps if you actually build something that uses the API. So build one small API-powered thing in month one, so that credit isn't wasted either.

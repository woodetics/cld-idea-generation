# Raw Research: How People Are Using Claude (Nov 2026)

Everything found during research on 2026-11-25, kept in full. Nothing here is summarized away. Star counts and dates are what GitHub showed on that day, so they will drift.

How this was gathered:

- Agent Reach (v1.6.1) was installed again in the cloud box. This time the GitHub channel WORKED, so every repo list below came straight from GitHub search through Agent Reach.
- YouTube and Reddit through Agent Reach were still blocked by the cloud box's network rules (YouTube said "blocked by proxy", Reddit couldn't download its helper). On your own Windows PC those blocks don't exist, see `../money-maker/12-agent-reach-setup.md`.
- Web searches filled in the rest (official Anthropic pages, blogs, news).

A note on honesty: star counts show interest, not income. A repo with 30k stars can still earn its author zero dollars. Treat every "I made $X" blog post as marketing until you see proof.


## Part A. The official facts (read from Anthropic's own pages)

### Plans (from claude.com/pricing, read 2026-11-25)

- Free: $0. Limited usage. Chat, web search, code execution, memory, Artifacts. No Claude Code, no Opus, no Fable.
- Pro: $20/month billed monthly ($17/month on annual, $200 up front). "1x" usage every 5 hours and every week. Includes Claude Code, Claude Science, Projects, Claude in Chrome and Microsoft 365, "Hand off and schedule tasks", Opus, Sonnet, Haiku. Fable only through paid usage credits. No monthly API credits.
- Max: $100/month (monthly only). "5x Pro usage" every 5 hours and every week. Everything in Pro, plus "Fable included, up to half your weekly limit", "$100 a month in API credits to build on the Claude Platform", early access to advanced features, priority access at high traffic times.
- Ultra: $200/month. "No 5-hour limit for verified accounts" and "10x Pro usage every week". Everything in Max, plus "$200 a month in API credits, up from $100 on Max". Fable up to 50% of weekly limits.
- Footnotes on the page: "Price and plans are subject to change at Anthropic's discretion." and "How fast you reach a limit depends on the model you use, how long your chats are, and how large your files are."
- Some third-party blogs still say "Max 5x" ($100) and "Max 20x" ($200). One says the old Max 20x was renamed Ultra and existing subscribers moved over with no price change. Trust the official page over those blogs.

### How Max limits work (support.claude.com "What is the Max plan?", updated ~3 weeks before 2026-11-25)

- "Max plans have a five-hour limit, a weekly usage limit that applies across all models, and a separate weekly limit for Fable."
- "The weekly limit resets at a fixed time each week that is assigned to your account." You can see the next reset in Settings > Usage.
- "you receive your full weekly allowance each cycle" (unused usage does NOT roll over, so an idle week is wasted money).
- "If you have a limit reset, you can use it to reset your five-hour session limit or weekly usage limits back to full."
- "Additional usage limits may apply to manage capacity and ensure fair access to all users." and "We don't guarantee uninterrupted service."
- Monthly API credits come with Max, Ultra and Team.
- Cowork is described as "Hand Claude work like reports, spreadsheets, and presentations, and it keeps going in the background."

### The rules on subscription logins (code.claude.com/docs/en/legal-and-compliance)

This part matters a LOT for making money, so it's quoted word for word:

- "OAuth authentication is intended exclusively for purchasers of Claude" Free, Pro, Max, Ultra, Team and Enterprise plans, and is "designed to support ordinary use of Claude Code and other native Anthropic applications."
- "Developers building products or services that interact with Claude's capabilities, including those using the Agent SDK, should use API key authentication through Claude Console or a supported cloud provider."
- "Anthropic does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, Max, or Ultra plan credentials on behalf of their users."
- "developers may not collect, store, or intermediate Claude.ai credentials or session tokens" (sign-in must "complete through Anthropic's own flow").
- It does NOT prevent "an end user from signing in to the unmodified Claude Code binary with their own Claude subscription, including where a platform hosts Claude Code".
- "The Claude Code binary must not be modified."
- "Advertised usage limits for Pro, Max, and Ultra plans assume ordinary, individual usage of Claude Code and the Agent SDK."
- "Anthropic reserves the right to take measures to enforce these restrictions and may do so without prior notice."

### The OpenClaw "ban" story (news, Feb to Jun 2026)

- Several outlets (MindStudio, The Next Web, DEV Community, Medium) reported Anthropic updated its terms on February 20, 2026 to forbid subscription OAuth tokens in third-party tools, then started blocking them on April 4, 2026 at 12:00 PM PT. OpenClaw was the big name hit.
- First-party apps kept working: Claude Code, Claude.ai, Claude Desktop.
- Workaround offered: pay-as-you-go API keys. One source quoted Sonnet 4.6 API pricing at $3 per million input tokens and $15 per million output tokens.
- One newer blog (BetterClaw) claimed the ban was reversed on May 13, 2026 and a planned "Agent SDK credit" was paused on June 15. I could NOT confirm this anywhere else, and that site wouldn't load from the cloud box. The official legal page above is what counts.
- Sources: [MindStudio](https://www.mindstudio.ai/blog/anthropic-openclaw-ban-oauth-authentication), [The Next Web](https://thenextweb.com/news/anthropic-openclaw-claude-subscription-ban-cost), [DEV Community](https://dev.to/mcrolly/anthropic-kills-claude-subscription-access-for-third-party-tools-like-openclaw-what-it-means-for-3ipc), [BetterClaw](https://www.betterclaw.io/blog/openclaw-anthropic-subscription-ban), [Is OpenClaw allowed in Claude Code?](https://metricnexus.ai/blog/is-openclaw-allowed-in-claude-code)

### First-party features people build Jarvis setups on

- Channels: research preview launched March 20, 2026. Telegram and Discord first, iMessage about a week later. You message a RUNNING Claude Code session on your machine from your phone. Setup is a plugin install, then start Claude Code with the channels flag. Every channel has a sender allowlist (only paired accounts can talk to it). Sources: [DataCamp](https://www.datacamp.com/tutorial/claude-code-channels), [claudefa.st](https://claudefa.st/blog/guide/development/claude-code-channels), [fast.io](https://fast.io/resources/claude-channels-guide/), [aiforautomation](https://aiforautomation.io/news/2026-03-20-claude-code-channels-telegram-discord-ai-agent)
- Remote Control: watch and steer a local session from elsewhere (`claude remote-control`).
- Routines: saved Claude Code jobs that run on Anthropic's cloud, created at claude.ai/code/routines or with `/schedule`. They keep running when your PC is off. Source: [fast.io scheduled tasks guide](https://fast.io/resources/claude-scheduled-tasks-guide/), [claudefa.st scheduled tasks](https://claudefa.st/blog/guide/development/scheduled-tasks)
- Local scheduled tasks and `/loop`: run inside your local session, often paired with a channel so results land in Telegram.
- Cowork Dispatch: message Claude from your phone and it works on your desktop with your files, connectors, plugins and apps. The desktop must stay awake with the Claude Desktop app open. Computer use (Claude clicking around apps with no API) is in research preview for Pro, Max and Ultra. Risky actions pause and ping your phone for approval. Examples Anthropic gives: check email every morning, pull metrics every week. Sources: [Anthropic blog](https://claude.com/blog/dispatch-and-computer-use), [support article](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork), [XDA](https://www.xda-developers.com/claudes-dispatch-feature-turned-my-phone-into-a-remote-control-for-my-entire-workflow/), [Cowork use cases](https://www.claudecoworkexpert.com/en/blog/claude-dispatch-use-cases/), [DataCamp Dispatch](https://www.datacamp.com/tutorial/claude-cowork-dispatch)

### Windows install (code.claude.com/docs/en/setup)

- PowerShell, no Administrator needed: `irm https://claude.ai/install.ps1 | iex`
- Git for Windows is listed as optional on native Windows but RECOMMENDED (it gives Claude Code the Bash tool). Without it, Claude Code uses a PowerShell tool.
- If Claude Code can't find Git Bash, set the path in settings.json.
- Older guides that call Git "required" are outdated.


## Part B. Jarvis-style personal assistants (GitHub, via Agent Reach)

Search "claude code jarvis":
- adewaskar/jarvis (1006★, pushed 2026-11-07): J.A.R.V.I.S for automating your daily tasks using Claude Code
- ethanplusai/jarvis (1024★, pushed 2026-09-10): JARVIS, a voice assistant for Claude Code. Talk to your Mac and he brainstorms a project with you, builds it, and tells you out loud when a Claude Code session needs you. macOS, on your Claude subscription.
- Julian-Ivanov/jarvis-voice-assistant (143★, pushed 2026-04-08): Personal AI assistant with voice control, browser automation, and screen capture. Double-clap to launch. Built with Claude Code.
- ReshefElisha/jarvis-onshape-mcp (178★, pushed 2026-04-22): Claude Code plugin for driving real Onshape CAD. Vision-decomposition skill, truth-telling, parametric iteration, FeatureScript.
- Itsme23476/jarvis-claude-code (16★, pushed 2026-08-25): Local voice and memory-graph HUD driven by Claude Code, speaking through Fish Audio. Runs on your Claude subscription, memory is a folder of markdown.

Search "claude code telegram assistant":
- nanocoai/nanoclaw (31157★, pushed 2026-11-25): Your own always-on AI assistant, self-hosted, open source, lightweight. Each agent runs in its own container on your machine, on the harness you choose (Claude Code, Codex, Cursor, OpenCode).
- chenhg5/cc-connect (16484★, pushed 2026-11-25): Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Discord, LINE, WeChat Work).
- archetyx/telegram-mcp-server (30★, pushed 2025-10-22): Remote control Claude Code/Codex via Telegram
- seedprod/claude-code-telegram (20★, pushed 2026-02-02): Connect Claude Code to Telegram for a personal AI assistant
- daxaur/openpaw (183★, pushed 2026-05-23): Personal Assistant Wizard for Claude Code (npx pawmode)

Search "claude agent sdk personal assistant":
- ClickHouse/nerve (117★, pushed 2026-11-24): Self-hosted AI agent runtime for personal assistants and autonomous workers. Built on the Claude Agent SDK.
- is0383kk/claude-agent-sdk-resident-assistant (5★): Casra, a Claude Code-native personal assistant
- khaterdev/kirie (7★, pushed 2026-11-24): Personal AI assistant on Telegram, Discord, Slack. Official Claude Agent SDK. Proactive, persistent memory, background tasks.
- aviv-edri/whatsapp-personal-assistant (2★): Single-user executive assistant for WhatsApp, tasks, goals, Google Calendar/Gmail, "reflective intelligence". TypeScript + Claude Agent SDK.
- JungwooHur/paperclaw (3★, pushed 2026-11-19): WhatsApp-based personal research assistant built on NanoClaw.

Search "claude code voice assistant":
- 0xMaxMa/claude-gateway (25★, pushed 2026-11-25): Turn Claude Code into a voice-enabled, multi-channel assistant that runs tasks in parallel
- calesthio/generative-media-skills (252★): Agent skills for image, video, audio, voice production
- kcosr/assistant (92★, pushed 2026-11-15): Panel-based personal assistant. AI agents share a workspace of notes, lists and other panels with the user. Supports Claude Code, Codex, pi.

Web search on Jarvis + Telegram:
- Common architecture: Telegram, then a small relay, then the Claude Code CLI, with the relay running as a background service (launchd on Mac, PM2 or systemd on Linux/Windows).
- Some repos let Claude Code set itself up by reading a CLAUDE.md and walking you through it.
- Access control: message your bot once, get your chat ID, put it on the allowlist.
- One write-up: small Linux VPS, systemd running the Telegram bot and scheduled briefings, plus email and the Claude Code CLI.
- At least one popular gateway got marked deprecated in favor of another plugin, so check a repo is alive before using it.
- Repos: [godagoo/claude-telegram-relay](https://github.com/godagoo/claude-telegram-relay), [enochko/jarvis](https://github.com/enochko/jarvis), [qwwiwi/jarvis-telegram-gateway](https://github.com/qwwiwi/jarvis-telegram-gateway), [ShevArtV/jarvis](https://github.com/ShevArtV/jarvis) (per-topic persistent sessions), [Jammore1203/jarvis](https://github.com/Jammore1203/jarvis) (Agent SDK, Telegram, voice, mail, calendar, Obsidian vault as long-term memory), [coleam00/remote-agentic-coding-system](https://github.com/coleam00/remote-agentic-coding-system), [Kiwop guide](https://www.kiwop.com/en/blog/build-personal-ai-assistant-claude-code-mcp)

NanoClaw (web):
- One user was a parent who wanted a codebase small enough to understand for home errands.
- Built-in examples: a Monday briefing task, joining a family group chat ("@Andy pause the Monday briefing task").
- Advertises "Agent Swarms": teams of agents that collaborate inside your chat.
- Forks add Telegram, Signal, Discord, email. ClaudeClaw is a Claude Code plugin built on NanoClaw that routes Slack/WhatsApp/Telegram messages to sandboxed agents with structured memory.

OpenClaw (web, what people use it for):
- Personal admin: email, calendar, research, morning briefing over WhatsApp, auto-unsubscribing from newsletters.
- Digests from Reddit or YouTube, inbox cleanup, research summaries.
- Dev: PR reviews, Sentry log monitoring, tests, GitHub issues. Start a coding task from the phone, the home machine runs Claude Code, ping when done.
- Small business: support triage, lead qualification, appointment booking, follow-ups.
- Cron jobs, SSH server management.
- Most common setup: a home server or Mac mini.
- Sources: [Towards Data Science](https://towardsdatascience.com/use-openclaw-to-make-a-personal-ai-assistant/), [Parallel](https://parallel.ai/articles/openclaw-vs-claude-code-which-ai-agent-should-you-actually-use), [Turing Post](https://www.turingpost.com/p/openclaw), [How are people using OpenClaw?](https://thenuancedperspective.substack.com/p/how-are-people-using-openclaw)


## Part C. "AI office" / multi-agent company setups

Search "claude code multi agent office":
- agentvivekkumar/dontbemichael (594★, 493 forks, pushed 2026-11-21): A local multi-agent harness that works with your existing Claude Code and Codex subscriptions, lets you run an office of agents. MIT.
- Laplace-bit/GT-Office (24★): Cross-platform multi-agent desktop workspace for Claude Code, Codex CLI, Gemini CLI. Rust + React + Tauri. Works on Windows.
- nakotomagami-a11y/agent-office (4★, pushed 2026-11-19): Multi-agent IDE as an isometric office you watch agents work in. Beta.
- kylian-08/AgentsOffice (2★): Local-first multi-agent office with @mention routing, shared briefs, live board, supervisor dispatch.
- AGIoffice/claude-code-office (0★): Clock your agents into Office.xyz across cloud and local machines.

Search "claude code agent team orchestrator":
- Yeachan-Heo/oh-my-claudecode (41053★, pushed 2026-11-25): Teams-first multi-agent orchestration for Claude Code
- vijaythecoder/awesome-claude-agents (4408★): An orchestrated sub-agent dev team powered by Claude Code
- catlog22/Claude-Code-Workflow (2112★): JSON-driven multi-agent team development framework
- Gentleman-Programming/agent-teams-lite (1243★): Orchestrator + 9 specialized sub-agents. Zero dependencies. Pure Markdown.
- hugoguerrap/crypto-claude-desk (122★): Multi-agent crypto intelligence, 6 agents, 66 MCP tools, Agent Teams, zero orchestration code.

Paperclip (the big one, web + GitHub):
- "Open-source orchestration for zero-human companies." Node.js server + React UI. Org charts, job titles, budgets, goals, task tracking, audit logs. Several businesses in one install. MIT, self-hosted, no hosted tier.
- One Medium article claims 43,000+ stars since a March 2026 launch (not verified by me).
- A dev ran seven agents, each with a job, through Paperclip with Claude Code as the runtime.
- Several sources say "zero-human" is aspirational. It cuts human work, it doesn't remove the need for judgment.
- Paperclip ecosystem repos found via Agent Reach:
  - Yesterday-AI/paperclip-plugin-company-wizard (197★): Bootstrap AI agent companies from modular templates.
  - aronprins/paperclip-company-playbook (213★): A practical playbook for setting up an AI agent company in Paperclip that actually works.
  - IncomeStreamSurfer/paperclip-surfers (77★, pushed 2026-11-14): Self-improving agent companies, Paperclip V2 fork with persistent memory, MCPs, skills management, KPI tracking. Built by an SEO company.
  - kcleto-ai/paperclip-company-a360-example (16★): A Brazilian "AI company" with 5 agents that structures, sells and implements AI infrastructure per niche.
  - runtimenoteslabs/gladiator (78★): Two zero-human AI companies battle for GitHub stars (hackathon project).
- Sources: [DEV zero-human company](https://dev.to/manja316/running-a-zero-human-company-with-paperclip-and-claude-code-1nk8), [MindStudio](https://www.mindstudio.ai/blog/what-is-paperclip-zero-human-ai-company-framework), [paperclip.ing docs](https://paperclip.ing/docs), [Geeky Gadgets](https://www.geeky-gadgets.com/paperclip-autonomous-business/)

Other "company" setups (web):
- OpenExecutive: 8 specialist Claude agents behind one "Executive" persona. Apache-2.0, ~475 stars, 37 forks. [explainx](https://www.explainx.ai/blog/openexecutive-open-source-ai-ceo-agent-architecture-august-2026)
- AI Team OS, CronusL-1141/AI-company: 108 MCP tools, 40+ agent templates, 10 hooks, 7 pipelines, persistent teams, structured meetings, task wall, React dashboard. MIT. [GitHub](https://github.com/CronusL-1141/AI-company)
- rjmurillo/ai-agents: 30 agents, plan-to-ship workflows, review and security gates. Dev-focused. [GitHub](https://github.com/rjmurillo/ai-agents)
- Multica: manage coding agents as teammates, assign them tasks like human colleagues. Apache 2.0. [flowtivity](https://flowtivity.ai/blog/multica-open-source-managed-agents-platform/)
- Claude Code Agentrooms: [claudecode.run](https://claudecode.run/)
- FlorianBruniaux guide chapter on AI executive agents: [GitHub](https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/ecosystem/ai-executive-agents.md)
- THE CAUTIONARY TALE: "I Built a 5-Agent AI Company with Claude Code. It Sent 241 Emails and Got Zero Replies." CEO agent reading reports, plus sales, marketing, analytics, product agents. Zero replies. [DEV](https://dev.to/agentkit/i-built-a-5-agent-ai-company-with-claude-code-it-sent-241-emails-and-got-zero-replies-4dfi)


## Part D. Memory and "second brain" (the thing every Jarvis needs)

- AgriciDaniel/claude-obsidian (16745★, pushed 2026-10-25): Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude reads, links and files it into one knowledge graph of plain Markdown.
- eugeniughelbur/obsidian-second-brain (5458★, pushed 2026-11-22): Persistent memory for Claude Code, Codex and 6 other agents as plain markdown in Obsidian. "Crew": one shared logbook so Claude Code, Codex, Cursor and Grok Bot know what each other did.
- huytieu/COG-second-brain (1518★): Self-evolving second brain with 35 skills, 10 agents, people CRM. "The worker never grades its own homework." Anti-slop.
- charlie947/ai-second-brain (255★): Build a searchable second brain from your ChatGPT, Claude and research history, Karpathy-style.
- jessepinkman9900/claude-second-brain (182★): Scaffold an LLM knowledge base, Obsidian + Claude Code + qmd + GitHub.
- rohitg00/agentmemory (30579★, pushed 2026-11-18): "#1 Persistent memory for AI coding agents based on real-world benchmarks"
- zilliztech/memsearch (2934★): Unified memory layer for all your agents, Markdown + Milvus.
- MemTensor/memmy-agent (2309★): Personal agent and local memory hub so "all AI remember the same you".
- Gentleman-Programming/gentle-ai (9555★): Configures the agents you already use with persistent memory, curated skills.
- omega-memory/omega-memory (226★): Persistent memory for coding agents.


## Part E. Video, Shorts, clipping

- Vincentwei1021/video-shotcraft (22492★, pushed 2026-11-24): AI video skill for Claude Code & Codex. Cinematic, editable product promos with Remotion, 124 shot recipe cards, 150 motion previews, beat sync, sound design, JianYing (CapCut CN) export.
- digitalsamba/claude-code-video-toolkit (2755★): Script, AI voiceover, music, clips and render, on open-source models that cost cents.
- zhuyansen/awesome-claude-video-skills (2694★): 180 repos of video skills, each security-graded. English/Chinese.
- haidrrrry/claude-remotion-skill (1322★): Motion graphics with Remotion, B-roll, captions, sound design.
- wshuyi/remotion-video-skill (482★).
- ymybxx/SoloMCN (78★): "Turn Claude Code into your short-video team." From Chinese trending lists and X posts to publishing on Douyin, Xiaohongshu, Bilibili, YouTube, X.
- smixs/youtube-publisher (8★): Upload a recording to YouTube from Drive, transcribe, timestamps, metadata.
- generalizingai/shadowcast (13★): "Paste a YouTube channel link, get your own original channel in that format, produced and scheduled on autopilot." Claude Code plugin.
- krishnasharma2212/stream-clip-machine (14★, pushed 2026-11-19): Watches the biggest live GTA 6 streams 24/7, catches the moment chat explodes, Claude edits it into a captioned vertical Short. Posts up to 5 a day to Shorts and Reels.
- SantiagoThinker/youtube-radar (3★): Daily YouTube digests filtered through your own lenses with Claude Code routines.
- Faceless: yashaiguy-dev/faceless-youtube-agents (41★, clone a channel's style), kevinbadi/claude-motion-faceless-skills (18★, 74 explainer styles: whiteboard, chalkboard, claymation, CRT terminal, manga), joshpocock/faceless-channel-recreator (2★, Higgsfield MCP), rebexstudio/claude-channel-kit (templates, gates, ledgers).
- Clipping: hector-ai-91/video-podcast-clipper (14★, face-tracked crop, "8-dim neuro-engagement scoring"), gouthamk16/clipper (26★, Claude picks moments and writes hooks), RealAdii/clipper-skill (12★, local MLX Whisper, cuts on word boundaries, QA-checked), vitor-pecanha/pods-and-reels (8★, Portuguese), TheNoumanDev/zero-dollar-studio (21★, make YouTube videos for $0, clip podcasts, streams and GTA gameplay into Shorts, cartoons).
- UGC ads: charlesdove977/UGC-Factory (104★, Higgsfield + Seedance 2.0, 15 genre skills, ffmpeg stitching), LordVayron/video-factory (72★, "UGC ads, micro-dramas, sitcoms, launch films, fantasy shorts, hour-long meditations", APIMart + Kie.ai + ElevenLabs), Pika-Labs/Pika-Plugins (42★, official Pika plugin: podcast, explainer, ugc-ads), docusphere/ugc-reaction-studio (6★, phone-realistic reaction ads), osama0561/claude-mockingbird (9★, "Clone winning UGC ads with any AI video provider").
- E-commerce video: Clipcat-ai/clipcat-skill (568★, TikTok Shop video generator, replicate winning videos), xianyu110/ecommerce-video-skills (156★, 12 Chinese e-com short video skills: 3-second hooks, storyboards, edge-tts voice, ffmpeg, TikTok Shop export, live-stream slicing, multi-language dubbing, cover A/B).
- Real estate video: charlesdove977/re-walkthrough-pro (182★): Zillow listing into a cinematic room-by-room walkthrough video (Apify, Higgsfield, ffmpeg). "Built to sell to real estate agents."

Micro-dramas (web):
- TikTok Series (since 2023): paywall up to 80 videos of up to 20 minutes, creator sets the price, 94 countries, must apply in Creator Center.
- TikTok partnered with Made By Us on creator-led micro-series and invites brands to make branded microdramas with AI tools.
- TikTok launched a paid microdrama app (Tubefilter, July 2026, "Lime Shorts"). YouTube rolled out Shorts series subscriptions (MediaPost).
- Vendor (invideo) lists four revenue routes: micro-drama app payouts, short-feed ad revenue, per-episode unlocks, brand integrations. Vendor marketing, not data.
- Owl & Co. projected vertical video at ~$150B global revenue this year excluding China (whole category, not just dramas).
- No reliable per-creator earnings data found.
- Sources: [invideo](https://invideo.io/blog/ai-micro-drama-monetization/), [Tubefilter](https://www.tubefilter.com/2026/07/23/tiktok-lime-shorts-paid-microdrama-app/), [MediaPost YouTube Shorts series](https://www.mediapost.com/publications/article/419074/youtube-rolls-out-shorts-series-subscriptions.html), [eMarketer](https://www.emarketer.com/content/tiktok-courts-microdrama-viewers-brands-seek-new-repeat-exposure-formats), [Philstar/Reuters](https://interaksyon.philstar.com/hobbies-interests/2026/08/19/317988/microdramas-boom-in-a-shrinking-hollywood-as-studios-chase-a-tiktok-audience/)


## Part F. Business / niche skill packs (who's selling to whom)

Marketing and SEO:
- coreyhaines31/marketingskills (62512★, pushed 2026-11-24): Marketing skills for Claude Code. CRO, copywriting, SEO, analytics, growth.
- AgriciDaniel/claude-seo (32252★): 26 sub-skills + 19 sub-agents. Technical SEO, E-E-A-T, schema, GEO/AEO, "agent readiness" (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local.
- Illyism/seo-skills (2118★): 30 SEO skills, technical SEO roasts, Ahrefs & DataForSEO workflows, GEO.
- JeffLi1993/seo-audit-skill (791★), umutxyp/Seo-Promt-Master (601★, zero-dependency CLI + Google/Bing/AI-search knowledge base).

Lead generation:
- Mahanaicoach/google-maps-scraper-kit (2626★): Free Google Maps scraper, no API key, exports name, phone, email, website, rating, social links to CSV.
- gmapsscraper/google-maps-agent-skills (133★): Claude Code skills for Maps leads, emails, competitor analysis, cold outreach.
- yangshun2005/Codex-native-Lead-Hunter (3★): finds and scores leads, drafts outreach, creates Mail.app drafts, human approval before send.
- Rdzala30/ai-agent-freelancer (10★): "LeadHunter AI", finds local businesses, scores them, sends Email + WhatsApp outreach.
- jasonstrimpel/lead-genius-plugin (11★): lead gen plugin for Claude Code and Cowork.

E-commerce:
- Hainrixz/traxo-agente (10★): Agent that runs your e-commerce from Claude: shipping, tracking, marketing, messaging, store builder. Colombia first.
- Pipzzter/storeforge (8★): Idea to launch plan, sourced products and Shopify store code.
- erikholmberg/shopify-ceo-agent (0★): CEO advisor for a Shopify store using exported admin data.
- cr1707/shopify-audit-agents (0★, pushed 2026-10-13): "Audit any online store with a team of Claude Code agents: 8 area leads, 24 specialists, a verifier and an editor. Evidence-only findings and copy-paste fixes."
- motiful/product-shots (155★): One product photo into main images, A+ pages, multi-angle shots, social posts, ad creatives.
- DannylydST/sorftime-seller-agent (51★): Amazon product research, "Hidden Profit Index" for overlooked high-margin products, 124 MCP tools.
- coral870921-source/Ozon-Profit-Skills (28★): Cross-border listings translation, SEO tags, profit per order (Ozon).
- Etsy: semihbugrasezer/seerxo (29★, listing generation and audit, CLI + MCP + skill), abutun/etsy-seo-optimizer (23★), silennsong/etsy-listing-helper (15★, POD specs to copy-paste listing, 13 SEO tags), ghosttown123/etsy-ugc-compliance-harvester (10★), kennymatthew/etsy-pod-launcher (2★, Printify + Claude Code).

Real estate:
- zubair-trabzada/ai-realestate-claude (207★): comps, rental income, neighborhood, investment potential.
- ahacker-1/cre-agent-skills (143★): commercial real estate underwriting, due diligence, financing, brokerage, legal, closing.
- miron-tech/realtor-claude-skills (16★): 12 skills for agents, lead research, comps, listing marketing, follow-ups, reviews.
- TheProsperityAgent/prosperity-real-estate-skills (11★): Fair-Housing-compliant listing copy, MLS integration, compliance.

Bookkeeping and tax (country-specific, this is a pattern):
- head790/buhuchet (3★): 16 skills for Russian individual entrepreneurs: invoices, contracts, tax, deadlines.
- mathijs-oord/vink-plugin (6★, pushed 2026-11-14): Dutch freelancers (ZZP), invoices, receipts, quarterly VAT returns, year-end, all in CSV.
- ArsenBatyuchok/export-stripe-invoices (1★): Bulk-export Stripe invoices as PDFs with a CSV manifest.
- Tonymathewz/office-claude-skills (0★, pushed 2026-11-23): No-code office skills, bookkeeping, VAT/GST for UAE, Saudi, India, Singapore, Malta + 22 countries, approve-first email queue.
- itsZlatinIvanov/ai-bookkeeper (0★): Bank statement PDF to reconciled bookkeeping sheet, pulls invoices from Gmail, billing portals, Stripe (Playwright).

Jobs:
- devdattatalele/auto-apply (4★): Playwright form filler, multi-ATS.
- ShipItAndPray/job-apply-ai (5★): search, tailor resumes, auto-fill ATS forms.
- MS-Jahan/job-apply-kit (9★): tailored resumes, staged (NEVER auto-submitted) applications.
- dorddis/linkedin-easy-apply-automation (6★): LinkedIn Easy Apply via Chrome DevTools MCP.

Trading:
- galleonlabs/hypergrok-trading-desk (602★): Hyperliquid trading desk for agents, 7 roles, 17 skills. Execution needs your wallet and approved tickets.
- aabrole/claude-trading-desk (40★): "Build, honestly backtest, paper trade and self-host algorithmic trading bots."
- javajack/skill-algotrader (103★): Indian equities, Zerodha.
- Bodasaieswar/claude-trading-bot (22★): Gold bot, Claude Code + TradingView (LuxAlgo) + MetaTrader 5 + Telegram alerts.
- vanzan01/poe2scout-mcp (22★): Path of Exile 2 trading intelligence (game economy arbitrage!).

Game dev:
- MRCalderon3D/everything-game-dev-code (114★): 42 agents, 51 commands, 86 skills, Unity/Unreal/Godot/HTML.
- IdoCohen560/claude-unity-game-studio (30★): 49 agents, 120+ skills, a full studio hierarchy.
- Yakoub-ai/phaser4-gamedev (32★): Phaser 4 browser games.
- CodePhobiia/claude-roblox-game-studio (20★): Roblox studio, 36 agents, 50 skills, 201-page Luau wiki, Studio MCP, Blender MCP.

Publishing:
- danielrosehill/KDP-Publishing-Plugin (3★): typeset a print-ready KDP paperback with Typst, full-wrap cover built last.
- cdeistopened/book-studio (3★): manuscripts and scans into print-ready books, no InDesign.
- ChrisGutierrezNet/claude-book-publisher (0★): manuscript audit, KDP preflight, typography checks.
- Owen-gh/coloring-book-skill (0★): KDP coloring book end to end.

Competitor monitoring:
- nickajulia/competitor-monitor-kit (0★, pushed 2026-11-23): daily checks of rivals' pricing pages, weekly brief, battlecards.
- Dr-Growth-AI/competitor-monitoring-ai-skills, weiruye97/social-media-monitor, WaYneZXL/competitor-research-scanner, sunilpradhansharma/evidence-monitoring-agent (monitors what public LLMs SAY about pharma products vs competitors).

Newsletters:
- Jess1357992/energy-newsletter-automation: daily energy digest via Claude Code Remote + GitHub Actions, "zero-server".
- smorrel1/claude-code-skills: creator pack (transcript to X thread, LinkedIn, newsletter, AI-tell checker), plus FDA 510(k).

Browser automation:
- citrolabs/ego-lite (24447★): browser for agents that shares your logged-in browser state with Claude Code without disturbing you.
- browser-use/bux (465★): 24/7 Claude Code agent for browser automation with Telegram, on any box you own.
- cutetailbud/ff-ruyijs (979★): headless browser for agents "designed to navigate through various web protection systems" (gray).

Chrome extensions:
- harry-harish/chrome-extension-builder: build, validate, test, ship Manifest V3 extensions.
- Thealvarro/chrome-extension-builder: Spanish, "you don't need to know how to code".
- timleegoodman/google-sheet-crm-builder: Sheet CRM via Claude for Chrome.

Skill marketplaces (where skills get listed):
- davepoon/buildwithclaude (3796★): hub for skills, agents, commands, hooks, plugins.
- daymade/claude-code-skills (1546★), numman-ali/n-skills (1052★), mhattingpete/claude-skills-marketplace (696★), aiskillstore/marketplace (497★, "security-audited").

MCP monetization:
- xpack-ai/XPack-MCP-Marketplace (172★): open-source MCP store, "sell your own MCP server in minutes".
- apify/actor-mcp-servers (21★): MCP servers published and monetized as Apify Actors.
- xpaysh/awesome-mcp-monetization, learnwithsumit/github-issue-tracker-mcpize (MCPize tutorial).


## Part G. Money claims found (all unverified, mostly marketing)

- Solo automation agency in Austin: $15K MRR in four months, 12 B2B clients, Claude Code + n8n. Source is a case compilation site. [WayToClawEarn](https://waytoclawearn.com/en/cases/solo-ai-automation-agency-15k-claude-code-n8n-2026)
- Freelancer ~$6,000/month, ~$20/month tools, charges $1,500 to $2,500/month per client for automation.
- "Claude Code consulting" estimated $2K to $10K/month from code reviews, refactors, migrations (an estimate, not a result). [betonai](https://betonai.net/claude-code-consulting-side-business-2026/)
- A consultant runs 15 Claude Code agents to produce go-to-market packages, raised prices 4x, "deliver in 4 hours what used to take 2 weeks". Paid newsletter, no revenue numbers. [the-ai-corner](https://www.the-ai-corner.com/p/claude-code-ai-agent-pipeline-client-revenue-2026)
- Solo founder Mac app at $20K MRR with no Swift background, estimated from Indie Hackers posts. [WayToClawEarn](https://waytoclawearn.com/en/cases/claude-code-mac-app-20k-mrr-solo-founder-2026)
- "$2,000 for a client app, Claude wrote 80%". [Medium](https://medium.com/@aitrends24/claude-code-as-a-freelance-income-machine-i-charged-2-000-for-a-client-app-5d88a1166b88)
- "$1M/year SaaS with Claude Code", self-published, no verification. [Wealthy Tent](https://wealthytent.com/build-a-profitable-saas-with-claude-code)

## Part H. Non-coding uses of Claude Code (web)

- One writer's Claude Code started as a coding tool and now handles email, job searches, social media, content, scraping and Shopify store management. Their framing: Claude Code is "an execution layer that happens to be good at code".
- Businesses using it for legal workflows, research systems, document automation, SEO page analysis, spreadsheet editing, second brains, PRDs.
- People writing ALL their content in Claude Code inside VS Code.
- Karpathy connected it to a Lutron home automation system.
- The terminal scares newcomers, the desktop app is the gentler door.
- Sources: [Claude Code for Non-Coders](https://claudecodefornoncoders.substack.com), [Department of Product](https://departmentofproduct.substack.com/p/how-to-use-claude-code-for-non-engineering), [Nate's Newsletter](https://natesnewsletter.substack.com/p/claude-code-without-the-code-the), [Zvi](https://thezvi.substack.com/p/ai-149-3?open=false)

## Part I. Bug bounties and open-source bounties (a warning)

- A dev scanned 1,500 GitHub bounties with an agent and called the public bounty market "broken in 2026". Fresh Algora bounties attract 8 to 158 competing PRs within hours. [DEV](https://dev.to/dyclgtm/i-scanned-1500-github-bounties-with-an-ai-agent-the-public-bounty-market-is-broken-in-2026-33pg), [Bot Farms and Dead Repos](https://marchantdev.github.io/blog/bot-farms.html)
- Ghostty restricted AI contributions to pre-approved issues (Jan 2026). tldraw auto-closes all external PRs. ESLint ended its paid contributor program because AI PRs took over. curl ended its six-year HackerOne bug bounty in Jan 2026 after AI slop floods. [Axios](https://axios.com/2026/03/10/ai-agents-spam-the-volunteers-securing-open-source-software), [Socket](https://socket.dev/blog/eslint-ends-paid-contributor-program), [InfoQ](https://infoq.com/news/2026/02/ai-floods-close-projects)

## Part J. UK Making Tax Digital (used for one idea)

- From 6 April 2026, UK sole traders and landlords with qualifying income over £50,000 (tested on 2024 to 2025) must keep digital records and send quarterly updates. First update (6 April to 5 July 2026) was due 7 August 2026.
- From April 2027: over £30,000 (tested on 2025 to 2026). First update due 7 August 2027.
- From April 2028: over £20,000.
- HMRC won't apply penalty points for late quarterly updates in 2026 to 2027, but updates still need to be sent before the tax return.
- A gov.uk press release said 864,000 sole traders and landlords faced the new rules in the first wave.
- Sources: [gov.uk policy paper](https://www.gov.uk/government/publications/extension-of-making-tax-digital-for-income-tax-self-assessment-to-sole-traders-and-landlords/making-tax-digital-for-income-tax-self-assessment-for-sole-traders-and-landlords), [gov.uk 864,000](https://www.gov.uk/government/news/act-now-864000-sole-traders-and-landlords-face-new-tax-rules-in-two-months), [ICAEW](https://www.icaew.com/technical/tax/making-tax-digital/mtd-guidance/mtd-and-income-tax), [Xero](https://www.xero.com/uk/programme/making-tax-digital/income-tax/)

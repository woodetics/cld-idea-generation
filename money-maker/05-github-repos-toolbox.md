# GitHub Repos and Tools Toolbox (the Lego bricks)

Open source repos are building blocks. The money is rarely in the repo itself. It's in (a) running it as a SERVICE for people who can't, (b) gluing two repos together into something new, or (c) hosting it for non-technical users (where the license allows).

Always check: license (MIT/Apache = do almost anything; AGPL = if you host it for others, you must share your modified source; "non-commercial" = can't sell), last commit date, open issues.

Note: star counts and repo activity below weren't all verified from this cloud session (GitHub API was blocked). Check each repo yourself before relying on it.

---

## Research / data gathering

| Repo / tool | What it does | Money angle |
|---|---|---|
| Panniantong/Agent-Reach (MIT) | One CLI for agents to read YouTube (subtitles, transcripts), Reddit, GitHub, Twitter/X, LinkedIn jobs, Bilibili, Xiaohongshu, V2EX, Xueqiu, web. JSON output. Read-only. | Trend research, lead research, content research, Chinese-platform trend arbitrage (G10), Reddit pain-point mining, YouTube transcript datasets. See `12`. |
| yt-dlp | Downloads video/audio/subtitles from YouTube and 1000+ sites | Clipping pipelines, transcript mining (respect platform terms and copyright) |
| OpenAI Whisper / faster-whisper | Speech-to-text, free, local | Captions, clip finding, podcast transcripts |
| Apify actors (not GitHub, but same idea) | Google Maps scrapers, "no website" lead finders ($2/1,000 results), dead-website checkers | Lead lists for every local service idea |
| Crawl4AI, Firecrawl (open source versions) | Turn websites into clean text for LLMs | Data products, directories, competitor monitoring |

## Video

| Repo | What it does | Money angle |
|---|---|---|
| remotion-dev/remotion + remotion-dev/skills | Video as React code; official Claude Code skills | Templated video services (V1, V8, G6) |
| calesthio/OpenMontage (AGPL-3.0) | Agentic video production system for Claude Code/Cursor; works offline with Piper TTS, FFmpeg, Remotion | Full faceless/explainer pipeline with zero API cost |
| harry0703/MoneyPrinterTurbo | Topic -> script -> stock footage -> TTS -> subtitles -> short video | Fast Shorts drafts (add transformation or it's "inauthentic") |
| OpenShorts | Self-hosted short-form generation + distribution | Clipping agency backend |
| Pixelle-Video | Automated short video engine | Same |
| AI-YouTube-Shorts-Generator | Cuts vertical clips from long videos | Podcast clipping (V3, V4) |
| Piper TTS, Kokoro TTS | Free local text-to-speech | Voiceovers with zero cost |
| FFmpeg | The Swiss army knife of video | Everything |
| Wan2.1, HunyuanVideo, LTX-Video, Mochi, CogVideoX | Open video generation models (need about 24GB VRAM) | Only via cloud GPU once you have paying clients |

## Automation

| Repo | What it does | Money angle |
|---|---|---|
| n8n-io/n8n (fair-code license, self-host free) | Workflow automation | Client automations, template sales (`08`) |
| Activepieces (MIT) | n8n alternative, more permissive license | Hosted white-label automation for clients |
| Model Context Protocol servers (modelcontextprotocol org) | Reference MCP servers | Fork + specialize for a niche tool (S11) |

## Trading / markets (high risk, see `07`)

| Repo | What it does | Note |
|---|---|---|
| Synpath-ai/prediction-market-arbitrage-trading-bot (MIT) | Scans Kalshi + Polymarket, paper trades, backtests | Use paper mode only. Sell alerts, don't trade with rent money. |
| ImMike/polymarket-arbitrage | Watches 10,000+ markets for inefficiencies | |
| AlexM800/poly-kalshi-arb | Scanner only, no trades | Safest starting point for an alerts product |
| Tydog99/Polymarket-Kalshi-Arbitrage-bot (Rust) | Arb bot with confirmation mode | |
| speedyhughes/kalshi-poly-arb | Cross-platform arb | |

## Website / app building

| Tool | Use |
|---|---|
| Next.js / Astro templates | Client sites, directories, pSEO sites |
| Supabase (free tier) | Database + auth for tiny SaaS |
| Vercel / Netlify / Cloudflare Pages | Free hosting for demos and client sites |
| Chrome extension MV3 boilerplates (e.g., Plasmo, WXT) | Reviving abandoned extensions (G9) |

---

## Remix patterns using repos (how to turn bricks into businesses)

1. Repo + niche = service. "OpenMontage, but I run it for dentists" (dental education Shorts).
2. Repo A + Repo B = new product. Agent-Reach (find trending Reddit questions) + Remotion (answer each as a video) = automatic "answers channel" for a niche brand.
3. Repo + hosting = SaaS (license permitting). Many self-hosted tools have no hosted version, and non-technical users would pay $9 to $29/month for someone else to run it.
4. Repo + data = data product. A scraper + a public dataset = a lead list subscription (G4).
5. Abandoned repo + fork = takeover. Popular repo, maintainer gone, users asking in issues "is this dead?" -> fork, fix, and offer paid support or a hosted version.

## How to find more bricks (on your own machine with Agent-Reach or just GitHub)

- GitHub search: `stars:>500 pushed:<2025-06-01` + a topic = popular but abandoned (takeover candidates).
- GitHub trending, weekly, in Python and TypeScript.
- Issues sorted by most reactions: "hosted version?", "is there a SaaS?", "can someone set this up for me?" = demand signals.
- Agent-Reach: `agent-reach github search "<topic>"`, then `agent-reach github read <repo>` to pull README + issues for Claude to analyze.

# Upskilling and Fast Cash

Two goals here: (1) money THIS month with no portfolio, and (2) the skills that will be worth the most in 6 to 12 months.

---

## Part 1: Cash floor jobs (apply day 1)

### AI training / data annotation

| Platform | Reported pay | Eligibility (sources conflict, check yourself) | Notes |
|---|---|---|---|
| Mercor | Avg contracted rate about $107 to $112/hr, range $10 to $190/hr by role | US/UK/CA/AU/IN+ or 107 countries depending on source | Expert roles (law, finance, medicine, coding) pay most. Has referral bonuses. |
| DataAnnotation | $20+ general; $50 to $100 coding/STEM/professional; up to $150+ coding | Reportedly US, UK, CA, AU only | PayPal payout. Qualification test. |
| Outlier | $10 to $50/hr by tier; one PH listing at $7/hr | 40+ or 117 countries depending on source | Needs ID + phone from your country. |
| Others to check | Alignerr, Turing, Invisible, Prolific (surveys), Appen, TELUS AI | varies | |

- Upwork reports AI data annotation demand +154% YoY.
- Pay is lower outside the US for the same task.
- These platforms generally prohibit using AI to complete tasks. Getting caught = removal and possibly unpaid work. That rule is strictly enforced, so don't risk your cash floor on it.
- Your edge as a "non-coder": many projects need generalist writers, raters, and domain experts (whatever you studied or worked in counts). Also, being fluent in English + another language (Tagalog, Spanish, etc.) qualifies you for multilingual projects that pay better than generic English rating.

### Other quick-cash with your existing skills

- Fiverr micro-gigs in the fastest-growing categories: "Claude Code setup", "n8n automation", "AI video editing", "faceless YouTube scripts + edits".
- Transcription/translation is DECLINING (-22 to -28%), so avoid plain versions. Sell AI-assisted localization with human QA instead.
- Upwork "quick fix" jobs: broken Google Sheets formulas, Zapier zap fixes, WordPress small fixes. Claude Code solves most in minutes.

---

## Part 2: The skills worth the most (12-month view)

Ranked by (demand growth) x (how well a non-coder + Claude Code can do it):

1. AI video production (Remotion, clipping, UGC, dubbing). +329% Upwork.
2. AI integration / automation (n8n, Make, Zapier, MCP, Claude skills). +178% Upwork.
3. Claude Code / agent setup and "agent ops". +938% Fiverr searches.
4. Sales and cold outreach. Not AI, but it's the bottleneck for EVERY idea in this folder. The person who can get clients beats the person who can build.
5. Copywriting in a specific voice (prompting Claude well = editing well).
6. Basic security literacy (for bug bounty later, and so you don't get your clients hacked).

## Part 3: A 30-day learning path for a non-coder

Week 1: Claude Code fundamentals
- Install Claude Code on your own computer (needs a Claude Pro plan).
- Learn: CLAUDE.md files, skills (SKILL.md), slash commands, plan mode, how to ask it to explain code.
- Build: a personal landing page, deploy to Vercel or Netlify.
- Build: your first skill (e.g., "write a cold email in my voice").

Week 2: Automation
- n8n (self-host free or use cloud trial) or Make free tier.
- Build: Google Form -> Google Sheet -> Claude summary -> email. Then: new Google review -> draft reply -> Slack/email.
- Learn: webhooks, APIs, JSON (Claude explains as you go).

Week 3: Video
- `npx create-video --yes --blank my-video` then add Remotion skills.
- Build: one stats video, one captioned clip, one listing-style slideshow.
- Try OpenMontage with free tools (Piper TTS + FFmpeg).

Week 4: Selling
- Write 3 offers (see `09`). Send 100 messages. Track replies.
- Package everything you built into portfolio videos.

## Part 4: Long-term upskill bets

- Bug bounty (LONG game, not fast cash): AI hackbots flood low-severity bugs (49% valid of 1,100+ reports), payouts shifting to business-logic and chained exploits, which 58% of researchers say AI misses. Median HackerOne payout reportedly about $450 (late 2025). Anthropic's program pays up to $15,000 per finding. Start with PortSwigger Web Security Academy (free), then HackerOne's AI "long tail" programs. AI red-teaming / prompt-injection testing is the newest area with the least competition.
- AI evaluation / red-teaming contractor work (Mercor-type roles pay well for people who understand how models fail).
- Becoming THE person in one niche (e.g., "AI automation for dental clinics in Australia"). Niche authority compounds.

## Part 5: Free learning sources

- Anthropic docs and courses (Claude Code docs, skills docs, Anthropic Academy / courses on prompt engineering and MCP).
- Remotion docs + remotion.dev/skills.
- n8n docs + community templates (study them, then build niche versions).
- PortSwigger Web Security Academy (security).
- YouTube: search the exact tool + "tutorial" and filter by last 3 months (AI tooling goes stale fast).

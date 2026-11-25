# Earning Projects (Claude Max as the engine)

These are NEW ideas, built by snapping together pieces of what people are doing with Claude right now (the raw pieces are in `01-raw-research-how-people-use-claude.md`). None of them is a copy of one repo or one person's business. Each one says where the building blocks came from, so you can go look at the originals yourself.

I also checked every idea against your `money-maker/` folder so this isn't a rerun. Where an idea is a cousin of something there, it says so.

How to read each card:
- Building blocks: the real repos or trends it's remixed from.
- The twist: the part nobody (or almost nobody) is selling yet.
- Who pays: buyer and a starting price. Prices are my estimates for Western buyers, not quotes from anywhere.
- How Max does the work: where your subscription earns its keep.
- Learn: which module in `04-learning-path.md` you need.
- Rules check: how it fits Anthropic's login rules (see `00-max-plan-facts-and-rules.md`).
- Speed / difficulty / fun: rough 1 to 5 scores.

## E1. Pocket Ops Manager for one-van trades businesses

What it is: a plumber, electrician or cleaner finishes a job and sends ONE voice note on Telegram ("Done at Mrs Patel's, replaced the valve, 2 hours, £180, she wants the boiler looked at in spring"). Their assistant turns it into a draft invoice, a job log row, a review request text for tomorrow, and a reminder for spring.

Building blocks: the Jarvis-over-Telegram repos (claude-telegram-relay, kirie, NanoClaw's Monday briefing), Channels, the bookkeeping skill packs (Dutch ZZP plugin, ai-bookkeeper), your money-maker S4 review desk.

The twist: everyone builds Jarvis for THEMSELVES. Nobody sells a boring, single-job Jarvis to people who hate admin and live on their phone. Tradespeople don't want "AI", they want their evenings back. You sell "no more paperwork after 6pm", not a chatbot.

Who pays: solo trades in the UK, AU, US, CA. Setup $300 to $600, then $49 to $99/month care plan.

How Max does the work: you use Max to BUILD the skills, the prompts, the job-sheet template and the install script once, then reuse them for every client.

Learn: Modules 1, 2, 3, 5, 7.

Rules check: two clean paths. Path A, the client gets their own Claude Pro ($20) and you install Claude Desktop/Cowork with their login on their machine (allowed). Path B, you run the bot on an API key, starting on your free $100/month API credit. Path B is smoother for the client and the one that scales.

Speed 3, difficulty 3, fun 3.

## E2. "Department by the Month" (your AI office, sold as one department)

What it is: you run a Paperclip-style agent office (researcher, writer, editor, SEO checker, designer) and rent it to a small B2B SaaS company as their content department. They don't buy "AI content", they buy a department with a weekly output quota.

Building blocks: Paperclip and its company playbooks, oh-my-claudecode teams, coreyhaines31/marketingskills (62k stars), claude-seo, the consultant who runs 15 agents and charged 4x.

The twist: give the client a READ-ONLY view of the agent board (who's working on what, what's in review). Agencies hide their process. You SHOW it, because watching a little office of agents work on their stuff is honestly the best sales demo there is. You stay as the editor-in-chief who approves everything before it ships (which also fixes the "241 emails, zero replies" problem, since a human checks the output).

Who pays: seed to Series A SaaS with no content hire. $800 to $2,000/month for, say, 4 articles + 8 social posts + 1 newsletter.

How Max does the work: this is the dream Max workload. Routines draft overnight, you review in the morning, Fable plans the monthly content strategy.

Learn: Modules 1, 2, 4, 6, and the parked AI office notes in `05-jarvis-and-ai-office-parked.md`.

Rules check: fine. You're doing the work with your own tools and selling the output.

Speed 2, difficulty 4, fun 5.

## E3. Listing Swarm Audits (Airbnb first)

What it is: an Airbnb host sends their listing link. A swarm of agents (photos, title, description, amenities, pricing vs nearby listings, reviews, house rules) each tears into one area, a verifier throws out anything without evidence, an editor writes a report with copy-paste fixes.

Building blocks: cr1707/shopify-audit-agents ("8 area leads, 24 specialists, a verifier and an editor. Evidence-only findings"), claude-seo's sub-agent structure, Claude in Chrome for reading pages.

The twist: the swarm-audit format exists for Shopify stores. Nobody's pointed it at Airbnb hosts, who are obsessed with occupancy and will pay to know why the place 3 doors down is booked solid. Same engine, then copy it to Etsy shops, Amazon listings, Kickstarter pages, Upwork profiles. ONE engine, many niches.

Who pays: Airbnb hosts and small property managers (US, UK, AU). $49 to $149 per audit, upsell $199 to rewrite and reshoot the photo order. Property managers with 10 to 30 listings can be a monthly deal.

How Max does the work: each audit is a big parallel job (perfect for subagents). Batch 5 audits a night.

Learn: Modules 1, 2, 4, 6.

Rules check: fine (you deliver a report).

Speed 4, difficulty 2, fun 4.

## E4. Exit Brain (sell the owner's head with the business)

What it is: a small business owner selling their business (a cleaning company, a print shop) has 15 years of "how we do things" in their head. That's what scares buyers. You run voice interviews (Claude as the interviewer, the owner just talks), then build a full operations vault: SOPs, supplier quirks, client notes, a CLAUDE.md so the NEW owner's Claude can answer "how do we handle X?" on day one.

Building blocks: the second-brain repos (claude-obsidian 16k stars, COG-second-brain's people CRM), "memory is a folder of markdown" from the Jarvis repos, your money-maker S6 "Ask My Business" bot.

The twist: S6 sells a bot to a business that's staying. Exit Brain sells to a business that's LEAVING, where the knowledge is worth real money in the sale price. And you don't chase owners one by one. You partner with business brokers, who want deals to close faster.

Who pays: owners selling businesses in the $200k to $2M range, via brokers. $1,500 to $5,000 per project, with a referral cut for the broker.

How Max does the work: transcribing, structuring and cross-linking hours of interviews into a clean vault is exactly what Claude Code does well (long, careful, file-heavy work).

Learn: Modules 1, 2, 3, 6.

Rules check: fine. The vault is plain markdown, the new owner uses their own Claude.

Speed 2, difficulty 3, fun 3. Hidden gem rating: HIGH, almost nobody does this.

## E5. Out-of-Stock Sniper

What it is: a daily (or hourly) watch on a seller's top 10 competitors. The second a rival product goes OUT OF STOCK or jumps its price, the seller gets a Telegram ping: "Competitor X is out of stock on the blue variant. Raise your ad budget now."

Building blocks: nickajulia/competitor-monitor-kit (daily price page checks), Routines for scheduling, Channels/Telegram for alerts, Amazon research tools (sorftime-seller-agent's "hidden profit" angle), your money-maker G15 competitor ad reports.

The twist: competitor monitoring tools report prices in a weekly dashboard nobody opens. The money is in the MOMENT a rival runs dry, because for a few days the buyers have nowhere else to go. You sell the moment, not the dashboard.

Who pays: Shopify and Amazon sellers doing $10k+/month. $29 to $99/month per store.

How Max does the work: you build and test the checker with Claude Code, run your first few clients' checks as Routines.

Learn: Modules 1, 2, 5, 7.

Rules check: for your first few clients you're doing a service. Once it's a self-serve product, move it to an API key (your $100 credit covers a LOT of small checks) or plain code with no AI at all for the checking part.

Speed 3, difficulty 3, fun 3.

## E6. One Country, One Paperwork Pain (flagship: UK Making Tax Digital)

What it is: a Claude skill pack plus setup that turns a sole trader's bank CSV and phone photos of receipts into clean, categorized quarterly records, ready to drop into their MTD software or hand to their accountant.

Building blocks: the country-specific bookkeeping packs found on GitHub (Dutch ZZP VAT plugin, Russian entrepreneur pack, UAE/Saudi/India VAT pack), ai-bookkeeper (bank PDF to reconciled sheet), your money-maker G20 profession skill packs.

The twist: the pattern is "one country, one deadline that scares people". The UK just handed you a big one. Since 6 April 2026, sole traders and landlords over £50,000 MUST keep digital records and send quarterly updates. From April 2027 that drops to £30,000, and to £20,000 in 2028. HMRC said 864,000 people were in the first wave alone. Most of them hate this.

Who pays: UK sole traders and small landlords. £29 to £79 for the skill pack, or £15 to £40/month done-for-you "record prep". Better yet, sell to small accounting firms who are drowning in new MTD clients (they buy the prep service at volume).

How Max does the work: building and testing the categorizer on fake data, writing the skill, writing the guides.

Learn: Modules 1, 2, 3.

Rules check: fine. Big other rule: you're doing record prep, NOT tax advice. Say so on everything and let an accountant or their software do the filing. Copy the pattern to Australia (BAS/GST), New Zealand (GST) or Ireland once the UK one works.

Speed 3, difficulty 3, fun 2. Hidden gem rating: HIGH, because the deadline does the selling for you.

## E7. Ad Copy Pre-Flight for regulated niches

What it is: before an agency runs an ad, they paste it in and get a "would this get us in trouble?" check: real estate fair housing words, supplement health claims, finance promos, before/after claims, "guaranteed" language.

Building blocks: TheProsperityAgent's Fair-Housing-compliant real estate skills, the pharma "what do LLMs say about us" monitor, the claude-seo pattern of one big skill with many sub-checks.

The twist: compliance tools exist for big banks and pharma at huge prices. Small agencies in these niches get nothing, and they get burned (ad accounts banned, angry clients). A cheap, fast, niche-specific "pre-flight" is a gap.

Who pays: small agencies running ads for realtors, supplements, coaches, mortgage brokers. $99 to $300/month, or $10 to $25 per check.

How Max does the work: building and testing the rule sets per niche, which is careful reading of rules and lots of example ads.

Learn: Modules 1, 2, 3.

Rules check: fine as a service you run. As a self-serve app, use an API key. Also, it's a "risk flag" tool, not legal advice. Say that clearly.

Speed 3, difficulty 3, fun 2.

## E8. AI Shelf Check for local businesses

What it is: you ask ChatGPT, Claude, Perplexity and Google's AI "best dentist in [town]" and screenshot the answers. Your client isn't there. Their competitor is. You sell the fix: schema markup, llms.txt, reviews push, Google Business Profile clean-up, citations.

Building blocks: claude-seo's "agent readiness" and GEO/AEO skills, Illyism/seo-skills, the pharma LLM-monitor idea, your money-maker G18 Google Business Profile sprint.

The twist: GEO audits are getting common, but they're PDFs full of jargon. Your pitch is just the screenshots. "When people ask AI for a dentist in your town, it sends them to Dr. Smith." That one image does the selling (it's honestly a little brutal).

Who pays: dentists, lawyers, clinics, home services. $150 for the screenshot audit (or free as a lead magnet), $300 to $800 for the fix.

How Max does the work: Claude in Chrome runs the queries, Claude Code builds the schema and llms.txt.

Learn: Modules 1, 2, 4.

Rules check: fine.

Speed 4, difficulty 2, fun 3.

## E9. Book Interior Desk

What it is: print-ready paperback and ebook formatting for self-published authors, done with Typst (code-based typesetting) instead of $250 Vellum or InDesign.

Building blocks: danielrosehill/KDP-Publishing-Plugin (Typst, KDP trim sizes), cdeistopened/book-studio, claude-book-publisher (KDP preflight checks), coloring-book-skill.

The twist: book formatting is a real, steady Fiverr/Reedsy market that authors already pay $100 to $400 for. Doing it with Claude + Typst means you can deliver in hours with a consistent quality check, and offer a "preflight guarantee" (if KDP rejects it, you fix it free) that hand-formatters can't afford to promise.

Who pays: indie authors (romance, fantasy, memoir, self-help). $99 to $299 per book, plus covers and large-print editions as upsells.

How Max does the work: the first 3 books are where you build your templates. After that, it's mostly reruns.

Learn: Modules 1, 2, 3.

Rules check: fine.

Speed 4, difficulty 2, fun 3.

## E10. Chat-Spike Clip Desk for niche live sports and events

What it is: small leagues and events (pickleball, local boxing, amateur esports, chess, college club sports) stream live but have NO media team. You watch the streams with an agent, catch the moments when chat goes wild, and turn them into captioned vertical clips the same night.

Building blocks: krishnasharma2212/stream-clip-machine (watches GTA streams, clips when chat explodes), the clipping skills (clipper, clipper-skill, video-podcast-clipper), your money-maker V3/V4 clipping.

The twist: V3/V4 are about clipping creators. Chat spikes as the signal is a neat trick, and pointing it at small LEAGUES means one client gives you dozens of matches a week and the players themselves share the clips (free distribution).

Who pays: league organizers, event promoters, small esports orgs. $300 to $1,000/month per league, or a revenue share on sponsorships you help them sell with the views.

How Max does the work: Claude picks moments and writes hooks, your PC does the cutting. A batch of streams overnight.

Learn: Modules 1, 2, 8.

Rules check: fine (you're clipping their own content with permission).

Speed 3, difficulty 3, fun 5.

## E11. The Import Channel (Chinese AI tools nobody in the West talks about)

What it is: a YouTube channel plus a GitHub org. Each video: "This Chinese AI tool has 22,000 stars and almost nobody here has heard of it." You test it, make an English tutorial, and publish an English port of its skills.

Building blocks: video-shotcraft (22k stars, Chinese, CapCut CN export), SoloMCN (Chinese short-video team), cc-connect (16k stars, built for Feishu/DingTalk first), Agent Reach's Bilibili, V2EX and Xiaohongshu channels, your money-maker G10 China-to-West trend reports.

The twist: G10 sells TREND reports to brands. This one is content plus ports, and you get paid three ways: YouTube ads, sponsorships from AI tool companies (they pay well for dev audiences), and selling or tipping on polished English ports. Your Agent Reach setup is a real edge here, most Western creators can't even read these sources.

Who pays: viewers (ads), AI tool sponsors ($300 to $3,000 per video once you have a few thousand subs), developers (ports and templates).

How Max does the work: reading Chinese READMEs and code, testing the tools, writing the English ports, drafting scripts.

Learn: Modules 1, 2, 8, and Agent Reach in `../money-maker/12-agent-reach-setup.md`.

Rules check: fine. Respect each repo's license when you port (MIT and Apache are friendly, keep the credit).

Speed 2, difficulty 3, fun 5.

## E12. Browser Game Micro-Studio

What it is: you run a small agent "game studio" that ships simple, polished HTML5 games fast, publishes them on web game portals and itch.io, watches which ones people actually replay, and doubles down on the winners.

Building blocks: Yakoub-ai/phaser4-gamedev, claude-unity-game-studio (49 agents, a whole studio hierarchy), everything-game-dev-code, claude-roblox-game-studio (Roblox variant).

The twist: everybody uses these studio setups to build ONE dream game and burns out. You use them like a casino. Ship small games quickly, let the numbers pick the winner, then polish only that one.

Who pays: web game portals pay revenue share on ads, itch.io has tips and sales, and a winner can go to Steam or mobile. Roblox pays creators through its exchange program. This is SLOW money, treat it as a fun side project that might pop.

How Max does the work: game dev is very Claude-heavy (code, levels, balancing, bug fixing). Great use of overnight builds.

Learn: Modules 1, 2, 4, 6.

Rules check: fine. Check each portal's rules on AI-made assets.

Speed 1, difficulty 3, fun 5.

## E13. "Bring Your ChatGPT Brain" migration

What it is: people switching from ChatGPT to Claude lose 2 years of "it knows me". You export their ChatGPT history, turn it into a clean personal knowledge vault (who they are, their projects, their writing voice, their preferences), and set it up as Claude Projects instructions, a CLAUDE.md, and a skill for their writing style.

Building blocks: charlie947/ai-second-brain (build a second brain from your ChatGPT and Claude history), claude-obsidian, agentmemory (30k stars), the writing-style skill idea (you already HAVE one of these in your own setup, so you know exactly what it's worth).

The twist: memory is the reason people don't switch AI tools. Selling the move as a one-time "white glove" service is something I didn't find anyone doing as a named offer.

Who pays: consultants, writers, coaches, founders switching to Claude. $49 to $149 personal, $300+ for a small team.

How Max does the work: chewing through huge export files and organizing them is perfect Claude Code work.

Learn: Modules 1, 2, 3.

Rules check: fine. Sensitive data though, so do it on THEIR machine or delete everything after, and say so in writing.

Speed 4, difficulty 2, fun 3. Hidden gem rating: HIGH (it's also great content for YouTube/TikTok, "I moved my whole ChatGPT memory into Claude").

## E14. Weekly Deal Sheet for small landlords and flippers

What it is: every Monday, a short list of the 10 best-looking properties in ONE city or ZIP code, with comps, rent estimates, cash-flow math and the red flags, so small investors don't spend their weekends on spreadsheets.

Building blocks: zubair-trabzada/ai-realestate-claude (comps, rental income, investment potential), cre-agent-skills (underwriting), Routines for the weekly run, your money-maker G23 real estate content machine.

The twist: the analysis tools exist, but they wait for the investor to bring a property. You flip it, the list comes TO them, pre-filtered, every week, for their one area.

Who pays: small landlords, flippers, house hackers in one metro. $29 to $99/month per area. Local investor meetups and Facebook groups are where you find them.

How Max does the work: the weekly Routine does the heavy lifting. You spot-check before sending.

Learn: Modules 1, 2, 5.

Rules check: fine on the Claude side. The gray part is getting listing data, see `03-gray-zone-projects.md` Z7.

Speed 3, difficulty 3, fun 3.

## E15. AI Micro-Drama Series (owned IP)

What it is: a short vertical drama series (1 to 2 minute episodes) made with AI video tools, in ONE niche genre with a hungry audience (office revenge, fantasy romance, sports underdog), released free on YouTube Shorts and TikTok, with later episodes behind a paywall or Shorts series subscription.

Building blocks: LordVayron/video-factory ("micro-dramas, sitcoms, fantasy shorts"), video-shotcraft, UGC-Factory's style skills, TikTok Series (paywall up to 80 videos), YouTube Shorts series subscriptions, TikTok's own paid microdrama app.

The twist: the big microdrama apps pay studios. Solo creators mostly make one-off AI clips. A consistent SERIES with recurring characters and cliffhangers is where the binge (and the paywall) lives, and the agent studio makes consistency cheap.

Who pays: viewers (paywall, subscriptions), platform payouts, brands (branded episodes). No reliable earnings data exists yet, so treat this as a bet.

How Max does the work: writing the series bible, scripts, shot lists, prompts for the video tools, and the edit (Remotion/ffmpeg).

Learn: Modules 1, 2, 8.

Rules check: fine. Video generation tools cost extra money though (your $50 budget won't stretch far here), so do this AFTER one of the faster ideas pays.

Speed 1, difficulty 4, fun 5.

## E16. Hackathon Circuit

What it is: online hackathons with cash prizes run every month. With Max you can build a working demo in a weekend that would take most solo entrants a month.

Building blocks: the "AI company battle" hackathon project (gladiator), every studio and team repo above, the overnight build ritual.

The twist: most people treat hackathons as fun. You treat them as a pipeline. Pick ones with sponsor prizes for using a specific tool (those categories often have few entries), and reuse winning demos as portfolio pieces for E1/E2 clients.

Who pays: sponsors and organizers, $500 to $10,000+ prizes. Also a portfolio and contacts.

How Max does the work: weekend sprints, Fable for the idea and architecture, Sonnet for the build.

Learn: Modules 1, 2, 4, 6.

Rules check: fine. Read each hackathon's rules on AI-assisted code (most allow it now, some don't).

Speed 2, difficulty 3, fun 5.

## Pure side projects (fun first, money maybe)

You said you also want projects on the side. These are for learning and fun, and each one teaches a module you'll reuse for money.

- S1. Your own morning brief: a Routine that reads your Gmail, calendar and 5 subreddits or YouTube channels you like, and sends you a 1-minute brief on Telegram at 7am. Teaches Routines, connectors, Channels.
- S2. A "watch my back" agent for game sales and free game drops (Steam, Epic, itch). Teaches scheduled checks and alerts. Very you, if you're the gamer type.
- S3. A voice-controlled "build buddy": talk out loud to plan a project, Claude writes the spec file, you approve, it builds overnight. (Basically your own version of ethanplusai/jarvis, but on Windows.)
- S4. A Claude skill of your OWN brain: your writing voice, your money-maker vault, your goals. You partly have this already. Make it travel with you to every project.
- S5. A tiny game in a weekend with Phaser (see E12), just to feel how far Claude Code can go.
- S6. Point Agent Reach at Bilibili/V2EX weekly and keep a "things the West hasn't noticed" log. Feeds E11 for free.

## My honest ranking for you right now

Fastest to first dollar: E3 (Listing Swarm Audits), E8 (AI Shelf Check), E9 (Book Interior Desk), E13 (ChatGPT Brain migration).

Best hidden gems (low competition): E4 (Exit Brain), E6 (UK MTD), E13.

Highest ceiling, slower: E2 (Department by the Month), E11 (Import Channel), E1 (Pocket Ops Manager once it's on an API key).

Most fun: E10, E11, E12, E15, E16.

If I had to pick ONE to start this week: E3. It needs no client relationship, the output is a document, you can make the first one for free on a friend's (or a random) Airbnb listing to show as a sample, and it teaches you subagents, which every other idea here needs.

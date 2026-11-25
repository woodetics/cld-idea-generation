# Hidden Gems (original remixes)

Each idea here is built by snapping together 2 or 3 proven building blocks from the research. The "Built from" line shows the bricks, so you can see the reasoning and remix further yourself.

Scoring (1 to 5): Speed = how fast to first dollar. Ceiling = how big it can get. Competition = 5 means almost nobody does it. Non-coder fit = how well Claude Code covers the technical side.

---

## G1. Website Rescue (dead sites, not missing sites)

- Built from: Apify actor that checks if a listed website is dead/parked/expired + "20+ reviews, no website converts 3x better" + Claude Code builds a site in an hour.
- The insight: everyone pitches businesses with NO website. Nobody targets businesses whose website DIED. Those owners already paid for a site once (they believe in it), and their Google listing is currently sending customers to an error page. That's a pain they'll feel the moment you show it.
- Find them: Google Maps scrape by niche + city -> keep businesses with a website URL -> check each URL (domain expired, parked "for sale" page, SSL error, 404, "account suspended" hosting page, site not updated since 2015).
- Offer: "Your Google listing sends people to a broken page. I rebuilt it, here's the live link: [demo]. Want me to put it on your domain?"
- Pricing: $300 to $600 setup + $29 to $49/month (hosting, edits, Google Business Profile updates).
- Bonus gray move: if their old domain EXPIRED and is available, you can register it (about $10) and point it to the new site. You then hold the asset they need. Be straight with them about it (sell it to them at cost + setup). Holding it hostage is where it turns into extortion, so don't.
- Scores: Speed 5, Ceiling 3, Competition 4, Non-coder fit 5.

## G2. Demo-First Proposals as a Product

- Built from: Upwork automation demand + Claude Code speed + "proof beats promises".
- Twist on S2: sell the SYSTEM to other freelancers. A Claude Code skill pack + n8n flow that watches Upwork/job boards, drafts a proposal, and scaffolds a demo project automatically.
- Pricing: $49 to $99 one-time, or $19/month with updates.
- Scores: Speed 3, Ceiling 3, Competition 3, Non-coder fit 4.

## G3. Competitor Review Gap Reports (lead magnet that sells itself)

- Built from: Google Maps review scraping + Claude analysis + local agency model.
- What: for a local business, scrape their top 5 competitors' Google reviews, and Claude writes a 2-page PDF: "What customers HATE about your competitors (and how to steal them)". E.g., "3 of your competitors get complaints about not answering the phone after 5pm."
- Use as a free door-opener for S3/S4/G1, or sell standalone at $49 to $99.
- Why it's a gem: owners LOVE reading about their competitors. Open rate is huge. And it naturally leads to "want me to fix that for you?"
- Scores: Speed 4, Ceiling 3, Competition 5, Non-coder fit 5.

## G4. New Business Filings Lead List (public records subscription)

- Built from: public state business registrations (new LLCs/corporations are public record in US states and UK Companies House) + scraping + B2B lead list demand.
- What: every day, new businesses register. They ALL need: an accountant, insurance, a website, a logo, a bank account, a business phone, payroll, signage. Service providers pay for fresh leads.
- Product: a weekly or daily CSV/email of new business filings in a specific state/county, filtered by industry, cleaned and enriched (Claude classifies the business type from the name and filing info).
- Sell to: local accountants/bookkeepers, insurance agents, web designers, sign shops, commercial cleaners, business bankers.
- Pricing: $49 to $199/month per county/state per buyer. Sell the same list to non-competing buyers (accountant AND insurance agent AND web designer).
- UK version: Companies House has a free official API. That's the easiest place to start technically.
- Gray notes: data is public, but some states restrict bulk commercial use or charge for bulk data. Read each state's terms. Email outreach by your buyers must follow CAN-SPAM/GDPR (UK/EU personal data rules are stricter, sole-trader data counts as personal data).
- Scores: Speed 3, Ceiling 4, Competition 4, Non-coder fit 4.

## G5. Building Permit Leads

- Built from: same public-records logic as G4 + contractor lead gen pricing ($25 to $100 per lead in rank-and-rent).
- What: many US cities publish building permit data (open data portals). A new pool permit = needs a fence, landscaping, lighting. A new roof permit = solar company lead. A new home = needs everything (blinds, security system, furniture, internet, landscaping).
- Product: weekly filtered permit lists by trade, sold to contractors.
- Pricing: $99 to $299/month per trade per city.
- Scores: Speed 3, Ceiling 4, Competition 4, Non-coder fit 4.

## G6. Changelog Videos for SaaS (video as code)

- Built from: Remotion + Claude Code skills + "every SaaS ships updates and nobody watches the changelog".
- What: SaaS companies publish changelogs/release notes. Almost none turn them into short videos. You build a Remotion template in THEIR brand, and every release becomes a 30 to 60 second video for Twitter/X, LinkedIn, YouTube Shorts, and their in-app "what's new".
- Why it's a gem: it's templated (cheap for you after the first one), recurring (they ship every week), and B2B (they pay in USD without blinking).
- Find clients: Product Hunt launches, "changelog" pages of small SaaS (5 to 50 employees), Indie Hackers, YC company lists.
- Pricing: $500 to $1,500/month for unlimited release videos, or $150 per video.
- Cold pitch: make their LAST changelog into a video for free and send it.
- Scores: Speed 3, Ceiling 5, Competition 5, Non-coder fit 4.

## G7. Bilingual AI Receptionist for Immigrant-Owned US Businesses

- Built from: AI receptionist resale ($400 to $800/client) + language arbitrage + an underserved segment.
- What: AI phone agent that handles calls in English AND Spanish (or Vietnamese, Korean, Chinese, Tagalog). Huge numbers of US small businesses are run by owners more comfortable in another language (nail salons, taquerias, auto shops, cleaning companies, remittance shops, dental clinics in immigrant neighborhoods).
- Why it's a gem: mainstream agencies pitch in English to English-speaking owners. You pitch in the owner's language. Your own multilingual ability is the moat (if you speak Tagalog, Filipino-owned businesses in the US are a natural first niche: care homes, caregiving agencies, restaurants, remittance and cargo shippers).
- Pricing: $297 setup + $247 to $497/month.
- Scores: Speed 3, Ceiling 4, Competition 5, Non-coder fit 4.

## G8. Twin Channels (localized clone channels on revenue share)

- Built from: YouTube auto-dub commoditized plain dubbing + localized markets still underserved + revenue share model (Linguana-style).
- What: find English creators with 20k to 300k subs and evergreen content (tutorials, explainers, documentaries). Offer: "I'll launch and run a Spanish (or German, or Portuguese) version of your channel. You pay nothing. We split revenue 50/50 (or 60/40 your favor)."
- Why separate channels beat auto-dub: native titles, native thumbnails, localized Shorts, cultural edits, local community replies, and YouTube recommends it to that language audience directly.
- Process: their video -> Whisper transcript -> Claude translation + cultural adaptation -> AI voice (with their permission, a voice clone of THEM speaking Spanish is the killer version) -> re-edit -> upload.
- Why it's a gem: no upfront cost for the creator = easy yes. You build equity in 5 to 10 channels.
- Contract: put the revenue split and channel ownership in writing (who owns the channel if you part ways).
- Scores: Speed 2, Ceiling 5, Competition 4, Non-coder fit 4.

## G9. Abandoned Extension Revival (fork, don't buy)

- Built from: abandoned Chrome extensions with users still searching for them + Manifest V3 forcing removals + Claude Code can do MV3 rewrites.
- What: find extensions removed for not upgrading to MV3 (or abandoned) that still have search demand in the Chrome Web Store. If open source (check license), fork it, rewrite for MV3 with Claude Code, publish your own version with a better UI. If closed source, rebuild the FUNCTIONALITY from scratch (don't copy code or branding).
- Monetize: freemium ($2 to $5/month pro features), one-time license, or a related SaaS.
- Score opportunities by keyword volume still owned, not install count.
- Avoid: buying extensions and injecting ads/affiliate links. That's exactly what gets reported (Save image as Type, the Socket wallet-drainer report) and Google bans it.
- Scores: Speed 2, Ceiling 4, Competition 4, Non-coder fit 3.

## G10. China-to-West Trend Arbitrage Reports

- Built from: Agent-Reach's Xiaohongshu (RedNote) + Bilibili channels + the pattern that consumer trends, product formats and content formats often show up in China before the West + TikTok Shop / Amazon sellers hungry for the next product.
- What: weekly report "What's blowing up on Xiaohongshu/Bilibili/Douyin that hasn't hit TikTok US yet": products, content formats, aesthetic trends, beauty/skincare, gadgets, kitchen tools, fitness formats. Claude translates and analyzes.
- Sell to: TikTok Shop sellers, Amazon FBA sellers, DTC brands, dropshippers, content agencies, trend forecasters.
- Pricing: $29 to $99/month newsletter (Substack/beehiiv paid tier), or $300 to $1,000 custom reports for brands.
- Why it's a gem: very few Western sellers can read these platforms. Agent-Reach makes it a CLI command. Language + tooling = moat.
- Free funnel: post the top 3 trends weekly as Shorts/threads, gate the full list.
- Scores: Speed 3, Ceiling 4, Competition 5, Non-coder fit 4.

## G11. Reddit Pain-Point Mining as a Service

- Built from: Agent-Reach Reddit channel (on your machine) + Claude analysis + founders/marketers wanting voice-of-customer data.
- What: "Send me your niche. I'll pull 1,000+ Reddit posts and comments where your customers complain, and deliver: top 20 pains, exact phrases they use (for ad copy), product gaps, competitor mentions."
- Sell to: SaaS founders, DTC brands, copywriters, agencies.
- Pricing: $97 to $497 per report.
- Product version: Notion/Sheets database of pains per niche, sold on Gumroad.
- Scores: Speed 4, Ceiling 3, Competition 3, Non-coder fit 5.

## G12. YouTube Transcript Datasets / "Expert Brain" Bots

- Built from: Agent-Reach YouTube subtitles + RAG chatbots + coaches/creators wanting to monetize their back catalog.
- What: take a creator's entire YouTube back catalog (their OWN content, with permission), turn it into a chatbot their fans pay to access ("Ask [Creator]'s brain", with timestamps linking to the exact video).
- Pricing: $1,000 to $3,000 setup + hosting, or revenue share on subscriptions ($5 to $15/month per fan).
- Scores: Speed 2, Ceiling 5, Competition 4, Non-coder fit 4.

## G13. Church / Sermon Clipping

- Built from: podcast clipping retainers + a massively underserved niche.
- What: thousands of US churches livestream every Sunday and post nothing else. You turn each sermon into 5 to 10 captioned clips, quote graphics, and a blog post.
- Pricing: $200 to $600/month per church.
- Why it's a gem: churches have budgets for media, the content is weekly (recurring), they rarely hire freelancers online, and they refer each other within networks/denominations.
- Scores: Speed 4, Ceiling 3, Competition 5, Non-coder fit 5.

## G14. Grant and RFP Radar for Small Nonprofits and Contractors

- Built from: public grant databases (Grants.gov, state portals, foundation lists) + public procurement RFPs (SAM.gov, state/city bid portals) + Claude matching and summarizing.
- What: weekly email of grants/bids matching a client's profile, with a plain-English summary and deadline. Upsell: AI-assisted first draft of the application.
- Pricing: $29 to $99/month (nonprofits), $99 to $299/month (contractors chasing government bids).
- Scores: Speed 3, Ceiling 4, Competition 3, Non-coder fit 4.

## G15. "Your Competitor's Ads" Swipe Reports

- Built from: public ad libraries (Meta Ad Library, TikTok Creative Center, Google Ads Transparency Center) + Claude analysis + AI UGC production (V5).
- What: monthly report of every ad a client's competitors are running, which ones run longest (= winners), the hooks used, and 5 AI UGC variants made from the winning angles.
- Pricing: $300 to $1,000/month.
- Why it's a gem: it bundles research with production. The report sells the ads.
- Scores: Speed 3, Ceiling 4, Competition 3, Non-coder fit 4.

## G16. Niche Job Board Fed by Public Listings

- Built from: Agent-Reach LinkedIn public jobs channel + job board model + affiliate/referral programs.
- What: a niche board like "Remote AI training jobs open to non-US workers" or "Claude Code / AI automation freelance gigs". Aggregate public listings, add filters nobody else has (country eligibility, pay rate).
- Monetize: featured posts ($49 to $199), newsletter sponsors, referral bonuses from platforms that pay for referrals (e.g., AI training platforms with referral programs).
- Scores: Speed 3, Ceiling 3, Competition 3, Non-coder fit 4.

## G17. Public-Domain History Shorts Channel (with a persona)

- Built from: YouTube inauthentic content rules (transformation needed) + free public-domain archival footage (NASA, Prelinger, Library of Congress, National Archives, Internet Archive) + Remotion captions.
- What: a history/science channel using REAL archival footage + a strong scripted narrative + a consistent persona and point of view. Real footage + original commentary is far safer than stock clips + AI voice.
- Monetize: YouTube Partner (long-form compilations of Shorts topics), sponsorships, a history newsletter, licensing your edits.
- Scores: Speed 2, Ceiling 4, Competition 3, Non-coder fit 5.

## G18. "Fix My Google Business Profile" Sprint

- Built from: local SEO + G1/G3 lead lists + the fact that half of Google Business Profiles have wrong hours, no photos, no posts, unanswered Q&A.
- What: $149 to $299 one-time sprint: fix categories, hours, services, description, add photos, seed Q&A, reply to all reviews, set up review link QR code. Upsell monthly posts + review replies (S4).
- Scores: Speed 5, Ceiling 2, Competition 3, Non-coder fit 5.

## G19. Hosted Version of a Popular Self-Hosted Tool

- Built from: GitHub issues asking "is there a hosted version?" + permissive licenses (MIT/Apache) + non-technical users willing to pay to avoid servers.
- What: pick a popular self-hostable tool with an MIT/Apache license and no official cloud offering. Offer a managed hosted version for $9 to $29/month.
- License: MIT/Apache = fine with attribution. AGPL = allowed, but you must publish your modifications. Check trademark (don't use their brand name as yours).
- Scores: Speed 2, Ceiling 4, Competition 3, Non-coder fit 3.

## G20. Skill Packs for Claude Cowork Users in One Profession

- Built from: Ryan Doser's $5k in 50 days at $99 (Claude skills product) + Claude Marketplace launch (Sept 2026) + professions that live in documents.
- What: "The Claude Skill Pack for Property Managers" (lease summaries, maintenance request triage, tenant emails, owner reports, vacancy listings). Repeat for: insurance agents, recruiters, mortgage brokers, paralegals, therapists (notes, careful with privacy), teachers, HR, bookkeepers.
- Pricing: $49 to $149 per pack. Bundle with a 30-minute setup call for $249.
- Distribution: niche Facebook groups, LinkedIn, Reddit communities for that profession, Claude Market (90% to you), MCP Market (85%), Gumroad/Lemon Squeezy.
- Scores: Speed 3, Ceiling 4, Competition 3, Non-coder fit 5.

## G21. AI Voice "Answering Service" for Overnight Only

- Built from: AI receptionist + the objection "I don't want a robot answering MY customers".
- What: only covers after-hours and overflow (nights, weekends, lunch rush). Easier yes, because it only catches calls that were being lost anyway.
- Pricing: $99 to $199/month (low friction entry), upsell full-day later.
- Scores: Speed 4, Ceiling 3, Competition 3, Non-coder fit 4.

## G22. Podcast Guest Booking Research

- Built from: podcast clipping research + Listen Notes data + founders who want PR.
- What: for a founder/coach, build a list of 50 podcasts that fit them (audience size, topic, contact), with a personalized pitch per show written by Claude. Optionally send the pitches for them.
- Pricing: $200 to $500 per list, or $1,000 to $2,000/month for booking service.
- Combo: then sell them clipping (V4) of every appearance.
- Scores: Speed 4, Ceiling 3, Competition 3, Non-coder fit 5.

## G23. Real Estate "Listing to Content" Machine

- Built from: V8 listing videos + listing descriptions + social posts + structured listing data.
- What: every new listing -> video + 3 social posts + email blast + property website page, generated automatically.
- Pricing: $199 to $499/month per agent, brokerage deals higher.
- Scores: Speed 3, Ceiling 4, Competition 3, Non-coder fit 4.

## G24. Reverse Clipping (clip the CLIENT's competitors' audience)

- Built from: Whop clipping (paid per view) + brands' desire for reach.
- What: pitch brands that DON'T have a Content Rewards campaign: "Set aside $1,000, pay me $2 per 1,000 views, I'll run a clipper team for you." You become the campaign manager, recruit clippers (pay them $1/1k), keep the spread.
- Why: you graduate from clipper to clipping agency without needing clients to trust you upfront (they pay per result).
- Scores: Speed 3, Ceiling 5, Competition 3, Non-coder fit 5.

---

## Shortlist for YOUR situation (broke, non-coder, Western buyers)

Start with one fast + one compounding:
- Fast: G1 Website Rescue, G18 GBP Sprint, G13 Church Clipping, G3 Review Gap Reports.
- Compounding: G6 Changelog Videos, G8 Twin Channels, G10 China Trend Reports, G20 Skill Packs, G4 Filings Lead List.

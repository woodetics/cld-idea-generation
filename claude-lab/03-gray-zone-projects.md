# Gray Zone Projects (Claude-powered)

Same deal as `../money-maker/07-gray-zone.md`: no lectures, just the actual mechanics of what can go wrong (bans, refunds, fines, lost accounts), so you can decide for yourself. The new ones here are the gray ideas that come out of how people use Claude agents specifically.

The biggest risk with any of these isn't a lawsuit. It's losing your Claude account, your YouTube channel or your Stripe account, which for someone starting from zero is basically the whole business. So each card has a "what you can lose" line.

## Z1. Format Bible reports for faceless channel builders

What it is: someone wants to start a faceless channel. You pick a channel that's winning, pull its last 50 videos (titles, transcripts, pacing, thumbnails, upload times), and write a "format bible": hook formulas, script structure, video length, posting rhythm, rough RPM, how crowded the niche is.

Building blocks: generalizingai/shadowcast ("paste a YouTube channel link, get your own original channel in that format"), faceless-youtube-agents ("clone any channel's style"), Agent Reach's YouTube subtitles.

Why it's gray: you're reverse engineering another creator's work and selling it. Analyzing public videos is fine. Copying their scripts, characters or exact look is NOT, and buyers will try to.

Who pays: faceless channel students in paid Discords/Whop groups. $29 to $99 per bible. Sell to the community owner as a bulk deal.

What you can lose: little for you. Your BUYERS can get hit with YouTube's "reused content" or "inauthentic content" demonetization if they copy too closely. Put "format, not copy" all over the report.

## Z2. Game economy arbitrage

What it is: some online games have real player economies (Path of Exile 2, EVE, MMOs, Steam marketplace items). Agents watch prices across markets and flag items that are cheap in one place and pricey in another.

Building blocks: vanzan01/poe2scout-mcp ("trading intelligence, arbitrage detection"), the trading desk repos.

Why it's gray: trading in-game with in-game currency is fine. Selling items or currency for REAL money (RMT) breaks most games' terms. Bots that trade automatically break them almost always.

Who pays: you (your own flipping), or other players for a paid alert Discord.

What you can lose: your game account and everything on it. Using Claude for analysis is fine, letting a bot click "buy" is where bans happen.

## Z3. Reverse recruiter with automation

What it is: job seekers pay you a monthly fee, an agent finds matching jobs, tailors their CV and cover letter for each, and you apply on their behalf.

Building blocks: MS-Jahan/job-apply-kit (staged, NEVER auto-submitted), job-apply-ai (auto-fills ATS forms), linkedin-easy-apply-automation.

Why it's gray: "reverse recruiters" are a real paid service. The gray part is automation. LinkedIn bans automated activity, and fully auto-submitted, spray-and-pray applications get people flagged.

Who pays: laid-off tech and corporate workers in the US, UK, CA. $150 to $400/month.

What you can lose: your CLIENT'S LinkedIn account (much worse than yours). The safer version is what job-apply-kit does: the agent prepares everything, a human clicks submit. Slower, but nobody gets banned.

## Z4. The "very fast human" freelancer

What it is: you take normal freelance jobs (data entry, research, transcription cleanup, spreadsheet work, VA tasks) on Upwork or Fiverr and Claude Cowork, computer use and browser agents do 90% of it. You deliver faster than anyone and check the work.

Building blocks: Cowork Dispatch and computer use, citrolabs/ego-lite (browser that shares your logged-in state with agents), browser-use/bux.

Why it's gray: many clients assume a human is doing the work. Some job posts now say "no AI". Some platforms ask you to disclose AI use.

Who pays: the usual freelance buyers. $10 to $40/hour equivalent, but you finish in a fraction of the time.

What you can lose: bad reviews or a platform account if a client finds AI mistakes you didn't check. Rule for yourself: never take a job that says "no AI", and ALWAYS check before delivering. Sometimes just saying "I use AI tools to work fast, which is why my price is low and my turnaround is same-day" turns the gray into a selling point.

## Z5. Signals desk (research, sold as alerts)

What it is: a multi-agent "trading desk" (news reader, chart reader, risk checker) writes a daily market brief, and you sell access to a paid Telegram or Discord.

Building blocks: crypto-claude-desk (6 agents, 66 tools), hypergrok-trading-desk (research first, execution needs approved tickets), claude-trading-desk ("honestly backtest, paper trade"), Telegram alerts from the gold bot repo.

Why it's gray: in many countries, telling paying people what to buy is regulated advice. "Signals groups" also have a scammy reputation, so trust is hard.

Who pays: retail traders. $15 to $50/month per member.

What you can lose: legal trouble in strict countries, refund wars, a reputation hit. The safer framing is "research and education, not advice", PAPER trades only, and a public record of every call (wins AND losses). If you can't show an honest track record after 3 months of paper trading, don't sell it.

## Z6. Bounty grinding (DON'T, and here's the flip)

What it is: point agents at open-source bounties (Algora and others) and submit fixes for cash.

Why it's not worth it: research found the public bounty market "broken in 2026". Fresh Algora bounties get 8 to 158 competing PRs within hours. Maintainers are drowning in AI pull requests. curl killed its six-year bug bounty in January 2026 because of AI slop, ESLint killed its paid contributor program, Ghostty restricted AI contributions. You'd be one more bot in a bot farm.

The flip: sell to the OTHER side. Open-source companies (the ones with a paid product on top of an open repo) need an AI-slop filter for incoming PRs and issues. Set up a triage agent on their GitHub (on their API key) that labels, dedupes and flags low-effort PRs. $500 to $1,500 setup.

What you can lose (if you grind anyway): your GitHub reputation. Some maintainers now ban accounts that send AI slop.

## Z7. Scraped deal and lead data

What it is: data feeds built from scraping public listing sites (property portals, Google Maps, marketplaces). Powers the E14 Deal Sheet and lots of lead-gen.

Building blocks: google-maps-scraper-kit (no API key), gmapsscraper skills, ff-ruyijs ("navigate through various web protection systems").

Why it's gray: most big sites ban scraping in their terms. Courts in the US have often said scraping PUBLIC data isn't hacking, but you can still get blocked, sued for breach of terms, or get in trouble under privacy laws (GDPR in the UK and EU) if you collect personal data like emails and phone numbers.

What you can lose: IP bans (annoying, not fatal), a cease and desist (scary, usually just means stop), GDPR fines if you sell personal data of people in the UK/EU (actually serious). Business data (a company's name, address, website) is much safer than personal data.

## Z8. AI-hosted persona channels

What it is: a YouTube or TikTok channel hosted by an AI character (consistent face, voice, personality) who reviews, explains or tells stories.

Building blocks: Jarvis-style voice repos (Fish Audio voices), video-factory, UGC reaction studio, claude-motion-faceless-skills.

Why it's gray: YouTube requires you to disclose realistic altered or synthetic content. Characters that look like REAL people are a big no. Undisclosed "realistic human" AI hosts can get you demonetized.

What you can lose: monetization, or the channel. Cartoon, stylized or obviously-AI hosts with the disclosure ticked are much safer, and audiences honestly don't mind as much as you'd think.

## Z9. Hosting Claude Code for clients (gray-but-allowed, if you do it right)

What it is: you rent a VPS per client, install the unmodified Claude Code plus their Jarvis setup (Telegram, memory vault, skills), and THEY log in with their own Claude subscription. You charge for setup and hosting.

Why it looks gray but isn't (if done right): Anthropic's legal page explicitly allows "an end user signing in to the unmodified Claude Code binary with their own Claude subscription, including where a platform hosts Claude Code".

Where it turns black: you log in with YOUR Max and let clients share it, you store their Claude login, or you modify Claude Code. Anthropic says it can enforce "without prior notice", so this is how you lose your account.

Who pays: busy professionals who want a Jarvis but will never touch a terminal. $200 to $500 setup, $30 to $80/month hosting and care.

What you can lose: done right, nothing beyond normal client headaches. Done wrong, your Claude account.

## Z10. Sharing or reselling Max (DON'T)

What it is: splitting one Max plan with friends, or selling "Claude access" off your account.

Why not: it breaks the terms in the clearest way possible, it's easy to detect (logins from many places, heavy parallel use), and the person who loses is YOU, the account owner. The ban in April 2026 showed Anthropic will act on subscription misuse. Not worth it for a few bucks a month.

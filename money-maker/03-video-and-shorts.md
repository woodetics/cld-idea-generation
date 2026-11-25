# Video Generation and Shorts

The single fastest-growing AI skill on Upwork is AI video generation and editing (+329% YoY). Fiverr reports AI video/animation +278% and faceless YouTube +488%. Video is where the demand is.

BUT: YouTube's inauthentic content policy (July 2025, enforced hard in Jan 2026: 16 channels removed, one with 4.7B views) kills mass-produced, low-effort AI channels. So the money is in:
1. Making video FOR other people (service), where they own the channel risk.
2. Making video that's actually transformative (real angle, real script, persona).
3. Getting paid per view by brands (clipping), not by YouTube ads.

---

## The core toolchain (cheap or free)

| Job | Free option | Paid option |
|---|---|---|
| Video as code (templated motion graphics) | Remotion + Claude Code with `npx skills add remotion-dev/skills` | Remotion company license if you grow |
| Full agentic production pipeline | OpenMontage (AGPL, works offline with Piper TTS, FFmpeg, Remotion) | Add fal.ai / ElevenLabs / HeyGen keys |
| Shorts from long video | AI-YouTube-Shorts-Generator (GitHub), OpusClip free tier, CapCut | OpusClip $15 to $29/month |
| Topic-to-short generator | MoneyPrinterTurbo, Pixelle-Video, OpenShorts | |
| Voice | Piper TTS, Kokoro (open source TTS) | ElevenLabs |
| Captions | Remotion captions skill, CapCut auto captions, Whisper | |
| Stock footage | Pexels, Pixabay, public domain archives (NASA, Prelinger, Library of Congress, Internet Archive) | Storyblocks |
| Editing | CapCut, DaVinci Resolve (free) | |
| AI avatars / UGC | | HeyGen, Arcads-type tools, Creatify (paid) |
| Local video gen models | Wan2.1, HunyuanVideo, LTX-Video (need about 24GB VRAM, so cloud only) | fal.ai / Replicate per-second pricing |

---

## V1. Remotion Video Factory (service)

- What: Claude Code + Remotion skills = you describe a video, Claude writes React code, it renders an MP4. Perfect for TEMPLATED videos.
- Videos it's great at: stat/data videos, listicles, kinetic typography quotes, product feature explainers, changelog videos, "year in review", podcast audiograms, animated charts, real estate listing slideshows with motion, event promos, YouTube intros, captioned talking-head overlays.
- Sell to: SaaS companies, agencies, real estate agents, coaches, newsletters (turn issues into videos).
- Pricing: $75 to $300 per video, or $500 to $1,500/month for 8 to 20 videos.
- The trick: once one template exists, each new video is minutes of work. Your margin climbs every month.
- See also: `06` G6 (Changelog videos for SaaS) which is the sharpest version.

## V2. Faceless channel done RIGHT (owned channel)

Only do this if you accept it's a 3 to 9 month bet.

Rules to survive the inauthentic content policy:
- A consistent persona/voice and a POINT OF VIEW (opinions, rankings, verdicts).
- Original script every time (Claude writes the draft, you inject the angle and facts).
- Transformation: commentary over footage, original analysis, data you compiled.
- No AI "experts" on health, finance or legal topics.
- Lower volume, higher quality. 3 to 5 good videos/week beats 3 per day.

Niche selection (RPM varies several-fold between sources, so use as direction only):
- Higher RPM: personal finance, investing, B2B/SaaS, tech/AI tools, real estate, digital marketing.
- Lower RPM: gaming, memes, entertainment, food, kids stories.
- Shorts RPM is tiny (about $0.01 to $0.80 per 1,000 views depending on niche and source). Shorts are a FUNNEL, not the income. Monetize with affiliate links, a product, a newsletter, or a service.

Faceless angles that are transformative by nature (remix-ready):
- "I tested X so you don't have to" with screen recordings (AI tools, apps, SaaS). Your screen = original footage.
- Public-domain archive history: real archival footage (NASA, Prelinger, Library of Congress) + a strong narrative script. Real footage + commentary passes the "transformation" bar much better than stock clips.
- Data stories: "What 10,000 Reddit posts say about X" (Agent-Reach makes this easy on your own machine). Original data = original content.
- Software tutorial channels for boring business software (QuickBooks, Airtable, GoHighLevel, n8n). High RPM, B2B, and you can sell services to viewers.
- Local-government/public-records explainers (permits, zoning, property tax appeals) per US state. High intent viewers.

## V3. Whop Clipping (no client needed)

- Pay: median about $1.30 per 1,000 views (Oct 2026 sample of 100 campaigns), range $0.20 to $6. Only 12% of campaigns pay $3+. Typical cap about $200 per clip. Whop takes 10%.
- Payout about every 10 days. Watch for: view rejections, bot flags, holds up to 90 days.
- Process: pick a campaign with a big budget left and a rate above $1.50 -> download source content -> cut 20 to 45 second clips with the strongest hook in the first 2 seconds -> big captions -> post to TikTok, Reels, Shorts (separate accounts per niche) -> submit links.
- Build your own pipeline with Claude Code: transcript (Whisper) -> Claude picks the 5 most "hooky" moments with timestamps -> FFmpeg cuts -> auto captions -> you review and post. This turns 1 hour of footage into 10 clips in minutes.
- Highest-paying campaigns tend to be gambling and crypto brands (e.g., Roobet $1.50/1k with a $250k budget, MUTUUM $6/1k). Gray, but legal in many places. Your call.
- Use it as: cash, plus PROOF that you can make clips that get views. Then sell V4.

## V4. Podcast / Creator Clipping Retainer (the grown-up version of V3)

- Benchmark pricing: Fame Clips $700/month for 15 clips, $1,000 for 25, $2,350 for 60, first clip free. Castos $990/month for 4 clips per episode. Full production agencies $2,000 to $20,000+/month.
- Your offer: "15 clips/month, captioned, posted for you on 3 platforms, $497/month. First 3 clips free."
- Why they buy despite OpusClip existing: OpusClip leaves posting/scheduling and judgment to the creator. You sell DONE, not software.
- Targets: B2B podcasts (founders, SaaS, marketing, finance), coaches with YouTube channels, church sermons (huge underserved niche), local real estate podcasts, university lecture channels.
- Find them: Apple Podcasts / Spotify charts by category, Listen Notes, YouTube search "podcast" + niche with 1k to 50k subs (big enough to pay, small enough to not have a team).

## V5. AI UGC Ads for brands and TikTok Shop sellers

- Arbitrage: AI production cost about $1 to $13 per ad. Human UGC $150 to $400. Agencies $300 to $800 per variant. Retainers $2,000 to $3,000/month for indie operators doing 15 to 30 videos.
- Your offer: "10 AI UGC ad variants for $397" (still a fraction of human cost) or "$1,500/month for 20 ads + monthly winners report".
- Who: DTC Shopify brands doing $10k to $200k/month, TikTok Shop sellers, app developers (app install ads), supplement/skincare brands (careful with health claims).
- Where AI wins: testing hooks at volume. Where it loses: anything needing a real creator account. Pitch it as "hook testing at scale" so you don't compete with real creators.
- Gray zone: AI avatars that look like real people "reviewing" a product. FTC endorsement rules and TikTok's AI-generated content labels apply. Label it as AI-generated, and don't fake testimonials (fake reviews/testimonials are where fines happen). See `07`.

## V6. Localization / Dubbing Service

- YouTube opened auto-dubbing to all eligible channels Feb 2026 (27 languages). So plain dubbing is commoditized.
- What's NOT commoditized: separate localized channels (native titles, thumbnails, cultural edits, localized Shorts, community management). See `06` G8 for the revenue-share version.
- Targets: German, French, Spanish (US Hispanic + Spain), Portuguese (Brazil), Japanese. Spanish/Portuguese = volume; German/Japanese = better CPM.
- Pricing: $3 to $10 per finished minute, or revenue share 30 to 50% of the localized channel.

## V7. "Video Newsletter" Repurposing

- What: take a newsletter writer's weekly issue and turn it into 1 long video + 5 Shorts + 1 carousel, automatically (Claude Code + Remotion + TTS or their own voice clone with permission).
- Who: Substack/beehiiv writers with 5k+ subscribers who aren't on video yet.
- Pricing: $300 to $800/month.

## V8. Real Estate Listing Videos at Scale

- What: every new listing -> auto-generated vertical video (photos + motion + price + captions + agent branding) via Remotion template.
- Who: real estate agents and brokerages (US/UK/AU/CA).
- Pricing: $25 to $50 per listing video, or $199 to $499/month unlimited for an agent, more for a brokerage.
- Why it's a gem: listing data is structured (address, price, beds, photos), perfect for code-generated video. Agents need volume.

## V9. Course Creator "Lesson to Shorts" Engine

- What: take a course creator's lessons, cut and caption the best teaching moments, post daily as free value that funnels to the course.
- Pricing: $500 to $1,500/month, or a % of course sales attributed via a tracked link.

---

## The traps (read before spending a dollar)

- Buying "faceless channel automation" courses. They sell the dream to broke people.
- Volume-only AI channels. That's exactly what YouTube removes.
- Renting GPUs to run local video models before you have a paying client.
- Expensive avatar tools before you have a client. Use free trials to make your demo.

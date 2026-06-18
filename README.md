# FoneClaw — Android AI Phone Assistant

> **Say it. Done.**  
> FoneClaw is the Android AI agent that actually controls your phone — not just answers questions.

---

## What is FoneClaw?

FoneClaw is an independent Android AI Phone Assistant that executes real phone actions through voice commands. It supports **120+ supported Android actions** across **16 feature categories** on **Android 9+** devices.

Unlike cloud-based AI assistants that only generate text, FoneClaw reads your screen, identifies interface elements, and executes physical taps and swipes — like a human finger.

## Key Features

| Category | Examples |
|----------|----------|
| **Daily Briefing** | Weather, calendar, notifications summary |
| **Phone Health** | Battery, storage, app status monitoring |
| **Passive Triggers** | Automated routines based on time/location/context |
| **Messaging** | Draft, reply, and manage SMS, WhatsApp, Telegram |
| **Media Control** | YouTube, Spotify, podcast playback |
| **Navigation** | Maps, directions, location sharing |
| **Smart Home** | IoT device control via phone apps |
| **120+ actions** | Full list on [foneclaw.ai/features](https://www.foneclaw.ai/features) |

## How It Works

1. **Install** from Google Play Store
2. **Grant permissions** — transparent, user-controlled
3. **Speak commands** — "Send a message to Mom saying I'll be late"
4. **FoneClaw executes** — opens apps, navigates screens, performs actions
5. **Sensitive actions require confirmation** — you stay in control

## Privacy & Security

- **Local-first processing** — core phone control runs on your Android device
- **Transparent permissions** — you see and approve what FoneClaw can access
- **Confirmation for sensitive actions** — messages, calls, purchases require your review
- **No hidden data collection** — FoneClaw does not sell your data

## Project Structure

```
foneclaw-v2/
├── build_multi.py              # Build system — generates all HTML pages
├── _components.py              # Shared components (nav, footer, CTA)
├── _homepage.py                # Homepage generator
├── _features_page.py           # Features page generator
├── _article_template.py        # Article page template
├── _hub_pages.py               # Category hub pages
├── _subhub_pages.py            # Sub-category pages
├── articles_batch*.py          # Article source content (125+ articles)
├── batch*_data.json            # Article data files
├── article_keywords_data.py    # Internal linking keywords
├── compress_images.py          # Image optimization
└── images/                     # Static assets
```

## Building

```bash
python3 build_multi.py
# Generates: index.html, features.html, 125+ article pages, hub pages, sitemap.xml
```

## Links

- **Website**: [foneclaw.ai](https://www.foneclaw.ai)
- **Download**: [foneclaw.ai/download](https://www.foneclaw.ai/download)
- **Features**: [foneclaw.ai/features](https://www.foneclaw.ai/features)
- **Blog**: [foneclaw.ai/resources](https://www.foneclaw.ai/resources)

## Competitive Landscape

FoneClaw operates in the growing Android AI agent space:

| Agent | Focus | Platform |
|-------|-------|----------|
| **FoneClaw** | Phone action execution | Android 9+ |
| **Gemini Intelligence** | Google ecosystem AI | Pixel / Android |
| **MiClaw** | Xiaomi phone agent | Xiaomi devices |
| **Samsung Galaxy AI** | On-device AI features | Samsung devices |

FoneClaw is **independent** — not owned by any phone manufacturer. It works across Android devices from any brand.

## License

Proprietary — FoneClaw is a commercial product by an independent company.

---

*FoneClaw is not affiliated with Xiaomi, Google, Samsung, or any other phone manufacturer. Android is a trademark of Google LLC.*

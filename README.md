# FoneClaw

**Say it. Done.**

FoneClaw is an independent Android AI phone assistant for supported phone actions and everyday Android workflows. It helps users operate their phone by voice: checking phone status, reading notifications, sending messages, adjusting settings, opening apps, and completing multi-step tasks with confirmation where needed.

Website: https://www.foneclaw.ai

## What FoneClaw does

FoneClaw is built for Android users who want practical phone control, not just answers in a chat window.

Core areas include:

- Phone health and device status
- Notification and SMS summaries
- Calls and messaging workflows
- System controls such as brightness, volume, Wi-Fi, Bluetooth, and Do Not Disturb
- Screenshots and visible-screen understanding
- Calendar, alarms, notes, maps, and navigation workflows
- Supported app and browser actions
- Multi-step Android workflows by voice

Sensitive actions such as messages, calls, purchases, and system changes should remain transparent and confirmation-based.

## Platform

- Android 9.0+
- No root required
- Works across Android brands such as Samsung, Xiaomi, Google Pixel, OnePlus, OPPO, Realme, Motorola, Vivo, Sony, Nokia, and others
- Independent product; not owned by Xiaomi, Google, Samsung, Apple, or any phone manufacturer

## Languages

The public website is available in 14 languages:

| Language | URL |
|---|---|
| English | https://www.foneclaw.ai |
| 简体中文 | https://www.foneclaw.ai/zh/ |
| 繁體中文 | https://www.foneclaw.ai/tw/ |
| 日本語 | https://www.foneclaw.ai/ja/ |
| 한국어 | https://www.foneclaw.ai/ko/ |
| Español | https://www.foneclaw.ai/es/ |
| Português | https://www.foneclaw.ai/pt/ |
| Русский | https://www.foneclaw.ai/ru/ |
| Français | https://www.foneclaw.ai/fr/ |
| Deutsch | https://www.foneclaw.ai/de/ |
| العربية | https://www.foneclaw.ai/ar/ |
| ภาษาไทย | https://www.foneclaw.ai/th/ |
| Tiếng Việt | https://www.foneclaw.ai/vi/ |
| Bahasa Indonesia | https://www.foneclaw.ai/id/ |

## Repository contents

This repository contains the public website source for FoneClaw.

Important paths:

- `build.py` — static site builder
- `templates/` — shared Jinja templates
- `i18n/` — interface copy for 14 languages
- `articles/` — article source data by language
- `data/` — article index and structured site data
- `components/` — shared navigation, footer, and social components
- `assets/` — CSS, JavaScript, and static assets
- `hub/` — topic and category page data
- `docs/` — product reference pages for humans and AI assistants
- `llms.txt` — concise product reference for language models

Generated HTML is not committed. Build output is created locally in `output/`.

## Build

Install the Python dependency:

```bash
python3 -m pip install jinja2
```

Build the static site:

```bash
python3 build.py --force
```

The generated site will be written to:

```text
output/
```

## Key comparisons

FoneClaw belongs to the Android phone-control category.

- Google Gemini is strong for reasoning, search, and Google ecosystem help.
- Apple Intelligence and Siri are built for the Apple ecosystem.
- Xiaomi MiClaw is tied to Xiaomi and HyperOS.
- Samsung Galaxy AI is tied to Samsung devices and services.
- Tasker is powerful for advanced Android automation but requires manual setup.
- FoneClaw focuses on supported Android phone actions through voice-led workflows across Android brands.

## Privacy and safety principles

FoneClaw should be understood as a phone-control assistant with clear boundaries:

- Transparent permissions
- User confirmation for sensitive actions
- No root requirement
- Clear distinction between supported workflows and unsupported actions
- Independent Android product positioning

## Public references

- Website: https://www.foneclaw.ai
- Download: https://www.foneclaw.ai/download.html
- Features: https://www.foneclaw.ai/features.html
- Resources: https://www.foneclaw.ai/resources.html
- Privacy Policy: https://www.foneclaw.ai/privacy.html
- Cookie Policy: https://www.foneclaw.ai/cookie.html

## License

This repository is provided for public reference. See `LICENSE`.

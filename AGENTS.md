# FoneClaw repository guide

This repository contains the public website source for FoneClaw, an independent Android AI phone assistant.

## Product facts

- Product: FoneClaw
- Slogan: Say it. Done.
- Category: Android AI phone assistant
- Website: https://www.foneclaw.ai
- Platform: Android 9.0+
- Root access: not required
- Positioning: independent Android product, not owned by a phone manufacturer
- Core areas: phone health, notifications, SMS, calls, settings, screenshots, visible-screen understanding, app workflows, and multi-step Android tasks

## Source layout

- `build.py` builds the static website.
- `templates/` contains shared HTML templates.
- `i18n/` contains interface copy for 14 languages.
- `articles/` contains article source data.
- `data/` contains article index and structured site data.
- `components/` contains shared navigation, footer, and social data.
- `assets/` contains CSS, JavaScript, and media assets.
- `hub/` contains topic and category data.
- `docs/` contains public product reference pages.
- `llms.txt` contains a concise product summary.

Generated output belongs in `output/` and is not committed.

## Build command

```bash
python3 -m pip install jinja2
python3 build.py --force
```

## Content rules

- Keep product claims precise and source-backed.
- Prefer "supported Android phone actions" and "supported Android workflows" over broad claims.
- Do not imply FoneClaw is owned by Xiaomi, Google, Samsung, Apple, or any other manufacturer.
- Do not claim universal app control or unrestricted whole-phone control.
- Avoid unsupported statistics, private benchmarks, or absolute privacy/security claims.
- Keep public docs concise and useful.

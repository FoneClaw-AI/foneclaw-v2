#!/usr/bin/env python3
"""Localize 4 zh article JSON files: body_html, faq, toc, summary."""
import json, os, glob

DIR = os.path.dirname(os.path.abspath(__file__))

# Read all body text files
body_files = sorted(glob.glob(os.path.join(DIR, '*_body.html')))
bodies = {}
for bf in body_files:
    key = os.path.basename(bf).replace('_body.html', '')
    with open(bf, 'r', encoding='utf-8') as f:
        bodies[key] = f.read().strip()

# Read all metadata text files
meta_files = sorted(glob.glob(os.path.join(DIR, '*_meta.json')))
metas = {}
for mf in meta_files:
    key = os.path.basename(mf).replace('_meta.json', '')
    with open(mf, 'r', encoding='utf-8') as f:
        metas[key] = json.load(f)

# Apply updates
json_files = [
    'voice-control-visually-impaired.json',
    'voice-control-whatsapp.json',
    'wwdc-2026-ai-do-over-phone-agent.json',
    'xiaomi-ai-ecosystem-2026.json',
]

for fname in json_files:
    key = fname.replace('.json', '')
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    if key in bodies:
        data['body_html'] = bodies[key]
    if key in metas:
        data['faq'] = metas[key]['faq']
        data['toc'] = metas[key]['toc']
        data['summary'] = metas[key]['summary']

    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)

    print(f'Updated: {fname}')

print('\nDone.')

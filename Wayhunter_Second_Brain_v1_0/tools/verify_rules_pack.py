#!/usr/bin/env python3
"""Offline consistency check for Second Brain source PDF hashes and copied ACTIVE_RULES."""
from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'SOURCE_MANIFEST.json').read_text('utf-8'))
issues=[]
for f in manifest['sources']:
 p=root/f['file']
 if not p.is_file(): issues.append('Missing source: '+str(p));continue
 if hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']: issues.append('Changed source: '+str(p))
canonical=(root/'knowledge/LATEST_APPROVED_2026-11-11.md').read_bytes()
for d in ['angular-admin','flutter-mobile','aspnet-backend']:
 p=root/f'repo_overlays/{d}/docs/second-brain/ACTIVE_RULES.md'
 if not p.is_file() or p.read_bytes()!=canonical: issues.append('Active rules drift: '+str(p))
if issues:
 print('\n'.join(issues));sys.exit(1)
print('PASS: source PDFs unchanged and 3 repo overlay active rules synchronized. This does not test app code.')

#!/usr/bin/env python3
"""Read-only inventory of local clones. No uploads, writes, network, or code changes."""
from pathlib import Path
from datetime import datetime, timezone
import argparse

p=argparse.ArgumentParser()
p.add_argument('--admin',type=Path,required=True)
p.add_argument('--flutter',type=Path,required=True)
p.add_argument('--backend',type=Path,required=True)
a=p.parse_args()
skip={'node_modules','.git','.dart_tool','.angular','build','bin','obj','.idea','.vs','.vscode','dist','coverage','.next','Pods'}
print('# Wayhunter read-only local file inventory')
print(f"Created: {datetime.now(timezone.utc).isoformat()}")
for label,folder in [('Angular Admin',a.admin),('Flutter',a.flutter),('Backend',a.backend)]:
    print(f'\n## {label}\nPath: `{folder}`')
    if not folder.exists() or not folder.is_dir():
        print('**MISSING or inaccessible**')
        continue
    files=[]
    for q in folder.rglob('*'):
        if any(x in skip for x in q.relative_to(folder).parts): continue
        if q.is_file(): files.append(q.relative_to(folder).as_posix())
    print(f'Files (excluding build/cache directories): {len(files)}')
    for f in sorted(files)[:250]: print('- '+f)
    if len(files)>250: print(f'- ... {len(files)-250} additional files omitted')
print('\nNOTE: Listing is not a functional code audit.')

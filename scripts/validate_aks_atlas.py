#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
atlas = root / 'aks-troubleshooting'
files = [sorted((atlas / level).glob('*.md')) for level in ('beginner','intermediate','advanced')]
flat = [p for group in files for p in group]
assert len(flat) == 30, f'expected 30 runbooks, found {len(flat)}'
ids=[]
required=['## Think first','## First evidence','## Common root causes','## Resolution path','## Verify','## Escalate with evidence','## Sources']
for path in flat:
    text=path.read_text()
    match=re.search(r'^# ([BIA]\d{2}):',text,re.M)
    assert match, f'missing ID: {path}'
    ids.append(match.group(1))
    for heading in required:
        assert heading in text, f'{path}: missing {heading}'
    assert 'https://learn.microsoft.com/' in text or 'https://kubernetes.io/' in text
assert len(ids)==len(set(ids)), 'duplicate runbook identifiers'
index=(atlas/'README.md').read_text()
coverage=(atlas/'COVERAGE.md').read_text()
for path, ident in zip(flat, ids):
    rel=path.relative_to(atlas).as_posix()
    assert rel in index, f'{rel} missing from index'
    assert ident in coverage, f'{ident} missing from coverage matrix'
print(f'PASS: {len(flat)} AKS runbooks have unique IDs, required sections, primary sources, and index coverage')

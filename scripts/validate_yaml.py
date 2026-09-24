#!/usr/bin/env python3
"""Parse every repository YAML document without applying the manifests."""

from pathlib import Path

import yaml


root = Path(__file__).resolve().parents[1]
paths = sorted(
    path for path in root.rglob('*')
    if path.suffix.lower() in {'.yaml', '.yml'} and '.git' not in path.parts
)

for path in paths:
    try:
        with path.open(encoding='utf-8') as stream:
            list(yaml.safe_load_all(stream))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise SystemExit(f'{path.relative_to(root)}: invalid YAML: {exc}') from exc

print(f'PASS: parsed {len(paths)} YAML files')

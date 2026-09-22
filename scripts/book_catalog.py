"""Render living catalogs from CSV; shared by modality chapters and appendices."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLUMNS = {
    'datasets': [('name','Dataset'),('size','Size / release'),('labels','Supervision'),('license/access','Access / terms'),('notes','Caveats'),('link','Source')],
    'models': [('model','Model / framework'),('task','Task'),('weights','Weights'),('license','Terms'),('notes','Scope'),('link','Source')],
    'fda-products': [('product','Device'),('vendor','Vendor'),('clearance','Submission'),('indication','Indication summary'),('notes','Boundary'),('link','FDA record')],
}

def render_catalog(kind, modalities=None, include_general=False):
    with (ROOT/'data'/f'{kind}.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    allowed=set(modalities or [])
    if include_general: allowed.add('any')
    if modalities is not None: rows=[r for r in rows if r['modality'] in allowed]
    cols=COLUMNS[kind]
    if modalities is None: cols=[('modality','Modality')]+cols
    if not rows:
        print('No entry is curated in this catalog for this modality. This is not evidence that no product or resource exists.\n')
        return
    def cell(v):return v.replace('|','\\|').replace('\n',' ')
    print('::: {.table-responsive}\n')
    print('| '+' | '.join(label for _,label in cols)+' |')
    print('|'+'---|'*len(cols))
    for r in rows:
        print('| '+' | '.join('[Source]('+r[key]+')' if key=='link' else cell(r[key]) for key,_ in cols)+' |')
    print('\n:::\n')

def render_community_datasets():
    with (ROOT/'data'/'community-datasets.csv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    groups = {}
    for row in rows:
        groups.setdefault(row['group'], []).append(row)
    def cell(value):
        return value.replace('|', '\\|').replace('\n', ' ')
    for group, entries in groups.items():
        print(f'### {group} ({len(entries)})\n')
        print('::: {.table-responsive}\n')
        print('| Dataset | Anatomy | Modality as listed | Segmentation target | Source |')
        print('|---|---|---|---|---|')
        for row in sorted(entries, key=lambda item: item['name'].casefold()):
            source = f"[{row['link_type']}](<{row['link']}>) ({row['worksheet']} row {row['row']})"
            print('| ' + ' | '.join(cell(row[key]) for key in ('name', 'anatomy', 'modality', 'targets')) + f' | {source} |')
        print('\n:::\n')

import sys
import pandas as pd
import json

pango_df = pd.read_csv(sys.argv[1])
for row in pango_df.to_dict('records'):
    # files have been concatenated - skip additional headers
    if row['taxon'] == 'taxon':
        continue

    id = row['taxon']
    acc = row['taxon']
    has_lineage = 'false' if row['lineage'] == 'None' else 'true'
    lineage = '' if row['lineage'] == 'None' else row['lineage']

    who_short, who_long = '', ''
    if not pd.isna(row['scorpio_call']):
        who_long = row['scorpio_call']
        who_short = who_long.split()[0] 

    pango_dict = {'fields': [
        {"name": "id", "value": id},
        {"name": "acc", "value": acc},
        {"name": "has_lineage", "value": has_lineage},
        {"name": "lineage", "value": lineage},
        {"name": "who", "value": who_short},
        {"name": "who_long", "value": who_long}
    ]}
    pango_json = json.dumps(pango_dict, indent=4) + ','
    pango_json = "\n".join([f"\t\t{x}" for x in pango_json.split("\n")]) # formatting
    print(pango_json)

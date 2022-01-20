import sys, os
import json
import subprocess
from datetime import datetime

# set version number
dir_path = os.path.dirname(os.path.realpath(__file__))
version_file = "{}/lineages_version".format(dir_path)
with open(version_file, 'r') as vfile:
    release_num = vfile.readline().strip()
release_num = "{:.1f}".format(float(release_num)+0.1)
with open(version_file, 'w') as vfile_out:
    vfile_out.write(release_num)

release_date = datetime.today().strftime('%Y-%m-%d')

infile = sys.argv[1]
total_seqs = subprocess.check_output("grep -c 'acc' {}".format(infile), shell=True)
entry_count = int(total_seqs)
sys.stderr.write("Found {} entries in {}\n\n".format(entry_count, infile))

jdict = {
    "name": "lineage-covid19",
    "release": release_num,
    "release_date": release_date,
    "entry_count": entry_count,
    "entries": [
        {
        "placeholder" : "placeholder"
        }
    ]
}
json_object = json.dumps(jdict, indent = 4) 
print(json_object)

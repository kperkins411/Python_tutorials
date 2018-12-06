import os
from pathlib import Path
dir_to_scan = '/home/keith/data/plant_seedlings/'
p=Path(dir_to_scan)
p.is_dir()
print(p.parts)

folders =[]
files=[]
other = []


def enumerate(p):
    for entry in os.scandir(p):
        if entry.is_dir():
            print('Found dir: %s'%entry)
            # folders.append(entry)
            enumerate(entry)
        elif entry.is_file():
            print('\t%s'%entry)
            # files.append(entry)
        # else:
        #     other.append(entry);

# recursively enumerate these fellows
# enumerate(dir_to_scan)

# for folder in folders:

print("folders -{}".format(folders))
print("files -{}".format(files))
print("other -{}".format(other))

import pandas as pd
from pathlib import Path
import time

all_files = []
for i in p.rglob('*.*'):
    all_files.append((i.name, i.parent, time.ctime(i.stat().st_ctime)))

columns = ["File_Name", "Parent", "Created"]
df = pd.DataFrame.from_records(all_files, columns=columns)

print(df.head())

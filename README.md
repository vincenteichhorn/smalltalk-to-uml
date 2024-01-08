# Usage
```
usage: index.py [-h] --folder FOLDER [--abbrv ABBRV]

options:
  -h, --help       show this help message and exit
  --folder FOLDER  relative path to folder containing all class.st files (clone the SWA-Group-Repo into any folder e.g. /data/[repo-name])
  --abbrv ABBRV    project abbreviation (e.h. 'OMG' for OMGGiraffe, OMGLion, ...) to remove in class names
```

```
$ python3 src/index.py --folder data/swa23-24-groupXX/src/SWAGroupXX --abbrv ABC > out/diagram.drawio
$ python3 src/index.py --folder data/swa23-24-group13/src/SWAGroup13 --abbrv OMG > out/diagram.drawio
```
- Open the .drawio with https://draw.io (Open Existing Diagram)
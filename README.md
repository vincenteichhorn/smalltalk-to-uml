# Usage
```
usage: index.py [-h] --folder FOLDER [--abbrv ABBRV]

options:
  -h, --help       show this help message and exit
  --folder FOLDER  relative path to folder containing all class.st files
  --abbrv ABBRV    project abbreviation (e.h. 'OMG' for OMGGiraffe, OMGLion, ...) to remove in class names
```

```
python3 src/index.py --folder data/swa23-24-group13/src/SWAGroup13 --abbrv OMG > diagram.drawio
```
- Open the .drawio with https://draw.io (Open Existing Diagram)
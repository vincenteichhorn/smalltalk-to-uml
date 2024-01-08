from uml import UMLXML
from st_parser import STParser
import argparse

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--folder", help="relative path to folder containing all class.st files", required=True)
    arg_parser.add_argument("--abbrv", help="project abbreviation (e.h. 'OMG' for OMGGiraffe, OMGLion, ...) to remove in class names")
    args = {k:v for k, v in vars(arg_parser.parse_args()).items() if v is not None}

    st_parser = STParser()
    uml = UMLXML()
    clss = st_parser.parse_classes(**args)
    xml = uml.create_uml(clss)
    print(xml)

from uml import UMLXML
from st_parser import STParser

if __name__ == "__main__":

    parser = STParser()
    clss = parser.parse_classes("./data/swa23-24-group13/src/SWAGroup13")
    uml = UMLXML()
    print(uml.create_uml(clss))

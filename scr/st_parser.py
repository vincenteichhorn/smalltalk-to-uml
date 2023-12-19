import os

class STParser:
    def __init__(self) -> None:
        pass

    def parse_classes(self, folder):
        classes = []
        for file in os.listdir(folder):
            if file.endswith(".class.st"):
                classes.append(self.__parse_file(os.path.join(folder, file)))
        return classes

    def __parse_file(self, filename):
        cls = {
            "name": "",
            "superclass": "",
            "attributes": [],
            "instance": [],
            "class": []
        }
        with open(filename) as file:
            got_instvars = False
            for ln in file:
                line = ln.rstrip()
                if "#name" in line: cls["name"] = line.split("#")[-1][:-1]
                if "#superclass" in line: cls["superclass"] = line.split("#")[-1][:-1]
                if "#instVars" in line: got_instvars = True
                if got_instvars and "'," in line: cls["attributes"].append(line[3:-2])
                if got_instvars and "]," in line: got_instvars = False
                if ">>" in line: 
                    cls["class" if "class" in line else "instance"].append(f'{self.__get_method_name(line)}')
        return cls

    def __get_method_name(self, line):
        return line.split(">> ")[1].split(" [")[0]
                
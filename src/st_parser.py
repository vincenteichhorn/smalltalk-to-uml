import os

class STParser:
    def __init__(self) -> None:
        pass

    def parse_classes(self, folder, *args, **kwargs):
        classes = []
        for file in os.listdir(folder):
            if file.endswith(".class.st"):
                classes.append(self.__parse_file(os.path.join(folder, file), *args, **kwargs))
        return classes

    def __parse_file(self, filename, remove_abbrv=""):
        cls = {
            "name": "",
            "superclass": "",
            "attributes": [],
            "instance": [],
            "class": []
        }
        with open(filename) as file:
            got_instvars = False
            last_category = ""
            for ln in file:
                line = ln.rstrip()
                if "#name" in line: cls["name"] = line.split("#")[-1][:-1].replace(remove_abbrv, "")
                if "#superclass" in line: cls["superclass"] = line.split("#")[-1][:-1]
                if "#instVars" in line: got_instvars = True
                if "#category" in line: last_category = line.split("#")[-1][:-1]
                if got_instvars and "'," in line: cls["attributes"].append(line[3:-2])
                if got_instvars and "]," in line: got_instvars = False
                if ">>" in line: 
                    cls["class" if "class" in line else "instance"].append((last_category, self.__get_method_name(line)))
        cls["instance"] = sorted(cls["instance"], key=lambda x: x[0])
        cls["class"] = sorted(cls["class"], key=lambda x: x[0])
        return cls

    def __get_method_name(self, line):
        return line.split(">> ")[1].split(" [")[0]
                
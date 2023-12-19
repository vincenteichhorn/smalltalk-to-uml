

class UMLXML:
    def __init__(self) -> None:
        self.root = "WIyWlLk6GJQsqaUBKTNV"
        self.objects = "zkfFHV4jXpPFQw0GAbJ"
        self.object_count = 0

        self.should_collapse = False
        self.class_box_height = 50
        self.object_height = 20
        self.line_height = 10
        self.class_width = 250
        self.last_position = [0, 0]

        self.collapse_string = "collapsed=\"1\""

    def create_uml(self, classes):
        classes = [self.create_class(cls["name"], cls["attributes"], cls["instance"], cls["class"]) for cls in classes]
        return f'{self.__begin()}{"".join(classes)}{self.__end()}'

    def create_class(self, name, attribute_names, instance_method_names, class_method_names):
        height = (len(attribute_names) + len(instance_method_names) + len(class_method_names)) * self.object_height + self.line_height + self.class_box_height + 10
        self.last_position[0] += self.class_width + 20
        class_box, class_id = self.__create_class_box(name, self.last_position, height)
        entities = []
        y = self.class_box_height
        for attr in attribute_names:
            entities.append(self.__create_content_text(attr, class_id, y)[0])
            y += self.object_height
        entities.append(self.__create_line(class_id, y)[0])
        y += self.line_height
        for meth in class_method_names:
            entities.append(self.__create_content_text(meth, class_id, y, underline=True)[0])
            y += self.object_height
        for meth in instance_method_names:
            entities.append(self.__create_content_text(meth, class_id, y)[0])
            y += self.object_height
        return f'{class_box}{"".join(entities)}'

    def __create_class_box(self, name, position, height):
        self.object_count += 1
        id = f'{self.objects}--{self.object_count}'
        return (
            f'<mxCell id="{id}" value="{name}" style="swimlane;fontStyle=2;align=center;verticalAlign=middle;childLayout=stackLayout;horizontal=1;startSize={self.class_box_height};horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=10;rounded=0;shadow=0;strokeWidth=1;fontSize=16;" parent="{self.root}-1" vertex="1" {self.collapse_string if self.should_collapse else ""}>\n' #
                f'<mxGeometry x="{position[0]}" y="{position[1]}" width="{self.class_width}" height="{height}" as="geometry">\n'
                    f'<mxRectangle x="{position[0]+30}" y="{position[1]+50}" width="{self.class_width}" height="{self.class_box_height}" as="alternateBounds" />\n'
                '</mxGeometry>\n'
            '</mxCell>\n'
        ), id
    
    def __create_line(self, parent, y):
        self.object_count += 1
        id = f'{self.objects}--{self.object_count}'
        return (
            f'<mxCell id="{id}" value="" style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;" parent="{parent}" vertex="1">\n'
                f'<mxGeometry y="{y}" width="{self.class_width}" height="{self.line_height}" as="geometry" />\n'
            f'</mxCell>\n'
        ), id
    
    def __create_content_text(self, name, parent, y, underline=False):
        self.object_count += 1
        id = f'{self.objects}--{self.object_count}'
        return (
            f'<mxCell id="{id}" value="{name}" style="text;{"fontStyle=4;" if underline else ""}align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rounded=0;shadow=0;html=0;" parent="{parent}" vertex="1">\n'
                f'<mxGeometry y="{y}" width="{self.class_width}" height="{self.object_height}" as="geometry" />\n'
            f'</mxCell>\n'
        ), id
    
    def __begin(self):
        return (
            f'<mxfile host="app.diagrams.net" modified="2023-12-19T08:20:30.630Z" agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0" etag="aA-VcDsM2x5fQgSPhtNZ" version="22.1.11" type="device">'
                f'<diagram id="C5RBs43oDa-KdzZeNtuy" name="Page-1">'
                    f'<mxGraphModel dx="1658" dy="889" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">'
                        f'<root>'
                            f'<mxCell id="{self.root}-0" />'
                            f'<mxCell id="{self.root}-1" parent="{self.root}-0" /> \n'
        )
    
    def __end(self):
        return "</root></mxGraphModel></diagram></mxfile>"
class HTMLElement():
    tag_name = ""
    attributes = []
    text = ""
    closing_tag = False

    def __init__(self, tag_name, attributes=[], text="", closing_tag=False):
        self.tag_name = tag_name
        self.attributes = attributes
        self.text = text
        self.closing_tag = closing_tag

    def get_html(self):
        return (
            "<" + self.tag_name + " " +
            " ".join([attr[0] + "='" + attr[1] + "'" for attr in self.attributes]) +
            ">" + self.text + (("</" + self.tag_name + ">") if self.closing_tag else "")
        )
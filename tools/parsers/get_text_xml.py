import xml.etree.ElementTree as ET


def get_text_xml(file_path):
    tree = ET.ElementTree(file=file_path)
    root = tree.getroot()
    text = ''
    for child_of_root in root.find('channel').iter():
        if child_of_root.tag == 'description':
            for item in child_of_root.text:
                text += item
    return text

from pprint import pprint
from tools.parsers.get_text_json import get_text_json
from tools.parsers.get_text_xml import get_text_xml
from tools.parse import Parse

with Parse('./data/newsafr.xml', get_text_xml) as data:
    pprint(len(data))

with Parse('./data/newsafr.json', get_text_json) as data:
    pprint(len(data))

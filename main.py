from tools.parsers.get_text_json import get_text_json
from tools.parsers.get_text_xml import get_text_xml
from tools.parse import Parse
from tools.top_words import top_words
from tools.get_message import get_message

with Parse('./data/newsafr.xml', get_text_xml) as data:
    print(get_message(top_words(data), 'Топ 10 слов в файле XML'))

with Parse('./data/newsafr.json', get_text_json) as data:
    print(get_message(top_words(data), 'Топ 10 слов в файле JSON'))

from json import load
import xml.etree.ElementTree as ET


def top_words(paths):
    def get_message(message, title):
        result = f'{title}:\n'
        position = 0
        for item in message:
            position += 1
            result += f'{position}. "{item[1]}": {item[0]}\n'
        return result

    def get_text_json(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            items = load(f)['rss']['channel']['items']
            text = ''
            for item in items:
                text += item['description']
        return text

    def get_text_xml(file_path):
        tree = ET.ElementTree(file=file_path)
        root = tree.getroot()
        text = ''
        for child_of_root in root.find('channel').iter():
            if child_of_root.tag == 'description':
                for item in child_of_root.text:
                    text += item
        return text

    def t_words(string, quantity=10, min_length=6):
        words = string.lower().split(' ')
        result = {}
        for word in words:
            result.setdefault(word, 0)
            result[word] += 1
        return list(
            sorted(
                (value, key) for (key, value) in result.items() if len(key) >= min_length)
        )[::-1][:quantity]

    parsers = {
        'xml': get_text_xml,
        'json': get_text_json,
    }
    for path in paths:
        ext = path.split('.')[-1]
        print(get_message(t_words(parsers[ext](path)), f'Топ 10 слов в файле {ext}'))


if __name__ == '__main__':
    top_words(['./data/newsafr.xml', './data/newsafr.json'])

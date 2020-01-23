from json import load


def get_text_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        items = load(f)['rss']['channel']['items']
        text = ''
        for item in items:
            text += item['description']
    return text

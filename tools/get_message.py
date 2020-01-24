def get_message(message, title):
    result = f'{title}:\n'
    position = 0
    for item in message:
        position += 1
        result += f'{position}. "{item[1]}": {item[0]}\n'
    return result

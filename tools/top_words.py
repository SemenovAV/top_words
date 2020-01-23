def top_words(string, quantity=10, min_length=6):
    words = string.split(' ')
    result = {}
    for word in words:
        result.setdefault(word, 0)
        result[word] += 1
    return list(sorted((value, key) for (key, value) in result.items() if len(key) >= min_length))[::-1][:quantity]

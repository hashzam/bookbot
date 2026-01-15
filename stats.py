def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    chars = {}
    for ch in text:
        ch = str.lower(ch)
        if ch in chars:
            chars[ch] = chars[ch] + 1
        else:
            chars[ch] = 1
    return chars

def sort_on(item):
    return item["num"]

def sort_ch(chars):
    sorted = []
    for char in chars:
        sorted.append({"char": char, "num": chars[char]})
    # then sort `sorted` with .sort(...) and return it
    sorted.sort(reverse=True, key=sort_on)
    return sorted
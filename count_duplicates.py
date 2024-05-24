from collections import Counter
def count_duplicates(text):

    text = text.lower()
    char_count = Counter(text)
    repeated_chars = [char for char, count in char_count.items() if count > 1]

    return len(repeated_chars)

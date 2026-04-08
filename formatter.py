def format_word(word, found_letters):
    p = []
    for l in word:
        if l in found_letters:
            p.append(l)
        else:
            p.append('_')
    return ''.join(p)

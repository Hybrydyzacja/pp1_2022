# duplicate = 0


def f(sentence):
    sentence_sorted = sorted(sentence)
    for e in sentence:
        count = sentence_sorted.count(e)
    return count


print(f("You never get a second chance to make a first impression"))

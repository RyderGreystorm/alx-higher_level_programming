#!/usr/bin/python3
def remove_char_at(words, pos):
    if pos < 0:
        return (words)
    return (words[:pos] + words[pos+1:])

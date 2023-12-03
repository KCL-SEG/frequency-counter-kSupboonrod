"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        if isinstance(item, (int, float, str, tuple)):
            frequencies[item] = frequencies.get(item, 0) + 1

    return frequencies
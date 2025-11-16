from unicodedata import combining, normalize


unicode_words = [
    "Skjöldur",      # Icelandic - shield
    "Château",       # French - castle
    "Ñoño",          # Spanish - dull/bland
    "Pâté",          # French - pâté
    "Łódź",          # Polish - city name
    "Hühnchen",      # German - chicken
    "Čeština",       # Czech - Czech language
    "Reykjavík",     # Icelandic - capital city
    "Søster",        # Norwegian/Danish - sister
    "Działanie"      # Polish - action/operation
]

for word in unicode_words:
    print(word)

    # print the encoding of the word
    print(word.encode('utf-8'))

    # normalize the word so that combining marks are separate
    normalized_word = normalize('NFD', word)
    print(normalize('NFD', normalized_word))

    # remove the combining mark
    print(''.join('' if combining(ch) else ch for ch in normalized_word))

print("Incorrectly sorted list:")
print(sorted(unicode_words))
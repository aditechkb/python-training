# pip install pyspellchecker

from spellchecker import SpellChecker

spell = SpellChecker()

# Example sentence with spelling mistakes
sentence = "When are you returning form the temple?"
words = sentence.split()

corrected_sentence = []
for word in words:
    # Correct each word and add to the corrected_sentence list
    corrected_word = spell.correction(word)
    corrected_sentence.append(corrected_word)

# Join the corrected words back into a sentence
corrected_sentence = " ".join(corrected_sentence)
print(corrected_sentence)

# When are you returning form the temple?
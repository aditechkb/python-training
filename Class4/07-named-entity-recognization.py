# Install this: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# Load SpaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample sentence
sentence = "Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University."

# Process the sentence
doc = nlp(sentence)

# Print entities in the sentence
for ent in doc.ents:
    print(ent.text, ent.label_)


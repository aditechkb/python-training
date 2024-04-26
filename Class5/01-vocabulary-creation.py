import spacy
import pickle

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Example sentences
sentences = [
    "Rama and Sita are characters in an epic.",
    "The cricket match in Hyderabad was exciting and full of surprises.",
    "Students from Chennai travel by bus to the science fair.",
    "Many festivals in Kerala feature traditional dance performances.",
    "Bangalore is known for its vibrant tech industry and pleasant weather."
]

def preprocess(text):
    """ Uses spaCy to tokenize, lemmatize, remove stopwords and punctuation, and normalize text. """
    doc = nlp(text)
    # Return lemmatized tokens that aren't stopwords or punctuation marks, converted to lower case
    return [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

def create_vocabulary(sentences):
    """ Process a list of sentences to create a sorted list of unique lemmatized tokens. """
    vocab_set = set()  # Using a set to automatically handle uniqueness
    for sentence in sentences:
        processed_tokens = preprocess(sentence)
        vocab_set.update(processed_tokens)  # Add tokens to set, duplicates are automatically ignored
    return sorted(vocab_set)  # Convert set to sorted list to finalize the vocabulary

# Generate the vocabulary from the sentences
vocabulary = create_vocabulary(sentences)

# Save the vocabulary to a pickle file
with open('Class5/vocabulary.pkl', 'wb') as f:
    pickle.dump(vocabulary, f)

print("Vocabulary created and saved successfully:", vocabulary)
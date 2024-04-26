import spacy
import pickle

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def load_vocabulary(vocab_path):
    """ Load the vocabulary from a pickle file. """
    with open(vocab_path, 'rb') as f:
        vocabulary = pickle.load(f)
    return vocabulary

def preprocess(text):
    """ Tokenize, lemmatize, and normalize the text. Remove stopwords and punctuation. """
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

def vectorize_sentence(sentence, vocabulary):
    """ Vectorize the sentence based on the loaded vocabulary. """
    tokens = preprocess(sentence)
    vector = [0] * len(vocabulary)
    for wordIndex, word in enumerate(vocabulary):
        for token in tokens:
            if word == token:
                vector[wordIndex] = vector[wordIndex]+1
            
    return vector

# Load the vocabulary from a pickle file
vocabulary = load_vocabulary('Class5/vocabulary.pkl')

# Example sentence to vectorize
sentences = [
    "Rama and Sita are characters in an epic.",
    "The cricket match in Hyderabad was exciting and full of surprises.",
    "Students from Chennai travel by bus to the science fair.",
    "Many festivals in Kerala feature traditional dance performances.",
    "Bangalore is known for its vibrant tech industry and pleasant weather."
]

vectors = []
# Vectorize the example sentence
for sentence in sentences:
    vector = vectorize_sentence(sentence, vocabulary)
    vectors.append(vector)

print("Vector for the sentence:", vectors)

# Save the vocabulary to a pickle file
with open('Class5/vectors.pkl', 'wb') as f:
    pickle.dump(vectors, f)
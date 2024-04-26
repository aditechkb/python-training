import spacy
import numpy as np
import pickle

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Example documents
documents = [
    "Rama and Sita are characters in an epic.",
    "The cricket match in Hyderabad was exciting and full of surprises.",
    "Students from Chennai travel by bus to the science fair.",
    "Many festivals in Kerala feature traditional dance performances.",
    "Bangalore is known for its vibrant tech industry and pleasant weather."
]

# Search query
search_query = "Did Rama meet Hanuma in Kerala during festival"

def preprocess(text):
    """Tokenize, lemmatize, and normalize the text. Remove stopwords and punctuation."""
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

def vectorize_texts(texts, vocabulary):
    """Vectorize a list of texts based on the given vocabulary."""
    vectors = []
    for text in texts:
        tokens = preprocess(text)
        vector = [0] * len(vocabulary)  # Initialize vector with zeros
        for token in tokens:
            if token in vocabulary:
                vector[vocabulary.index(token)] += 1
        vectors.append(vector)
    return vectors

def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def load_vocabulary(vocab_path):
    """ Load the vocabulary from a pickle file. """
    with open(vocab_path, 'rb') as f:
        vocabulary = pickle.load(f)
    return vocabulary

vocabulary = load_vocabulary('Class5/vocabulary.pkl')

# Vectorize documents and search query
document_vectors = vectorize_texts(documents, vocabulary)
query_vector = vectorize_texts([search_query], vocabulary)[0]

# Calculate similarities
similarities = [cosine_similarity(query_vector, doc_vec) for doc_vec in document_vectors]

# Sort documents by similarity (ascending order of distance)
sorted_docs = sorted(zip(documents, similarities), key=lambda x: -x[1])

# Print sorted documents and their similarity scores
for doc, similarity in sorted_docs:
    print(f"Document: {doc}\nSimilarity: {similarity:.4f}\n")

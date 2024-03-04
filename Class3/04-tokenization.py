import nltk
nltk.download('punkt')  # Download necessary datasets
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello, world. Welcome to Natural Language Processing with Python. My email address: sample@gmail.com"
words = word_tokenize(text)
sentences = sent_tokenize(text)

print("Words:", words)
print("Sentences:", sentences)

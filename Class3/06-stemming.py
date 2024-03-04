from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

ps = PorterStemmer()

sentence = "The boys are playing and one boy is running."
words = word_tokenize(sentence)

stemmed_words = [ps.stem(word) for word in words]

print("Original Words:", words)
print("Stemmed Words:", stemmed_words)

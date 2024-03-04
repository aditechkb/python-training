import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

text = "This is an example sentence demonstrating stopword removal."
stop_words = set(stopwords.words('english'))

print(stop_words)

word_tokens = word_tokenize(text)

filtered_sentence = []
for word in word_tokens:
    word_lower = word.lower()
    if word_lower not in stop_words:
        filtered_sentence.append(word)

print("Original sentence:", text)
print("Filtered sentence:", ' '.join(filtered_sentence))

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

# sentence = "I love to eat pizza on weekends."
sentence = "After a long hike, we finally made camp and had our first eat of the day."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

print(tagged_words)

# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

sentence = "The birds are flying."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

lemmatizer = WordNetLemmatizer()
lemmatized_sentence = []

for word, tag in tagged_words:
    wn_tag = get_wordnet_pos(tag)
    if wn_tag:
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos=wn_tag))
    else:
        lemmatized_sentence.append(word)

print("Lemmatized Sentence:", " ".join(lemmatized_sentence))

# The man went to the market, and he bought some berries
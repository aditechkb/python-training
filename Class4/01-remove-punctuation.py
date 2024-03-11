import string

text = "Hello, world! This is an example sentence; with punctuation."
cleaned_text = ''.join([char for char in text if char not in string.punctuation])

print(cleaned_text)

# Useful for tokenization, keyword extraction, text classification etc.
# Not use full for entity recognization for example "Wipro Ltd."
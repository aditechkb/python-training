import re

text = " This is an example text    with excessive spaces and other white space character like \t\n\r\f\v. "
cleaned_text = re.sub(r'\s+', ' ', text).strip()

print(cleaned_text)

# https://docs.python.org/3/library/re.html
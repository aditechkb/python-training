text = "In 2020, the population of City X increased by 5%."
cleaned_text = ''.join([char for char in text if not char.isdigit()])

print(cleaned_text)

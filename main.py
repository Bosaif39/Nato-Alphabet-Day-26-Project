import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Use dictionary comprehension to create a dictionary where:
# The key is the letter (from the "letter" column in the CSV)
# The value is code (from the "code" column in the CSV)
# `data.iterrows()` iterates over each row in the DataFrame
phonetic = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter a word: ").upper()
# phonetic[letter]` looks up the phonetic code for the given letter in the dictionary
output_list = [phonetic[letter] for letter in word]
print(output_list)

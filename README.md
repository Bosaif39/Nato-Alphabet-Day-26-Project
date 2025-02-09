# **Nato Alphabet Translator**

## **Overview:**
This is the Day 26 project from the 100 Days of Code: The Complete Python Pro Bootcamp. 

The NATO Alphabet Translator is a Python program that converts any word or phrase into its corresponding NATO phonetic alphabet codes. The NATO phonetic alphabet is used to ensure clarity in communication, especially in fields like aviation, military, and telecommunications.

This program reads a CSV file containing the NATO phonetic alphabet, creates a dictionary for quick lookup, and translates user input into a list of phonetic codes.

## **How It Works:**
1. **Data Loading**:
   - The program reads a CSV file (`nato_phonetic_alphabet.csv`) containing the NATO phonetic alphabet. The file should have two columns: `letter` and `code`.

2. **Dictionary Creation**:
   - A dictionary is created using dictionary comprehension, where each letter is a key, and its corresponding NATO code is the value.

3. **User Input**:
   - The user is prompted to enter a word or phrase. The input is converted to uppercase to match the dictionary keys.

4. **Translation**:
   - The program translates each letter of the input word into its corresponding NATO phonetic code using the dictionary.

5. **Output**:
   - The program outputs a list of NATO phonetic codes for the input word.

## **Example:**


### Input:
```
Enter a word: Hello
```

### Output:
```
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## **Requirements:**
- **Python 3.x**
-- `pandas` module 

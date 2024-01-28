import os

def read_file(path):
  with open(path, 'r') as file:
    return file.read()
  
def count_words(text_string):
  words = text_string.split()
  return len(words)

def get_letter_dict(text_string):
  text_string = text_string.lower()

  letters = {}
  for char in text_string:
    if char.isalpha():
      if char in letters:
        letters[char] += 1
      else:
        letters[char] = 1
  
  return letters

def print_report(book_path):

  book_text = read_file(book_path)
  print(f"--- Begin report of {book_path} ---")
  
  words_in_doc = count_words(book_text)
  print(f"{words_in_doc} words found in the document\n")

  letter_dict = get_letter_dict(book_text)
  letters_found = list(letter_dict.keys())
  letters_found.sort()

  for letter in letters_found:
    print(f"The '{letter}' character was found {letter_dict[letter]} times")

  print("--- End report ---")

def main():
  print_report("./books/frankenstein.txt")

if __name__ == "__main__":
  main()
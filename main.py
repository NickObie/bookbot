
def main():
   book_path = "books/frankenstein.txt"
   text = get_book_contents(book_path)
   num_words = get_num_words(text)
   letters = get_char_nums(text)
   report(book_path, num_words, letters)

def get_char_nums(text):
   lower_letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
   text = text.lower()
   for i in text:
      if(i in lower_letters):
         lower_letters[i] += 1
   return lower_letters

def get_book_contents(path):
   with open(path) as f:
      file_contents = f.read()
   return file_contents

def get_num_words(text):
   words = text.split()
   return len(words)

def sort_dict(dict):
   return sorted(dict.items(), key=lambda x:x[1], reverse=True)

def report(path, num_words, letters):
   print(f"-- Begin report of {path} --")
   print(f"{num_words} words found in the document")
   print()
   sorted_letters = sort_dict(letters)
   for k, v in sorted_letters:
      print(f"The '{k}' character was found {v} times")

main()
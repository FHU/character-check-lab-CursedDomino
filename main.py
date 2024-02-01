def check_character(word, index):
   if word[index:index + 1].isalpha():
      return 'letter'
   elif word[index:index + 1].isnumeric():
      return 'digit'
   elif word[index] == ' ':
      return 'whitespace'
   else:
      return 'unknown'
   
#test

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
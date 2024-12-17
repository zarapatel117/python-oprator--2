def is_alphabet(character):
 
  return character.isalpha()

character = input("Enter a character: ")

if is_alphabet(character):
  print(f"{character} is an alphabet.")
else:
  print(f"{character} is not an alphabet.")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
# take if statement out of for loop cause loop is for encode and if statement is for decode only
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
# used to keep numbers and characters the same and only encrypting the alphabet
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
# adding the same characters to whatever the encrypted end_text is
    else:
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#use while loop to ask user to restart program
should_contine = True
while should_contine:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
#shift is redefined to divide by 26(the number of letters) to get a remainder (%) if input is beyond 26...the remainder is considered the input
    shift = shift % 26
#calling the function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#defining while loop as false if input is 'no'
    result = input("Do you want to go again?  yes or no. \n")
    if result == "no":
        should_contine = False
        print("Goodbye")
    

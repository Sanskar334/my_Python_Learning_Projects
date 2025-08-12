# def new_string(new_word): # This function is useless because I have to change logic in the dencryption function.
#     for letter in new_word:
#         encrypted_word = chr(ord(letter) + 1)
#         final_word += encrypted_word
    
def encryption_1(word):
    new_word = word[::-1]

    final_word = ""

    for letter in new_word:
        encrypted_word = chr(ord(letter) + 1) # ord converts a letter into its unicode and chr converts a unicode into a letter.
        final_word += encrypted_word

    # return final_word
    print(f"\nYour encrypted message is: {final_word}\n")

def dencryption(encrypted_word):

    new_word = encrypted_word[::-1]

    final_dencrypted_word = ""

    for letter in new_word:
        dencrypted_word = chr(ord(letter) - 1)
        final_dencrypted_word += dencrypted_word

    print(f"\nYour dencrypted message is: {final_dencrypted_word}\n")

while True:

    word = input("\nEnter the message to be encrypted:\n")

    encryption_1(word)

    dencryption_word = input("Enter the encrypted message:\n")
    dencryption(dencryption_word)
# Caesar's cipher

import string

def encrypt(message, shift):
    encryption_str = ""    
    for i in range(len(message)):
        symbol = message[i]                
        if (symbol.isupper()):
            encryption_str += chr((ord(symbol) + shift - 65) % 26 + 65)        
        elif symbol.islower():
            encryption_str += chr((ord(symbol) + shift - 97) % 26 + 97)
        else:
            encryption_str = encryption_str + symbol
    return encryption_str 

def encrypt_with_alphabet(message, shift, alphabet):    
    encryption_str = ''
    for symbol in message:
        if symbol in alphabet:
            symbol_number = alphabet.find(symbol)
            symbol_number = symbol_number + shift
            if symbol_number >= len(alphabet):
                symbol_number = symbol_number - len(alphabet)
            encryption_str = encryption_str + alphabet[symbol_number]
        else:
            encryption_str = encryption_str + symbol  
    return encryption_str
    
def decrypt(message, shift):
    decryption_str = ""    
    for i in range(len(message)):
        symbol = message[i]                
        if (symbol.isupper()):
            decryption_str += chr((ord(symbol) - shift - 65) % 26 + 65)        
        elif symbol.islower():
            decryption_str += chr((ord(symbol) - shift - 97) % 26 + 97)
        else:
            decryption_str = decryption_str + symbol
    return decryption_str 

def decrypt_with_alphabet(message, shift, alphabet):    
    decryption_str = ''
    for symbol in message:
        if symbol in alphabet:
            symbol_number = alphabet.find(symbol)
            symbol_number = symbol_number - shift
            if symbol_number < 0:
                symbol_number = symbol_number + len(alphabet)
            decryption_str = decryption_str + alphabet[symbol_number]
        else:
            decryption_str = decryption_str + symbol  
    return decryption_str

def bruteforce(message, alphabet):
    decrypted_strings = []
    for key in range(len(alphabet)):
        decrypted_string = ''
        for symbol in message:
            if symbol in alphabet:
                symbol_number = alphabet.find(symbol)
                symbol_number = symbol_number - key
                if symbol_number < 0:
                    symbol_number = symbol_number + len(alphabet)
                decrypted_string = decrypted_string + alphabet[symbol_number]
            else:
                decrypted_string = decrypted_string + symbol
        decrypted_strings.append(decrypted_string)        
    return decrypted_strings

def print_separator():
    print("-" * 50)

def main():

    shift = 3 # cipher shift, can be adjusted
    message = input("Your message: ").upper()

    print_separator()
    print("Test encryption")        
    encrypted_message = encrypt(message,shift) 
    print("Message: " + message)
    print("Shift: " + str(shift))    
    print("Encrypted Message: " + encrypted_message)
    
    print_separator()
    print("Test encryption with custom alphabet")         
    ALPHABET = 'EQRSTUVWXYZ' # ALPHABET = ''.join([string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
    encrypted_with_alphabet_message = encrypt_with_alphabet(message, shift, ALPHABET)
    print("Message: " + message)
    print("Shift: " + str(shift))     
    print("Alphabet: " + ALPHABET)
    print("Encrypted Message: " + encrypted_with_alphabet_message)    
    
    print_separator()
    print("Test Decryption")    
    print("Encrypted Message: " + encrypted_message)
    print("Shift: " + str(shift))
    print("Decrypted Message: " + decrypt(encrypted_message, shift))        
    
    print_separator()
    print("Test Decryption with alphabet")    
    print("Encrypted Message: " + encrypted_with_alphabet_message)
    print("Shift: " + str(shift))
    print("Alphabet: " + ALPHABET)
    print("Decrypted Message: " + decrypt_with_alphabet(encrypted_with_alphabet_message, shift, ALPHABET))     
    
    print_separator()
    print("Test Brute Force")    
    print("Encrypted Message: " + encrypted_message)
    LETTERS = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_strings = bruteforce(encrypted_message, LETTERS)
    for i in range(len(decrypted_strings)):            
        decrypted_string = decrypted_strings[i] 
        if i == shift:
            print('Brute Force shift: #%s: Decypted message: %s <------------' % (i, decrypted_string))            
        else:
            print('Brute Force shift: #%s: Decypted message: %s' % (i, decrypted_string))            
  
if __name__== "__main__":
  main()    
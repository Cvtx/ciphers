# Substitution cipher

import random
from math import factorial

def get_random_permutation(alphabet:str):
   random_permutation = list(alphabet)
   random.shuffle(random_permutation)
   return ''.join(random_permutation)

def print_separator():
    print("-" * 50)

def generate_permutations(alphabet: str):
    from itertools import permutations
    permutations_list = list(permutations(alphabet))
    return permutations_list

def generate_permutations_alt(remaining, candidate=''): 
    if len(remaining) == 0:
        print(candidate)
 
    for i in range(len(remaining)): 
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:] 
        generate_permutations_alt(newRemaining, newCandidate)     

def print_permutations(permutations: list):
    for permutation in permutations:
        print(permutation)

def save_permutations_in_file(permutations: list, filename: str):          
    file = open(filename, "w", encoding="utf-8") 
    i = 0
    for permutation in permutations:
        file.writelines(str(i) + ' ' + ''.join(permutation) + "\n")    
        i += 1
    file.close() 

def get_permutation_at_index(alphabet:str, index: int):
    permutations = generate_permutations(alphabet)
    if len(permutations) > index and index >= 0:
        return ''.join(permutations[index])
    return ''

def encrypt_with_permutation_index(alphabet:str, index:int, message:str):
    permutation = get_permutation_at_index(alphabet, index)
    return encrypt_with_permutation(alphabet, permutation, message)        

def encrypt_with_permutation(alphabet:str, permutation:str, message:str):
    if is_permutation_valid(alphabet, permutation):
        encrypted_message = ''                   
        for symbol in message:        
            if symbol.upper() in alphabet:
                symIndex = alphabet.find(symbol.upper())
                if symbol.isupper():
                    encrypted_message += permutation[symIndex].upper()
                elif symbol.islower():
                    encrypted_message += permutation[symIndex].lower()
                else:
                    encrypted_message += permutation[symIndex]
            else:
                encrypted_message += symbol
        return encrypted_message
    
    return ''

def decrypt_with_permutation(alphabet:str, permutation:str, encrypted_message:str):
    if is_permutation_valid(alphabet, permutation):
        decrypted_message = ''
        for symbol in encrypted_message:        
            if symbol.upper() in permutation:
                symIndex = permutation.find(symbol.upper())
                if symbol.isupper():
                    decrypted_message += alphabet[symIndex].upper()
                elif symbol.islower():
                    decrypted_message += alphabet[symIndex].lower()
                else:
                    decrypted_message += alphabet[symIndex]
            else:
                decrypted_message += symbol
        return decrypted_message
    
    return ''    

def is_permutation_valid(alphabet:str, permutation:str):
    return len(alphabet) == len(permutation) and sorted(alphabet) == sorted(permutation)

def bruteforce(alphabet:str, encrypted_message:str):
    file = open("bruteforce.txt", "w", encoding="utf-8")     
    permutations = generate_permutations(alphabet)
    i = 0
    for permutation in permutations:
        permutation = ''.join(permutation)
        decrypted = decrypt_with_permutation(alphabet, permutation, encrypted_message)
        file.writelines(str(i) + ' ' + ''.join(decrypted) + "\n")    
        i += 1        
    file.close() 


def main():
    print_separator()
    LETTERS = "??O??????????_" #string.ascii_uppercase
    MESSAGE = "??????????_??????????_??????????"
    FILENAME = "permutations.txt"

    permutations = generate_permutations(LETTERS)        
    random_permutation_index = random.randint(0, factorial(len(LETTERS) - 1))
    random_permutation = get_permutation_at_index(LETTERS, random_permutation_index)
    print(f"??????????????: {LETTERS}")
    print(f"?????????????????? ???????????????????????? ???{random_permutation_index}: {random_permutation}")
    
    encrypted_message = encrypt_with_permutation(LETTERS, random_permutation, MESSAGE)
    decrypted_message = decrypt_with_permutation(LETTERS, random_permutation, encrypted_message)
    print(f"C????????????????: {MESSAGE}")
    print(f"?????????????????????????? ??????????????????: {encrypted_message}")
    print(f"???????????????????????????? ??????????????????: {decrypted_message}")

    
    print_separator()
    #print_permutations(permutations)
    save_permutations_in_file(permutations, FILENAME)
    print(f"???????? ?? ???????????????????????????? ???????????????? ?????? ???????????? {FILENAME}")    
    print_separator()
    bruteforce(LETTERS, encrypted_message)
    print(f"???????? ?? ???????????????????? ???????????????? ?????? ???????????? bruteforce.txt (???????????????????????? ?????????????????? ???? ???????????? #{random_permutation_index})")    
    print_separator()            
         
if __name__== "__main__":
  main() 
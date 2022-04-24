# Thread cipher

import random

LENGTH = 256

def get_random_key() -> list:
    l = list(range(LENGTH))
    random.shuffle(l)
    return l

def swap(list: list, pos1: int, pos2: int) -> list:
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def intialize_generator(key: list) -> list:
    generator = key[:]    
    j = 0
    for i in range(LENGTH):
        j = (j + generator[i] + key[i]) % LENGTH
        generator = swap(generator, generator[i], generator[j])        
    return generator

def from_unicode_to_ascii_bytes(message: str) -> list:
    ascii_bytes = []    
    for s in message:
        sb, mb, = (ord(s) & 0xFFFFFFFF).to_bytes(2, 'big')
        ascii_bytes.append(sb)
        ascii_bytes.append(mb)  
    return ascii_bytes;            

def get_gamma(gen: list, message: list) -> list:
    gamma = []    
    i = 0
    j = 0
    for k in range(len(message)):
        i = (i + 1) % LENGTH
        j = (j + gen[i]) % LENGTH
        gen = swap(gen, gen[i], gen[j])        
        t = (gen[i] + gen[j]) % LENGTH
        gamma.append(gen[t])
    return gamma

def encrypt(message: list, gamma: list) -> list:    
    return [(message[i] ^ gamma[i]) for i in range(len(message))]

def decrypt(message: list, gamma: list) -> list:
    return encrypt(message, gamma)

def to_str(l: list) -> str:
    return "".join([chr((l[i] * LENGTH) + l[i + 1]) for i in range(0, len(l), 2)])

def shortprint(m: str, l: list, n : int = 10):
    print(f"{m} {l[:n]} ...")

def main():    
    key = get_random_key()          
    generator = intialize_generator(key)         
    message = input("Your message: ")
    ascii_bytes = from_unicode_to_ascii_bytes(message)        
    gamma = get_gamma(generator, ascii_bytes)
    encrypted_message = encrypt(ascii_bytes, gamma)        
    translated_message = to_str(encrypted_message)            
    decrypted_message = decrypt(encrypted_message, gamma)            
            
    shortprint("Key", key)       
    shortprint("Random numbers generator: ", generator)
    print("Message: " + message)
    shortprint("Message in unicode:", [ord(letter) for letter in message])
    shortprint("Message bytes:", ascii_bytes)
    shortprint("Gamma", gamma)
    shortprint("Encrypted message bytes:", encrypted_message)
    print("Encrypted message (unicode): " + str(translated_message))
    shortprint("Decrypted message bytes: ", decrypted_message)
    print("Decrypted message (unicode): " + str(to_str(decrypted_message)))
    

if __name__ == '__main__':    
    main()
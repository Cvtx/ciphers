# RSA cipher

import random

def two_different_large_prime_numbers():
    return 17, 29

# Получение наибольшего общего делителя
def gcd(a, b):
    while not b == 0:
        a, b = b, a % b
    return a

# нахождения обратного числа
def multiplicative_inverse(e, phi):
    for i in range(phi):
        if ((e*i)%phi) == 1:
            return i

# Проверка на простое число
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

# Генерация ключей из двух простых чисел
def generate_keypair(p, q):    
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers should be prime')
    elif p == q:
        raise ValueError('p and q can\'t be the same')

    # модуль публичного ключа
    n = p * q
    
    # phi (φ или ϕ) - это функция Эйлера от n:
    # число целых чисел k в диапазоне 1 ≤ k ≤ n
    # , для которых наибольший общий делитель gcd(n, k) равен 1
    phi = (p-1) * (q-1)

    # выберите целое число e такое, чтобы e и φ(n) были взаимно простыми числами и e находится между 1 и φ(n)
    e = random.randrange(1, phi)
    
    # проверка на взаимно простые числа (наибольший общий делитель должен быть 1)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    # генерация приватного ключа
    d = multiplicative_inverse(e, phi)
    
    # пары публичного и приватного ключа
    return ((e, n), (d, n))

# шифрование
def encrypt(public_key, message):    
    key, n = public_key    
    # каждую букву в сообщении преобразуем в число
    cipher = [(ord(char) ** key) % n for char in message]    
    return cipher

# дешифрование
def decrypt(private_key, cipher):    
    key, n = private_key    
    # из числа получаем текст
    message = [chr((char ** key) % n) for char in cipher]    
    return ''. join(message)

def print_seprator() -> None:
    print('-'*50)

def main() -> None:    
    p, q = two_different_large_prime_numbers()

    public, private = generate_keypair(p, q)
    print('Public key: ', public)
    print('Private key: ', private)

    message = input('\nYour message: \n')
    encrypted_msg = encrypt(private, message)

    print_seprator()
    print('Encrypted message:', ''.join(map( lambda x: str(x), encrypted_msg)))
    print('Decrypted message:', decrypt(public, encrypted_msg))
    print_seprator()
    print()

if __name__ == '__main__':
    main()
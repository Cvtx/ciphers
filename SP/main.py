# SP network cipher (P - S - P)

import math
import random
import secrets

S_Box = random.sample(range(16), 16)       # значения должны быть в отрезке [0, 15] и по одному разу
P_Box = random.sample(range(1, 17, 1), 16) # значения должны быть в отрезке [1, 16] и по одному разу

def SPN(message, s_box, p_box, round_keys):
    """    
    message =  16 бит сообщение
    s_box = S блок
    p_box = P блок
    round_keys = раундовые ключи 16 бит
    Возвращает 16 бит зашифрованного сообщения
    """
    pr = message    
        
    # блоки для построения сети
    # pr = pr ^ round_keys[0]  # xor c ключом
    # pr = pi_p (p_box, pr) # перестановки p-блока
    # pr = pi_s (s_box, pr) # подстановки s-блоков
    
    # P - S - P сеть
    pr = perm_p (p_box, pr) # перестановки p-блока
    pr = sub_s (s_box, pr) # подстановки s-блоков
    pr = perm_p (p_box, pr) # перестановки p-блока    

    y = pr
    return y      

def invert_Sbox(s_box):
    """
    Обратный s-блок    
    """
    inverse_box = [-1] * 16
    for i in range(16):
        inverse_box[s_box[i]] = i
    return inverse_box


def invert_Pbox(p_box):
    """
    Обратный P-блок    
    """
    inverse_box = [-1] * 16
    for i in range(16):
        inverse_box[p_box[i] - 1] = i + 1
    return inverse_box

def gen_round_keys(key):
    """
    Генерация подключей 16 бит из 32 бит ключа  (раундовые ключи)
    Возвращает список из 5 ключей 16 бит ключей
    """
    rounds = 5
    round_keys = []
    for i in range(rounds, 0, -1):
        ki = key % (2 ** 16)
        round_keys.insert(0, ki)
        key = key >> 4
    return round_keys


def sub_s(s_box, x):
    """
    Подстановки по 4 бита
    s_box = S блок    
    x = 16 бит строка
    """
    x_sub = 0
    for i in range(4):
        bit16 = x % (2 ** 4)
        x = x >> 4 # шифт на 4 бита
        sub = s_box[bit16]
        x_sub = x_sub + (sub << (4 * i))        
    return x_sub


def perm_p(p_box, x):
    """
    Перестановка одного бита    
    p_box = P блок
    x = 16 бит строка
    Возвращает перестановку 16 бит    
    """
    x_perm = 0
    for i in range(15, -1, -1):
        bit = x % 2              
        x = x >> 1  # шифт на 1 следующий бит
        x_perm = x_perm + (bit << (16 - p_box[i])) # шифт бита на значение из p-блока
    return x_perm

def encrypt(key, message):
    """
    Шифрование 
    key = 32 бит ключ
    message = 16 бит текста
    Возвращает 16 бит зашифрованного текста
    """
    round_keys = gen_round_keys(key)
    return SPN(message, S_Box, P_Box, round_keys)

def decrypt(K, y):
    round_keys = gen_round_keys(K)
    # раундовые ключи в обратном порядке
    round_keys.reverse()     
    round_keys[1] = perm_p(P_Box, round_keys[1])
    round_keys[2] = perm_p(P_Box, round_keys[2])
    round_keys[3] = perm_p(P_Box, round_keys[3])

    S_rbox = invert_Sbox(S_Box)
    P_rbox = invert_Pbox(P_Box)
    return SPN(y, S_rbox, P_rbox, round_keys)

def to_binary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def to_string(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m  

def main():
    KEY = secrets.randbits(32)
    print(f"Key: {format(KEY,'032b')}")
    print(f"S-box {S_Box}")
    print(f"P-box {P_Box}")
    
    message = input("Your message: ")
    b_text = []
    encrypted = []
    decrypted = []

    # строка в двоичную кодировку
    for symbol in message:
        b_symbol = to_binary(symbol)[0]                
        b_text.append(b_symbol)

    # шифрование
    for symbol in message:        
        e_symbol = encrypt(KEY, ord(symbol))     
        encrypted.append(e_symbol)
    
    # расшифрование
    for e_symbol in encrypted:
        b_symbol = decrypt(KEY, e_symbol)       
        decrypted.append(b_symbol)
    
    print(f"Message: {message}")
    print(f"Message in binary: {b_text}")
    print(f"Message in encrypted binary: {[format(x,'016b') for x in encrypted]}")
    print(f"Message in decrypted binary:  {[format(x,'016b') for x in decrypted]}")  

if __name__ == '__main__':    
    main()
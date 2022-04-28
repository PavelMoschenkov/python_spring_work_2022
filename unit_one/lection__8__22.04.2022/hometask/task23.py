# # Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.


s = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

def encrypt_caesar(plaintext: str, shift: int = 3):
    num_Z = ord("Z")
    num_A = ord("A")
    num_z = ord("z")
    num_a = ord("a")
    ciphertext = [plaintext[j] for j in range(len(plaintext))]
    i = 0
    for letter in plaintext:
        if letter.isalpha() and letter.isupper():
            if ord(letter) + shift > num_Z:
                ciphertext[i] = chr(num_A - 1 + (shift - (num_Z - ord(letter))))
                # индексу алфавита плюсуем то, что оснется от шифта МИНУС (конец алфавита - индекс нашей буквы)
            else:
                ciphertext[i] = chr(ord(letter) + shift)
        elif letter.isalpha() and letter.islower():
            if ord(letter) + shift > num_z:
                ciphertext[i] = chr(num_a - 1 + (shift - (num_z - ord(letter))))
            else:
                ciphertext[i] = chr(ord(letter) + shift)
        i += 1
    return ''.join(ciphertext)


for i in range(1, 29):
    print(i, encrypt_caesar(s, i))

print('ANSWER:', "although that way may not be obvious at first unless you're dutch.", 'shift = 20')
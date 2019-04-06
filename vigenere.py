# -*- coding: utf-8 -*-
import sys

ALPHABET = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def read_file(filename):
    """
    Считывает файл и возвращает содержимое
    :param filename: имя файла
    :return: содержимое
    """

    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text

    except IOError:
        print("Нет такого файла")
        sys.exit()


def encrypt(plaintext):
    """
    Шифрует текст с помощью метода Вижинера с «самоключом»
    (в качестве буквы ключа используется предыдущая буква открытого текста)
    :param plaintext: открытый текст
    :return: зашифрованный текст
    """

    ciphertext = []
    key = []
    key.append('a')

    for i in range(len(plaintext)):

        if plaintext[i] not in ALPHABET:
            ciphertext.append(plaintext[i])
            key.insert(i, '')
            continue

        plaintext_index = ALPHABET.index(plaintext[i]) + 1
        key_index = ALPHABET.index(key[i])
        index = (plaintext_index + key_index) % 26

        ciphertext.append(ALPHABET[index - 1])
        key.append(ALPHABET[index - 1])

    return ('').join(ciphertext)


def decrypt(ciphertext):
    """
    Расшифровывает текст с помощью метода Вижинера с «самоключом»
    (в качестве буквы ключа используется предыдущая буква открытого текста)
    :param ciphertext: зашифрованный текст
    :return: расшифрованный текст
    """

    plaintext = []
    key = ['a']

    for i in range(len(ciphertext)):

        if ciphertext[i] not in ALPHABET:
            plaintext.append(ciphertext[i])
            key.insert(i, '')
            continue

        ciphertext_index = ALPHABET.index(ciphertext[i]) + 1
        key_index = ALPHABET.index(key[i])
        index = (ciphertext_index - key_index) % 26

        plaintext.append(ALPHABET[index - 1])
        key.append(ciphertext[i])

    return ('').join(plaintext)

if __name__ == "__main__":

    filename_ciphertext = 'ciphertext.txt'
    filename_decrypted_text = 'decrypt_out.txt'
    filename_plaintext = input('Введите имя файла с открытым текстом: ')

    plaintext = read_file(filename_plaintext)
    ciphertext = encrypt(plaintext)

    with open(filename_ciphertext, 'w') as file:
        file.write(ciphertext)

    decrypted_text = decrypt(ciphertext)

    with open(filename_decrypted_text, 'w') as file:
        file.write(decrypted_text)

# var alphabet = 'abcdefghijklmnopqrstuvwxyz';
# var key = 'password';
#
# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
# var c = new VigenèreCipher(key, alphabet);
#
# c.encode('codewars'); // returns 'rovwsoiv'
# c.decode('laxxhsj');  // returns 'waffles'
# Если n - количество букв в алфавите, mj - номер буквы открытого текста, kj —
# номер буквы ключа в алфавите, то шифрование Виженера
# Cj =(mj+kj) mod n
# И расшифровывание:
#
# mj = (cj -kj) mod

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        res = ''
        for i in range(len(text)):
            if text[i] in self.alphabet:
                res += self.alphabet[
                    (self.alphabet.index(text[i]) + self.alphabet.index(self.key[i % len(self.key)])) % len(
                        self.alphabet)]
            else:
                res += text[i]
        return res

    def decode(self, text):
        res = ''
        for i in range(len(text)):
            if text[i] in self.alphabet:
                res += self.alphabet[
                    (self.alphabet.index(text[i]) - self.alphabet.index(self.key[i % len(self.key)])) % len(
                        self.alphabet)]
            else:
                res += text[i]
        return res


test_cipher = VigenereCipher("password", "abcdefghijklmnopqrstuvwxyz")
print(test_cipher.encode('codewars'))
print(test_cipher.decode('rovwsoiv'))

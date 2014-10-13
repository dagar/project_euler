#! /usr/bin/env python
"""
problem 59: decrypt p059_cipher.txt with 3 character xor key
"""

with open("p059_cipher.txt") as f:
    cipher = f.read()

cipher = cipher.split(",")
wordlist = set([line.strip() for line in open('/usr/share/dict/words')])

lowercase = 'abcdefghijklmnopqrstuvwxyz'
for a in lowercase:
    for b in lowercase:
        for c in lowercase:
            key = [a, b, c]
            message = ""
            for i, ciph in enumerate(cipher):
                message += chr(int(ciph) ^ ord(key[i % 3]))

            word_count = 0
            message_words = message.split(" ")
            for word in message_words:
                if word in wordlist:
                    word_count += 1

            # rough estimate for word count
            if word_count > len(cipher) / 8:
                message_sum = 0
                for c in message:
                    message_sum += ord(c)

                print("key = %s" % "".join(key))
                print("Sum of all ascii letters = %d" % message_sum)
                print(message)

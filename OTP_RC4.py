

class Cryptography:

    def __init__(self, message, key, choice):
        self.choice = choice
        self.message = message
        self.key = key
        self.key_size = len(key)
        binary_message = ""
        binary_key = ""
        keystream = []
        self.keystream = keystream
        self.binary_message = binary_message
        self.binary_key = binary_key

    # OTP convert message to binary
    def binary_otp_message_conversion(self):

        # verify binary is correctly joined
        print(([bin(ord(ltr))[2:].zfill(8) for ltr in self.message]))

        # fixed 8 bits to represent each character binary value
        self.binary_message = "".join([bin(ord(ltr))[2:].zfill(8) for ltr in self.message])
        return self.binary_message

    # OTP convert key to binary
    def binary_otp_key_conversion(self):

        # fixed 8 bits to represent each character binary value
        self.binary_key = "".join([bin(ord(ltr))[2:].zfill(8) for ltr in self.key])
        return self.binary_key

    # OTP Encrypt the binary message an key using xor, return encrypted message
    @staticmethod
    def otp_return_ciphertext(binary_message, binary_key):

        # using zip() to map values
        otp_encrypted = "".join([str(int(messageIndex) ^ int(keyIndex)) for messageIndex, keyIndex in
                                 zip(binary_message, binary_key)])

        print('OTP Ciphering Text Now!')

        return otp_encrypted

    # RC4 ciphertext, Encrypt the rc4 message an keystream given by the key using xor, return encrypted message
    def RC4_return_ciphertext(self):
        message = self.message

        print('\nRC4 receiving info to Cipher now!')
        print('Message to encrypt: ' + message)
        print('Key used to encrypt: ' + self.key)
        print('Your key converted to Keystream bytes: ' + str(self.keystream))

        # using zip() to map values
        rc4_encrypted = " ".join([str(ord(messageIndex) ^ int(keyIndex)) for messageIndex, keyIndex in
                                 zip(message, self.keystream)])

        print('RC4 encrypted your message below:')

        return rc4_encrypted

    # RC4 Decrypt(plaintext) the message  using the same key and make sure the decrypted  message (plaintext)
    # matches the original message.
    @staticmethod
    def rc4_return_plaintext(rc4_encrypted_message, is_match_key):
        print('\nRC4 receiving info to Decrypt to plaintext now!')
        print('Your Original Encrypted message ' + rc4_encrypted_message)
        print('Yor key converted to Keystream bytes: ' + str(is_match_key))
        print('RC4 Decrypting Text Below:')
        rc4_encrypted_message = rc4_encrypted_message.split(' ')

        text = ''
        for message_index, key_index in zip(rc4_encrypted_message, is_match_key):
            xor_value = int(message_index) ^ key_index
            text += chr(xor_value)

        return text

    # OTP takes ciphertext and returns plaintext
    # Decrypt the message using the same key and make sure the decrypted message matches the original message
    @staticmethod
    def otp_return_plaintext(encrypted_message, is_match_key):

        print('Encrypted message ' + encrypted_message)
        print('match_key used: ' + is_match_key)
        print('OTP Decrypting Text Now!')

        # using zip() to map values
        otp_decrypted = "".join([str(int(messageIndex) ^ int(keyIndex)) for messageIndex, keyIndex in
                                 zip(encrypted_message, is_match_key)])
        print('Decrypted binary: ' + otp_decrypted)

        # take the joined string of original binary_message and turn back into list items for plaintext conversion (s1)
        n = 8
        s1 = [otp_decrypted[i:i+n] for i in range(0, len(otp_decrypted), n)]
        otp_plaintext = ''.join([chr(int(x, 2)) for x in s1])
        # print('Plaintext: ' + otp_plaintext)

        return otp_plaintext

    # ONCE RC4 runs its loops, then we have the generated keystream and message for rc4 function to encrypt!
    def rc4_initialize(self):
        key = self.key
        s = [n for n in range(256)]
        k = [n for n in range(256)]
        key_size = len(key)
        message_size = len(self.message)

        # initialization
        for i in range(256):
            # initialize Temporary list s[i]: 0-255
            s[i] = i
            # temp list k assignment of each key value to a list index 0-255 (ex. [k], [e], [y], [k], [e], [y]...
            k = key[i % key_size]
            print('k[' + str(i) + '] = ' + str(k))

        # index pointer J
        j = 0
        # Phase 2:
        for i in range(256):
            # we need initialize permuted state list s[j] 0-255, get j value
            j = (j + s[i] + (ord(key[i % key_size]))) % 256
            print('j = ' + str(j))
            s[j], s[i] = s[i], s[j]

        # index pointer i and j
        i = 0
        j = 0

        print(message_size)
        plaintext = message_size
        while plaintext > 0:
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            # print('index before swap: ')
            # print('s[j] = ' + str(s[j]))
            # print('s[i] = ' + str(s[i]))
            s[j], s[i] = s[i], s[j]
            # print('index after swap: ')
            # print('s[j] = ' + str(s[j]))
            # print('s[i] = ' + str(s[i]))
            t = s[(s[i] + s[j]) % 256]

            self.keystream.append(t)
            # print('keystream byte: ' + str(self.keystream))
            plaintext -= 1
            # print('subtract plaintext: ' + str(plaintext))

        return self.keystream

# ---------------------------------Main() - Cryptography Menu:------------------------------------------------


def main():

    # Console loop
    print('\nWelcome to Caesar Cipher.\n')
    print('\nPlease enter your choice from menu below:\n')

    test_cases = {1: 'One Pad Time, select 1',
                  2: 'RC4, select 2',
                  3: 'Exit this menu'}

    # Map user console input to a test case
    # userChoices is a dictionary, key points to test case
    # Includes user input exception handling
    # Loop until user input is '3'
    def user_input(user_choices):
        while True:
            print(' your choices'.upper(), '\t\t\tTest Case\n'.upper(), '-' * 55)

            for key, value in user_choices.items():
                print('\t', key, ' \t\t\t\t', value)
            try:
                choice = int(input("\nPlease enter the numeric choice for a Test Case \n\t --> ".upper()))
            except:
                print("\nSomething went wrong, please enter a numeric value!!!\n")
                continue

            if choice == 3:
                break

            menu_except(choice)

    # "Please enter the numeric choice for a Test Case"
    # Map user menu selection (parameter) to module (function call)
    def menu_except(choice):

        # Ask the user for a message and key = choice 1
        # Ask the user for a message  and a short  key = choice 2
        if choice == 1:
            print('One Time Pad: ')
            print('Encrypting Now: ')
            otp_input_message = input('\tEnter a message! ')
            otp_encrypt_key = input('\tEnter message key (key must be as long as the message)! ')

            # check to see if lengths are the same btwn key and input message
            if len(otp_input_message) == len(otp_encrypt_key):
                otp_encryption = Cryptography(otp_input_message, otp_encrypt_key, choice)
                # convert message to binary
                binary_message = otp_encryption.binary_otp_message_conversion()
                print('Original Binary message: ' + binary_message)
                # convert key to binary
                binary_key = otp_encryption.binary_otp_key_conversion()
                print('Key: ' + binary_key)
                # encrypt with otp using message xor key
                encrypted_message = otp_encryption.otp_return_ciphertext(binary_message, binary_key)
                print('Encrypted message: ' + encrypted_message)

                # decrypt otp
                print('\nDecrypting Now: ')
                print('Please enter a key to decrypt One Time Pad!')
                otp_decrypt_key = input('\tWaiting...,Enter message key (it must be as long as the message)! ')
                if len(otp_input_message) == len(otp_decrypt_key):
                    print('Original Binary message: ' + binary_message)
                    # need to decrypt another key so created an opt_decryption object
                    otp_decryption = Cryptography(binary_message, otp_decrypt_key, choice)
                    #get the binary key
                    match_key = otp_decryption.binary_otp_key_conversion()
                    #return plaintext
                    decrypted_message = otp_encryption.otp_return_plaintext(encrypted_message, match_key)
                    print('\nDecrypted! ')
                    print('PlainText: ' + str(decrypted_message + '\n'))
            else:
                print('\nTry Again! Length of the key must be equal to the length of the plaintext string!\n')
                user_input(test_cases)
        elif choice == 2:
            print('RC4 ')
            rc4_input_message = input('\t Please enter a message to encrypt! ')
            rc4_input_key = input('\tEnter message short key! ')
            # RC4 encrypt key
            rc4_initialize_key = Cryptography(rc4_input_message, rc4_input_key, choice)
            # get keystream
            keystream = rc4_initialize_key.rc4_initialize()
            print('keystream = ' + str(keystream))
            # encrypt rc4 using one time pad encryption
            #rc4_key = Cryptography(rc4_input_message, keystream, choice)
            rc4_encrypted_message = rc4_initialize_key.RC4_return_ciphertext()
            print('Encrypted message: ' + str(rc4_encrypted_message))

            # Decrypt RC4
            print('Please enter a key to decrypt RC4!')
            rc4_decrypt_key = input('\tWaiting...,Enter message key! ')
            # decrypt key
            rc4_decrypt_key = Cryptography(rc4_input_message, rc4_decrypt_key, choice)
            is_match_key = rc4_decrypt_key.rc4_initialize()
            print('keystream = ' + str(is_match_key))
            # Decrypted message (Plaintext)
            decrypted_message = rc4_decrypt_key.rc4_return_plaintext(rc4_encrypted_message, is_match_key)
            print('\nDecrypted! ')
            print('PlainText is: ' + str(decrypted_message + '\n'))
        else:
            print('What you talking about? Please try a valid choice! Choose 1, 2, or 3')
            input('*************** Press Enter to continue ******************\n\n'.upper())

    user_input(test_cases)
    input('\n\nPress ENTER, Say Bye-bye'.upper())


main()

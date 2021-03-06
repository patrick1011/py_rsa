from flask import abort
import datetime


def log_message(message):
    """Logs message to message_log

    Args:
        message (str): plaintext to save.

    Side effects:
        Reads and alters message_log.txt
    """

    with open('server/message_log.txt', 'a') as log:
        line = ' '.join(['[', str(datetime.datetime.now()), ']', message, '\n'])
        log.write(line)
        log.close()


def decrypt(ciphertext, private_exponent, modulus, not_unicode_handler):
    """Decrypts RSA excrypted message using plaintext =
    ciphertext**PRIVATE_EXPONENT % MODULUS.  Once decrypted turns plaintext
    back into ASCII.

    Args:
        ciphertext (int): Ciphertext to be decrypted.
        private_exponent (): Private exponent of encryption scheme.
        modulus (): Modulus of encryption scheme.
        not_unicode_handler (): Function to be called if plaintext not unicode.

    Environment variables:
        PRIVATE_EXPONENT (int): private exponent of encryption scheme.
        MODULUS (int): modulus used in encryption scheme.

    Returns:
        if plaintext is decodable: (str) Decrypted plaintext
        if plaintext is not decodable: not_unicode_handler()
    """

    int_plaintext = pow(ciphertext, private_exponent, modulus)

    _bytes = (modulus.bit_length() + 7) // 8
    byte_plaintext = int_plaintext.to_bytes(_bytes, 'big')

    try:
        plaintext_string = byte_plaintext.decode()
    except UnicodeDecodeError:
        message = 'Plaintext not unicode, message not logged.'
        return not_unicode_handler(message)

    return plaintext_string

message = 'SOMETHING ELSE'

bin_message = int.from_bytes(message.encode(), 'big')

cypertext = pow(bin_message, public_exponent, n)

plaintext = pow(cypertext, private_key, n)

plaintext_message = plaintext.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

print(plaintext_message)

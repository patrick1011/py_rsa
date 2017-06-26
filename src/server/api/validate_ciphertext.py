from flask import abort


def validate_ciphertext(body):
    """Validates incoming request body to ensure well-formed ciphertext.

    Returns 400 if:
        1. Request body doesn't have 'cipher_text' key.
        2. Ciphertext is not type int.

    Args:
        (dict) request body.

    Side Effects:
        Returns 400 and termiantes request processing.
    """

    try:
        cipher_text = body['cipher_text']
    except KeyError as error:
        return abort(400, 'malformed body, expecting cipher_text key.')

    if (type(cipher_text) is not int):
        return abort(400, 'malformed body, expecting int cipher_text.')
    return cipher_text

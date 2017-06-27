from flask import abort


def validate_ciphertext(body, invalid_handler):
    """Validates incoming request body to ensure well-formed ciphertext.

    Calls invalid_handler if:
        1. Request body doesn't have 'ciphertext' key.
        2. Ciphertext is not type int.

    Args:
        body (dict): Request body.
        invalid_handler (func) .

    Side Effects:
        Returns 400 and termiantes request processing.
    """

    try:
        ciphertext = body['ciphertext']
    except KeyError as error:
        return abort(400, 'malformed body, expecting ciphertext key.')

    if (type(ciphertext) is not int):
        return abort(400, 'malformed body, expecting int ciphertext.')
    return ciphertext

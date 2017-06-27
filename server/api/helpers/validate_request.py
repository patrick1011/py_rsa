def validate_request(body, invalid_handler):
    """Validates incoming request body to ensure well-formed ciphertext.

    Calls invalid_handler if:
        1. Request body doesn't have 'ciphertext' key.
        2. Ciphertext is not type int.

    Args:
        body (dict): Request body.
        invalid_handler (func).
    """

    try:
        ciphertext = body['ciphertext']
    except KeyError as error:
        return invalid_handler('malformed body, expecting ciphertext key.')

    if (type(ciphertext) is not int):
        return invalid_handler('malformed body, expecting int ciphertext.')
    return ciphertext

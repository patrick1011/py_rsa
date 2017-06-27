from flask import abort


def abort_wrapper(http_code):
    """Wrapper around flask abort.

    Motivation: returns function we can pass into services to ensure
    they are pure (and so can be tested).

    Args:
        http_code (int): http code to pass into flask's abort.

    Returns:
        (func) which when called triggers flask's abort.
    """

    def wrapped(message):
        return abort(http_code, message)
    return wrapped

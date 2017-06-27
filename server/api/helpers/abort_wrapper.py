from flask import abort


def abort_wrapper(http_code):
    def wrapped(message):
        return abort(http_code, message)
    return wrapped

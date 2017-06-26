from flask import Blueprint
from flask import request

from src.server.api.validate_ciphertext import validate_ciphertext
from src.server.decrypt import decrypt

from src.server.log_message import log_message

blueprint = Blueprint('routes', __name__)


@blueprint.route('/message', methods=['POST'])
def process_incoming_ciphertext():
    """Route to process incoming message.  Validates, decrypts, and saves
    incoming message.

    Args:
        Uses global flask request object. Request can be aborted anywhere using
        flask/abort.

    Returns:
        200 if message successfully prossessed otherwise exception rasied
        and appropriate HTTP status.
    """

    request_body = request.get_json(force=True)
    validated_ciphertext = validate_ciphertext(request_body)

    plaintext = decrypt(validated_ciphertext)
    log_message(plaintext)

    return 200

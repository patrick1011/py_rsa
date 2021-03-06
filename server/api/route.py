from flask import Blueprint
from flask import request

from server.api.helpers.abort_wrapper import abort_wrapper
from server.api.helpers.validate_request import validate_request as validate
from server.services import decrypt
from server.services import log_message

from server.settings import PRIVATE_EXPONENT, MODULUS

blueprint = Blueprint('routes', __name__)


@blueprint.route('/', methods=['POST'])
def process_incoming_ciphertext():
    """Route to process incoming message.  Validates, decrypts, and saves
    incoming message.

    Args:


    Variables required from settings.py:
        PUBLIC_EXPONENT (int): Public exponent used to decrypt.
        MODULUS (int): Modulus used to decrypt

    Returns:
        200 if message successfully prossessed otherwise exception rasied
        and appropriate HTTP status.
    """

    request_body = request.get_json(force=True)

    validated_ciphertext = validate(body=request_body,
                                    invalid_handler=abort_wrapper(400))

    plaintext = decrypt(ciphertext=validated_ciphertext,
                        private_exponent=PRIVATE_EXPONENT,
                        modulus=MODULUS,
                        not_unicode_handler=abort_wrapper(400))

    log_message(plaintext)

    return "message received successfully", 200

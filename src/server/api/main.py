from flask import Flask
import os

import src.server.api.infrastructure.error_handlers as error_handlers
import src.server.api.process_incoming as routes

app = Flask(__name__)

app.register_blueprint(error_handlers.blueprint)
app.register_blueprint(routes.blueprint)

if __name__ == "__main__":
    """Flask application to decrypt and save incoming messages.

    Environment variables required:
        PORT (int): which server is listening on.
        PUBLIC_EXPONENT (int): Public exponent used to decrypt.
        MODULUS (int): Modulus used to decrypt

    Returns:
        Outputs incoming messages to message_stream.txt.

    PUBLIC_EXPONENT and MODULUS generated using the key generator.
    """
    app.run(host='0.0.0.0', port=int(os.environ.get(key='PORT')))

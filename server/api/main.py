from flask import Flask
import os

import server.api.helpers.error_handlers as error_handlers
import server.api.process_incoming as routes

app = Flask(__name__)

app.register_blueprint(error_handlers.blueprint)
app.register_blueprint(routes.blueprint)

if __name__ == "__main__":
    """Flask application to decrypt and save incoming messages.

    Run this file as a module using:

    python -m server.api.main

    Returns:
        Outputs incoming messages to message_stream.txt.

    PUBLIC_EXPONENT and MODULUS generated using the key generator.
    """

    app.run(host='0.0.0.0', port=int(os.environ.get(key='PORT')))

"""Flask application to decrypt and save incoming messages.

Run this file as a module using:

python -m server.api.main

Requires:
    variables in server.settings to be populated.
"""

from flask import Flask

from server.settings import PORT

import server.api.helpers.error_handlers as error_handlers
import server.api.route as routes

app = Flask(__name__)

app.register_blueprint(error_handlers.blueprint)
app.register_blueprint(routes.blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)

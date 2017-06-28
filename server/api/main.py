"""Flask application to decrypt and save incoming messages.

Run this file as a module using:

python -m server.api.main

Requires:
    variables in server.settings to be populated.
"""

from flask import Flask

from server.settings import PORT

from server.api.helpers.error_handlers import blueprint as error_handlers
from server.api.route import blueprint as routes

app = Flask(__name__)

app.register_blueprint(error_handlers)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)

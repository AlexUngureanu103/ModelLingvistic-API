from flask import Flask, request, jsonify
from flasgger import Swagger

from Rest.Controllers.TranslateController import translate_controller
from Rest.Controllers.UserController import user_controller
from Rest.Controllers.TranslatedEntryController import translated_entry_controller

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(user_controller)
app.register_blueprint(translate_controller)
app.register_blueprint(translated_entry_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)



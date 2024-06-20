from flask import Flask
from flasgger import Swagger

from Rest.Controllers.FavoriteTranslationEntryController import favorite_translation_entry_controller
from Rest.Controllers.TranslateController import translate_controller
from Rest.Controllers.UserController import user_controller
from Rest.Controllers.HistoryTranslationEntryController import history_translation_entry_controller

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(user_controller)
app.register_blueprint(translate_controller)
app.register_blueprint(history_translation_entry_controller)
app.register_blueprint(favorite_translation_entry_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

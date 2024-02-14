from flask import Flask, request, jsonify
from flasgger import Swagger
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from Rest.Controllers.TranslateController import translate_controller
from Rest.Controllers.UserController import user_controller

app = Flask(__name__)
swagger = Swagger(app)

checkpoint = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

app.register_blueprint(user_controller)
app.register_blueprint(translate_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)



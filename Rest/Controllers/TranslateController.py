from flask import Flask, request, jsonify, Blueprint
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

translate_controller = Blueprint('translate_controller', __name__)


@translate_controller.route('/translate-ro', methods=['Post'])
def translate_to_ro():
    """
    Translate English to Romanian
    ---
    tags:
      - Translate
    parameters:
      - name: prompt
        in: body
        required: true
        type: string
        description: The prompt string to process.
    responses:
      200:
        description: Successful operation
    """
    print(request.json)
    prompt = request.json.get('prompt')  # Accessing prompt from request body

    prefix = "Translate English to Romanian: "
    return translate(prefix, prompt)


@translate_controller.route('/translate-fr', methods=['Post'])
def translate_to_fr():
    """
    Translate English to French
    ---
    tags:
      - Translate
    parameters:
      - name: prompt
        in: body
        required: true
        type: string
        description: The prompt string to process.
    responses:
      200:
        description: Successful operation
    """
    print(request.json)
    prompt = request.json.get('prompt')  # Accessing prompt from request body

    prefix = "Translate English to French: "
    return translate(prefix, prompt)


@translate_controller.route('/translate', methods=['GET'])
def test():
    """
    Test
    ---
    tags:
      - Translate
    responses:
      200:
        description: Successful operation
    """
    return jsonify({"output": "Hello World"})


def translate(prefix, prompt):
    text = prefix + prompt

    inputs = tokenizer(text, return_tensors="pt").input_ids

    outputs = model.generate(inputs, max_new_tokens=200, do_sample=True, top_k=30, top_p=0.95)

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"output": result})

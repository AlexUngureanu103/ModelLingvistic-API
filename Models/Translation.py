class Translation:
    def __init__(self, _id: str, prompt: str, prompt_translation: str, translation_type: str):
        self.prompt = prompt
        self.prompt_translation = prompt_translation
        self.translation_type = translation_type
        self._id = _id

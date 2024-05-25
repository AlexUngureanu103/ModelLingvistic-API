class TranslatedEntry:
    def __init__(self, _id: str, prompt: str, prompt_language: str, translated_prompt: str, translated_language: str,
                 user_id: str):
        self.user_id = user_id
        self.prompt = prompt
        self.prompt_language = prompt_language
        self.translated_prompt = translated_prompt
        self.translated_language = translated_language
        self._id = _id


class CreateOrUpdateTranslatedEntry:
    def __init__(self, prompt: str, prompt_language: str, translated_prompt: str, translated_language: str,
                 user_id: str):
        self.user_id = user_id
        self.prompt = prompt
        self.prompt_language = prompt_language
        self.translated_prompt = translated_prompt
        self.translated_language = translated_language
        self._id = None

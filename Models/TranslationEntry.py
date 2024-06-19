class TranslationEntry:
    def __init__(self, _id: str, prompt: str, prompt_language: str, translated_prompt: str, translated_language: str,
                 user_id: str, locale_id: str):
        self.user_id = user_id
        self.prompt = prompt
        self.prompt_language = prompt_language
        self.translated_prompt = translated_prompt
        self.translated_language = translated_language
        self.locale_id = locale_id
        self._id = _id

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'prompt_language': self.prompt_language,
            'translated_language': self.translated_language,
            'prompt': self.prompt,
            'translated_prompt': self.translated_prompt,
            'locale_id': self.locale_id,
            '_id': self._id
        }


class CreateOrUpdateTranslationEntry:
    def __init__(self, prompt: str, prompt_language: str, translated_prompt: str, translated_language: str,
                 user_id: str, locale_id: str):
        self.user_id = user_id
        self.prompt = prompt
        self.prompt_language = prompt_language
        self.translated_prompt = translated_prompt
        self.translated_language = translated_language
        self.locale_id = locale_id
        self._id = None

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'prompt_language': self.prompt_language,
            'translated_language': self.translated_language,
            'prompt': self.prompt,
            'translated_prompt': self.translated_prompt,
            'locale_id': self.locale_id,
            '_id': self._id
        }

from database.db import db
from .abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)

    def to_dict(self):
        return {
            'name': str(self.data['name']),
            'acronym': self.data['acronym']
        }

    @classmethod
    def list_dicts(cls):
        languages = cls._collection.find()
        language_dicts = []

        for language in languages:
            language_dict = {
                'name': language['name'],
                'acronym': language['acronym']

            }
            language_dicts.append(language_dict)

        return language_dicts

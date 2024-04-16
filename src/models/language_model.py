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

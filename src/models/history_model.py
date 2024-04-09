from database.db import db
from models.abstract_model import AbstractModel

import json
from bson import ObjectId
from datetime import datetime


class HistoryModel(AbstractModel):
    _collection = db["history"]

    def __init__(self, json_data):
        super().__init__(json_data)

    @classmethod
    def list_as_json(cls, query={}):
        data = cls._collection.find(query)
        return BsonToJson().encode(list(data))


class BsonToJson(json.JSONEncoder):
    def default(self, attribute):
        if isinstance(attribute, (ObjectId, datetime)):
            return str(attribute)
        return json.JSONEncoder.default(self, attribute)

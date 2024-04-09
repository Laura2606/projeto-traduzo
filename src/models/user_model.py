from database.db import db
from models.abstract_model import AbstractModel


class UserModel(AbstractModel):
    _collection = db["users"]

    def token_is_valid(self, token):
        return self.data["token"] == token

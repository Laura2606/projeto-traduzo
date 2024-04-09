from src.models.history_model import HistoryModel


class _TestUppperVersionOfJson(HistoryModel):
    """E se os dados vierem com todas as letras maiúsculas?"""

    @classmethod
    def list_as_json(cls, query={}):
        return super(_TestUppperVersionOfJson, cls).list_as_json(query).upper()


class _TestLowerVersionOfJson(HistoryModel):
    """E se os dados vierem com todas as letras minúsculas?"""

    @classmethod
    def list_as_json(cls, query={}):
        return super(_TestLowerVersionOfJson, cls).list_as_json(query).lower()

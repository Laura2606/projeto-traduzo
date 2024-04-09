from src.models.user_model import UserModel


class _TestUserEmptyAttributes(UserModel):
    """
    E se os atributos do usuário forem salvos com valor diferente no banco?
    """

    def __init__(self, json_data: dict):
        json_data.update({key: "" for key in json_data})
        super().__init__(json_data)


class _TestUserNameEqualsToken(UserModel):
    """
    E se o token e nomes possuirem valores iguais?
    """

    def __init__(self, json_data: dict):
        json_data.update(name=json_data["token"], token=json_data["name"])
        super().__init__(json_data)

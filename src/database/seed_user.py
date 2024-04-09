from models.user_model import UserModel

languages = [
    {"name": "Peter", "level": "admin", "token": "token_secreto123"},
    {"name": "Vini", "level": "admin", "token": "soeusei"},
]


def seed_user():
    UserModel.drop()

    print("Carregando os Usuários")
    for language in languages:
        UserModel(language).save()

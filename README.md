Olá!
Neste projeto foi desenvolvida uma ferramenta de tradução de textos para vários idiomas, utilizando
Python com Framework Flask para criar uma aplicação Server Side.
Para realizá-lo implementei uma API utilizando arquitetura em camadas MVC, utilizei o Docker, POO,
escrevi testes para APIs para garantir a implementação correta dos endpoints e interagi com o MongoDB (banco de dados não relacional).

Como executar o projeto:

1º passo - Criar o ambiente virtual para o projeto:
python3 -m venv .venv && source .venv/bin/activate

2º passo - Instalar as dependências:
python3 -m pip install -r dev-requirements.txt

3º Subir o conteiner:
docker compose up translate

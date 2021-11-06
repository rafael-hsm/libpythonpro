import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github

    :param usuario: str com o nome de usuário
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


user = input('Digite o nome do usuário: ')
print(buscar_avatar(user))

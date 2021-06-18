import requests

def buscar_cidade_cep(cep):
    response = requests.get(
        f'http://viacep.com.br/ws/{cep}/json/'
    )
    return response
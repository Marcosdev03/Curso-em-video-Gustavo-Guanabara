import requests

def testa_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'O site {url} está acessível.')
        else:
            print(f'O site {url} não está acessível. Status code: {response.status_code}')
    except requests.ConnectionError:
        print(f'Erro! Não foi possível acessar o site {url}.')

# Exemplo de uso
testa_site('http://www.pudim.com.br')

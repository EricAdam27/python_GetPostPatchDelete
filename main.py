import requests

# Pegar Informações - GET

requisicao = requests.get('https://testgetpostpatchdelete-default-rtdb.firebaseio.com/.json')
print(requisicao)  # Retorna o Status

requisicao = requisicao.json()
print(f'\n{requisicao}')  # Retorna o Dicionário

# Criar Informações - POST

informacoes = '{"Nome":"Deric"}'

requisicao = requests.post('https://testgetpostpatchdelete-default-rtdb.firebaseio.com/.json', data=informacoes)
print(requisicao)

requisicao = requisicao.json()
print(f'\n{requisicao}')

# Editar Informações - PATCH

informacoes = '{"Nome":"Deric", "Sobrenome":"Adam", "Idade":0}'

requisicao = requests.patch('https://testgetpostpatchdelete-default-rtdb.firebaseio.com/-NEqOZFcM6CtOCE24Sau.json', data=informacoes)
print(requisicao)

requisicao = requisicao.json()
print(f'\n{requisicao}')

# Deletar Informações - DELETE

requisicao = requests.delete('https://testgetpostpatchdelete-default-rtdb.firebaseio.com/-NEqg4tkAzbADJaGK7u5.json')
print(requisicao)

requisicao = requisicao.json()
print(f'\n{requisicao}')

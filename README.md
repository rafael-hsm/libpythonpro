# Lib Python Pro
## Módulo para exemplificar a construção de projetos Python no curso PyTools

Nesse curso é ensinado como contribuir com projetos de código aberto.

Link para o curso [Python Pro](https://pythonpro.com.br/)

[![Build Status](https://app.travis-ci.com/rafael-hsm/libpythonpro.svg?branch=main)](https://app.travis-ci.com/rafael-hsm/libpythonpro)
[![Updates](https://pyup.io/repos/github/rafael-hsm/libpythonpro/shield.svg)](https://pyup.io/repos/github/rafael-hsm/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/rafael-hsm/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/rafael-hsm/libpythonpro/)
[![codecov](https://codecov.io/gh/rafael-hsm/libpythonpro/branch/main/graph/badge.svg?token=zlCJjFFDJ6)](https://codecov.io/gh/rafael-hsm/libpythonpro)

Tópicos a serem abordados:
1. Git
2. Virtualenv
3. Pip

# Instalação e Utilização

Instale via pip:
`pip install libpythonpro_rafa`


Para utilizar importe a biblioteca dessa forma:

`from libpythonpro.github_api import buscar_avatar`

Exemplo:
```
from libpythonpro.github_api import buscar_avatar

avatar = input('Digite o nome do Usuário: ')
resp = buscar_avatar(avatar)
print(resp)

Digite o nome do usuário: rafael-hsm
https://avatars.githubusercontent.com/u/82055965?v=4

```
O print retornará o link do avatar desejado.

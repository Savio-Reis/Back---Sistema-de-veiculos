# Minha API

Esta API foi desenvolvida para gerenciar veículos, permitindo operações de adição, visualização, atualização e remoção de veículos na base de dados. A API é documentada utilizando o Swagger, Redoc e RapiDoc.
Possui 5 Endpoints: POST /veiculo, GET /veiculos, PUT /veiculos GET /veiculos por codigofipe, DELETE /veiculos

Endpoint: POST /veiculo
Parâmetros de entrada:
form (corpo da solicitação): Dados do veículo a ser adicionado.
Respostas:
200 OK: Retorna uma representação do veículo de acordo com as informações selecionadas.
409 Conflict: Retorna uma mensagem de erro se já tiver um mesmo veículo cadastrado.
400 Bad Request: Retorna uma mensagem de erro se não for possível salvar a nova veiculo.

Endpoint: GET /veiculos
Respostas:
200 OK: Retorna uma representação da listagem de veiculos no banco de dados.
404 Not Found: Retorna uma mensagem de que não há veiculos cadastradas.

Endpoint: PUT /veiculos
Respostas:
200 OK: Retorna uma representação da listagem de veiculos.
404 Not Found: Retorna uma mensagem de que não há veiculos cadastrados.

Endpoint: GET /veiculos
Parâmetros de entrada:
query (corpo da solicitação): ID da veiculo a ser removida.
Respostas:
200 OK: Retorna uma mensagem de confirmação da remoção.
404 Not Found: Retorna uma mensagem de erro se a veiculo não for encontrada na base.

Endpoint: DELETE /veiculo
Parâmetros de entrada:
query (corpo da solicitação): Codigofipe do veiculo a ser removido.
Respostas:
200 OK: Retorna uma mensagem de confirmação da remoção.
404 Not Found: Retorna uma mensagem de erro se o veiculo não for encontrada na base.

## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```


Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.



Criar imagem Docker: docker build -t api-docker .
Executar Docker:  docker run -p 5000:5000 api-docker
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Veiculo
from logger import logger
from schemas import *
from flask_cors import CORS

from datetime import datetime

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
veiculo_tag = Tag(name="Veículos", description="Adição, visualização e remoção de veículos à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# adiciona um veiculo no baco de dados
@app.post('/veiculo', tags=[veiculo_tag],
          responses={"200": VeiculoViewSchema,"409": ErrorSchema, "400": ErrorSchema})
def add_veiculo(form: VeiculoSchema):
    """Adiciona um novo veiculo à base de dados

    Retorna uma representação do veiculo.
    """
    (form)
    # criar novo veiculo com base nos dados recebidos
    veiculo = Veiculo(
        marca = form.marca,
        modelo = form.modelo,
        data_fabricacao = form.data_fabricacao,
        valor = form.valor,
        codigo_fipe= form.codigo_fipe)

    logger.debug(f"Adicionando novo veiculo: '{veiculo.marca}'")
    
    print(veiculo)
    try:
        # criando conexão com a base
        session = Session()

        # adicionando veiculo
        session.add(veiculo)

        # comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado veiculo em nome de: '{veiculo.marca}'")
        return apresenta_veiculo(veiculo), 200

    except Exception as e:
        # caso ocorra um erro
        error_msg = "Não foi possível salvar novo veiculo, verifique se os dados estão corretos"
        logger.warning(f"Erro ao adicionar veículo '{veiculo.marca}', {error_msg}")
        return {"message": error_msg}, 400
    
    except IntegrityError as e:
        # não permite mais de um veículo igual no cadastro
        error_msg = "Veículo já cadastrado"
        logger.warning(f"Erro ao adicionar veículo '{veiculo.marca}', {error_msg}")
        return {"mesage": error_msg}, 409

# atualiza um veiculo no baco de dados
@app.put('/veiculo', tags=[veiculo_tag],
          responses={"200": VeiculoViewSchema,"409": ErrorSchema, "400": ErrorSchema})
def update_veiculo(form: VeiculoUpdateSchema):
    """Atualiza um veículo cadastrado.

    Retorna uma representação de um veículo.
    """
    # criando conexão com a base
    session = Session()
    # buscando veiculo
    veiculo = session.query(Veiculo).filter(Veiculo.codigo_fipe == form.codigo_fipe_anterior).first()

    if veiculo:
        veiculo.marca = form.marca
        veiculo.modelo = form.modelo
        veiculo.data_fabricacao = form.data_fabricacao
        veiculo.valor = form.valor
        veiculo.codigo_fipe = form.codigo_fipe
        session.commit()
        return {"message": "Veículo localizado", "id": form.id}

    error_msg = "Não foi possível encontrar o veículo, verifique se os dados estão corretos"
    return {"message": error_msg}, 404

# busca por veículo cadastrado
@app.get('/veiculo/<codigo_fipe>', tags=[veiculo_tag],
         responses={"200": VeiculoViewSchema, "404": ErrorSchema})
def get_veiculo(path: VeiculoBuscaSchema):
    """Faz a busca por um veículo cadastrado.

    Retorna uma representação de um veículo.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    veiculo = session.query(Veiculo).filter(Veiculo.codigo_fipe == path.codigo_fipe).first()
    
    if veiculo:
       return apresenta_veiculo(veiculo), 200

    error_msg = "Não foi possível encontrar o veiculo, verifique se os dados estão corretos"
    return {"message": error_msg}, 404


# busca por todas os veículos cadastrados
@app.get('/veiculos', tags=[veiculo_tag],
         responses={"200": ListagemVeiculoSchema, "404": ErrorSchema})
def get_veiculos():
    """Faz a busca por todos os veículos cadastrados.

    Retorna uma representação da listagem de veículos.
    """
    logger.debug(f"Coletando veículos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    veiculos = session.query(Veiculo).all()

    #verifica se não há veículos cadastrados
    if not veiculos:
        return {"veiculos": []}, 200
    else:
        logger.debug(f"%d veículos encontrados" % len(veiculos))
        # retorna a representação de veículo
        return apresenta_veiculos(veiculos), 200

# deleta veiculos selecionadas
@app.delete('/veiculo', tags=[veiculo_tag],
            responses={"200": VeiculoDelSchema, "404": ErrorSchema})
def del_veiculo(query: VeiculoBuscaSchema):
    """Deleta um veículo a partir do id informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    logger.debug(f"Deletando dados sobre veículo selecionado #{query.codigo_fipe}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Veiculo).filter(Veiculo.codigo_fipe == query.codigo_fipe).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado o Veículo. #{query.codigo_fipe}")
        return {"message": "Veículo removido", "codigo_fipe": query.codigo_fipe}
    else:
        # se o veículo não foi encontrado
        error_msg = "Veículo não encontrado na listagem."
        logger.warning(f"Erro ao deletar Veículo #'{query.codigo_fipe}', {error_msg}")
        return {"message": error_msg}, 404

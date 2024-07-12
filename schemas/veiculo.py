from datetime import date
from pydantic import BaseModel
from typing import List
from model.veiculo import Veiculo


class VeiculoSchema(BaseModel):
    """ Define como um novo veículo deve ser representada
    """
    marca: str = "Fiat"
    modelo: str = "Palio"
    data_fabricacao: int = 2009
    valor: str = "R$ 20.000"
    codigo_fipe: str = "AAA1324"

class VeiculoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca de um veículo. Que será
        feita apenas com base no id do veículo.
    """
    codigo_fipe: str

def apresenta_veiculos(veiculos: List[Veiculo]):
    """ Retorna uma representação de veículos seguindo o schema definido em
        VeiculoViewSchema.
    """
    result = []
    for veiculo in veiculos:
        result.append({
            "id": veiculo.id,
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "data_fabricacao": veiculo.data_fabricacao,
            "valor": veiculo.valor,
            "codigo_fipe": veiculo.codigo_fipe
       })

    return {"veiculos": result}

class VeiculoViewSchema(BaseModel):
    """ Define como uma será exibido um veículo: marca + modelo + fabricacao + valor
    """
    id: int = 1
    marca: str = "Fiat"
    modelo: str = "Palio"
    data_fabricacao: int = 2009
    valor: str = "R$ 20.000"
    codigo_fipe: str = "AAA1324"

class VeiculoUpdateSchema(BaseModel):
    """ Define como uma será exibido um veículo: marca + modelo + fabricacao + valor
    """
    marca: str = "Fiat"
    modelo: str = "Palio"
    data_fabricacao: int = 2009
    valor: str = "R$ 20.000"
    codigo_fipe: str = "AAA1324"
    codigo_fipe_anterior: str = "AAA1324"
    

class ListagemVeiculoSchema(BaseModel):
    """ Define como uma listagem de veículos que será retornada.
    """
    veiculos:List[VeiculoViewSchema]
    
class VeiculoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome_pessoa: str

def apresenta_veiculo(veiculo: Veiculo):
    """ Retorna uma representação de veículo seguindo o schema definido em
        VeiculoViewSchema.
    """
    return {
        "id": veiculo.id,
        "marca": veiculo.marca,
        "modelo": veiculo.modelo,
        "data_fabricacao": veiculo.data_fabricacao,
        "valor": veiculo.valor,
        "codigo_fipe": veiculo.codigo_fipe
    }



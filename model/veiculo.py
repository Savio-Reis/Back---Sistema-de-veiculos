from sqlalchemy import Column, String, Integer, Float
from  model import Base


class Veiculo(Base):
    __tablename__ = 'veiculos'

    id = Column(Integer, primary_key=True)
    marca = Column(String(100), nullable=False)
    modelo= Column(String(100), nullable=False)
    data_fabricacao= Column(Integer)
    valor= Column(String(100))
    codigo_fipe= Column(String(100))

    def __init__(self, marca: str, modelo: str, data_fabricacao: int, valor: str, codigo_fipe: str):
        """
        Cria um Veículo

        Arguments:
            marca: marca do veiculo.
            modelo: modelo do veículo
            data_fabricacao: ano de fabricação do veículo.
            valor: valor do veículo.
            codigo_fipe: mostra o codigo fipe do veiculo
        """
        self.marca = marca
        self.modelo = modelo
        self.data_fabricacao = data_fabricacao
        self.valor = valor
        self.codigo_fipe = codigo_fipe
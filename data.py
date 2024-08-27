import pandas as pd
from pyspark.sql import SparkSession


class Precos:
    def __init__(self):
        self.path = "precos_manaus.csv"
        self.spark = SparkSession.builder \
            .appName("Leitura de CSV") \
            .getOrCreate()
        self.df = self.spark.read.csv("precos_combustivel.csv",
                                      header=True, sep=";", inferSchema=True)

    @property
    def data(self):
        return self.df.filter(self.df['Estado - Sigla'] == "AM")

    @property
    def get_unique_bairros(self):
        return sorted([row['Bairro'] for row in self.data.filter(self.data['Municipio'] == 'MANAUS').select('Bairro').distinct().collect()])

    @property
    def get_unique_products(self):
        return sorted([row['Produto'] for row in self.data.filter(self.data['Municipio'] == 'MANAUS').select('Produto').distinct().collect()])

    def get_distrib_preco_by_bairro(self, bairro, produto):
        resultado = self.data.filter(self.data['Municipio'] == 'MANAUS').filter(
            self.data['Bairro'] == bairro).filter(self.data['Produto'] == produto).select('Valor de Venda')
        return resultado.toPandas()

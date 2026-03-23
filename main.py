import csv

from modelos.municipio import Municipio

try:
    with open("dados/municipios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        municipios = []
        for linha in leitor:
            municipio = Municipio(
                nome=linha["municipio"],
                estado=linha["estado"],
                regiao=linha["regiao"],
                populacao=int(linha["populacao"])
            )
            municipios.append(municipio)
            print(municipio.resumo())

except FileNotFoundError:
    print("Arquivo não encontrado.")
except ValueError:
    print("Erro ao ler o arquivo.")
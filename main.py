import csv
import json

from modelos.municipio import Municipio

def municipio_mais_populoso(municipios):
    maior = municipios[0]
    for municipio in municipios[1:]:
        if municipio.populacao > maior.populacao:
            maior = municipio
    return maior
    
def populacao_por_regiao(municipios):
    regiao_populacao = {}
    for municipio in municipios:
        if municipio.regiao not in regiao_populacao:
            regiao_populacao[municipio.regiao] = 0
        regiao_populacao[municipio.regiao] += municipio.populacao
    return regiao_populacao
    
def municipios_por_regiao(municipios):
    regiao_municipios = {}
    for municipio in municipios:
        if municipio.regiao not in regiao_municipios:
            regiao_municipios[municipio.regiao] = []
        regiao_municipios[municipio.regiao].append(municipio)
    return regiao_municipios

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

        mais_populoso = municipio_mais_populoso(municipios)

        pop_por_regiao = populacao_por_regiao(municipios)

        muns_por_regiao = municipios_por_regiao(municipios)

        print(f"Município mais populoso: {mais_populoso.nome} com {mais_populoso.populacao} habitantes.")

        print("População por região:")
        print(pop_por_regiao)
            
        print("Municípios por região:") 
        for regiao, lista in muns_por_regiao.items():
            nomes = [m.nome for m in lista]
            print(f"{regiao}: {nomes}")

        relatorio = {
            "municipio_mais_populoso": {
                "nome": mais_populoso.nome,
                "populacao": mais_populoso.populacao
            },
            "populacao_por_regiao": pop_por_regiao,
            "municipios_por_regiao": {regiao: [m.nome for m in lista] for regiao, lista in muns_por_regiao.items()}
        }

        with open("relatorio.json", "w", encoding="utf-8") as saida:
            json.dump(relatorio, saida, ensure_ascii=False, indent=4)

except FileNotFoundError:
    print("Arquivo não encontrado.")
except ValueError:
    print("Erro ao ler o arquivo.")
class Municipio:
    def __init__(self, nome, estado, regiao, populacao):    
        self.nome = nome
        self.estado = estado
        self.regiao = regiao
        self.populacao = populacao

    def resumo(self):
        return f"{self.nome} é um município localizado no estado de {self.estado}, na região {self.regiao}, com uma população de {self.populacao} habitantes."
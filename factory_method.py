class Veiculo:
    def _init_(self, id, modelo, disponibilidade, preco):
        self.id = id
        self.modelo = modelo
        self.disponibilidade = disponibilidade
        self.preco = preco

    def alugar(self):
        self.disponibilidade = False

    def devolver(self):
        self.disponibilidade = True

class Carro(Veiculo):
    def _init_(self):
        super()._init_(id=None, modelo="Carro", disponibilidade=True, preco=100)

class Moto(Veiculo):
    def _init_(self):
        super()._init_(id=None, modelo="Moto", disponibilidade=True, preco=50)

class Caminhao(Veiculo):
    def _init_(self):
        super()._init_(id=None, modelo="Caminhão", disponibilidade=True, preco=150)

class VeiculoFactory:
    @staticmethod
    def criarVeiculo(tipo):
        if tipo == 'Carro':
            return Carro()
        elif tipo == 'Moto':
            return Moto()
        elif tipo == 'Caminhão':
            return Caminhao()
        else:
            raise ValueError("Tipo de veículo desconhecido")
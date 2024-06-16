from datetime import datetime

class PrecoStrategy:
    def calcularPreco(self, dataInicio, dataFim):
        raise NotImplementedError

class PrecoPorHora(PrecoStrategy):
    def calcularPreco(self, dataInicio, dataFim):
        return (dataFim - dataInicio).total_seconds() / 3600 * 10

class PrecoPorDia(PrecoStrategy):
    def calcularPreco(self, dataInicio, dataFim):
        return (dataFim - dataInicio).days * 100

class Aluguel:
    def _init_(self, clienteId, veiculoId, dataInicio, dataFim, strategy: PrecoStrategy):
        self.clienteId = clienteId
        self.veiculoId = veiculoId
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.strategy = strategy
        self.valorTotal = self.strategy.calcularPreco(dataInicio, dataFim)
    
    def calcularValor(self):
        return self.valorTotal
    
    def gerarRecibo(self):
        recibo = f"Recibo:\nCliente ID: {self.clienteId}\nVeículo ID: {self.veiculoId}\nData Início: {self.dataInicio}\nData Fim: {self.dataFim}\nValor Total: {self.valorTotal}"
        return recibo
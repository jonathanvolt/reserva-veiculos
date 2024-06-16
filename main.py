from factory_method import VeiculoFactory
from strategy_pattern import PrecoPorHora, PrecoPorDia, Aluguel
from datetime import datetime

def main():
    # Criação de veículos
    carro = VeiculoFactory.criarVeiculo('Carro')
    moto = VeiculoFactory.criarVeiculo('Moto')
    caminhao = VeiculoFactory.criarVeiculo('Caminhão')

    # Exemplo de aluguel por hora
    dataInicio = datetime(2024, 6, 16, 10, 0, 0)
    dataFim = datetime(2024, 6, 16, 14, 0, 0)
    aluguel_por_hora = Aluguel(clienteId=1, veiculoId=carro.id, dataInicio=dataInicio, dataFim=dataFim, strategy=PrecoPorHora())

    print("Aluguel por Hora")
    print(f"Valor: {aluguel_por_hora.calcularValor()}")
    print(aluguel_por_hora.gerarRecibo())
    print()

    # Exemplo de aluguel por dia
    dataInicio = datetime(2024, 6, 16)
    dataFim = datetime(2024, 6, 18)
    aluguel_por_dia = Aluguel(clienteId=2, veiculoId=moto.id, dataInicio=dataInicio, dataFim=dataFim, strategy=PrecoPorDia())

    print("Aluguel por Dia")
    print(f"Valor: {aluguel_por_dia.calcularValor()}")
    print(aluguel_por_dia.gerarRecibo())

if _name_ == "_main_":
    main()
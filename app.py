def calcular_consumo_mensal(potencia, horas_dia):
    return (potencia * horas_dia * 30) / 1000

def calcular_custo_mensal(consumo, tarifa):
    return consumo*tarifa

while True:
    try:
        aparelho = input("Digite o nome do aparelho: ").strip()
        potencia = float(input("Digite a potência do aparelho (W): "))
        horas_dia = float(input("Digite as horas de uso por dia: "))

        if potencia <= 0 or horas_dia <= 0:
            print("Erro! Os valores devem ser maiores que zero.\n")
            continue

        consumo = calcular_consumo_mensal(potencia, horas_dia)
        custo = calcular_custo_mensal(consumo, 0.9)

        print("\n===== RESULTADO =====")
        print(f"Aparelho: {aparelho}")
        print(f"Consumo mensal estimado: {consumo:.2f} kWh")
        print(f"Custo mensal estimado: R${custo:.2f}")

        break

    except ValueError:
        print("Erro! Digite apenas números válidos.\n")
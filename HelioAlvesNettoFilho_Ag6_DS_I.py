def calcular_desconto(valor_compra):
    # Verifica em qual faixa de valor a compra se encaixa e define o percentual de desconto correspondente

    if valor_compra < 200:
        # Compras abaixo de R$ 200,00 recebem 5% de desconto
        percentual_desconto = 0.05
    elif valor_compra < 300:
        # Compras entre R$ 200,00 e R$ 300,00 recebem 10% de desconto
        # (o caso "< 200" já foi eliminado pelo if acima, então aqui já sabemos que valor_compra >= 200)
        percentual_desconto = 0.10
    else:
        # Qualquer valor a partir de R$ 300,00 recebe 15% de desconto
        percentual_desconto = 0.15

    # Calcula quanto em reais corresponde o desconto
    valor_desconto = valor_compra * percentual_desconto

    # Subtrai o desconto do valor original para obter o valor final a pagar
    valor_final = valor_compra - valor_desconto

    # Retorna os três valores calculados para quem chamou a função
    return percentual_desconto, valor_desconto, valor_final


def main():
    # Solicita ao usuário o valor da compra
    # input() sempre retorna uma string, por isso usamos float() para converter o texto digitado em um número com casas decimais
    valor_compra = float(input("Digite o valor total da compra: R$ "))

    # Chama a função que calcula o desconto e desempacota os valores retornados
    percentual, desconto, total_pagar = calcular_desconto(valor_compra)

    # Exibe os resultados formatados com duas casas decimais
    print(f"\nValor da compra: R$ {valor_compra:.2f}")
    print(f"Percentual de desconto aplicado: {percentual * 100:.0f}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor total a pagar: R$ {total_pagar:.2f}")


# Garante que main() só seja executada quando o arquivo for rodado diretamente
# (e não quando for importado como módulo em outro programa)
if __name__ == "__main__":
    main()
from unittest import case
import cambio
import divisao
import divisaointeira
import logaritmo
import potencia
import raiz
import soma
import subtrair
import multiplicar

def calculadora():
    print("\n--- CALCULADORA TERCEIRÃO: MODO MULTI-OPERACIONAL ---")
    
    try:
        opcao = input("Deseja realizar uma operação? (s/n): ").strip().lower()
        while opcao == 's':
            print("\nEscolha a operação:")
            operacao = input("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Divisão Inteira\n6. Potência\n7. Logaritmo\n8. Raiz Quadrada\n9.Preço cambial do dolar\nDigite o número da operação desejada: ").strip()
            match operacao:
                case '1':
                    print("Você escolheu: Soma")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    print(f"Soma: {soma.somar(a, b)}")
                case '2':
                    print("Você escolheu: Subtração")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    print(f"Subtração: {subtrair.subtrair(a, b)}")
                case '3':
                    print("Você escolheu: Multiplicação")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    print(f"Multiplicação: {multiplicar.multiplicar(a, b)}")
                case '4':
                    print("Você escolheu: Divisão")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    try:
                        print(f"Divisão: {divisao.divisao(a, b)}")
                    except ValueError as e:
                        print(f"Divisão: {e}")
                case '5':
                    print("Você escolheu: Divisão Inteira")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    try:
                        print(f"Divisão Inteira: {divisaointeira.divisaointeira(a, b)}")
                    except ValueError as e:
                        print(f"Divisão Inteira: {e}")
                case '6':
                    print("Você escolheu: Potência")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    print(f"Potência: {potencia.potencia(a, b)}")
                case '7':
                    print("Você escolheu: Logaritmo")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    try:
                        log_a, log_b = logaritmo.logaritmo(a, b)
                        print(f"Logaritmo de a: {log_a}, Logaritmo de b: {log_b}")
                    except ValueError as e:
                        print(f"Logaritmo: {e}")
                case '8':
                    print("Você escolheu: Raiz Quadrada")
                    a = float(input("Digite o primeiro número (a): "))
                    b = float(input("Digite o segundo número (b): "))
                    raiz_a, raiz_b = raiz.raiz(a, b)
                    print(f"Raiz de a: {raiz_a}, Raiz de b: {raiz_b}")
                case '9':
                    print("Você escolheu: Preço cambial do dólar")
                    print(cambio.cotacao_dolar())
                    continuar = input("Deseja realizar a conversão? (s/n): ").strip().lower(
                    )
                    if continuar == 's':
                        valor_real = float(input("Digite o valor em reais (R$): "))
                        valor_dolar = valor_real / float(cambio.cotacao_dolar())
                        print(f"Valor em dólares: ${valor_dolar:.2f}")
                    else:
                        print("Operação de conversão cancelada.")
                case _:
                    print("Opção inválida. Por favor, escolha uma operação válida.")
            opcao = input("\nDeseja realizar outra operação? (s/n): ").strip




    except ValueError:
         print("Erro: Por favor, digite apenas números válidos (use ponto para decimais).")

moedaentrada = { 1: 'libra', 2: 'dolar', 3: 'euro', 4: 'iene', 5: 'yuan', 6: 'real' }
moedasaida = { 1: 'libra', 2: 'dolar', 3: 'euro', 4: 'iene', 5: 'yuan', 6: 'real' }

#Taxas em relação ao dolar
taxas = {'dolar': 1.0,'libra': 0.79,'euro': 0.92,'iene': 147.50,'yuan': 7.10,'real': 5.40}

while True:
    print(moedaentrada)
    moeda1 = int(input('escolhe uma moeda da lista para converter: '))
    if moeda1 in moedaentrada:
        print(moedasaida)
        moeda2 = int(input('Agora escolha a moeda a qual deseja converter: '))
        if moeda2 in moedasaida:
            nome_entrada = moedaentrada[moeda1]
            nome_saida = moedasaida[moeda2]
            print(f'Você escolheu converter {nome_entrada} para {nome_saida}')
            valor = float(input(f'Digite o valor em {nome_entrada}: '))
            # entrada(base dollar) e a moeda de saída
            valor_em_dolar = valor / taxas[nome_entrada]
            valor_final = valor_em_dolar * taxas[nome_saida]

            print(f'{valor} {nome_entrada} = {valor_final:.2f} {nome_saida}')
            break
        else:
            print('Escolha uma moeda de saída válida!')
    else:
        print('Escolha uma moeda de entrada válida!')
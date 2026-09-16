#agenda
meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'} #lista de Meses do ano, atribuindo 1 numero a cada mes
dias = {1: range(1, 32), 2: range(1, 29), 3: range(1, 32), 4: range(1, 31), 5: range(1, 32), 6: range(1, 31), 7: range(1, 32), 8: range(1, 32), 9: range(1, 31), 10: range(1, 32), 11: range(1, 31), 12: range(1, 32)} #lista de dias para cada mês, ou seja, o 1 é janeiro, janeiro vai de 1 a 31, um range

while True:   #rodar o codigo até pedir sua parada
   mes = int(input('Digite o Mês de 1 à 12: ')) 
   if 1 <= mes <= 12: #vai rodar até o mês que a pessoa colocar for entre 1 e 12
      print(meses[mes]) #mostra o mês escolhido dentro dos meses
      print(f'Dias do mês {mes}: {list(dias[mes])}!') #printa quais dias tem no determinado mês da lista
      break #para o while e continua o codigo
   else:
      print('Escolha um Mês válido!') #caso a pessoa escolha fora do intervalo, retorna ao inicio do codigo até escolher um valido
while True: #rodar o codigo até pedir sua parada
   dia = int(input('Escolha um dia do Mês: ')) 
   if dia in dias[mes]: #verifica se o dia que a pessoa digitou esta na lista dias do mes escolhido
      print(f'Você escolheu o dia {dia} de {meses[mes]}!') #mostra ao usuario que ele escolheu um dia determinado mes nos meses
      break #para o while e continua o codigo
   else: 
      print('Escolha um dia válido para o mês selecionado!') #caso tenha escolhido um dia invalido(que não esta na lista de dias daquele determinado mes), a pessoa precisa escolher novamente
while True: #rodar o codigo até pedir sua parada
   certo = input('Prosseguir? ') #confirma os dados que a pessoa deu, ou seja ela falou o dia e o mês e pede pra confirmar
   if certo.lower() == 'sim' or certo.lower() == 's' or certo.lower() == 'ss': #função lower é o que faz com que as respostas possam ser digitadas de todas as formas, tipo, ela vai tratar uma resposta como uma unica coisa, ou seja, se for Sim, siM, SIM, vai tratar como apenas sim, sempre, isso facilita na hora das variações de resposta, por serem abertas
      print(f'Compromisso Marcado com sucesso, Você escolheu o dia {dia} de {meses[mes]}!') #então se estiver certo, afirma como marcado o compromisso, mostrando o dia e mes que a pessoa escolheu
      break #para o while e continua o codigo
   else:
        print('Certo vamos escolher um novo dia!') #se não estiver certo, ela volta e escolhe outro dia
        dia = int(input('Escolha um dia do Mês: ')) #aqui ela escolhe de fato outro dia
        
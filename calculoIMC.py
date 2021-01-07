# IMC 	Resultado
pesoXaltura = [[0, 18.5, 'Abaixo do peso'],[18.5, 24.9, 'Peso normal'],[25, 29.9, 'Sobrepeso'], [30, 34.9, 'Obesidade grau 1'], [35, 39.9, 'Obesidade grau 2'],[40, 0, 'Obesidade grau 3']]

def imc(peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  resultImc = meu_imc
  return resultImc

sNome = input('Qual é seu nome: ')
sAltura = input('Qual a sua altura: ')
sPeso = input('Qual seu peso: ')

calcPesoAltura = imc(float(sPeso), float(sAltura))

#print(f'teste {pesoXaltura[0][1]}')
#print(f'calculo de peso x altura: {calcPesoAltura:.2f}')

if calcPesoAltura <= float(pesoXaltura[0][1]):
  tabelaRecomendada = pesoXaltura[0][2]
elif calcPesoAltura > float(pesoXaltura[1][0]) and calcPesoAltura <= float(pesoXaltura[1][1]):
  tabelaRecomendada = pesoXaltura[1][2]
elif calcPesoAltura > float(pesoXaltura[2][0]) and calcPesoAltura <= float(pesoXaltura[2][1]):
  tabelaRecomendada = pesoXaltura[2][2]
elif calcPesoAltura > float(pesoXaltura[3][0]) and calcPesoAltura <= float(pesoXaltura[3][1]):
  tabelaRecomendada = pesoXaltura[3][2]
elif calcPesoAltura > float(pesoXaltura[4][0]) and calcPesoAltura <= float(pesoXaltura[4][1]):
  tabelaRecomendada = pesoXaltura[4][2]
elif calcPesoAltura > float(pesoXaltura[5][0]) and calcPesoAltura <= float(pesoXaltura[5][1]):
  tabelaRecomendada = pesoXaltura[5][2]

resposta = print(f'Olá {sNome}, seu peso é: {iPeso}, sua altua é: {iAltura}, seu IMC é: {calcPesoAltura:.2f} e você está: {tabelaRecomendada}')

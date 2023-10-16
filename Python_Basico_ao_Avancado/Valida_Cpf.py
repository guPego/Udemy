"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import os
import re

def validar_cpf(cpf):
  return bool(re.match(r'^\d{11}$', cpf))

while True: 
  cpf = input("Digite o CPF: ")
  cpfFiltrado = ''.join(filter(str.isdigit, cpf))
  
  if len(cpfFiltrado) != 11 or not validar_cpf(cpfFiltrado):
    os.system('cls')
    print("CPF inválido, favor digitar 11 números.")
    continue

  lista_de_digitos = list(cpfFiltrado);

  # ------- PRIMEIRO DIGITO -------

  somaDigitos = 0;
  multiplicadorPrimeiroDigito = 10;

  for i in range(9):
    digito = int(lista_de_digitos[i]);
    somaDigitos += digito * multiplicadorPrimeiroDigito;
    multiplicadorPrimeiroDigito -= 1;
  
  multiplicaSomaDigitos = somaDigitos * 10;
  restoDivisaoDaSomaMultiplicada = multiplicaSomaDigitos % 11;

  if restoDivisaoDaSomaMultiplicada > 9:
    primeiroDigito = restoDivisaoDaSomaMultiplicada = 0;
  else:
    primeiroDigito = restoDivisaoDaSomaMultiplicada;
  
  # ------- SEGUNDO DIGITO -------

  somaDigitos = 0;
  multiplicadorSegundoDigito = 11;

  for i in range(10):
    digito = int(lista_de_digitos[i]);
    somaDigitos += digito * multiplicadorSegundoDigito;
    multiplicadorSegundoDigito -= 1;

  multiplicaSomaDigitos = somaDigitos * 10;
  restoDivisaoDaSomaMultiplicada = multiplicaSomaDigitos % 11;

  if restoDivisaoDaSomaMultiplicada > 9:
    segundoDigito = restoDivisaoDaSomaMultiplicada = 0;
  else:
    segundoDigito = restoDivisaoDaSomaMultiplicada;

  cpf_calculado = ''.join(lista_de_digitos[0:9]) + str(primeiroDigito) + str(segundoDigito);
  
  if cpf_calculado == cpfFiltrado:
    os.system('cls');
    print(f'O primeiro dígito do CPF {cpf} é: {primeiroDigito}');
    print(f'O segundo dígito do CPF {cpf} é: {segundoDigito}');
    print(f'O cpf {cpf} é válido.' + "\n");
  else:
    os.system('cls');
    print(f'O primeiro dígito do CPF {cpf} é: {primeiroDigito}');
    print(f'O segundo dígito do CPF {cpf} é: {segundoDigito}');
    print(f'CPF {cpf} inválido.' + "\n");
    continue;
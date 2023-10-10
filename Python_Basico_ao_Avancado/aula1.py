frase = "Gustavo e Isadora pra sempre juntos."

i = 0;
while i < len(frase):
  letra_atual = frase[i];
  quantas_vezes_letra_apareceu = frase.count(letra_atual);

  print(letra_atual, quantas_vezes_letra_apareceu)
  i+=1;
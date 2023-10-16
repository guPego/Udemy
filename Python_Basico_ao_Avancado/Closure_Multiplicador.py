# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# 
# Exercicio com foco em Closures.

def multiplicador(multiplo):
  def multiplicacao(numero):
    return multiplo * numero;
  return multiplicacao;

resultado = multiplicador(32);

print(resultado(15));


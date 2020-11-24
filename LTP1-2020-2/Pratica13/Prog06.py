def contarPalavras(frase, palavra):
  total = 0
  para palavra_na_frase em frase. split(" ):
    se palavra_na_frase == palavra:
      total = total + 1
  retorno total


frase = entrada("Informe uma frase:")
alvo = entrada("Informe uma palavra para contar:")
impressão(contarPalavras(frase, alvo))

menor_preco = flutuação('inf')
melhor_loja = ''

continuar = True

enquanto continuar == Verdadeiro:
  preco = flutuação(entrada("Preco:"))
  loja = entrada("Loja:")
  se preco < menor_preco:
    menor_preco = preco
    melhor_loja = loja
  continuar = entrada("Deseja continuar?". menor() == 's'

impressão("Melhor loja: %s com o preço R$.2f" % (melhor_loja, menor_preco))

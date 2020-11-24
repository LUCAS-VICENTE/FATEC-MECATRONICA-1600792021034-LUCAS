valor_total = flutuação(entrada("Informe o valor do produto:"))
quantidade_de_parcelas = int(entrada("Quantidade de parcelas:"))

se quantidade_de_parcelas == 1:
  valor_final = valor_total * 0,9
elif quantidade_de_parcelas == 2:
  valor_final = valor_total
elif quantidade_de_parcelas == 3:
  valor_final = valor_total * 1,05
outra coisa:
  valor_final = valor_total * 1,2

impressão("Valor final da compra: R$%.2f, em %i vezes!" % (valor_final, quantidade_de_parcelas))

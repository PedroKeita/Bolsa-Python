import unittest


def verbing(s):
    threelastletters = s[-3:]
    if threelastletters == "ing":
        return s + "ly"
    elif s == "do":
        return s

    else:
        return s + "ing"



# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    #Definir a localização das substring na string dada:
    substring_not = s.find("not")
    substring_bad = s.find("bad")

    #Definir a condição onde se "bad" for maior, ou seja, tiver um valor maior na string em comparação a "not" realiza a seguinte ação dada:
    if substring_bad > substring_not:
        string_substituir = s[substring_not:(substring_bad + 3)]
        string_novinha = s.replace(string_substituir, "good")
        return string_novinha
    return s

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a aprte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
    af = a[:len(a) // 2 + len(a) % 2] #Pega a quantidade de letras da string divide por 2 para analisar se é par ou não
    ab = a[len(a) // 2 + len(a) % 2:] #Depois se soma com o resto para o caracter extra está na frente (front)
    bf = b[:len(b) // 2 + len(b) % 2] #Podemos analisar as partiçoes, onde o : fica antes no indice caso for front e depois caso for back
    bb = b[len(b) // 2 + len(b) % 2:]

    return af + bf + ab + bb




class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()
import unittest

# Dado um `count` como sendo o números de donuts, retornar uma string
# na forma "Número de donuts: <count>", caso `count` seja
# maior ou igual a 10 retornar "many".
def donuts(count):
    #definindo a condição
    if count >= 10:
        return "Number of donuts: many"
    else:
        return "Number of donuts: {}".format(count)


# Outra versão
def donutsV2(count):
    if count >= 10:
        print("Many")
    else:
        print("Número de donuts: {}".format(count))



# Dado uma string qualquer `s`, retonar uma string
# composta dos 2 primeiros e os 2 últimos caracteres, exemplo:
#
# panela ----> pala
# bala   ----> bala
# mao    ----> maao
# ja     ----> jaja
#
# Caso a string `s` contenha menos que 2 caracteres,
# retornar "" (string de cumprimento zero).
def both_ends(s):
    #definindo as variaveis para pegar as 2 primeira letra e duas ultimas e depois juntar para se ter a palavra nova
    duasprimeira_letra = s[:2]
    duasultima_letra = s[-2:]
    if len(s) < 2:
        return ""
    else:
        return duasprimeira_letra + duasultima_letra



# Dado uma string `s`, retornar uma string onde
# todas as ocorrências de seu primeiro caractere
# seja alterado para '*', exceto o primeiro caracter. Exemplo:
#
# babble ---> ba**le
#
# Presuma que o tamanho da string seja 1 ou mais.
# Dica: s.replace (strA, strB) retorna uma versão da string s
def fix_start(s):
    if len(s) >= 1:
        firstcaractere = s[0]
        # transformando todos os caracter equivalente ao primeiro até mesmo o proprio em *
        palavra_alterada = s.replace (firstcaractere, "*")
        palavra_alterada = palavra_alterada[1:] #aqui se retira o primeiro caractere da variavel para depois somar com a antes da alteração
        return firstcaractere + palavra_alterada


# Dado duas string `a` e `b`,  trocar os 2 primeiros caracteres entre as variáveis
# e retornar uma única string separada por espaço como no exemplo:
#
# "pezzy", "firm" ----> "fizzy perm"
def mix_up(a, b):
    palavra_a = b[0:2] + a[2:] #pega a palavra_a e faz a troca
    palavra_b = a[0:2] + b[2:]#pega palavra_b e faz a troca
    return "{}".format(palavra_a) + " " + "{}".format(palavra_b)


class MyTest(unittest.TestCase):

    def test_donuts(self):
      self.assertEqual(donuts(4), 'Number of donuts: 4')
      self.assertEqual(donuts(9), 'Number of donuts: 9')
      self.assertEqual(donuts(10), 'Number of donuts: many')
      self.assertEqual(donuts(99), 'Number of donuts: many')

    def test_both_ends(self):
      self.assertEqual(both_ends('spring'), 'spng')
      self.assertEqual(both_ends('Hello'), 'Helo')
      self.assertEqual(both_ends('a'), '')
      self.assertEqual(both_ends('xyz'), 'xyyz')
      self.assertEqual(both_ends('xy'), 'xyxy')

    def test_fix_start(self):
      self.assertEqual(both_ends('xy'), 'xyxy')
      self.assertEqual(fix_start('babble'), 'ba**le')
      self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
      self.assertEqual(fix_start('google'), 'goo*le')
      self.assertEqual(fix_start('donut'), 'donut')

    def test_mix_up(self):
      self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
      self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
      self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
      self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')



if __name__=="__main__":
    #Questão 1
    unittest.main()





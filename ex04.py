import unittest

# Dado um a lista de números, retorna uma lista onde
# todo elemento adjacente e repetido será deletado reduzindo a um único elemento.
# Então, [1, 2, 2, 3] retornará [1, 2, 3]
# Você pode criar uma nova lista ou modificar a lista atual.

def remove_adjacent(nums):

    if len(nums) == 0: #caso lista seja vazia, retornar ela mesma
        return nums
    else:
        lista_nova = [nums[0]]
        for num in range (1, len(nums)):
            if nums[num] == nums[num-1]: #identificar se o anterior desse valor é igual a ele
                pass
            else:
                lista_nova.append(nums[num]) #se não for igual adicionar a lista
    return lista_nova

# Dado duas listas ordenadas em ordem crescente, criar e retornar uma
# lista de todos os elementos em ordem algabética.
# Você pode modificar as listas passadas.
# Idealmente, a solução deve trabalhar em tempo "linear", que passa uma única vez em ambas as listas.

def linear_merge(list1, list2):
    
    list3 = list1 + list2 #Fazer uma lista com toda as string das duas listas
    lista_organizada = sorted(list3)  #Usar sorted para organizar em ordem alfabetica
    return lista_organizada

class MyTest(unittest.TestCase):
  def test_remove_adjacent(self):
    self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    # Repare que são excluídos apenas os valores repetidos e adjacentes
    self.assertEqual(remove_adjacent([1, 2, 3, 2, 3]), [1, 2, 3, 2, 3])
    self.assertEqual(remove_adjacent([]), [])

  def test_linear_merge(self):
    self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])

if __name__ == '__main__':
  unittest.main()
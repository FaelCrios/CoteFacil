from arvore import Arvore, No
import unittest

class TestArvore(unittest.TestCase):
    def setUp(self):
        raiz = No(1)
        filho1 = No(2)
        filho2 = No(3)
        filho3 = No(4)
        filho4 = No(5)
        filho5 = No(6)
        filho6 = No(7)
        filho7 = No(8)

    #fazendo a instanciacao de dados para teste, simulando uma situacao real
        raiz.adicionar_filhos(filho1)
        raiz.adicionar_filhos(filho2)
        filho1.adicionar_filhos(filho3)
        filho1.adicionar_filhos(filho4)
        filho3.adicionar_filhos(filho5)
        filho3.adicionar_filhos(filho6)
        filho3.adicionar_filhos(filho7)
        self.arvore = Arvore(raiz)

    #Neste teste montei a arvore para que tenha o seguinte formato
    #           1
    #         2   3
    #       4   5 
    #     6 7 8


    def test_passear_na_arvore_em_ordem(self):
        saida_esperada = [1, 2, 4, 6, 7, 8, 5, 3]
    # para o nosso modelo de testes precisamos definir qual será a saida esperada 
    # Nesse caso como estamos utilizando uma árvore genérica, ou seja, ela possui um numero indeterminado de filhos por nó
    # Optei por fazer uma busca em profundidade 
        saida_real = self.arvore.percorrer()
        self.assertEqual(saida_real, saida_esperada)


if __name__ == '__main__':
    unittest.main()

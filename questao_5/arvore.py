class No:   
#Esta classe é um no para no da arvore. 
#É nele que sera definido qual será o valor e quandos "filhos" que ele irá possuir, pois se trata e uma arvore genérica, então ela não possui limitação de filhos para um nó
    def __init__(self, valor):
        self.valor = valor
    
    #Os filhos se tratam das estruturas que estarão ligadas umas as outras
        self.filhos = []
    
    #função para definir a ligação entre os nós, definindo uma hierarquia entre eles
    def adicionar_filhos(self, filho):
        self.filhos.append(filho)

#Já esta classe é onde definimos qual será o no principal de onde todos irão descender, 
#E também é definido aqui os métodos que irão estar presentes para nossa árvore, neste caso uma busca em profundidade
class Arvore: 
    def __init__(self, raiz):
        self.raiz = raiz

    def percorrer(self, no=None):
            if no is None:
                no = self.raiz
            resultado = [no.valor]
            for filho in no.filhos:
                resultado.extend(self.percorrer(filho))
            return resultado
        


# # Na prática, a classe Node só precisa de:
# # Um __init__ que recebe o 'value'
# # self.data = value
# # self.next = None (porque ele nasce solto)

# class Node:
#     def __init__(self, value):
#         self.data = value # atribui o valor ao nó
#         self.next = None # o ponteiro que começa apontando para o vazio

# class LinkedList:
#     def __init__(self):
#         self.head = None  # A lista começa vazia, então a cabeça é None

#     def is_empty(self):
#         # Se o self.head for None, a lista está vazia. 
#         # Retorne True ou False baseado nisso.
#         return self.head is None

#     def insert_beginning(self, value):
#         # 1. Cria um novo nó com o valor
#         new_node = Node(value)
#         # 2. O 'next' do novo nó aponta para onde a cabeça apontava
#         new_node.next = self.head
#         # 3. A cabeça agora passa a ser o novo nó
#         self.head = new_node

#     def print_list(self):
#         # Começamos pela cabeça
#         current = self.head
#         # Enquanto o nó atual não for None, a gente imprime e pula pro próximo
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")


# --- DEFINIÇÃO (Onde você escreve a lógica) ---

# from platform import node
# from typing import Self


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     # Aqui você coloca todos os métodos que discutimos:
#     # insert_beginning, insert_end, remove, etc.
#     def insert_beginning(self, value):
#         novo_no = Node(value)
#         novo_no.next = self.head
#         self.head = novo_no

#     def print_list(self):
#         atual = self.head
#         while atual:
#             print(atual.data, end=" -> ")
#             atual = atual.next
#         print("None")

# # --- EXECUÇÃO (Onde a mágica acontece) ---

# if __name__ == "__main__":
#     # 1. Instanciar (Criar o objeto da lista)
#     minha_lista = LinkedList()

#     # 2. Chamar os métodos
#     print("Inserindo elementos...")
#     minha_lista.insert_beginning(10)
#     minha_lista.insert_beginning(20)
#     minha_lista.insert_beginning(30)

#     # 3. Ver o resultado
#     print("Estado atual da lista:")
#     minha_lista.print_list()

#============================== ATIVIDADE ============================#
from platform import node
from typing import Self

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None


    # INSERE NO INICIO
    def insert_beginning(self, value):
        novo_no = Node(value)
        novo_no.next = self.head
        self.head = novo_no
    

    # INSERE NO FINAL
    def insert_end(self, value):
        novo_no = Node(value)

        #verifica se esta vazia
        if self.head is None:
            self.head = novo_no
            return
        #se tiver vazia ele vai até o ultimo para char o valor dele
        atual = self.head
        while atual.next:
            atual = atual.next

        # Quando o while termina, o 'atual' é o último nó da lista
        #faz esse ultimo apontar pro novo que vc criou
        atual.next = novo_no


    #REMOVE
    def remove(self, value):
        
        if self.head is None:
            return
        
        # Caso especial: remover o primeiro nó
        if self.head.data == value:
            self.head = self.head.next
            return
        
        # Procurando no restante da lista
        atual = self.head
        anterior = None

        while atual and atual.data != value:
            anterior = atual
            atual = atual.next
        #Exemplo: 
#       Se você quer remover o 30 na lista 10 -> 20 -> 30 -> 40:
#        Rodada 1: atual é 10. Não é 30? Então anterior vira 10 e atual vira 20.
#        Rodada 2: atual é 20. Não é 30? Então anterior vira 20 e atual vira 30.
#        Rodada 3: atual é 30. Opa! A condição atual.data != value agora é falsa. O while para na hora!

        # Se saiu do loop e o atual não é None, significa que achamos!
        if atual:
            anterior.next = atual.next
#         Imagine que temos a lista: 10 -> 20 -> 30 -> 40 e queremos remover o 30.
#          O anterior vai parar no 20.
#          O atual vai parar no 30.
#          O atual.next é o 40.


    #BUSCA AI
    def search(self, value):
        atual = self.head

        while atual:
            if atual.data == value:
                return True
            # Se não achou ainda, pula para o próximo nó
            atual = atual.next
            
        #Se n tem
        return False



    #TAMANHO
    def size(self):
        contador = 0
        atual = self.head

        while atual:
            contador += 1 
            atual = atual.next
            
        return contador



    #IMPRIMI
    def print_list(self):
        atual = self.head

        while atual:
            print(atual.data, end=" -> ")
            atual = atual.next
        print("None")


#-------EXECUÇÃO------

if __name__ =="__main__": #não mostra oq ta dentro do if

    minha_lista = Linkedlist()

    print("Inserindo elemento...")
    minha_lista.insert_beginning(15)
    minha_lista.insert_beginning(14)
    minha_lista.insert_beginning(13)
    minha_lista.insert_beginning(12)

    #insere final
    minha_lista.insert_end(16)  
    minha_lista.insert_end(17)  
    minha_lista.insert_end(18)  

    #remove
    minha_lista.remove(16)
    minha_lista.remove(12)
    minha_lista.remove(18)

    #Procura
    print(f"elemento Procurado 14:{minha_lista.search(14)}")
    print(f"elemento Procurado 14:{minha_lista.search(16)}")
    print(f"elemento Procurado 14:{minha_lista.search(13)}")

    #Tamanho
    print(f"O tamanho: {minha_lista.size()}")
    


    print("Estado atual da lista:")
    minha_lista.print_list()
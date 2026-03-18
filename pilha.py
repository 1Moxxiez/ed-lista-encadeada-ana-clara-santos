# ADICIONAR TAIL
from inspect import stack
from platform import node
from typing import Self



# def inverter (palavra):
#         pilha = []

#         #empilha td
#         for letra in palavra:
#             pilha.append(letra)
#             # A
#             # L
#             # G
#             # O
#             # R
#             # I
#             # T
#             # M
#             # O
#         palavra_invertida = ""

#         #desempilha
#         while len(pilha) > 0:
#             palavra_invertida += pilha.pop()
#             # O
#             # M
#             # T
#             # I
#             # R
#             # O
#             # G
#             # L
#             # A
        
#         return palavra_invertida

# #-------EXECUÇÃO------

# print(inverter("ALGORITMO"))



# def parenteses(item):
#     pilha = []

#     for letras in item:
#         if letras == "(":
#             pilha.append("(")

#         elif letras == ")":
#             if len(pilha) == 0:
#                 return "invalido" #fechou sem abrir parenteses
#             pilha.pop()
    
#     # se a pilha estiver vazia ta certo. se sobrou alguem perdido dentro dela n
#     return "Valido" if len(pilha) == 0 else "invalido"


# def parenteses2(item2):
#     pilha = []

#     for letra in item2:
#         if letra == "(":
#             pilha.append
        
#         if letra == ")":
#             if len() #n faz sentido tentar colocar os dois de uma vez dentro
#                         #pq a existencia de um depende do outro
#             pilha.append





#-------EXECUÇÃO------

# valores = ["((A+B) * C)","(A+B))","((A+B)"]

# for v in valores:
#     print(parenteses(v))


class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None


class Stack: #o ponteiro topo aponta sempre para o último que entrou.
    def __init__(self):
        self.topo = None
        self._size = 0

    #Empilhar
    def push(self, data):
        new_node = Node(data)       
        new_node.next = self.topo   
        self.topo = new_node        
        self._size = self._size + 1

    #Desempilhar
    def pop(self):
        if self.topo is None:
            return None
        removed = self.topo
        self.topo = self.topo.next
        self._size = self._size - 1
        return removed.data

    def peek(self):
        if self.topo is None:
            return None
        return self.topo.data
    
    def __len__(self):
        return self._size

def contrario(palavra):
        s = Stack()

        for letra in palavra:
            s.push(letra)

        final = ""
        while len(s) > 0:
            remove = s.pop()
            final += remove

        return final

def parenteses(palavra):
    s = Stack ()

    for letra in palavra:
        if letra == "(":
            s.push(letra)

        elif letra == ")":
            if len(s) == 0:
                return "invalido"
            s.pop()
    
    return "Valido" if len(s) == 0 else "Invalido"

#-------EXECUÇÃO------

palavra = "ALGORITMO"
resultado = contrario(palavra)

print (resultado)

valores = ["((A+B) * C)","(A+B))","((A+B)"]

for v in valores:
    print (parenteses(v))








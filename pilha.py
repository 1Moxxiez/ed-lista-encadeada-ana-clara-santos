def inverter (palavra):
    pilha = []

    #empilha td
    for letra in palavra:
        pilha.append(letra)
    
    palavra_invertida = ""

    #desempilha
    while len(pilha) > 0:
        palavra_invertida += pilha.pop()
    
    return palavra_invertida

#-------EXECUÇÃO------

print(inverter("ALGORITMO"))



def parenteses(item):
    pilha = []

    for letras in item:
        if letras == "(":
            pilha.append("(")

        elif letras == ")":
            if len(pilha) == 0:
                return "invalido" #fechou sem abrir parenteses
            pilha.pop()
    
    # se a pilha estiver vazia ta certo. se sobrou alguem perdido dentro dela n
    return "Valido" if len(pilha) == 0 else "invalido"


#-------EXECUÇÃO------

valores = ["((A+B) * C)","(A+B))","((A+B)"]

for v in valores:
    print(parenteses(v))
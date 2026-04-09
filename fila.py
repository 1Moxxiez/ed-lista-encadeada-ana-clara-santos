class Node:
    def __init__(self, data=None):
        self.data = data            # armazena o dado
        self.next = None            # referência para o próximo nó  

class Queue:
    def __init__(self):
        self.head = None            # indica a posição para remoção (início da fila);
        self.tail = None            # indica a posição para inserção (final da fila);
        self._size = 0              # armazena o número atual de elementos na fila.

    # Insere um elemento na fila
    def enqueue(self, elem):
        node = Node(elem)
        if self.tail is None:           # Fila vazia
            self.tail = node            # Último nó da lista aponta para o novo nó 
            self.head = node            # Primeiro nó da lista aponta para o novo nó             
        else:
            self.tail.next = node       # Último elemento aponta para o novo nó
            self.tail = node            # Novo nó passa a ser o último elemento da fila
        self._size = self._size + 1

    # Remove um elemento do ínicio da fila
    def dequeue(self):
        if self._size > 0:
            elem  = self.head.data
            self.head = self.head.next
            self._size = self._size - 1

            #fila ficou vazia
            if self.head is None:
                self.tail = None

            return elem
        raise IndexError("The queue is empty")

    # retorna o início da fila
    def front(self):
        if self._size > 0:
            elem = self.head.data
            return elem
        raise IndexError("The queue is empty")

    # retorna o tamanho da fila
    def __len__(self):
        return self._size
    
    # retorna itens da fila
    def show(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next



class Processo:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo

def rodar_escalonador(fila, quantum):
    print(f"Tempo máximo por vez: {quantum}s")

    while len(fila) > 0:
        # 1. SAI DA FILA para ser atendido
        p = fila.dequeue()
        print(f" SAIU DA FILA  --> {p.nome} Faltam {p.tempo}s")

        # 2. TRABALHA (diminui o tempo)
        tempo_gasto = min(p.tempo, quantum)
        p.tempo -= tempo_gasto
        
        # 3. DECISÃO
        if p.tempo > 0:
            print(f"       {p.nome} ainda tem {p.tempo}s VOLTANDO para o fim da fil")
            fila.enqueue(p) # RE-ENTRA NO FUNDO
        else:
            print(f"       {p.nome} FINALIZADO e removido")
        
        print("-" * 40)

# --- TESTE ---
fila = Queue()
fila.enqueue(Processo("Processo_A", 5))
fila.enqueue(Processo("Processo_B", 5))

rodar_escalonador(fila, quantum=4)
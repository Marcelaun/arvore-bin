from pilha import Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class ArvoreBinaria:
    def __init__(self):
        self.root = None


    def inserir(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node

        else:
            node = self.root
            while node is not None:
                if data <= node.data:
                    if node.left is None:
                        node.left = new_node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        break
                    node = node.right

    def inserir_recursivo(self, data):
        self.root = self.inserir_aux(data, self.root)

    def inserir_aux(self, data, node):
        if node == None:
            return Node(data)
        elif data < node.data:
            node.left = self.inserir_aux(data, node.left)
        else:
            node.right = self.inserir_aux(data, node.right)

        return node

    def imprimirEmOrdem(self):
        self.imprimirEmOrdem_Aux(self.root)

    def imprimirEmOrdem_Aux(self, node):
        if node is None:
            return
        self.imprimirEmOrdem_Aux(node.left)
        print(node.data)
        self.imprimirEmOrdem_Aux(node.right)

    def contar_nos(self):
        return self.contar_nos_aux(self.root)

    def contar_nos_aux(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.contar_nos_aux(node.left) + self.contar_nos_aux(node.right)

    def contar_folhas(self):
        return self.contar_folhas_aux(self.root, 0)

    def contar_folhas_aux(self, node, current_node_count):

        if node is None:
            return 0

        if (node.left and node.right) is None:
            current_count = current_node_count + 1


            self.contar_folhas_aux(node.left, current_count)
            self.contar_folhas_aux(node.right, current_node_count)





    def imprimir_normalmente(self):
        pilha = Stack()
        pilha.push(self.root)

        while pilha.empty() is not True:
            no = pilha.pop()
            if no is not None:
                print(no.data)
                pilha.push(no.right)
                pilha.push(no.left)

    def nos_folhas(self):
        pilha = Stack()
        pilha.push(self.root)
        count_folhas = 0

        while pilha.empty() is not True:
            no = pilha.pop()
            if no is None:
                return
            if (no.right and no.left) is None:
                print('entrou aq')
                count_folhas = count_folhas + 1

            pilha.push(no.right)
            pilha.push(no.left)


        return count_folhas




    def busca_menor_valor(self):
        return self.menor_aux(self.root)

    def menor_aux(self, node):
        if node.left is None:
            return node
        return self.menor_aux(node.left)

    def busca_maior_valor(self):
        return self.maior_aux(self.root)

    def maior_aux(self, node):
        if node.right is None:
            return node
        return self.maior_aux(node.right)

    def busca_valor(self, value):
        return self.busca_valor_aux(value, self.root)

    def busca_valor_aux(self, value, node):
        if node is None:
            return
        elif value == node.data:
            return node.data
        elif value > node.data:
            print('dado atual quando maior', node.data)
            print('valor direita node atual', node.right.data)
            return self.busca_valor_aux(value, node.right)
        else:
            print('dado atual quando menor', node.data)
            print('valor esquerda node atual', node.left.data)
            return self.busca_valor_aux(value, node.left)


    def remover(self, value):
       return self.remover_aux(value, self.root)

    def remover_aux(self, value, node):
        if node is None:
            return

        elif value == node.data:
            pass

        elif value < node.data:
            node.left = self.remover_aux(value, node.left)
        elif value > node.data:
            node.right = self.remover_aux(value, node.right)

        else:
            if node.left is None:
                return node.right
            elif node.direita:
                pass









arvore = ArvoreBinaria()

arvore.inserir(7)
arvore.inserir(8)
arvore.inserir(5)
arvore.inserir(1)
arvore.inserir(6)
arvore.imprimirEmOrdem()
print(arvore.busca_maior_valor().data)
print(arvore.busca_menor_valor().data)
print(arvore.busca_valor(6))
print(arvore.contar_nos())
arvore.imprimir_normalmente()
print(arvore.nos_folhas())

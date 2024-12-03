class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None


    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)

    def insert_recursive(self, node, data):

        # if node is None:
        #     return node(data)

        if data < node.data:
            if node.left is None:
                node.left = Node(data)

            else:
                self.insert_recursive(node.left, data)
        
        else:
            if node.right is None:  
                node.right = Node(data)

            else:
                self.insert_recursive(node.right, data)


    def search(self, data):

        return self.search_recursive(self.root, data)
    
    def search_recursive(self, node, data):

        if node is None:
            return False
        
        if node.data == data:
            return True
        
        elif data < node.data:
            return self.search_recursive(node.left, data)
        
        else:
            return self.search_recursive(node.right, data)
        
        
    def print_tree(self, node, space: int = 0):

        if node is not None:

            self.print_tree(node.right, space + 10)

            print(' ' * space + str(node.data))

            self.print_tree(node.left, space + 10)

    def count_nodes(self, node):
        if node is None:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def count_leaves(self, node):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        return self.count_leaves(node.left) + self.count_leaves(node.right)

        

bt = BinaryTree()

num_nodes = int(input('Número de nós para inserir: '))

for i in range(num_nodes):
    data = int(input('Valor para ser inserido: '))
    bt.insert(data)


print('Árvore em ordem:')
bt.print_tree(bt.root)


num_search = int(input('Qual número você quer buscar? '))
if bt.search(num_search):
    print(f'O número {num_search} foi encontrado.')
else:
    print(f'O número {num_search} não foi encontrado.')
    

total_nodes = bt.count_nodes(bt.root)
total_leaves = bt.count_leaves(bt.root)

print(f'Total de nós: {total_nodes}.')
print(f'Total de folhas: {total_leaves}.')


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def add_Next(self, node):
        self.next = node
    
    # def count_Nodes(self, linkedlist):
    #     if self.next != None:

class linkedlist:
    def __init__(self,node):
        self.node = node

    def count_Nodes(self, node):
        count = 1
        if node.next == None:
            return 1
        else:
            count += self.count_Nodes(node.next)
            return count

if __name__ == "__main__":
    head = Node(3)
    node1 = Node(4)
    node2 = Node(5)
    head.add_Next(node1)
    node1.add_Next(node2)
    ll = linkedlist(head)
    print(ll.count_Nodes(head))

        
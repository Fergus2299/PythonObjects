# a class for a linked list

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        '''
        we create a node which contains the data variable as our list data
        the next node after this is the original ll head
        '''
        node = Node(data, self.head)
        self.head = node
    def add_at_end(self, data):
        # if empty
        if not self.head:
            self.head = Node(data, None)
            return
        # if not empty
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    def add_at_index(self, ind, data):
        '''
        we assume for now that it's a valid index of the list
        '''
        if ind == 0:
            self.add_at_beginning(data)
            return
        itr = self.head
        while ind != 1:
            itr = itr.next
            ind -= 1
        itr.next = Node(data, itr.next)
    def print(self):
        if self.head == None:
            print('linked list is empty')
            return
        itr = self.head
        liststr = ''
        while itr:
            liststr += str(itr.data) + '-->'
            itr = itr.next
        print(liststr)
if __name__ == '__main__':

    # example list:

    #ll = LinkedList()
    #ll.add_at_beginning(1)
    #ll.add_at_beginning(2)
    #ll.add_at_beginning(3)
    #ll.add_at_end(5)
    #ll.add_at_end(5)
    #ll.add_at_index(0, 10)
    #ll.print()

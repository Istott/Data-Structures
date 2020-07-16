"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value}"
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    

    def __str__(self):
        text = "\n==============>\n"
        text += f"= HEAD: {self.head}\n"
        text += f"= TAIL: {self.tail}\n"
        text += f"= LIST-->\n"
        current = self.head
        while current is not None:
            text += f"= {current.value}\n"
            current = current.next
        return text

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        newNode = ListNode(value)
        if self.length == 0:
            self.__init__(newNode)
        else:
            newNode.prev = None   
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.length += 1
      
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return

        if not self.head.next:
            node = self.head 

            self.head = None

            self.tail = None 
            self.length -= 1
            return node.value
        elif self.head and self.tail:
            node = self.head

            self.head = node.next
            self.head.prev = None
            self.length -= 1
            return node.value
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newNode = ListNode(value)

        if self.head is None and self.tail is None: 
            self.head = newNode 
            self.tail = newNode
            self.length += 1
        else:
            newNode.prev = self.tail
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode

            self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return

        if not self.head.next:
            node = self.tail 

            self.head = None

            self.tail = None 
            self.length -= 1
            return node.value
        elif self.head and self.tail:
            node = self.tail

            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
            return node.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        elif node is self.head:
            return self.remove_from_head()
        # elif node is self.tail:
        #     return self.remove_from_tail()
        else:
            current = self.head
            while current:
                if node.value == current.value:
                    break
                current = current.next
                
            if not current:
                return

            if current == self.tail:
                return self.remove_from_tail()
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        
        current = self.head
        maxValue = self.head.value

        while current:
            if current.value > maxValue:
                maxValue = current.value
            current = current.next

        return maxValue

        



x = DoublyLinkedList(ListNode(5))
print(x)
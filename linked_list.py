class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head) # adding to the linked list

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next  # remove the item by moving the head pointer
            return item

    def count(self):
        pointer = self.head
        count = 0
        while pointer != None:
            count += 1
            pointer = pointer.next
        return count

    def contains(self, target):

        pointer = self.head

        while pointer and pointer.item != target:
            pointer = pointer.next
        return pointer

    def after(self, target):
        pointer = self.head
        if pointer != None:
            while pointer.next != None:
                if pointer.item == target:
                    return pointer.next.item
                pointer = pointer.next
        return None

    def before(self,target):
        previouspointer = None
        currentpointer = self.head
        if currentpointer != None:
            while currentpointer.next != None:
                previouspointer = currentpointer
                currentpointer = currentpointer.next
                if currentpointer.item == target:
                    return previouspointer.item

        return None




    def is_empty(self) :
        return self.head == None

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next

        return tmp_str


    def append(self,item):
        ptr = self.head
        if self.head is None:
            self.head = Node(item,None)
        else:
            #ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next


            ptr.next = Node(item,None)

    def rotate(self):
        #ptr =self.head

        a = self.remove()
        self.append(a)

       


def detect_loop(lst):
    ptr = nextptr = lst.head

    while ptr and nextptr and nextptr.next:

        ptr = ptr.next
        nextptr = nextptr.next.next
        if ptr == nextptr:
            return True
    return False



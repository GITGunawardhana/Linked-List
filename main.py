class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    # Add new node to the end of Linked List.
    def append(self, data):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = Node(data)

    # Print the Linked List.
    def display(self):
        arr = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            arr.append(cur_node.data)
        print(arr)

    # Return the integer value which length of the Linked List.
    def length(self):
        cur_node = self.head
        count = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            count+=1
        return count

    # Return the value of the node.data which according to the index.
    def getData(self, index):
        if index > self.length()-1 or index < 0:
            return "IndexError: index is out of range"
        cur_node = self.head
        temp_index = 0
        while True:
            cur_node = cur_node.next
            if temp_index == index:
                return cur_node.data
            temp_index+=1

    # Check the passing value("data") whether it is in the Linked List.
    # If it is in here, return (True, index of the "data").
    # Otherwise, return False.
    def checkData(self, data):
        cur_node = self.head
        temp_index = -1
        while True:
            temp_index += 1
            cur_node = cur_node.next
            try:
                if cur_node.data == data:
                    return True, temp_index
            except:
                return False

    # Delete the node.data using index of data which what you want to delete.
    def deleteWithIndex(self, index):
        if index > self.length()-1 or index < 0:
            print("IndexError: index is out of range")
            return ""
        cur_node = self.head
        temp_index = 0
        while True:
            befor_cur_node = cur_node
            cur_node = cur_node.next
            if temp_index == index:
                befor_cur_node.next = cur_node.next
                return
            temp_index+=1
    # Delete the node.data using value of the data(passing value) which what you want to delete.
    # Additionally, at the same time, this return the index of data.
    def deleteWithData(self, data):
        cur_node = self.head
        temp_index = -1
        while True:
            temp_index += 1
            befor_cur_node = cur_node
            cur_node = cur_node.next
            try:
                if cur_node.data == data:
                    befor_cur_node.next = cur_node.next
                    return temp_index
            except:
                return f"{data} is not in the Linked List"

# Create object from LinkedList and return it.
# If not passed the array into this function, program exit.
def createLinkedList(list_ = None):
    if list_ != None:
        linked_list = LinkedList()
        for val in list_:
            linked_list.append(val)
        return linked_list
    exit()

# if __name__ == "__main__":
#     list_ = [10, 1, 4, 15, 30, 1]
#     linked_list = createLinkedList(list_)
#
#     print("Linked List: ", end=""); linked_list.display()
#     print("\nLenght of Linked List: ", linked_list.length())
#     print("Is there 25 in the Linked List? : ",linked_list.checkData(25))
#     print("Is there 4 in the Linked List? : ", linked_list.checkData(4))
#     print("The value of index 2: ", linked_list.getData(2))
#
#     print("\nRemove the element using \"deleteWithIndex\" function...")
#     print("Before that delete value of index 1: ", end=""); linked_list.display()
#     linked_list.deleteWithIndex(1)
#     print("After that delete value of index 1: ", end=""); linked_list.display()
#
#     print("\nRemove the element using \"deleteWithData\" function...")
#     print("Before that delete 4: ", end=""); linked_list.display()
#     print("Index of value 4: ", linked_list.deleteWithData(4))
#     print("After that delete 4: ", end=""); linked_list.display()



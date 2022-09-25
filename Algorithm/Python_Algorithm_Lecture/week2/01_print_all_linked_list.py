class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
node = Node(3) # 현재는 next 가 없이 하나의 노드만 있습니다. [3]
first_node = Node(4)
node.next = first_node
print(node.next.data)
print(node.data)
print("------------------\n")

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.
        print("무조건 오나?")

    def append(self, value):    # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        print("append 시작 value : ", value)
        if self.head is None:   # 예외처리 처음에 head가 None이면 안되니까?
            print("여긴없지")
            self.head = Node(value)
            return

        cur = self.head # self.head는 계속 최초 생성한 LinkedList를 가리킨다 (여기선 7)
        print("cur.data : ",cur.data, ", self.heaf : ", self.head)

        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다.
            cur = cur.next
            print("cur is : ", cur.data)
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)
linked_list.append(11)
#
linked_list.print_all()

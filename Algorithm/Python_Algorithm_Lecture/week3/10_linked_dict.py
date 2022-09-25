class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items) # 지금 self.items 에는 LinkedTuple 이 들어있다.
        self.items[index].add(key, value)   # key, value가 들어간 LinkedList 가 된다.

    def get(self, key):
        index = hash(key) % len(self.items)
        # self.items[index] 에 있는게 LinkedTuple 이다.
        return self.items[index].get(key)


# 참고로 hash 함수는 python에 있는 딕셔너리(dictionary)와 동일하다
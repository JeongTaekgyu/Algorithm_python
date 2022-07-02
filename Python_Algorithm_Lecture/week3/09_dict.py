
class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        # hash 함수를 사용해서 임의의 값을 구하고 배열의 길이만큼을 나눈 나머지를 구한다.
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
class Person:
    def __init__(self, param_name): # 파이썬에서 생성자 함수의 이름은 __init__ 으로 고정되어 있습니다!
        print("hihihi", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다")



person_1 = Person("김철수")
print("person_1.name = ",person_1.name)
print(person_1)  # <__main__.Person object at 0x1090c76d0> 이런식
person_1.talk()

print("\n---------------------\n")

person_2 = Person("최승훈")
print(person_2.name)
print(person_2)  # <__main__.Person object at 0x1034354f0> 이런식
person_2.talk()
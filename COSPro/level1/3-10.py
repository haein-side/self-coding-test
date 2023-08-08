class Customer:
    def __init__(self, id, time, num_of_people):
        self.id = id
        self.time = time
        self.num_of_people = num_of_people

class Shop:
    def __init__(self): # 자식 클래스(HairShop, Restaurant)에도 초기화되는 객체 필드
        self.reserve_list = []

    def reserve(self, customer): # self가 인자로 들어가기 때문에 객체별로 생성되어야 하는 메소드 (객체별로 reserve_list 다름)
        self.reserve_list.append(customer)
        return True

class Restaurant(Shop):
    def __init__(self): # Restaurant 클래스의 인스턴스 생성 시 자동으로 상속되지만 명시함
        super().__init__()

    def reserve(self, customer):
        if customer.num_of_people >= 2 and customer.num_of_people <= 8:
            count = 0
            for i in self.reserve_list:
                if i.time == customer.time:
                    count += 1
            if count <= 1:
                super().reserve(customer)
                return True
        return False

class HairShop(Shop):
    def __init__(self):
        super().__init__()

    def reserve(self, customer):
        if customer.num_of_people == 1:
            for i in self.reserve_list:
                if i.time == customer.time:
                    return False
            else:
                super().reserve(customer)
                return True
        return False


def solution(customers, shops):
    hairshop = HairShop()
    restaurant = Restaurant()

    count = 0
    for customer, shop in zip(customers, shops):
        if shop == "hairshop":
            if hairshop.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
        elif shop == "restaurant":
            if restaurant.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1

    return count


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
customers = [[1000, 2, 1], [2000, 2, 4], [1234, 5, 1], [4321, 2, 1], [1111, 3, 10]]
shops = ["hairshop", "restaurant", "hairshop", "hairshop", "restaurant"]
ret = solution(customers, shops)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
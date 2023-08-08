from abc import *

class Book(metaclass=ABCMeta):
    @abstractmethod
    def get_rental_price(self, day):
        pass

class ComicBook(Book):
    def get_rental_price(self, day):
        if day <= 2:
            result = 500
        else:
            result = 500 + (day - 2) * 200
        return result

class Novel(Book):
    def get_rental_price(self, day):
        if day <= 3:
            result = 1000
        else:
            result = 1000 + (day - 3) * 300
        return result

def solution(book_types, day):
    total = 0
    for i in book_types:
        if i == "comic":
            total += ComicBook().get_rental_price(day)
        else:
            total += Novel().get_rental_price(day)
    return total

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
book_types = ["comic", "comic", "novel"]
day = 4
ret = solution(book_types, day)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
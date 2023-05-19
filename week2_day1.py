#classについて
#データ型ではint,floatなどで数量や計測値を表せます。
#boolでyesかnoを表せます。
#stringでテキストを表せます。
#listで様々なデータのコレクションを表せます。
#dictionaryでデータをすぐに探せるような形のデータコレクションです。
#そこでclassが出てきます。
#なぜこのclassを使うのか？
#現実にある様々なものについてモデル化したいときに使います。
#特定の者に関するデータと機能をオブジェクトというかたまりにまとめることができます。


# __init__ という関数が必要になります。ダンダーメソッドまたはダブルアンダーラインメソッド。
#クラスがインスタンス化されるときに呼びます。


"""
class bodybuilder:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.weight = weight
        self.height = height 
        
    def bmi(self):
        return self.weight / (self.height_meters() ** 2)
    
    def height_meters(self):
        return self.height /100
"""


# print("練習1")
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def say_hello(self):
#         print(f"Hello, I am {self.name}")
        
# person1 = Person("Naomi", 25)
# person2 = Person("Gary", 30)

# person1.say_hello()

# print("練習2")
# class MenuItem():
#     def __init__(self, name, price, allergens):
#         self.name = name
#         self.price = price
#         self.allergens = allergens
    
#     def show_item(self):
#         print(self.name + " costs " + str(self.price) + " yen and has "
#               +str(len(self.allergens)) + " allergens.")

# grilled_cheese = MenuItem("Grilled Cheese", 400, ["wheat", "dairy"])
# grilled_cheese.show_item()


print("練習3")

class FlightInfos():
    def __init__(self,airport,flight, airline, departure_time, arrival_time, gate):
        self.airport = airport
        self.flight = flight
        self.airline = airline
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate = gate
        
        



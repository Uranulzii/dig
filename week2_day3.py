"""
onlyという名前の関数を宣言してください。
この関数は引数としてリストと文字列で型名を受け取ります。
リストの中から引数である型名のデータ型を持つ要素のみのリストを返します。
"""

# データ型の取り出し方法は以下を参考にしてください
# data = "hello"
# print(type(data).__name__) #左記は"str"となります
# print(type(data)) 

# def only(list, data):
#     list1 = []
#     for i in list:
#         if type(i).__name__ == data:
#             list1.append(i)
#     return list1
            
    

        # print(i)
        # print(data)
        # print(type(i).__name__)
        # if type(list[i][0]).__name__ == data:
        #     list1 += list[i]
        #     return list1
            
            
#この下にコードを書いてください

# print(only([1, 2, 3, 4, 5], "int")) # [1, 2, 3, 4, 5]
# print(only([0, 4, 36], "bool")) # []
# print(only([True, "a", 1, 2, False], "str")) # ["a"]

"""
build_object という名前の関数を宣言してください。
この関数は引数として 2 つのリストを受け取り、新しいディクショナリを返します。
返されるディクショナリは、第一引数のリストの要素をディクショナリのキーとして設定し、
第二引数のリストの要素をディクショナリの値として設定します。
"""

#この下にコードを書いてください

# def build_object(list1, list2):
#     dic1 = {}
#     for key, value in list2.items():
#         list1[key] +=  value
#     return list1

def build_object(list1, list2):
    dic1 = {}
    for i in range(len(list1)):
        dic1[list1[i]] = list2[i]
    return dic1


# def build_object(list1, list2):
#     dic1 = {}
#     i = 0
#     while i < len(list1):
#         dic1[list1[i]] = list2[i]
#         i += 1
#     return dic1
        
         
    

print(build_object(["a", "b", "c"], [1, 2, 3])) # {"a": 1, "b": 2, "c": 3}
print(build_object(["cat", "dog", "duck"], ["meow", "woof", "quack"])) # {"cat": "meow", "dog": "woof", "duck": "quack"}
print(build_object(["cat", "dog", "duck"], [None, 0, None])) # {"cat": None, "dog": 0, "duck": None}
print(build_object(["abc", "def", "ghi"], [[0, 1, 2], [3, 4, 5], [6, 7, 8]])) # {"abc": [0, 1, 2], "def": [3, 4, 5], "ghi": [6, 7, 8]}
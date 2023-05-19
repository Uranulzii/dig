# 問題 1
# 人の名前を引数にとり、以下のような挨拶を表示する greet という関数を作成してください。
# def greet(name):
#     print("Hi, " + name + "!")
#    #ここにコードを書いてください

# greet("Judi")  # "Hi, Judi!"


# 問題 2
# 人の名前を引数にとり、以下のようなメッセージを表示する get_first_alphabet という関数を作成してください。
# def get_first_alphabet(name):
#     print("My name starts with " + name[0].lower() + ".")
#    #ここにコードを書いてください

# get_first_alphabet("Jean") # "My name starts with j."


# # 問題 3
# # add という名前の関数を宣言しましょう。 ２つの数値型のデータを引数に取り、それらの合計を出力します。
# def add(number_1,number_2):
#     return number_1 + number_2
#    #ここにコードを書いてください

# # print(add(4, 3)) # 7
# # print(add(100, 43)) # 143
# # 上記の関数に 1 つだけ値を渡すと何が起こるでしょうか？もっとたくさんの値を渡したら何が起こるでしょうか？
# print(add(100)) # 何が起こる？
# print(add(1, 4, 5)) # 何が起こる？


# # 問題 4
# # subtract という名前の関数を宣言しましょう。 この関数は第一引数から第二引数を引き算する関数です。
# def subtract(num1, num2):
#     return num1 - num2
#    #ここにコードを書いてください

# print(subtract(4, 3)) # 1
# print(subtract(100, 42)) # 58

# 問題 5
# average という名前の関数を宣言しましょう。 ２つの数値型のデータを引数に取り、それらの数値の平均を出力します。
# def average(num1,num2):
#     print((num1+num2)/2)
    
# average(5,10)
    
#    #ここにコードを書いてください

# 問題 6
# greeting という名前の関数を宣言しましょう。 文字列型（string） のデータを引数に渡し、右側にある挨拶文を表示してください。
# def greeting(name):
#     return "Hello, " + name + "!"
#    #ここにコードを書いてください
# print(greeting("Alex")) # Hello, Alex!
# print(greeting("Beau")) # Hello, Beau!


# 問題 7
# 次の関数には誤りがあります。何が間違っているのでしょうか。
# def square(num):
#     return num * num

# print(square(5))

# def square(x):
#     return x * x

# print(square(111))

# # 一方こちらは問題なく動きます。さらに良い書き方はないでしょうか？
# def Square(monkey):
#     return monkey**2

# print(Square(10))

# 問題 8
# cubeという名前の関数を宣言しましょう。引数 'x' の 3 乗を出力してください。
# def cube(x):
#     print(x**3)
#     #return x ** 3
# cube(5)

#print(cube(7))
    #ここにコードを書いてください

 
# 問題 9
# 摂氏の温度を華氏に変換する関数を書いてください。
# def to_fahrenheit(celsius):
#     return (celsius * 9/5)+32

# print(to_fahrenheit(40))
    
#     #ここにコードを書いてください
# 問題 10
# 2 つの値を引数にとり、両者が等しければ True、等しくなければ False を返す関数 is_equal を作成してください。
# def to_equal(a,b):
#     return a==b
# print(to_equal(2,3))

#     #ここにコードを書いてください

# # 問題 11
# # 本体価格を表す浮動小数点数と税率を表す浮動小数点数を引数にとり、税込みの合計金額を返す関数 apply_tax を作成してください。
# # 例：
# # apply_tax(300, 0.1) # 330（300円の本体価格で税率 10 ％のときの合計金額として）

# def apply_tax(pre_price,tax):
#     print(type (int(pre_price*(1+tax))))
#     return int(pre_price*(1+tax))

# print(apply_tax(300, 0.1))

# 問題 12
# 整数を引数に取る asterisk_creator という名前の関数を書いてください。この関数はアスタリスク（＊）が与えられた整数値の数だけ連なっている文字列を返すようにします。
# 例えば、print(asterisk_creator(5)) とすると ***** と表示されるようにしてください.

def asterisk_creator(num):
    asterisk = ""
    for i in range(num):
        asterisk += "*" 
        print(asterisk)
    return num * "*"

print(asterisk_creator(5))

    #ここにコードを書いてください
    

# 中級問題
# 問題 13
# 次のコードを実行したら何が表示されますか？なぜそうなるのでしょうか？

def simpleHelloA():
    return "hello"

def simpleHelloB():
    return "hello"


a = simpleHelloA()
b = simpleHelloB()
print(a, b)

# 問題 14
# まだ習っていない構文を使います。調べてながら進めてみましょう！
# 2 つの値を引数にとり、両者が等しければ True、
# 等しくなければ False を返す関数 is_equal を作成してください。

def is_equal(a,b):
    if a == b:
        return True
    else:
        return False

print(is_equal(1,1))
    

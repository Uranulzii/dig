# loop_exercise

#exercise_1
# counter = 0
# while counter <= 20:
#     print(counter)
#     counter = counter + 1

#exercise_2
# counter = 20
# while counter >= 0:
#     print(counter)
#     counter = counter - 1

#exercise_3    
# counter = 1
# while counter <= 100:
#     print(counter)
#     counter = counter + 3
 
#exercise_4    
# counter = 1
# while counter <= 16777216:
#     print(counter)
#     counter = counter * 2

#exercise_5    
# counter = -1
# while counter <= 1:
#     print(counter)
#     counter = counter + 1 

#exercise_6
# placeholder = ""
# string = "hahahaha"
# while len(placeholder) <= len(string):
#     print(placeholder)
#     placeholder = placeholder + "ha"
    
#exercise_7
# placeholder = "abcdefghijklmnopqrstuvwxyz"
# string = ""
# while placeholder != string:
#     print(placeholder)
#     placeholder = placeholder[1:]

# exercise 8
# sentence = "this is a sentence with many words."
# counter = 0
# result = 0
# while counter < len(sentence) :
#     if sentence[counter] =="e":
#         result += 1
#     counter += 1
    
# print(result)

#exercise 9
# sentence = "this is a sentence with many words."
# counter = 0
# result = 0
# while counter < len(sentence) :
#     if sentence[counter] ==" ":
#         result += 1
#     counter += 1
# result +=1  
# print(result)

# string = "919"
# while len(string) <=8:
#     print(string)
#     string = "0" + string

"""
基礎演習
以下の問題を while ループを使って解いてください。
関数 count_word を宣言してください。引数に渡された文字列の長さを表示されてください。
"""

# #テストケース:
# def count_word(string):
#     num = 0
#     while num < len(string):
#         num += 1
#     print(num)
    
# count_word("hello") # 5
# count_word("world") # 5

"""
関数 underline を宣言してください。文字列をアンダーライン付きで表示させてください。アンダーラインの長さは文字列と同じにします。
# テストケース:
"""
# def underline(string):
#     num = 0
#     while num < len(string):
#         num += 1
#     print(string)
#     print("_"*num)
    
# underline("Chapter 4: While Loops")

# Chapter 4: While Loops
# ----------------------

"""
# 関数 consonant を宣言してください。あなたの出身地をアルファベットで記したときの最初の2つの子音を返してください。
# テストケース:
"""
# def consonant(country):
#     num = 0
#     sentence = ""
#     while len(sentence) < 2: # 子音の数が2以下の時に繰り返します。
#         letter = country[num]
#         if  letter not in "aieou":
#             sentence = sentence + letter
#         num = num + 1
#     print(sentence)
    
# consonant("Minneapolis") # Mn

"""
# 関数 calculate_from_age を宣言してください。1から自分の年齢までのすべての数字の合計を計算する。
# テストケース:
"""

# def calculate_from_age(age):
#     num = 0
#     sum = 0
#     while num <= age:
#         sum = sum + num # メインの処理
#         num += 1 # 収束条件の判定
#     print(sum)
# calculate_from_age(42) # 903

"""
# 関数 say_hello を宣言してください。引数に数字 n 分ループさせて Hello! を表示させましょう。
# テストケース:
"""
# def say_hello(n):
#     while n > 0:
#         print("Hello!")
#         n -= 1
# say_hello(4)
# # "Hello!"
# # "Hello!"
# # "Hello!"
# # "Hello!"

"""
# 関数 count_up を宣言してください。0 から 10 までの数字を毎行 1 増えていくように表示させてください。
# テストケース:
"""
# def count_up():
#     n = 0
#     while n <= 10:
#         print(n) 
#         n += 1

# count_up()
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

"""
# 関数 count_down を宣言してください。start の数値をを引数にとり、start から 0 までの数値をカウントダウンさせて表示しましょう。
# テストケース:
"""
# def count_down(start):
#     while start >= 0:
#         print(start)
#         start -= 1

# print('\n----------------------------')
# count_down(10)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

"""
# 関数 print_string を宣言してください。文字列を 1 つ引数にとり、そのすべての文字を 1 つずつ出力させてください。
# テストケース:
# """
# def print_string(string):
#     num = 0
#     while num < len(string):
#         print(string[num])
#         num += 1

# print_string("apple")
# a
# p
# p
# l
# e

"""
# 関数 add_one を宣言してください。与えられた文字列にそれぞれ 1 を足した文字列を返す。
# テストケース:
"""
# def add_one(num_str):
#     num = 0
#     sentence=""
#     while num < len(num_str):
#         i=int(num_str[num])
#         sentence += str(i+1)
#         num += 1
#     print(sentence)
        

# add_one("12345") # "23456"

"""
# 応用演習
# 関数 create_range_by_steps を宣言してください。第一引数から第二引数までの数を、第三引数分のステップで print してください。
# テストケース:
"""



#    create_range_by_steps(1, 10, 2)
   # 1
   # 3
   # 5
   # 7
   # 9

#    create_range_by_steps(10, 30, 5)
   # 10
   # 15
   # 20
   # 25
   # 30

"""
# 関数 unique を宣言してください。引数として文字列を 1 つとり、重複していない文字のみを返してください。
# テストケース:
"""
def unique(string):
    n = 0
    sentence = ""
    duplicate = ""
    while n < len(string):
        letter = string[n]
        if letter not in sentence:
            sentence += letter
        else:
            duplicate += letter
        n += 1
    print(string.replace(duplicate, ''))
    
unique("hello") # heo
unique("world") # world


"""
# 関数 zip を宣言してください。不特定の数の文字列を引数として取り、各文字列が全部入った文字列を返してください。
# テストケース:
"""

# zip("hello", "world") # "hello world"
# zip("a", "b", "c", "d") # "a b c d"

"""
# ナイトメア問題 😈
# 関数 sum を宣言してください。不特定の数の引数を取り、すべての引数の合計を返してください。
# テストケース:
"""

# sum(1) # 1
# sum(1, 1, 1, 1, 1) # 5
# sum(1, 2, 3, 4, 5) # 15

"""
# 関数 sleep を宣言してください。1秒ごとに "n 秒が経過しました" と第一引数に渡された数字分表示させてください。
# テストケース:
"""

#    sleep(1)
#    # 1秒が経過しました

#    sleep(3)
#    # 1秒が経過しました
#    # 2秒が経過しました
#    # 3秒が経過しました
# パーティに n 人のゲストが来ています。各ゲストには番号が割り当てられます。到着したすべてのゲストに新しいゲストを紹介する関数、 get_introductions を宣言してください。
# テストケース:
# get_introduction(1)
# # "welcome 1"

# get_introduction(2)
# # "welcome 1"
# # "welcome 2, meet 1"


# get_introduction(5)
# # "welcome 1"
# # "welcome 2, meet 1"
# # "welcome 3, meet 1 and 2"
# # "welcome 4, meet 1, 2 and 3"
# # "welcome 5, meet 1, 2, 3 and 4"
# クリスマスツリーを表示する関数 christmas_tree を宣言してください。
# テストケース:
#    christmas_tree("T", 1)
#    # "T"

#    christmas_tree("+", 2)
#    #  +
#    # + +

#    christmas_tree("#", 4)
#    #    #
#    #   # #
#    #  # # #
#    # # # # #
# # \n は改行を意味するコードです。実際に文字列を print すると、ツリーがこんな風に表示されますよ。
#     T
#    T T
#   T T T
#  T T T T
# T T T T T

#1
# list() を使って新しいリストを作るとき、そのもとになれるのはどんなデータ型の値でしょうか？（3 種類あります。）
# int, string, list
#2
# range(5) が表している数値は？
print(list(range(5)))
#3
# range(3, 9) が表している数値は？
print(list(range(3,9)))

#4
# range(5, 20, 5) が表している数値は？
print(list(range(5,20,5)))

#5
# range(10, 1, -1) が表している数値は？
print(list(range(10,1,-1)))

#6
# range(1000000000000)というコードを実行するときの CPU パワーとメモリの消費量は比較的高い？低い？
# 低い

#7
# list(range(1000000000000)) というコードを実行するときの CPU パワーとメモリの消費量は比較的高い？低い？
# 高い


"""
基本演習
"""
# 問題 1

# 整数を 1 つ引数にとり、1 からその数値まで順番にコンソールに表示する count_up という関数を書いてください。

def count_up(number):
    for num in range(number):
        print(num)

count_up(5)

# ...とすると以下のように表示されるようにしてください。
1
2
3
4
5

# 問題 2
# リストを 1 つ引数にとり、for ループを使ってリストの
# 後ろから前に向かって逆順に要素をコンソールに表示する関数 reverse_print を書いてください。

# def reverse_print(words):
#     new_words = ""
#     words2=list(words)
#     for num in words:
#         new_words += words2.pop()
#     print (new_words)
         
def reverse_print(words):
    new_words = ""
    words2=list(words)
    for num in words:
        new_words += words2.pop()
    print (new_words)

reverse_print(["Almond Eye", "Efforia", "Equinox"])

# ...とすると以下のように表示されるようにしてください。

# Equinox
# Efforiag
# Almond Eye

# 問題 3
# 文字列を 1 つ引数にとり、文字と文字の間にスペースを
# 1 つはさむようにした新しい文字列を作って返す関数 kerning_loop を書いてください。

def kerning_loop(word):
    word_1 = ""
    for num in word:
        word_1 += " " + num
    print(word_1)
        
    
print(kerning_loop("cat"))


# 問題 4 （チャレンジ問題）
# 2 つのリストを引数にとり、それを合体させた新しい 1 つのリストを返す関数 zip を書いてください。
# 要素の順番はもととなる 2 つのリストから交互に取り込むようにしてください。

# def zip(list1,list2):
# #     list_3 = list1.append(int(list2))
#     new = []
#     for i in len(list1):
#         new_list = list1[i] , list2[i]
#         new += new_list
#     print (new)


def zip(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append([list1[i], list2[i]])
    return new_list
print(zip(["A", "B", "C"], ["1", "2", "3"]))



print("zip問題_1")
def zip(list1,list2):
    s=""
    for i in range(len(list1)):
        s=s+list1[i]+list2[i]
    return list(s)


print(zip(["A", "B", "C"], ["1", "2", "3"]))

print("zip問題_2")
def zip(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i])
        new_list.append(list2[i])
    return new_list

print(zip(["A", "B", "C"], ["1", "2", "3"]))
 
    # for i in list2:
    #     list1.append(i)
    #     list3=list1
    # # print(list3)
    # n = 0
    # while n < len(list1):
    #     new_list.append(list1[n])
    #     n += 1
    #     # return new_list
    # while n < len(list2):
    #     new_list.append(list2[n])
    #     n += 1
    #     # return new_list
    # print(new_list)        

    # list1.append(list2)
    # list3=list1
    # print(list3)
    
# zip(["A", "B", "C"], ["1", "2", "3"])

# ["A", "1", "B", "2", "C", "3"]

# list = [1,2,3]
# list1 = [4,5,6]
# list.append(list1[0:2])
# list2 = list
# print(list2)


# list = [1,2,3]
# list1 = ["a","b","c"]
# new = list[1] , list1[1]
# print(new)


# 問題 5
print("問題5")
# 数字( n ) と文字 1 つを受け取り、その文字を n 個 x n 個コンソールに表示する関数 print_square を書いてください。

def print_square(a,b):
    for i in range(int(a)+1):
        c = b*i
    # print(c)
    for j in range(int(a)):
        print(c)

print_square(3, "X")


# ...とすると以下のように表示されるようにしてください。
# X X X
# X X X
# X X X
print_square(4, "$")
# ...とすると以下のように表示されるようにしてください。
# $ $ $ $
# $ $ $ $
# $ $ $ $
# $ $ $ $


# 問題 6
# While の演習問題を for ループで実装してみましょう！



#中級演習
#問題1


print("中級問題1")

# テキストファイルにある5,000人以上の名前の中で最もアルファベットの値が高いものを見つける関数
# name_score を書いてください 。組み込み関数の ord を使って Unicode コードポイントを使って計算しましょう。


import names
def name_score(names):
    max = 0
    name_box = ""
    for i in names:
        # print(i)
        x = 0
        for j in i:
            # print(j)
            x += ord(j)
        # print(x)
        if max < x:
            max = x
            name_box = i
    print(name_box)
    return max        
   
 

print(name_score(names.name))

#応用演習


#問題1
# 以下の条件を満たす関数 collatz_sequence を書いてください。
# 以下の正の整数のセットに関して以下のようなシーケンスが定義されています。
# n → n/2 (n は偶数)
# n → 3n + 1 (n は奇数)
# 上記のルールを使って13から始めると以下のようなシーケンスができます。
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 13で始まり1で終わるこのシーケンスは10項が含まれています。
# コラッツの問題として未だ解決されていない「コラッツの問題」ですが、どの数から始めても１になると予想されています。
# 100万未満で最も長い連なりを作れるのはどの数字から始めたときでしょうか。
# 注：途中では100万を超える項があってもよいこととします。

print("応用問題2")
# 問題2
# 10×10のグリッドがあるとします。マトリクスを転置して行を列に、列を行にする関数　rotate_matrix を書いてください。

import random
def make_matrix(size):
    matrix = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(random.randint(0,10))
        matrix.append(line)
    return matrix

def rotate_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix)):
            line.append(matrix[j][i])
        new_matrix.append(line)
    return new_matrix

matrix = make_matrix(4)
rotate_matrix(matrix)
print(matrix)
print(rotate_matrix(matrix))
                      
            
# print(make_matrix(10)) #10:10 no matrix tsukuri random ni
            
# def rotate_matrix(matrix):
#     new_matrix = list(matrix)
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             num = list(matrix)[j][i]
#             new_matrix[i][j] = matrix[j][i]
#             print(matrix)
#     return new_matrix
#     matrix = []
#     for i in range(size):
#         line = []
#         for j in range(size):
#             line.append(random.randint(0,10))
#         matrix.append(line)
#     return matrix
print("応用問題3")
# 問題 3
# 以下の条件を満たす関数 sudoku_checker を書いてください。
# 二次元リストを使用して、以下の完成された二つの数独が正しいか確認しましょう。
# 9つの各タテ列に1-9の数字が一つずつあるか確認してください。
# 9つの各ヨコ列に1-9の数字が一つずつあるか確認してください。
# 9つの3x3の各ブロックに1-9の数字が一つずつあるか確認してください。


# def sudoku_checker(sudoku):
#     for i in range(9):
#         options = list(range(1,10))
#         for j in range(9):
#             if sudoku[i][j] not in options:
#                 return False
#             options.remove(sudoku[i][j])
#         if len(options) != 0:
#             return False
#     for i in range(9):
#         options = list(range(1,10))
#         for j in range(9):
#             options.remove(sudoku[j][i])
#         if len(options) != 0:
#             return False
#     for i in range(9):
#         options = list(range(1,10))
#         gay_okamoto = i//3
#         gay_nakamura = i % 3
#         for j in range(3):
#             for g in range(3):
#                 element = sudoku[j+gay_okamoto][g+gay_nakamura]
#                 if element not in options:
#                     return False
#                 options.remove(element)
#         if len(options) != 0:
#             return False  
#     return True
            

    
def sudoku_checker(sudoku):
    for i in range(9):
        options = list(range(1,10))
        for j in range(9):
            if sudoku[i][j] not in options:
                return False
            options.remove(sudoku[i][j])
    for i in range(9):
        options = list(range(1,10))
        for j in range(9):
            if sudoku[j][i] not in options:
                return False
            options.remove(sudoku[j][i])
    for i in range(9):
        options = list(range(1,10))
        gay_okamoto = i//3
        gay_nakamura = i % 3
        for j in range(3):
            for g in range(3):
                element = sudoku[j+gay_okamoto*3][g+gay_nakamura*3]
                if element not in options:
                    return False
                options.remove(element)
    return True



sudoku_1 =[
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

sudoku_2 =[
    [1, 2, 3, 6, 7, 8, 9, 1, 5],
    [5, 8, 4, 2, 3, 9, 7, 6, 1],
    [9, 6, 2, 1, 4, 5, 3, 2, 8],
    [3, 7, 2, 4, 6, 1, 5, 8, 9],
    [6, 9, 1, 5, 8, 3, 2, 7, 4],
    [4, 5, 8, 7, 9, 5, 6, 1, 3],
    [8, 3, 6, 9, 2, 4, 1, 5, 7],
    [2, 7, 9, 8, 5, 7, 4, 3, 6],
    [7, 4, 5, 2, 1, 6, 8, 9, 2],
]

print(sudoku_checker(sudoku_1))# True
print(sudoku_checker(sudoku_2)) # False


#Nightmare問題
# #問題1
# 二次元リストで表された数独の問題が３つあります。空のマスは 0 で表されています。
# 数独を解く関数 solve_sudoku を書いてください。solve_sudokuは数独の二次元リストを引数にとり、リスト内の0を正しい数字に置換し、
# 全ての置換が終わると True 、それ以外は False を返します。（レクチャーの先取りになりますが、再帰関数やバックトラック法についても調べてみることをおすすめします。）

# easy_puzzle = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]

# medium_puzzle = [
#     [0, 2, 0, 6, 0, 8, 0, 0, 0],
#     [5, 8, 0, 0, 0, 9, 7, 0, 0],
#     [0, 0, 0, 0, 4, 0, 0, 0, 0],
#     [3, 7, 0, 0, 0, 0, 5, 0, 0],
#     [6, 0, 0, 0, 0, 0, 0, 0, 4],
#     [0, 0, 8, 0, 0, 0, 0, 1, 3],
#     [0, 0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 9, 8, 0, 0, 0, 3, 6],
#     [0, 0, 0, 3, 0, 6, 0, 9, 0],
# ]

# hard_puzzle = [
#     [0, 0, 0, 6, 0, 0, 4, 0, 0],
#     [7, 0, 0, 0, 0, 3, 6, 0, 0],
#     [0, 0, 0, 0, 9, 1, 0, 8, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 5, 0, 1, 8, 0, 0, 0, 3],
#     [0, 0, 0, 3, 0, 6, 0, 4, 5],
#     [0, 4, 0, 2, 0, 0, 0, 6, 0],
#     [9, 0, 3, 0, 0, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0, 0, 1, 0, 0],
# ]

# def show_result(puzzle):
#     if solve_sudoku(puzzle):
#       for row in puzzle:
#           print(row)
#     else:
#       print("No solution exists.")
#     print()

# show_result(easy_puzzle)
# show_result(medium_puzzle)
# show_result(hard_puzzle)

# 出力結果例
# [5, 3, 4, 6, 7, 8, 9, 1, 2]
# [6, 7, 2, 1, 9, 5, 3, 4, 8]
# [1, 9, 8, 3, 4, 2, 5, 6, 7]
# [8, 5, 9, 7, 6, 1, 4, 2, 3]
# [4, 2, 6, 8, 5, 3, 7, 9, 1]
# [7, 1, 3, 9, 2, 4, 8, 5, 6]
# [9, 6, 1, 5, 3, 7, 2, 8, 4]
# [2, 8, 7, 4, 1, 9, 6, 3, 5]
# [3, 4, 5, 2, 8, 6, 1, 7, 9]

# [1, 2, 3, 6, 7, 8, 9, 4, 5]
# [5, 8, 4, 2, 3, 9, 7, 6, 1]
# [9, 6, 7, 1, 4, 5, 3, 2, 8]
# [3, 7, 2, 4, 6, 1, 5, 8, 9]
# [6, 9, 1, 5, 8, 3, 2, 7, 4]
# [4, 5, 8, 7, 9, 2, 6, 1, 3]
# [8, 3, 6, 9, 2, 4, 1, 5, 7]
# [2, 1, 9, 8, 5, 7, 4, 3, 6]
# [7, 4, 5, 3, 1, 6, 8, 9, 2]

# [5, 8, 1, 6, 7, 2, 4, 3, 9]
# [7, 9, 2, 8, 4, 3, 6, 5, 1]
# [3, 6, 4, 5, 9, 1, 7, 8, 2]
# [4, 3, 8, 9, 5, 7, 2, 1, 6]
# [2, 5, 6, 1, 8, 4, 9, 7, 3]
# [1, 7, 9, 3, 2, 6, 8, 4, 5]
# [8, 4, 5, 2, 1, 9, 3, 6, 7]
# [9, 1, 3, 7, 6, 8, 5, 2, 4]
# [6, 2, 7, 4, 3, 5, 1, 9, 8]



# Dictionary

print("基礎演習"_of_dictionary)

# # 基礎演習
# # 問題 1

# # 文字列を 1 つ引数にとり、出現する文字とその出現回数を記録するディクショナリを返す関数 count_letters を書いてください。
# # まず空のディクショナリを作る必要があります。

def count_letters(name):
    counter = { }
    

# # その上で文字列をループ処理しながら、各文字がすでに出てきたかをチェックします。ある文字が初めて出てきた場合はディクショナリにその文字を加え、
# # 値を 1 とします。既出の場合はその文字に対する値を 1 つ増やします。
# # 例：
# # count_letters("salamander")

# # 以下のような返り値が得られるようにしたい。
# # {"s": 1, "a": 3, "l": 1, "m": 1, "n": 1, "d": 1, "e": 1, "r": 1}
# 問題 2
# 複数の文字列を含む 1 つのリストを引数にとり、重複する文字列は 1 つだけ残して余分な文字列を取り除いたリストを新しく作って返す関数 remove_repeats を書いてください。
# 例：
# # print(remove_repeats(["a", "b", "c", "b", "a", "d"])) # ["a", "b", "c", "d"]
# # ヒント: in が役に立つかも！
# 問題 3
# 文字列を 1 つ引数にとり、各母音（a, e, i, o, u）の出現回数をディクショナリに記録する関数 count_vowels を書いてください。
# 例：
# # count_vowels("digging for apples")

# # 以下のような返り値が得られるようにしたい。
# # {"i": 2, "o": 1, "a": 1, "e": 1}
# 問題 4
# 複数の文字列を含むリストを 1 つ引数にとり、重複する文字列があれば True を、すべて一意の文字列で重複がなければ False を返す関数 is_duplicated を書いてください。
# 例：
# # class_a = ["John", "Tom", "Alex"]
# # class_b = ["John", "Tom", "John"]

# # print(is_duplicated(class_a)) # False
# # print(is_duplicated(class_b)) # True
# 応用演習
# 問題 1
# 同じキーの場合は値を合算しつつ、以下の例のような形で 2 つのディクショナリをまとめたディクショナリを返す関数 merge_dictionaries を書いてください。
# 例：
# a = {'a': 100, 'b': 200, 'c':300}
# b = {'a': 300, 'b': 200, 'd':400}

# print(merge_dictionaries(a, b)) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}
# 問題 2
# ディクショナリの似通ったキー（例えば電話番号など）をまとめる関数 merge_orders を書いてください。
# 例：
# orders =  {
#      "070 1234 1234": 200,
#      "07012341234": 500,
#      "070-1234-1234": 100,
#      "(070) 1234-1234": 500
#      "+81 (70) 1234-1234": 500
# }

# merged_orders = merge_orders(orders)
# print(merged_orders)  # {"07012341234": 1800}
# 問題 3
# データセットを使い、男性と女性、それぞれの平均身長を求める関数を書いてください。また、このデータセットの中で150センチより背の高い男性は何人いますか。
# 例：
# age = average_age(people)
# height = average_height(people)
# weight = average_weight(people)

# print(age)
# print(height)
# print(weight)
# 問題 4
# アメリカの成績評価に使われるGPAに関する問題です。ある生徒の成績があり、それをもとにGPAを計算する関数　grades　を書いてください。計算に使う数字は以下に示したものを使ってください。なお、各科目で点数によりレターグレード（A, B, Cなど）が決まり、レターグレードによってグレードポイント（１，２，３，４）が決まります。GPAはグレードポイントの合計÷科目数で求められます。
# 例：
# grades = {
#     'Physics': 82,
#     'Math': 65,
#     'History': 75
# }

# grade_table = {
#     'A': 89.5,
#     'B': 79.5,
#     'C': 69.5,
#     'D': 59.5,
# }

# gpa_table = {
#     'A': 4,
#     'B': 3,
#     'C': 2,
#     'D': 1,
# }
# 科目において特に成績優秀だった場合（H）とその科目が大学レベルのカリキュラムだった場合（AP）には、その科目のグレードポイントに1点の加点がつきます。こちらの生徒のGPAを計算してください。
# 例：
# grades = {
#   'H Physics': 82,
#   'Math': 65,
#   'AP History': 75
# }



# # 問題 4
# # 複数の文字列を含むリストを 1 つ引数にとり、重複する文字列があれば True 
# # を、すべて一意の文字列で重複がなければ False を返す関数 is_duplicated を書いてください。
# # 例：

# # class_a = ["John", "Tom", "Alex"]
# # class_b = ["John", "Tom", "John"]
# # def is_duplicated(names):
# #     A = []
# #     count = 0
# #     for i in names:
# #         if i in A:
# #             count += 1
# #         else:
# #             A.append(i)
# #     if count >=1:
# #         kaesu = True
# #     else: 
# #         kaesu = False
# #     return kaesu   

# # print("問題4")
# # print(is_duplicated(class_a)) # False
# # print(is_duplicated(class_b)) # True

# #応用演習

# #問題1
# # 同じキーの場合は値を合算しつつ、以下の例のような形で
# # 2 つのディクショナリをまとめたディクショナリを返す関数 merge_dictionaries 
# # を書いてください。




# # a = {'a': 100, 'b': 200, 'c':300}
# # b = {'a': 300, 'b': 200, 'd':400}

# # def merge_dictionaries(list1, list2):
# #     for key,item in list2.items():
# #         if key in list1:
# #             list1[key] += item
# #         else:
# #             list1[key] = item
# #     return list1

# # print("応用問題1")
# # print(merge_dictionaries(a, b)) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}


# # 問題 2
# # ディクショナリの似通ったキー（例えば電話番号など）をまとめる関数 merge_orders を書いてください。
# # 例：



# # orders =  {
# #      "070 1234 1234": 200,
# #      "07012341234": 500,
# #      "070-1234-1234": 100,
# #      "(070) 1234-1234": 500
# #      "+81 (70) 1234-1234": 500
# # }



# # merged_orders = merge_orders(orders)
# # print(merged_orders)  # {"07012341234": 1800}
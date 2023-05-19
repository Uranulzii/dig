#５月16日module(モジュール)について

print("exercise1")
def fizz_buzz():
    for i in range(100):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i %5 ==0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()

print("exercise2")
# app.py

def calculate_pi_poorly():
    return 355 / 113

def calculate_circle_area(radius):
    return radius * radius * calculate_pi_poorly()

area = calculate_circle_area(4)

print(area)

calculate_pi_poorly()


print("exercise3")
#標準ライブラリモジュール
#importを使ってすぐに標準ライブラリから色々導入できる。

#pai wo daseru

import math

def calculate_circle_area(radius):
    return math.pi * (radius **2)

print("This pizza has ", calculate_circle_area(10), " square inches of deliciousness")


print("exercise3_1")
from math import pi #こんな感じで一個だけ入れるときこれでいい。
print ("pi is equal to", pi)


#moduleの演習
#ウォーミングアップ
# ① Pythonでは自分で作ったモジュールをう！
# 1. 今開いているファイルとは別のファイ使ったり、すでに誰かが作って用意されたライブラリ（外部ライブラリ）が利用できます。
# まず、自分でモジュールを作ってみましょルを作ります。こちらにmy_module.pyという名前をつけてください。
# 2. my_module.pyに “hello”とprintする関数 say_helloと、引数として受け取った数値を2倍にして返すdoubleという関数を書いてください。
# 3. もとのファイルに戻って、import my_moduleと入れます。このとき.pyはいれません。これでもとのファイルでmy_moduleのなかの関数が使えるようになっています。
# 4. でも！say_hello()では動きません。（試しに実行してみてください。）
# インポートされた関数を使うには　モジュール名.関数名　として入れる必要があります。my_module.say_hello()と書いて、ファイルを実行してください。上手く行きましたか？＾＾
# 5. では、doubleも使えるか試してください。

print("module_exercise1")
import my_module
my_module.say_hello()
my_module.double(5)

# ② Python にはたくさんのライブラリが用意されています。
# 組み込み関数　　　ひんぱんに使われるのでインポートしなくても使える。
# 皆さんが定義しなくても使える関数です。
# 例: print(), input(), str(), bool(), int(), float(), list(), len(), round(), type(), abs()

# インポートが必要なもの　
# - 外部ライブラリ
# - 標準ライブラリであっても組み込み関数ではないもの

# それではよく使われる標準ライブラリとしてmathモジュールを使ってみましょう。
# https://docs.python.org/ja/3/library/math.html
# こちらにドキュメンテーションがあり、mathモジュールで使える様々な関数がリストされています。
# 平方根　sqrt
# mathモジュールをインポートします。

print("module_exercise2")
import math
num = math.sqrt(4)
print(num)
# できましたか？

number = math.ceil(-6.7)
print(number)

number = math.floor(-6.7)
print(number)

def area_calculation(radius):
    print(math.ceil((math.pi * (radius ** 2))))
area_calculation(7)



# math.ceil、 math.floorなども試してみてください。
# mathモジュールには定数も提供(されています。例えば円周率もその一つです。math.piを使って実際に円の面積を計算してみてください。

# 便利なモジュールを調べてみましょう。
# Itertools モジュール トランプゲームの演習では itertools をインポートしました。itertoolsのドキュメンテーションに説明があります。以下のリストの問題は itertools の関数を単独または複数組み合わせて解くことができます。
# あなたが他の4人のルームメイトと暮らしていて、毎週2人が掃除をする掃除スケジュールを作りたいと思ったとします。組み合わせはいくつあるでしょうか？（重複するものは除きます。） 終わらない数字のリスト（タイマーのようなもの）を作りたいとします。 どうすればできるでしょう？ ['abc', 'bcd', 'cde'... ] というリストはどのように作成するのでしょうか？ 動物のリストと、名前のリストがあったとします。 両者のリストは同じ長さだとして、 動物と名前を対にしたリストを作るにはどうすればいいでしょうか？
print("module_exercise3")

# from itertools import product
import itertools
comb = itertools.combinations('abcde', 2)
list1 = list(comb)
# print(len(list1))
print(list1)


print("module_exercise4_1_stopwatch")

import time
import datetime
 
# # Create class that acts as a countdown
# def countdown(h, m, s):
 
#     # Calculate the total number of seconds
#     total_seconds = h * 3600 + m * 60 + s
 
#     # While loop that checks if total_seconds reaches zero
#     # If not zero, decrement total time by one second
#     while total_seconds > 0:
 
#         # Timer represents time left on countdown
#         timer = datetime.timedelta(seconds = total_seconds)
        
#         # Prints the time left on the timer
#         print(timer, end="\r")
 
#         # Delays the program one second
#         time.sleep(1)
 
#         # Reduces total time by one second
#         total_seconds -= 1
 
#     print("Bzzzt! The countdown is at zero seconds!")
 
# # Inputs for hours, minutes, seconds on timer
# h = input("Enter the time in hours: ")
# m = input("Enter the time in minutes: ")
# s = input("Enter the time in seconds: ")
# countdown(int(h), int(m), int(s))

# print("module_exercise4_2")

# def timer(h, m, s):
#     i = 0
#     total_seconds = h * 3600 + m * 60 + s
#     total_seconds_1 = h * 3600 + m * 60 + s
#     while total_seconds > i:  
#         while i < total_seconds_1
#         i += 1
#         time.sleep(1)
#         total_seconds += 1
#         print(total_seconds, end="\r")
    
# h = input("Enter the time in hours: ")
# m = input("Enter the time in minutes: ")
# s = input("Enter the time in seconds: ")
# timer(int(h), int(m), int(s))

# 終わらない数字のリスト（カウントアップしていくもの）を作りたいとします。 どうすればできるでしょう？
# print("module_exercise4_2_timer")
# def timer(h, m, s):
#     i = 0
#     total_seconds = h * 3600 + m * 60 + s
#     while i < total_seconds:  
#         time.sleep(1)
#         total_seconds -= 1
#         i += 1
#         print(total_seconds, end="\r")
    
# h = input("Enter the time in hours: ")
# m = input("Enter the time in minutes: ")
# s = input("Enter the time in seconds: ")
# timer(int(h), int(m), int(s))


# ['abc', 'bcd', 'cde'... ] というリストはどのように作成するのでしょうか？

import itertools
comb = itertools.combinations('abc', 2)



# 組み合わせはタプルで出力されます。以下は組み合わせパターンをリストで出力した場合 
# >>> list(comb)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
# 例えば [(‘elephant’, ‘david’), (‘tiger’: ‘francis’) ….]　など。
# レキソグラフィック・パミュテーション（辞書式順列） 順列とはアイテムを順番つきで並べたものです。例えば、3124は、1、2、3、4で作れる順列の1つです。 すべての順列を数の順で並べたものを辞書のような順番で並べた順列という意味で辞書式順列と呼びます。
# 例えば 0、1、2の辞書式順列は以下の通りです： 012 021 102 120 201 210
# 0、1、2、3、4、5、6、7、8、9で辞書式順列を作った場合、100万番目は何でしょう？
# Let’s explore a codebase! ここに requests というライブラリへのリンクがあります。 requests は何をするものなのだと思いますか？ モジュールはいくつあるでしょうか？ コードの主要な部分はどこにあると思いますか？ それぞれのモジュールが何をするのか考えてみてください！ まずは auth、exception、models、status_codes はどうでしょうか。
# これはBeautifulSoup4 ライブラリへのリンクです。 BeautifulSoupはどんなことをすると思いますか？ モジュールはいくつあるのでしょうか？ コードの主要な部分はどこにあると思いますか？ いくつかのモジュールを選んで何をするのか調べてみてください！
# 注：熟練したプログラマーであっても、これらのライブラリのすべてを理解することはできないでしょう！ それよりも、推測ができるようになることが重要です。


#afternoon class 
#first class の　復習

# class House:
#     def __init__(self,roof_color, floors) -> None:
#         self.roof_color = roof_color
#         self.floors = floors
    
#     def get_roof_color(self):
#         return self.roof_color
    

# urnaa_house= House("White", 3)

# print(urnaa_house.roof_color)
# print(urnaa_house.floors)


#object指向プログラミング(OOP)
#どうしてOOP?
#コードの構造：関連するデータをまとめるのでコードが整理されます。    

# class Vehicle:
#     def __init__(self,color):
#         self.color = color
#         self.__fuel = 0
        
#     def get_fuel(self):
#         return self.__fuel
    
#     def add_fuel(self,amount):
#         self.__fuel += amount
        
# blue_car = Vehicle("blue")
# print(blue_car.color)
# # print(blue_car.fuel)
# print(blue_car.add_fuel(10))



#classの演習
#基礎演習クラス
#問題1
print("問題1")
# BodyBuilderというクラスを書いてください。
# インスタンスが体重と身長という属性とBMIを返すget_bmiというメソッドを持つようにします。
# 実際にインスタンスを１つ作ってBMIを計算してみてください。

class Bodybuilder:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
    def get_bmi(self):
        bmi = self.weight /((self.height/100) **2)
        return bmi
      
person1 =Bodybuilder(58, 167) 
        
print(person1.get_bmi())

print("問題 2")
# AirLiner という航空会社を表すクラスを書いてください。 属性は
# 会社名を持ち、announceというメソッドで “Thank you for flying with “ + 会社名というメッセージをターミナルに表示します。
# 実際に航空会社名を入れたインスタンスをひとつ作って実行してみてください。

class Airliner:
    def __init__(self, name):
        self.name = name
        
    def announce(self):
        print("Thank you for flying with " + self.name)
        
airline1 = Airliner("JAL")

airline1.announce()

print("問題 3-1")
# 円のクラスを作ってみました。属性として直径を持ち、
# get_circumというメソッドで円周を返すメソッドを持つインスタンスができるはずだったのですが、
# get_circumを呼んでもうまく機能しません。どうやらpiとdiameterの書き方が悪いようなのですがどうすればよいでしょうか。

class Circle:
    pi = 3.1416

    def __init__(self, diameter):
        self.diameter = diameter

    def get_circum(self):
        return pi * self.diameter #　この行がおかしいようです。

small_circle = Circle(5)
print(small_circle.get_circum()) #　うまく計算できない。

print("問題 3-2")
# 上のコードでpiとdiameterはどちらも変数ですが、それぞれ〇〇変数と言うでしょうか。 
# ヒント　インスタンスに属する変数なのか、クラスに属する変数ですべてのインスタンスが利用できる変数なのかで名前が決まっています。
# （授業では出てきていませんので考えたら、調べて正解だったか確認してもいいですね。）

#piがクラス変数
#diameterがインスタンス変数

print("OOP演習")
print("問題 1")

# これはカードのデッキを表すクラスのスタブです（リンク）。 前回と比較して、新しい関数 compareがあることに注意してください！
# DeckBaseを継承して、トランプカードのデッキを作るにはどうしたらよいでしょうか？
# DeckBaseを継承して、花札のデッキを作ることはできますか？
# - 麻雀セットはどうでしょうか？
# - カルタのセットはどうでしょうか？

from itertools import product
import random


class DeckBase():
    SUITS = []
    CARDS = ''
    
    def __init__(self):
        if not self.SUITS or not self.CARDS:
             raise AttributeError("Cannot create a deck, no CARDS or SUITS are defined")
        self.deck = list(product(self.SUITS, self.CARDS))
        self.used = []
        print(self.deck)


        
    def compare(self, card_a, card_b):
        """ Compares the value of card_a to card b, and returns True if card_a is a higher value than card b. """
        if card_a > card_b:
            return True
        else:
            return False
        
    def shuffle(self):
        """ Moved the used cards back to the deck and shuffles the deck. """
        self.deck = self.used + self.deck
        self.used = []
        random.shuffle(self.deck)
        print(self.deck)
        
    def deal(self, n=1):
        """ Deals n cards from the deck """
        
    def cut(self):
        """ Cuts the deck in a random location, placing the top half on the bottom """
        
    def count(self):
        """ Counts the deck, returning how many cards are left in the deck. """
        
    def count_used(self):
        """ Counts how many cards have been discarded from the deck. """
        
    def sort(self, order=None):
        """ Sorts the deck.  If order is provided, sort according to that order. """
        
    def peek(self, n=1):
        """ Peek n cards from the top of the deck, and return them in the same order. """


class Deck(DeckBase):
    # SUITS = ['heart', 'spade', 'club', 'diamond']
    # CARDS = 'A23456789TJQK'
    
    def __init__(self, SUITS, CARDS):
        self.SUITS = SUITS
        self.CARDS = CARDS
        super().__init__()

       
    def get_info(self):
        self.compare(self.deck[0], self.deck[3])
        print(self.deck[0])
        print(self.deck[3])
        print(self.compare(self.deck[0], self.deck[2]))
        
    def deal(self, n=1):
        i = 0
        while i < n:
            my_deck = random.choice(self.deck)
            i = i + 1
            self.used.append(my_deck)
            self.deck.remove(my_deck)
            print(my_deck)    
    
    def cut(self):
        # print(int(len(self.deck) / 2))
        # print(int(random.choice(len(self.deck))))
        print(random.randint(0,int(len(self.deck))))
        random_shuffle = self.deck[0:random.randint(0,int(len(self.deck)))]
        del self.deck[0:random.randint(0,int(len(self.deck)))]
        self.deck.extend(random_shuffle)
    
            
    def count(self):
        return len(self.deck)


    def count_used(self):
        return len(self.used)



    def sort(self, order=None):  # up_order, down_order
        # set order
        if   order == 'up_order':
            suits_order = {'spade': 0, 'heart': 1, 'diamond': 2, 'club': 3}
            cards_order = {'A': 0, '2': 1, '3': 2, '4':  3, '5':  4, '6':  5, '7': 6,
                           '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}
        elif order == 'down_order':
            suits_order = {'spade': 3, 'heart': 2, 'diamond': 1, 'club': 0}
            cards_order = {'A': 12, '2': 11, '3': 10, '4': 9, '5': 8, '6': 7,
                           '7':  6, '8':  5, '9':  4, 'T': 3, 'J': 2, 'Q': 1, 'K': 0}
        else:
            return
        # sorting
        self.deck = sorted(sorted(self.deck, key=lambda x: cards_order[x[1]]),
                                  key=lambda x: suits_order[x[0]])

    def peek(self, n=1):
        for i in range(n):
            print(random.choice(self.deck))

    
SUITS = ['heart', 'spade', 'club', 'diamond']
CARDS = 'A23456789TJQK'
test = Deck(SUITS, CARDS)
test.shuffle()
test.get_info()
test.deal(5)
print(test.count())
print(test.count_used())
# test.sort("up_order")
# print(test.deck)
# test.sort("down_order")
# print(test.deck)
# test.peek(4)
test.cut()
print(test.deck)

# class Comparing:
#     def __init__(self, card_a, card_b):
#         self.card_a= card_a
#         self.card_b= card_b
            
#     def compare(self):
#         for key in self:
#             if self.key[0] > self.key[1]:
#                 return True
    
           


# import itertools
# comb = itertools.combinations(self.deck, 2)
# list1 = list(comb)
# # print(len(list1))
# print(list1)

# cards= Comparing(random.self.deckcard1,card2)
# cards.compare()
  

#トランプ演習

# from itertools import product
# import random

# test_deck = Deck()
# test_deck.shuffle()  # シャッフル


# class Deck():
#     SUITS = ['heart', 'spade', 'club', 'diamond']
#     CARDS = 'A23456789TJQK'

#     def __init__(self):
#         self.deck = list(product(self.SUITS, self.CARDS))
#         self.used = []

#     def shuffle(self):
#         """ 使ったカードを戻してシャッフルする """
#         self.deck = self.used + self.deck
#         self.used = []
#         random.shuffle(self.deck)

#     def deal(self, n = 1):
#         """ カードの束からｎ枚のカードを配る """
#         i = 0
#         while i < n:
#             my_deck = random.choice(self.deck)
#             i = i + 1
#             self.used.append(my_deck)
#             self.deck.remove(my_deck)
#             print(my_deck)

#     def cut(self):
#         """ カードの束を任意で2つに分けて上半分を下に持ってくる """
#         # print(int(len(self.deck) / 2))
#         half_shuffle = self.deck[0:int(len(self.deck) / 2)]
#         del self.deck[0:int(len(self.deck) / 2)]
#         self.deck.extend(half_shuffle)

#     def count(self):
#         """ 束にどれだけカードが残っているかを数えて返り値として戻す """
#         return len(self.deck)

#     def count_used(self):
#         """ 束から何枚のカードが使われたかを数える """
#         return len(self.used)

#     def sort(self, order=None):  # up_order, down_order
#         """ 束をソートする。順番が示されたらそれに応じてソートする。 """
#         # set order
#         if   order == 'up_order':
#             suits_order = {'spade': 0, 'heart': 1, 'diamond': 2, 'club': 3}
#             cards_order = {'A': 0, '2': 1, '3': 2, '4':  3, '5':  4, '6':  5, '7': 6,
#                            '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}
#         elif order == 'down_order':
#             suits_order = {'spade': 3, 'heart': 2, 'diamond': 1, 'club': 0}
#             cards_order = {'A': 12, '2': 11, '3': 10, '4': 9, '5': 8, '6': 7,
#                            '7':  6, '8':  5, '9':  4, 'T': 3, 'J': 2, 'Q': 1, 'K': 0}
#         else:
#             return

#         # sorting
#         self.deck = sorted(sorted(self.deck, key=lambda x: cards_order[x[1]]),
#                                   key=lambda x: suits_order[x[0]])

#     def peek(self, n=1):
#         """ 束の上からｎ枚のカードをそっと見て元の順に戻す。 """
#         for i in range(n):
#             print(random.choice(self.deck))

# print("\n-----ex. 2-----")
# test_deck = Deck()
# test_deck.shuffle()  # シャッフル

# print("\n* 2枚引く")
# test_deck.deal(2)

# print("\n* 昇順")
# test_deck.sort("up_order")
# print(test_deck.deck)

# print("\n* 降順")
# test_deck.sort("down_order")
# print(test_deck.deck)

# print("\n* ランダムで3枚そっと見")
# test_deck.peek(3)
# print("\n* ちなみにもとの位置に戻してます")
# print(test_deck.deck)
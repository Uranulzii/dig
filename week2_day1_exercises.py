"""
演習- クラス -
1. JanKenクラスはあるゲームを表しています。 
クラスの中の関数はそれぞれどんなことをしていますか。
OPTIONSはクラス変数、それに対してself.winnerとself.turn
はインスタンス変数です。この二種類の違いは何だと思いますか。 
evaluateという関数を完成させ、JanKenゲームが機能するようにしてください。
"""

# import random




# def janken_function():
#     value = input("> Gu, Choki, or Pa?: ")
#     winner = False
#     # gu, choki, pa からランダムに選ばれた勝ち手と入力された値を比較する


#     if winner:
#         print("おめでとう！")
#     else:
#         print("残念でした！")


# janken_function()


# import random

# class JanKen():
#     OPTIONS = ['gu', 'choki', 'pa']

#     def __init__(self):
#         self.winner = False
#         self.turn = None

#     def read(self):
#         value = input("> Gu, Choki, or Pa?: ")
#         value = value.lower()
#         while value not in self.OPTIONS:
#             value = input("> もう一度 Gu, Choki, or Pa?: ")
#         self.turn = value


#     def evaluate(self):
#         # self.value = input("> Gu, Choki, or Pa?: ")
#         # self.value = self.value.lower()
#         # value = input("> Gu, Choki, or Pa?: ")
#         # value = value.lower()

#         if self.turn == "gu":
#             if random.choice(self.OPTIONS) == "choki":
#                 self.winner = True
#             else:
#                 self.winner = False

#         if self.turn == "choki":
#             if random.choice(self.OPTIONS) == "pa":
#                 self.winner = True
#             else:
#                 self.winner = False

#         if self.turn == "pa":
#             if random.choice(self.OPTIONS) == "gu":
#                 self.winner = True
#             else:
#                 self.winner = False

#         self.turn = None


#     def print(self):
#         if self.winner == True:
#             print('おめでとう！')
#         else:
#             print('残念でした！')


#     def loop(self):
#         while True:
#             self.read()
#             self.evaluate()
#             self.print()


#             next_game = input('> 続けますか？ [y/n]')
#             if next_game != 'y':
#                 print('お疲れまでした！')
#                 return


# if __name__ == '__main__':  # 以下の説明ご覧ください。
#     janken = JanKen()
#     janken.loop()
    
# 注：　if __name__ == '__main__': はこのPythonファイルがpython　ファイル名.pyと言うふうに実行されているかを判定します。 これがないと、モジュールがインポートされただけで関数が実行されてしまいます。 まだモジュールをやっていないので分からなくても全然問題ありません。 とにかく、コードが意図した通りに動くような一行なんだなくらいを思っておいてください。


"""
２．こちらのゲームはトランプカードの束を表すクラスの
スタブです。（注：スタブとは中身のないダミーのことを言います。）未実装の関数を実装してください。
"""

# from itertools import product
# import random


# class Deck():
#     SUITS = ['heart', 'spade', 'club', 'diamond']
#     CARDS = 'A23456789TJQK'

#     def __init__(self):
#         self.deck = list(product(SUITS, CARDS))
#         self.used = []

#     def shuffle(self):
#         """ 使ったカードを戻してシャッフルする """
#         self.deck = self.used + self.deck
#         self.used = []
#         random.shuffle(self.deck)

#     def deal(self, n=1):
#         """ カードの束からｎ枚のカードを配る """

#     def cut(self):
#         """ カードの束を任意で2つに分けて上半分を下に持ってくる """

#     def count(self):
#         """ 束にどれだけカードが残っているかを数えて返り値として戻す """

#     def count_used(self):
#         """ 束から何枚のカードが使われたかを数える """

#     def sort(self, order=None):
#         """ 束をソートする。順番が示されたらそれに応じてソートする。 """

#     def peek(self, n=1):
#         """ 束の上からｎ枚のカードをそっと見て元の順に戻す。 """

"""
３．ナイトメア問題 上の二問に出てきたDeckクラスとJanKenクラスを組み合わせてあなたのカードゲームを作ってみてください
"""




#shortcuts
""" 
ctr + shift +p = show commant palette
ctr + p = show quick open, go to file
ctr + x = cut line(empty selection)
ctr + c = copy line
alt + up or down button = move line up/down
shift + alt + up or down = copy line up/down
ctr + shift + K = delete line
home/end = go to beginning/end of license
ctr + home = go to file beginning
ctr + end = go to file end
shift + alt + A = toggle block comment """  """

navigation 
ctr + T = go to line #??
ctr + H = find and replace;

ctr + D = hensuu wo erabete can replace



"""




def simpleHello():
    print("Hello")

def anotherGreeting(name):
    return "Hello, " + name

foo = simpleHello()
bar = anotherGreeting("Python")

print(foo)
print(bar)













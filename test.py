  # 課題1
#  「describe_the_weather」という名前の関数を宣言してください。
#  それぞれの季節には、適切な温度があります。
#  Spring --> warm
#  Summer --> hot
#  Fall --> cool
#  Winter --> cold
#  もし与えられた温度が適切であれば、The temperature is normal for the season. を返してください。もしそうでなければ、The temperature is unusual for the season. を返してください。


#  ここにコードを書いてください


#  以下のテストコードが正常に動作するようにしてください。

# テストケース
def describe_the_weather(season,temp):
    # temp = input("What is the outside? ")
    # season = input("What season is it? ")
    
    if season == "spring" and temp =="warm":
        return "The temperature is normal for the season"
   
    elif season == "summer" and temp == "hot":
        return "The temperature is normal for the season"
    
    elif season == "fall" and temp == "cool":
        return "The temperature is normal for the season"
    
    elif season == "winter" and temp == "cold":
        return "The temperature is normal for the season"
       
    else: 
      return "The temperature is not normal"
      
print(describe_the_weather("spring", "warm"))

# => "The temperature is normal for the season."

# さらにテストを追加して、コードが正しいことを確認してください



# 課題2
# 「snoring_maker」という名前の関数をwhile loopを使い宣言してください。
# この関数は任意の数値を引き数として取り、返り値として任意の長さのリストを返します。
# 例えば、snoring_maker(5)と呼び出すと、関数は5回繰り返し、リストに"Z"を追加することで、["Z","Z","Z","Z","Z"]というリストを作成します。


# ここにコードを書きましょう

# def snoring_maker(times):
#     i = 0
#     n = ("")
#     while i < int(times):
#         n += "Z" * i
#         print (n)
#         i += 1
#     return times
# テストケース

def snoring_maker(times):
    i = 0
    n = []
    while i < int(times):
        n.append("Z")
        i += 1
    return n

print(snoring_maker(19))
    
# ["Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z","Z"]


# snoring_maker(9)
# ["Z","Z","Z","Z","Z","Z","Z","Z","Z"]


# さらにテストを書いて、コードが正しいことを確認してください



#ASSESSMENT問題の回答
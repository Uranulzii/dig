### 授業内演習 ###

def convert_cm_to_inch(cm):
    return (cm / 2.54)

# print(str(convert_cm_to_inch(float(input("type cm...: ")))) + " inch")


### 練習問題 ###

### ウォームアップ ###

# 1.
# 以下のコードを見てください。
# どうすれば films の 3 つめの要素を print できますか。??? を編集しましょう。

'''
films = ["Dracula", "Frankenstein", "The Mummy", "Babe"]

print(???) # "The Mummy" と表示させたい
'''

print("\n-----ex. 1-----")
films = ["Dracula", "Frankenstein", "The Mummy", "Babe"]
print(films[2])


# 2.
# days というリストは不完全です。
# 残りの曜日をリストの末尾に足すにはどうすればよいですか？

'''
days = ["Monday", "Tuesday", "Wednesday", "Thursday"]

# ここにコードを書いてください。

print(days) # これですべての曜日が表示されるようにしたい
'''

days = ["Monday", "Tuesday", "Wednesday", "Thursday"]

days.append("Friday")

print("\n-----ex. 2-----")
print(days)


# 3.
# 3 つの文字列を持つ moon というリスト があります。一番最後の要素を削除する方法は？

'''
moons = ["Deimos", "Phobos", "Howard"]

# ここにコードを書いてください。

print(moons) # これで ["Deimos", "Phobos"] と表示させたい
'''

print("\n-----ex. 3-----")
moons = ["Deimos", "Phobos", "Howard"]

moons.pop()

print(moons)


### 基礎演習 ###

# 以下の演習から、テスト関数を使用して実行しましょう。
# ファイルの冒頭に追加して使用してください。

def test(actual, expected):
    if actual == expected:
        print("Yay! Test PASSED.")
    else:
        print("Test FAILED. Keep trying!")
        print("    actual: ", actual)
        print("  expected: ", expected)


# 1.
# 関数 print_list を宣言してください。
# 引数に 1 つのリストをとり、リストの各要素を 1 行に 1 つずつ表示してください。

def print_list(numbers):
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

print("\n-----基礎. 1-----")

print_list([1, 2])
# 1
# 2

print("")
print_list([3, 4, 5])
# 3
# 4
# 5


# 2.
# print_every_other_list を宣言してください。
# 引数に 1 つのリストをとり、まずリストの最初の要素、
# 次は 3 つめというふうに 1 つおきの要素を表示させてください。

def print_every_other_list(numbers):
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 2

print("\n-----基礎. 2-----")

print_every_other_list([1, 2, 3])
# 1
# 3

print("")

print_every_other_list([3, 4, 5, 6, 7])
# 3
# 5
# 7


# 3.
# 関数 sum_list を宣言してください。
# 引数に渡されたリストを全て足した値を返してください。

def sum_list(numbers):
    i = 0
    result = 0
    while i < len(numbers):
        result = numbers[i] + result
        i += 1
    return result

print("\n-----基礎. 3-----")
test(sum_list([1, 2, 3, 4]), 10)
test(sum_list([5, 6, 7, 8]), 26)


# 4.
# 関数 multiply_list を宣言してください。
# 引数に渡されたリストを全て掛け合わせた値を返してください。

def multiply_list(numbers):
    i = 0
    result = 1
    while i < len(numbers):
        result = numbers[i] * result
        i += 1
    return result

print("\n-----基礎. 4-----")
test(multiply_list([1, 2, 3, 4]), 24)
test(multiply_list([5, 6, 7, 8]), 1680)


# 5.
# 関数 has_fun を宣言してください。
# 渡されたリストに fun が入っていたら True を返してください。

def hasFun(words):
    i = 0
    word = ""
    while i < len(words):
        word = words[i]
        i += 1
        if word == "fun":
            return True
    return False

print("\n-----基礎. 5-----")
test(hasFun(["whatever", 2, False, "fun", "hello"]), True)
test(hasFun(["whatever", 2, False, "run", "hello"]), False)


# 6.
# 関数 contains_only_booleans を宣言してください。
# 与えられたリストの要素がすべてブーリアンかどうかを表すブーリアンを返してください。

def contains_only_booleans(words):
    i = 0
    while i < len(words):
        if type(words[i]) == bool:
            i += 1
        else: 
            return False
    return True

    
print("\n-----基礎. 6-----")
test(contains_only_booleans([True, False, True, False, False]), True)
test(contains_only_booleans([True, True, True, "not a boolean"]), False)


# 問題7 関数 concatenate を宣言してください。与えられた2つのリストを連結させたリストを返してください。実装には while を使ってください。
# テストケース:

def concatenate(list1,list2):
    i=0
    sentence = list1
    while i < 2:
        list1.append(list2[i])
        i += 1
    return (list1)
        
        
    
print("\n-----基礎. 7-----")
test(concatenate(["a", "b"], ["c", "d"]), ["a", "b", "c", "d"])
test(concatenate(["hello", "world"], ["python", "list"]), ["hello", "world", "python", "list"])


# 問題8 関数 get_even_numbers を宣言してください。与えられたリストの中から偶数の要素だけを抜き出したリストを返してください。
# テストケース:

def get_even_numbers(numbers):
    i = 0
    even_numbers = []
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
            i += 1 
        else:
            i += 1 
    return even_numbers

            

print("\n-----基礎. 8-----")
test(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), [2, 4, 6, 8])
test(get_even_numbers([10, 11, 12, 13, 14, 15, 16, 17]), [10, 12, 14, 16])

# 問題9 関数 get_multiplied_list を宣言してください。与えられたリストの値に第二引数の数値をかけた結果の新しいリストを返してください。
# テストケース:

def get_multiplied_list(numbers, times):
    i = 0 
    multiplied = []
    while i < len(numbers):
        multiplied.append(numbers[i] * int(times))
        i += 1
    return multiplied
    

print("\n-----基礎. 9----")
test(get_multiplied_list([1, 2, 3], 6), [6, 12, 18])
test(get_multiplied_list([4, 5, 6], 2), [8, 10, 12])

# 問題10 最後の要素を表示する文を書いてください。特定のインデックスをハードコーディングしてはいけません。
# ハードコーディングとは例えばこういう書き方です。3 という数字を直接指定していますが、これでは index が 3 の要素しか取得できないので、リストの長さが変わってしまうと期待する結果になりません。

instructors = ["Mike", "Paul", "Bob", "Tom"]
print("\n-----基礎. 10----")
print (instructors[-1])

# instructors = ["Mike", "Paul", "Bob", "Tom"]
# print(instructors[3]) # Tom
# 今回はハードコーディングではなく、以下のようなコードを考えてください。
# print(''' どんな場合もリストの最後の要素が得られる式 ''')


# 問題11 ターミナルには、なんと表示されるでしょう。
numbers = [1, 2, 3]

print("\n-----基礎. 11----")
print(numbers[2]) # 3
print(numbers[0]) # 1
print(numbers[len(numbers) - 1]) # 3

# # 次で使用しているメソッドやプロパティについて、分からないときはドキュメントで調べてみましょう！

print(numbers.pop() + numbers.pop()) # 5

numbers[:0] = [4, 5, 6]
print(numbers) # [4, 5, 6、1]

print(numbers.pop(0)) # 4

print(len(numbers)) # 3

numbers.append(5)
numbers.append(6)

print(numbers.pop() * numbers.pop()) # 30
print(numbers[0]) # 5

# 問題12 リストはリストを要素として持つことができます。後日じっくり触れますが、いったんこの「リストの入れ子」に挑戦してみましょう。
# 次のコードはターミナルに何を表示させるでしょう。

numbers = [
  [0, 1, 2, 3],
  ["zero", "one", "two", "three"],
  ["rei", "ichi", "ni", "san"],
]
print("\n-----基礎. 12----")
print(numbers[2]) # ???
print(numbers[1][1]) # ???
print(numbers[0][2]) # ???
print(numbers[len(numbers)-1][0]) # ???
print(len(numbers[2])) # ???
print(numbers.pop()) # ???
print(numbers[0].append(4)) # ???
print(len(numbers)) # ???

# 問題１3 文字列はリストととてもよく似た挙動をします。次のコードがターミナルに何と表示させるでしょうか。


string = "hello"

print("\n-----基礎. 13----")
print(len(string)) # ???
print(string[0]) # ???
print(string[3]) # ???
print(string[len(string) - 1]) # ???

# 問題１4 関数 last を宣言してください。リストの最後の要素を返しましょう。

def last(names):
    name = names[-1]
    return name

print("\n-----基礎. 14----")
test(last(["Mike" ,"Paul", "Tom", "Bob"]), "Bob")

# 問題１5 ビルトインの append メソッドの代わりになる関数 append 関数を作ってみましょう！
# ビルトインの append メソッドを使ってはいけません。
# 関数の第２引数にリストに追加する値を渡し、処理後のリストの長さを返しましょう。

def append(list,word):
    length = len(list+[word])
    return length

print("\n-----基礎. 15----")
test(append([1, 2, 3, 4], 5), 5)

# # さらにテストを追加してみましょう。

# 問題１6 関数 number_of_people を宣言してください。リストの要素数を返してください。
# テストケース:

def number_of_people(list):
    number = len(list)
    return number

print("\n-----基礎. 16----")

test(number_of_people(["Mike" ,"Paul", "Tom", "Bob"]), 4)


"""中級演習
問題１ 関数 is_sorted を宣言してください。
与えられたリストが昇順に並んでいるかを表すブーリアン
を返してください。
テストケース:
"""
def is_sorted(numbers):
    i = 0 
    j = 1
    while i < len(numbers):
        num1 = numbers[i]
        num2 = numbers[j]
        i += 1
        j += 1
        if num1 < num2:
            return True
        else:
            return False


print("\n-----中級. 1----")    
test(is_sorted([1, 2, 3]), True)
test(is_sorted([3, 2, 3]), False)

"""
問題2 関数 count_occurrences を宣言してください。
第一引数のリストの要素に第二引数の値が出現する回数を
出力してください。
テストケース:
"""

def count_occurrences(things):
    i = 0
    num1 = ""
    num2 = ""
    while i < len(things):
        num1 += 

print("\n-----中級. 2----")  
test(count_occurrences([1, 2, 3], 2), 1)
test(count_occurrences([1, 2, 2], 2), 2)
test(count_occurrences([1, 2, "elephant"], "elephant"), 1)

"""
問題3 関数 reverse を宣言してください。ビルトイン・メソッドの 
reverse は使わないでください。与えられたリストの要素が逆の順番に
入っているリストを作成してください。
テストケース:
"""

list_to_reverse = ["eeny", "meeny", "miny", "moe"]
test(reverse(list_to_reverse), ["moe", "miny", "meeny", "eeny"])
test(list_to_reverse, ["eeny", "meeny", "miny", "moe"])


"""
問題4  関数 get_operated_list を宣言してください。
与えられたリストの各要素に、引数の算術演算子と被演算子を
適用した結果が入った新たなリストを作成してください。
テストケース:
"""

test(get_operated_list([1, 2, 3], "+", 5), [6, 7, 8])
test(get_operated_list([9, 6, 3], "/", 3), [3, 2, 1])


"""
問題5  関数 unshift を宣言してください。
与えらえた値を与えらえたリストの先頭に追加する関数です。
与えられたリストに第二引数の要素を追加してください。
返り値は処理が終わった後のリストの長さを返してください。
ビルトインのinsert()メソッドを使わないでください。
テストケース:
"""

my_list = [1, 2, 3, 4]

test(unshift(my_list, 5), 5) # 正しい結果を返すことを確認する
test(my_list, [5, 1, 2, 3, 4]) # 元のリストが変更されていることを確認する

"""
問題6  関数 shift を宣言してください。
shift は与えられた リスト の先頭の値を削除し、削除された値を返します。 
ビルトインの pop メソッドを使わないでください。
テストケース:
"""
my_list = [1, 2, 3, 4]

actual = shift(my_list)
expected = 1
test(actual, expected)

actual = my_list
expected = [2, 3, 4]
test(actual, expected) # 元のリストが変更されていることを確認する


"""応用演習
この演習では、講義で取り上げたことのないテクニックを使う必要があるかもしれません。
問題1 関数 hi_in_the_middle を宣言してください。
まず初めに、引数として受け取ったリストの要素数が奇数かどうかを確認します。
リストの長さが奇数なら、真ん中の要素が何であろうと "hi" に置換し、
リストの長さが偶数なら、何も変更せず、リストを返してください。
テストケース:
"""

test(hi_in_the_middle([1, 2, 3, 4, 5], [1, 2, "hi", 4, 5]))
test(hi_in_the_middle([1, 2, 3, 4]), [1, 2, 3, 4])

"""
問題2  関数 call_a_doctor を宣言してください。
単数形と複数形では名詞と動詞の関係が変化することに注意してください。
例えば My head hurts!
は動詞に s が必要ですが、 My shoulders hurt! には必要ありません。
テストケース:
"""

test(call_a_doctor(["head"]), "Doctor, doctor! My head hurts!")
test(call_a_doctor(["shoulders"]), "Doctor, doctor! My shoulders hurt!")
test(call_a_doctor(["head", "shoulders", "knees", "toes"]), "Doctor, doctor! My head, shoulders, knees, and toes hurt!")


"""
問題3  関数 deep_count を宣言してください。
テストケース:
"""

test(deep_count([1]), 1)
test(deep_count([1, 3]), 2)
test(deep_count([1, 3, [2, 4]]), 4)
test(deep_count(["a", "b", ["c", ["d", "e", ["f"]]]]), 6)

"""
問題4 len を使わないで、関数 number_of_people を書き直してください。
テストケース:
"""

"""
問題5  2 つのリストが互いに逆順かどうかをチェックする関数 are_reverses 
を宣言してください。are_reverseは引数に二つのリストを取り、
2 つのリストが互いに逆順かどうかを示すブール値を返します。
これを機に、リストは、どのようなビルトイン・メソッドが利用できるのか調べてみましょう。
この問題を解くのにぴったりなメソッドが見つかるかもしれませんよ😉
テストケース:
"""
 list_1 = [1, 2, 3, 4]
 list_2 = [4, 3, 2, 1]

 actual = are_reverses(list_1, list_2)
 expected = True

 test(actual, expected)

 actual = list_1
 expected = [1, 2, 3, 4]

 # 元のリストが変更されていないことを確認する
 test(actual, expected)

 
 """
問題6 与えられた関数を、
リストの各要素に対して一度ずつ実行する関数for_eachを宣言してください。
テストケース:
 """
for_each([1, 2, 3, 4], print)
# 1
# 2
# 3
# 4

"""
問題7 for_each を使用して、リストの各要素に 2 を掛けた数値を表示してください。
"""

 

"""
Nightmare問題
問題1 関数 flatten_deep を宣言してください。リストのリスト
（何段階も入れ子になっている場合もある）を引数として受け取り、
平坦化された、つまり、入れ子のないリスト（＝一次元リスト）を返しましょう。
テストケース:
"""

test(flatten_deep([1, 2, 3, [4, 5, 6]]), [1, 2, 3, 4, 5, 6])
test(flatten_deep([[1, 2, 3],[4, 5, 6],]), [1, 2, 3, 4, 5, 6])
test(flatten_deep([[1], [2], [3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])
test(flatten_deep([[1], [2], [3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])



"""
問題2 関数 sort を宣言してください。
数字のリストを引数に取り、与えられたリストの要素を昇順に並べた
新しいリストを返す関数です。
ビルトインの sort メソッドを使ってはいけません。
テストケース:
"""

list_to_sort = [5, 4, 3, 2, 1]
actual = sort(list_to_sort)
expected = [1, 2, 3, 4, 5]

test(actual, expected) # 正しい結果を返すことを確認する
test(list_to_sort, [5, 4, 3, 2, 1]) # 元のリストが変更されていないことを確認する
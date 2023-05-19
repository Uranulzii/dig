#exercise of list (making list and adding sth to the list)
# a = [1,2,3]
# b = list(a)
# b(4)
# print(a)
# print(b)

#exercise to see the function of list function
print(list("Hello!"))

#exercise of range
numbers = range(1,10)
number_list = list(numbers)
print(number_list)

#exercise of range
numbers = range(10,-1,-1)
print(list(numbers))

print(list(":)"))

print(list(range(500,0,-100)))

print(list(range(0,7)))


#exercise of for and in loop

def count_to_ten():
    i = 1
    while i < 11:
        print(i)
        i += 1
        
count_to_ten()

def count_too_ten():
    for i in range(1,11):
        print(i)

count_too_ten()

def sum_list(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total 

print(sum_list([2,3,4]))

def sum_list(nums):
    total = 0
    for i in range(0,len(nums)):
        total += nums[i]
    return total

# print("sum")
# print(sum_list([2,3,4]))      

def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

print("sum")
print(sum_list([2,3,4]))  

def happy_new_year():
    t = 60
    while t > 0:
        print(t)
        t -= 1
    print("Happy New Year!")

happy_new_year()

def happy_new_year_1():
    for i in range(60,0,-1):
        print(i)
    print("Happy New Year!")
    
happy_new_year_1()

print("文字列をループ処理する。")

def spell(word):
    i = 0 
    while i < len(word):
        print(word[i])
        i += 1
    print("これが" + word + "のスペルです！")

spell("word")

def spell(word):
    for i in range(0,len(word)):
        print(word[i])
    print("これが" + word + "のスペルです！")

spell("Urnaa")       

def spell(word):
    for char in word:
        print(char)
    print("これが" + word + "のスペルです！")

spell("Justin")

#break's exercise
for i in range(1,11):
    if i == 6:
        break
    print(i)


#exercise of dictionary

#kisoenshuu
#mondai 1
def count_each_letter(word):
    letter_counts = {}
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1 
    return letter_counts

print(count_each_letter("humhumunukunukuapua'a"))

#dictionary class memo キーを使って値にアクセスできます。

#mondai 2
# 複数の文字列を含む 1 つのリストを引数にとり、重複する文字列は
# 1 つだけ残して余分な文字列を取り除いたリストを新しく作って返す関数 remove_repeats を書いてください。

def remove_repeats(word):
    letter_counts = {}
    X = []
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1 
    for key in letter_counts:
        X += key   
    return X
    
print(remove_repeats(["a", "b", "c", "b", "a", "d"])) # ["a", "b", "c", "d"]

# 問題 3
# 文字列を 1 つ引数にとり、各母音（a, e, i, o, u）の出現回数をディクショナリに記録する関数 count_vowels を書いてください。

def count_vowels(words):
    letter_counts = {}
    letter = {'a','e','i','o','u'}
    for letter in words:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1 
    return letter_counts
    
print(count_vowels("digging for apples"))

# 以下のような返り値が得られるようにしたい。
# {"i": 2, "o": 1, "a": 1, "e": 1}
    


import requests
# r = requests.get('https://toyota.jp/')
# print(r.text)


# class Pokemon:
#     def __init__(self, id):
#         response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
#         self.response = response.json()
#         self.name = self.response['species']['name']
#         self.abilities = self.response['abilities']
#         self.weight = self.response['weight']
#         self.height = self.response['height']
    
#     def get_pokemon_hp(self):
#         for stat in self.response['stats']:
#             if stat in self.response['stats']:
#                 hp = stat['base_stat']
#                 return hp
            
        
# p = Pokemon(1)
# print(p.get_pokemon_hp())
# print(p.name)
# print(p.weight)
# print(p.height)


#exercises
# 演習 Requests


# Requests を使ってインターネットから様々なものをダウンロードし、コンソールで見てみましょう。
# o = requests.get('https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A8%E3%82%BF%E8%87%AA%E5%8B%95%E8%BB%8A')
# print(o.text)


# Web ページをリクエストし、ステータスコードをチェックし、選択した wikipedia の記事から応答テキストを表示する python 関数を書きましょう。
# print(o.status_code)

# Web ページを要求する python 関数を書きなさい。 `r.encoding`は何をするものだと思いますか？
# print(o.encoding)

# これはコンピュータプログラミングに関する wikipedia の画像の URL です。



# from PIL import Image
# import requests
# from io import BytesIO

# response = requests.get('https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/2/25/Concepts-_Program_vs._Process_vs._Thread.jpg&sa=D&source=editors&ust=1684464334870863&usg=AOvVaw20RwmHzTQjNztmwb8kG8wj')
# img = Image.open(BytesIO(response.content))
# print(img)
# print(type(BytesIO(response.content)))


# import urllib.request

# from PIL import Image


# urllib.request.urlretrieve('https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/2/25/Concepts-_Program_vs._Process_vs._Thread.jpg&sa=D&source=editors&ust=1684464334870863&usg=AOvVaw20RwmHzTQjNztmwb8kG8wj', file)

# img = Image.open(file)

# img.show()


# importing modules
# import urllib.request
# from PIL import Image
  
# urllib.request.urlretrieve(
#   'https://upload.wikimedia.org/wikipedia/commons/2/25/Concepts-_Program_vs._Process_vs._Thread.jpg',
#    "gfg.png")
  
# img = Image.open("gfg.png")
# img.show()

# ※google documentからアクセスするとリダイレクト画面が出てくるけど気にしないでね！
# このコンテンツを取得する関数を書きましょう。
# 何が見えますか？
# なぜこれが見えると思いますか？



# Requestsのクイックスタートドキュメントを読んでください。
# ドキュメントの「Timeouts」のセクションを試してみてください。
# なぜ「すべてのプロダクションコードは、ほぼすべてのリクエストでこのパラメータを使用すべきである」ことが重要なのでしょうか？
# スライドではgetというHTTPのメソッドが使われています。それ以外にrequestsがサポートしている HTTP Methods はどんなものがあるか調べてみましょう。 それらのメソッドは何をするのですか？
# 「認証（Authentication）」のセクションを読んでください。 なぜ、ログインを必要とする情報を取得するのが難しいのでしょうか？

# requests.get('https://github.com/', timeout=1)



#午後のクラス


# file = open("filename.txt", "r", encoding='UTF'8) #rはreadのr,読み込み用, aは追記,appendのa, ファイルない場合は新規作成, wは書き込みwrite, xはexclusive creation指定されたファイルを作成します、bはbinaryモード

# data =  file.read()   #()の中に数字を入れるとその数字の文字を示してくれる。
# print(data)

# file.close()で閉じられるが with ..... as fileで閉じることが多い。

# with open("filename.txt", "r") as file:
#     print(file.read())
    


# with open("filename.txt", "w") as file: #これで元のファイルのHello worldがhiiiiに変わった
#     file.write("hiiiii")

    
# with open("filename.txt", "a") as file: #これで元のファイルのHello worldがhiiiiに変わった
#     file.write(" ellooo")


# import os 
# os.rename("filename.txt", "file.txt") nameをrenameする。

# os.remove("file.txt") file wo delete suru.

#file I/Oの演習in the 午後

# 問題１


# こちらのURLにアクセスし、以下のコードを実行してください：


# import requests


# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# res.raise_for_status()

# with open('RomeoAndJuliet.txt', 'wb') as play:

#     for chunk in res.iter_content(100000):

#         play.write(chunk)



# 質問

# RomeoAndJuliet.txtのコンテンツは何でしょうか？ Ebook of Romea and Juliet
# for chunk in res.iter_content は何をしたのでしょうか？ ちょっとずつデータを移すため
# wb は何をしているのでしょうか？ binary dataで書き込みをする。



# 問題2 


# 次のコードを実行してみてください：


# import csv


# pkmn = [

#     {'id': 1, 'type': 'grass/poison', 'name': 'bulbasaur'},

#     {'id': 2, 'type': 'grass/poison', 'name': 'ivysaur'},

#     {'id': 3, 'type': 'grass/poison', 'name': 'venusaur'}

# ]


# with open('pokemon.csv', 'w', newline='') as csvfile:

#     pkmn_writer = csv.DictWriter(csvfile, fieldnames=pkmn[0].keys())

#     pkmn_writer.writeheader()

#     for pokemon in pkmn:

#         pkmn_writer.writerow(pokemon)


# 質問

# pokemon.csvの出力を調べてみてください。何が見えますか？　csvコンマ区切りでid,type,nameが列名になっている。、が一つのセルの意味in excel
# csvファイルをエクセルにインポートすると、何が起こりますか？ セルに入っている。
# csvファイルをgoogle sheet（またはexcel）にインポートすると、どうなりますか？



# 問題3 


# 最初の151匹のポケモンの情報をダウンロードし、そのデータをCSVに保存するpythonプログラムを書いみましょう。CSVにはid、type、nameのフィールドがあるはずです。 ポケモンが複数のタイプに属している場合は、タイプ名をスラッシュでつなげてください。（例 : type_a/type_b)


# import requests


# res = requests.get('https://pokeapi.co/api/v2/pokemon/')

# res.raise_for_status()

# with open('Pokemon_names.txt', 'wb') as play:

#     for chunk in res.iter_content(100000):

#         play.write(chunk)






class Pokemon:
    def __init__(self, id):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon-form/{id}')
        self.response = response.json()
        self.name = self.response['name']
        self.types = self.response['types']
        self.type_name = ""
        for i in self.types:
            # print(i['type']['name'])
            temporary = i['type']['name']
            if self.type_name != "":
                self.type_name += "/" + temporary
            else:
                self.type_name = temporary
        # print(self.type_name)
    
pkmn = []
for id in range(1,152):
    output = {}
    p = Pokemon(id)
    # print(p)
    output["id"] = id
    output["type"] = p.type_name
    output["name"] = p.name
    pkmn.append(output)
    
    # print(output)
    

import csv

with open('pokemon_data.csv', 'w', newline='') as csvfile:

    pkmn_writer = csv.DictWriter(csvfile, fieldnames=pkmn[0].keys())

    pkmn_writer.writeheader()

    for pokemon in pkmn:

        pkmn_writer.writerow(pokemon)
        
     
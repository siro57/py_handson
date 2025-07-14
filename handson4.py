#1九九（1×1～9×9）の表を作るプログラムをfor文とwhile文の2パターン作成せよ。式と答えも表示せよ。
for i in range(1,10):
    for j in range(1,10):
        kake = i * j
        print(f"{i}×{j}={kake}")

x = 1
while x <= 9:
    y = 1
    while y <= 9:
        kakezan = x * y
        print(f"{x}×{y}={kakezan}")
        y += 1
    x += 1 

#2ユーザーから数字を1つ受取り、「*」を使って正方形を下記（「5」を受取った場合）のように画面に表示するプログラムを作成せよ。 

h = int(input("数字を入力して下さい"))

# 1行目
for i in range(h):
    print("*", end="")
print()

# 受取った値が1でない場合（1の場合は1行目のみの表示）
if h != 1:
    # 2～最終行前
    for i in range(2, h):
        print("*", end="")
        for j in range(2, h):
            print(" ", end="")
        print("*")
    # 最終行
    for i in range(h):
        print("*", end="")
    print() 

#3フィボナッチ数列を10000まで出力するプログラムを作成せよ
a = 0
b = 1
while a < 10000:
    print(a, end=' ')
    tmp = a #aがtmpに格納
    a = b #bがaに格納
    b = tmp + b #aとtmpの和(つまりa+b)がbに格納. つまりaが一時退避することで最終的にb+(a+b)ができる。つまり1番目と2番目の和が3番目になるという処理が続く。処理は1つずつ右にずれていく。
print()


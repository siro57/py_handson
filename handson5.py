#1 ユーザーから2つの正の整数値を受取り、両方とも素数であるか判定するプログラムを作成せよ。
# 素数である場合はTrue、素数でない場合はFalseと出力すること。
a = int(input("数字を入力してください:"))
b = int(input("数字を入力してください:"))

if 1 < a and 1 < b:
    for i in range(2, a+1):
        for j in range(2, (i//2)+1):
            if i % j == 0:
                print("false")
            else:   
                for x in range(2,b+1):
                    for y in range (2, (x//2)+1):
                        if x % y == 0:
                            print("false")
                        else:
                            print("True")     
else:
    print("素数ではない")

#2バブルソートを作成せよ。
#リストの長さが１以下
def bubble_sort(data):
    if len(data) <= 1:
#リストを返す
        return data
#（外側ループ）リストの長さ−１の間をループする変数i(隣同士の要素を比較する回数を表す。range(4)はiが0~4であることを表す。
#要素が5個なら隣同士の要素の比較が4回行われる。0と1,1と2,2と3,3と4)
    for i in range(len(data)-1):
#（内側ループ）リストのキーを表す変数j。jの移動範囲はiが大きくなるにつれ狭くなる。
#(要素数5で0回目のループの時、jは0~3までの値を取るので要素比較が4回行われる。最後の3回目のループの時は、jは0なので比較は0と1の1回のみ。)
        for j in range(len(data)-i -1):
#もしリストのキーjに対応する値が右隣の値よりも大きければ
            if data[j] > data[j+1]:
#リスト内の値を入れ替える(大きい値が右に移動する)
               data[j], data[j+1] = data[j+1], data[j]
#リストを返す（）
    return data
#リストを渡す
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
#リストのコピーに関数を適用させ、sorted_dataに格納する
sorted_data = bubble_sort(data.copy()) #copyメソッドは後ろに()が必要
#元リストとソート後のデータを並べて表示
print(f"{data} => {sorted_data}")

#3マージソートを作成せよ。
def merge_sort(data):
    if len(data) <= 1:#データが1以下の場合を除外
        return data
    # データを分割
    center_idx = len(data) // 2#２であまりの内容に割る
    left_data = data[:center_idx]
    right_data = data[center_idx:]
    # 分割したリストを渡して再帰的に関数を実行
    merge_sort(left_data)
    merge_sort(right_data)

    left_idx = right_idx = idx = 0#リストの要素が最小化されている
    # 分割したリストの左側リスト、右側リストの全要素を比較＆並べ替え
    while left_idx < len(left_data) and right_idx < len(right_data):
        if left_data[left_idx] <= right_data[right_idx]:
            data[idx] = left_data[left_idx]
            left_idx += 1
        else:
            data[idx] = right_data[right_idx]
            right_idx += 1
        idx += 1

    # 右側リストの要素が残っていればそれをすべて代入
    while right_idx < len(right_data):
        data[idx] = right_data[right_idx]
        idx += 1
        right_idx += 1

    # 左側リストの要素が残っていればそれをすべて代入      
    while left_idx < len(left_data):
        data[idx] = left_data[left_idx]
        idx += 1
        left_idx += 1

    return data

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
sorted_data = merge_sort(data.copy())

print(f"{data} => {sorted_data}")
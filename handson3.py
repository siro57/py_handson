#1ユーザーから10回数字を受取り、「前回と同じ数を入力した回数」を出力、10回連続したらperfectと返すプログラムを作成せよ。
previous_num = ""
same_as_previous = 0
consecutive_count = 0
for i in range (10):
    num = input("数字を入力してください:")
    if num == previous_num:
        consecutive_count += 1
        same_as_previous += 1
        print(f"前回と同じ数を{consecutive_count}回入力しています")
        if consecutive_count ==9:
            print("perfect!10回連続入力しました")
                
    else:
        consecutive_count = 0    
    previous_num = num

#2入力したn桁の数の中に5があるか調べるプログラムを作成せよ。
numbers = input("数字を入力してください:")

numbers_devided = numbers.split()
numbers_devided = numbers.strip(",")
count = 0
for number in numbers:
    if "5" in number:
        count += 1
        print("5です")
    else:
        print("5じゃないです")        
print(f"5は{count}回入力されました")


calculate_number = list(map(int,input("数字を2つ入力してください:")))
a = calculate_number[0]
b = calculate_number[1]
tasu = a + b
hiku = a - b

#3ユーザーから数字を2つ受取り、2つの数字の足し算と引き算の結果を出力するプログラムを作成せよ。
print(f"足し算の合計は{tasu}です。引き算の合計は{hiku}です。")
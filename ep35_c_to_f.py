c = input('請輸入攝氏溫度: ')
c = float(c) #這一行式型別轉換，把c這個變數轉換成浮點數 --- PS：可以用整數(int)或浮點數(float)
f = c * 9 / 5 + 32
print('華式溫度為: ', f)
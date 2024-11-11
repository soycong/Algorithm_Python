buget = int(input())
moneyChart = list(map(int, input().split()))

increase_Count = 0
decrease_Count = 0


buget_Joon = buget
stockNum_Joon = 0

buget_Seong = buget
stockNum_Seong = 0

for i in range(0, len(moneyChart)):
    stockNum_Joon += buget_Joon // moneyChart[i]
    buget_Joon %= moneyChart[i]

for i in range(1, len(moneyChart)-2):
    #성민 3일 연속 상승 OR 하락

    #3일 연속 상승 -> 매도
    if moneyChart[i-1] < moneyChart[i] < moneyChart[i+1] < moneyChart[i+2]:
        buget_Seong += stockNum_Seong * moneyChart[i+2]
        stockNum_Seong = 0

    #3일 연속 하락 -> 매수
    if moneyChart[i-1] > moneyChart[i] > moneyChart[i+1] > moneyChart[i+2]:
        stockNum_Seong += buget_Seong // moneyChart[i+2]
        buget_Seong %= moneyChart[i+1]


#틀린 답변
'''
buget_Joon = buget % moneyChart[0]
stockNum_Joon = buget // moneyChart[0]

buget_Seong = buget
stockNum_Seong = 0

for i in range(1,len(moneyChart)):
    stockNum_Joon+= buget_Joon // moneyChart[i]
    buget_Joon %= moneyChart[i]

    #성민 3일 연속 상승 OR 하락
    if moneyChart[i-1] < moneyChart[i]:
        increase_Count+=1

        if increase_Count == 3:
            increase_Count = 0
            decrease_Count = 0
            stockNum_Seong += buget_Seong // moneyChart[i]
            buget_Seong %= moneyChart[i]

    elif moneyChart[i-1] > moneyChart[i]:
        decrease_Count+=1

        if decrease_Count == 3:
            increase_Count = 0
            decrease_Count = 0
            buget_Seong += stockNum_Seong * moneyChart[i]
            stockNum_Seong = 0
'''

total_Joon = buget_Joon + (moneyChart[-1] * stockNum_Joon)
total_Seong = buget_Seong + (moneyChart[-1] * stockNum_Seong)

if total_Joon > total_Seong: print("BNP")
elif total_Joon < total_Seong: print("TIMING")
else: print("SAMESAME")
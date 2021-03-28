#거스름돈 입력받기
n = int(input()) 

count = 0

#큰 단위 화폐부터 나열한다
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

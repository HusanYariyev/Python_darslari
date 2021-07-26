son = int(input("Sonni kiriting: "))

sanoq = 1
while True:
    son = son // 10
    if son !=0:
        sanoq +=1
    else:
        break

print(f"Kiritgan soningiz {sanoq} xonali")

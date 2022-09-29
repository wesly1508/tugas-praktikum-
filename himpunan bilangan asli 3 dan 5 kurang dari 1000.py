x = 0 
jumlah = 0
while x < 1000 :
    if x%3 == 0 or x%5 == 0:
        jumlah = jumlah + x
        print(x)
    x += 1
print(jumlah)
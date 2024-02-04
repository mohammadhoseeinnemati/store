
print("welcome to the store")
print("t_shirt , pants , hat , hoodie , shoe ")

###################
print("first day sale")
import random

store1 =input("what was your first sale today?")
print("how many sold:")
rnd1 = random.randint(0,10)
print(rnd1)

store2 = input("what products were sold after the first sale?")
print("how many sold:")
rnd2 = random.randint(0,10)
print(rnd2)

store3 = input("what goods did you sell in the afternoon?")
print("how many sold:")
rnd3 = random.randint(0,10)
print(rnd3)

store4 = input("what items were sold at night?")
print("how many sold:")
rnd4 = random.randint(0,10)
print(rnd4)

store5 = input("what was your last sale?")
print("how many sold:")
rnd5 = random.randint(0,10)
print(rnd5)

day_1 = rnd1 + rnd2 + rnd3 + rnd4 + rnd5

print(f" on the first day {day_1} you sold")


###################

print("second day sales") 

store_1 = input("what was your first sale on the second day?")
print("how many sold:")
rnd_1 = random.randint(0,10)
print(rnd_1)

store_2 = input("what products were sold after the first sale?")
print("how many sold:")
rnd_2 = random.randint(0,10)
print(rnd_2)

store_3 = input("what goods did you sell in the afternoon?")
print("how many sold:")
rnd_3 = random.randint(0,10)
print(rnd_3)

store_4 = input("what items were sold at night?")
print("how many sold:")
rnd_4 = random.randint(0,10)
print(rnd_4)

store_5 = input("what was your last sale?")
print("how many sold:")
rnd_5 = random.randint(0,10)
print(rnd_5)

day_2 = rnd_1 + rnd_2 + rnd_3 + rnd_4 + rnd_5

print(f" on the second day {day_2} you sold")



########################

print("third day sales")

storee1 = input("what product was sold on the third day?")
print("how many sold:")
rndd1 = random.randint(0,10)
print(rndd1)

storee2 = input("what products were sold after the first sale?")
print("how many sold:")
rndd2 = random.randint(0,10)
print(rndd2)

storee3 = input("what goods did you sell in the afternoon?")
print("how many sold:")
rndd3 = random.randint(0,10)
print(rndd3)

storee4 = input("what items were sold at night?")
print("how many sold:")
rndd4 = random.randint(0,10)
print(rndd4)

storee5 = input("what was your last sale?")
print("how many sold:")
rndd5 = random.randint(0,10)
print(rndd5)

day_3 = rndd1 + rndd2 + rndd3 + rndd4 + rndd5

print(f" on the third day {day_3} you sold")

#############################

if day_1 > day_2 > day_3:
    print (" the first day had the highest sales")
elif day_2 > day_1 > day_3:
    print ("the second day had the highest sales")
elif day_3 > day_2 > day_1:
    print("the third day had the highest sales")

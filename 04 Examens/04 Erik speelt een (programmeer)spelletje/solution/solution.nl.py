def veelvoud3(getal):
   return getal % 3 == 0

def veelvoud5(getal):
   return getal % 5 == 0

start = int(input("Vul een startgetal in: "))
eind = int(input("Vul een eindgetal in: "))

for i in range(start, eind + 1):
   if veelvoud3(i) and veelvoud5(i):
      print("FIZZBUZZ")
   elif veelvoud3(i):
      print("FIZZ")
   elif veelvoud5(i):
      print("BUZZ")
   else:
      print(i)
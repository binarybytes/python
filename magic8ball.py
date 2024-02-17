import random


a = "Yes - definitely"
b = "It is decidedly so"
c = "Without a doubt"
d = "Reply hazy, try again"
e = "Ask again later"
f = "Better not tell you now"
g = "My sources say no"
h = "Outlook not so good"
i = "Very doubtful"

name = "Bum "
question = "Is this real life? "
answer = ""
random_number = random.randint(1,9)
print(name + "asks: " + question)

if random_number == 1:
  print(a)
elif random_number == 2:
    print(b)
elif random_number == 3:
      print(c)
elif random_number == 4:
        print(d)
elif random_number == 5:
          print(e)
elif random_number == 6:
            print(f)
elif random_number == 7:
              print(g)
elif random_number == 8:
                print(h)
elif random_number == 9:
                  print(i)
else:
  print("Error")       


import random


a = "Magic 8-Ball's answer: Yes - definitely"
b = "Magic 8-Ball's answer: It is decidedly so"
c = "Magic 8-Ball's answer: Without a doubt"
d = "Magic 8-Ball's answer: Reply hazy, try again"
e = "Magic 8-Ball's answer: Ask again later"
f = "Magic 8-Ball's answer: Better not tell you now"
g = "Magic 8-Ball's answer: My sources say no"
h = "Magic 8-Ball's answer: Outlook not so good"
i = "Magic 8-Ball's answer: Very doubtful"

name = input("What is your name? \n")
question = input("What would you like to ask my magic 8 ball? \n")
answer = ""
random_number = random.randint(1,9)

if name == "":
 print(question)
else:
 print(name + " asks: " + question)
if question == "":
	print(name + " said nothing. please play again.")

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

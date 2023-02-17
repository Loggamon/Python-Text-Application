firstName = ""
lastName = ""
fullName = "(omitted)"
favColor = ""
age = ""
breakLine = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'

print(breakLine)
print('  //  TTTTTTTT  EEEEEEEE  XX    XX  TTTTTTTT  \\\  ')
print(' //      TT     EE         XX  XX      TT      \\\ ')
print('||       TT     EEEE        XXXX       TT       ||')
print(' \\\      TT     EE         XX  XX      TT      // ')
print('  \\\     TT     EEEEEEEE  XX    XX     TT     //  ')
print(breakLine)

print('Hello!')
print('')
print('Welcome to the Text Application. In this exercise I will be asking you some questions.')
input("Let's begin! (press 'enter' to start)")

print('')

nameAsk = input ('Can I ask for your name?').lower()
if nameAsk in ['yes', 'y']:
    firstName = input ('What is your first name? ')
    lastName = input ('And what is your last name? ')
    fullName = firstName + " " + lastName
else:
    print('Okay!')

favColor = input ('Which color out of these do you prefer? (Red / Orange / Yellow / Green / Blue / Black): ').lower()
age = int(input ('Lastly, how old are you? '))

print(breakLine)
print(fullName)
print(favColor)
print(age)
print(breakLine)

input ("\n\n Let's plug these values in.")

print(breakLine)

if fullName == "":
    print("Out of privacy, we didn't catalogue a name.")
else:
    print(f"Hello {fullName}, it's nice to meet you!")

print('')

print(f"I see your favorite color is {favColor} ...")
if favColor == 'red':
    print("like licorice. Yummy!")
elif favColor == 'orange':
    print("like a tiger. Rawr!")
elif favColor == 'yellow':
    print("Like sunflowers. So Pretty!")
elif favColor == 'green':
    print("Like leaves. I love nature!")
elif favColor == 'blue':
    print("like the ocean. Let's go sailing!")
elif favColor == 'black':
    print("like the night sky. I'm getting sleepy...")
else:
    print(f"Sorry, I don't know what color {favColor} is!")

print('')

if age < 16:
    print("Looks like you're still too young to drive.")
if age >= 16 and age < 21:
    print("Looks like you are too young to drink.")
if age > 21:
    print("You are a legal adult!")

print(breakLine)

input ("This is the end!")



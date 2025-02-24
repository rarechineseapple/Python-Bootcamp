from time import sleep
print("Welcome to the awesome Superhero Name Generator!")
firstname = input("To begin, let's start with your first name! ")
secondname = input("Nice name! Now give me your second name! ")

#for fun below
loading = 'LOADING...'
for i in range(10):
    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.5)
#fun over

print("\nHello Superhero " + firstname + secondname + "!")
#Using String formatting to concatenate the string -> f"\nHello Superhero {firstname}{secondname}!"
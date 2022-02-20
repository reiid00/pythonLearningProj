import random

#My vers
def guess(x):
	random_number=random.randint(1,x)
	user_number=int(input("Take a guess "))
	while user_number!=random_number:
		if user_number<random_number :
			print("WRONG! Below random number. Guess again")
		elif user_number>random_number :
			print("WRONG! Above random number. Guess again")
		user_number=int(input("Take another guess! "))
	print("CORRECT!")

# Youtube vers
def guess2(x):
	random_number=random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess=int(input(f"Guess a number between 1 and {x} "))
		if guess<random_number:
			print("Sorry, guess again, too low.")
		elif guess>random_number:
			print("Sorry,guess again, too high.")
	print(f"Yay, congrats. You have guessed the number {guess} ")

def computer_guess(x,y):
	low=x
	high=y
	feedback=''
	while feedback!='c':
		guess=random.randint(low,high)
		feedback=input(f"Is{guess} too high (H), too low(L), or correct(C)?").lower()
		if feedback=='h':
			high = guess-1
		elif feedback=='l':
			low = guess+1
	print("The computer guessed the number ",guess," correctly")


# num=int(input("Random numbers:"))
# guess(num)
# guess2(num)

x=int(input("LOW:"))
y=int(input("HIGH:"))
computer_guess(x,y)




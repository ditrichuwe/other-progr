##print("hello")
##name="Nikita"
##print("hello"+name)
##user_name=input("what is your name")
##print("hello"+user_name)
import random 


print("Let's play a game.Guess a number. Picka Number from one to ten")
secret_number=random.randint(1,10)


while True:
    user_number=input("say the number ")
    user_number=int(user_number)
    if secret_number>user_number:
        print("secret number is bigger")

    if secret_number<user_number:
        print("secret number is smaller")
    if secret_number==user_number:
        print("correct")
        break

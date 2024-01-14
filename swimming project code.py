print("Let's play a quiz.")
secret_answer=("australia")


while True:
    user_answer=input("Where were the first swimming championships?")
    user_answer=int(user_answer)
    if secret_answer is not user_answer:
        print("incorrect")

    if secret_answer is user_answer:
        print("correct")
        
        break


    print("Question 2.")
secret_answer=("David Popovici")
while True:
    user_answer=input("who holds the world record on 100m freestyle(long course)?")
    user_answer=int(user_answer)
    if secret_answer is not user_answer:
        print("incorrect")

    if secret_answer is user_answer:
        print("correct")
        
        break

print("Question 3.")
secret_answer=("Caeleb Dressel")
while True:
    user_answer=input("who holds the world record on 100m butterfly(long course)?")
    user_answer=int(user_answer)
    if secret_answer is not user_answer:
        print("incorrect")

    if secret_answer is user_answer:
        print("correct")
        
        break


print("Question 4.")
secret_answer=("USA")
while True:
    user_answer=input("what land holds the world record on 4 × 200 m freestyle relay(long course)?")
    user_answer=int(user_answer)
    if secret_answer is not user_answer:
        print("incorrect")

    if secret_answer is user_answer:
        print("correct")
        break

print("Question 5.")
secret_answer=("23")
while True:
    user_answer=input("how many olimpic gold medals micheal phelps has?")
    user_answer=int(user_answer)
    if secret_answer is not user_answer:
        print("incorrect")

    if secret_answer is user_answer:
        print("correct")

        break

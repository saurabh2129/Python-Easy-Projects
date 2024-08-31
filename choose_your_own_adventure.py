name = input("Enter your name please! : ")
print(f"Welcome {name} to this adventure! \n Here we are gonna see what we should do if we missed our lecture :) ")

print("So now I'm gonna ask you some question and i will provide you some options... umm hmm i know you are confused!")

answer = input("\n Supposed we missed today's lecture and we are standing in front of our class! now where should we go (left/right): ").lower()

if answer == 'left':
    food = input("Good decission umm hmm now you have two choices (kachori/paratha):").lower()
    if food == 'kachori':
        food_1 = input("Swad to hai bohot chal ab bata or kya hona (chai/coffee): ").lower()
        if food_1 == 'chai':
            print("I know your fav spot LOC chal phir chalte hai... (you win buddy)")
        elif food_1 == 'coffee':
            print("Bohot paise hai tere pr mera bhi dede paise tu hi (you lose try again)")
        else:
            print("Invalid input pls read above instruction properly and try next time...")
    elif food == 'paratha':
        print("seriously tu kachori ke aage paratha liya oh man! (you lose try again)")
    else:
        print("Invalid input pls read above instruction properly and try next time...")

elif answer == 'right':
    print("waise mai bata du choice achi nhi thi magar wait mai kuch intresting karta hu...")
    extra = input("preet ki kahani (p) yeah kahi ghumne chalna hai (g) bracket wale word ko type karo").lower()
    if extra == 'p':
        print(f'Raha nhi jata na {name} tadap hi aise hai')
    elif extra == 'g':
        print(f'{name} mtlb tu preet ki kahani nhi ghumna pasand karega/karegi (you lose try again)')
    else:
        print("Invalid input pls read above instruction properly and try next time...")
else:
    print("Invalid input pls read above instruction properly and try next time...")

print(f'I know ye thoda ajeeb hai pr jo bhi hai theek hi hai')

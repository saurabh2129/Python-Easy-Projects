print("welcome to my computer quiz! ")

playing = input("Do you want to play? : ")

if playing.lower() != 'yes':
    quit()

print("Okay let's play :) ")
score = 0

answer = input("In python np stands or what? : ")
if  answer.lower() != "numpy":
    print('umhm!!! Wrong Answer')
else:
    print("Correct!")
    score += 1

answer = input("What is the extension of python file? : ")
if  answer.lower() != ".py":
    print('umhm!!! Wrong Answer')
else:
    print("Correct!")
    score += 1

answer = input("what is the fullform of SQL? : ")
if  answer.lower() != "structured query language":
    print('umhm!!! Wrong Answer')
else:
    print("Correct!")
    score += 1

answer = input("what is the fullform of XML? : ")
if  answer.lower() != "extensible markup language":
    print('umhm!!! Wrong Answer')
else:
    print("Correct!")
    score += 1

answer = input("what is the fullform of HTML? : ")
if  answer.lower() != "hypertext markup language":
    print('umhm!!! Wrong Answer')
else:
    print("Correct!")
    score += 1

print(f'You got {score} questions correct!')
print('You got'+ str((score/4) * 100)+'%.')
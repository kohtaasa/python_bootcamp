import random

print('...rock...')
print('...paper...')
print('...scissors...')
p1 = input("Enter your choice:").lower()

comp = random.choice(['rock','paper','scissors'])
print(f"Computer's choice: {comp}")

if p1 == comp:
    print('Draw')
elif p1 == 'rock':
    if comp =='scissors':
        print('You win')
    else:
        print('Computer wins')
elif p1 == 'paper':
    if comp =='rock':
        print('You win')
    else:
        print('Computer wins')
elif p1 == 'scissors':
    if comp =='paper':
        print('You win')
    else:
        print('Computer wins')
else:
    print('Something went wrong')
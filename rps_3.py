import random

p1_wins = 0
comp_wins = 0

while p1_wins < 2 and comp_wins < 2:
    print(f'Player Score: {p1_wins} Computer Score: {comp_wins}')
    print('...rock...')
    print('...paper...')
    print('...scissors...')
    p1 = input("Enter your choice:").lower()
    if p1 == "quit" or p1 == 'q':
        break

    comp = random.choice(['rock','paper','scissors'])
    print(f"Computer's choice: {comp}")

    if p1 == comp:
        print('Draw')
    elif p1 == 'rock':
        if comp =='scissors':
            print('You win')
            p1_wins +=1
        else:
            print('Computer wins')
            comp_wins +=1
    elif p1 == 'paper':
        if comp =='rock':
            print('You win')
            p1_wins +=1
        else:
            print('Computer wins')
            comp_wins +=1
    elif p1 == 'scissors':
        if comp =='paper':
            print('You win')
            p1_wins +=1
        else:
            print('Computer wins')
            comp_wins +=1
    else:
        print('Something went wrong')
print(f'FINAL SCORES... Player Score: {p1_wins} Computer Score: {comp_wins}')
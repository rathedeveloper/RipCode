import random

def play():
    user = input("What is your choice 'r' for roock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    op_choic = computer


    if user == computer:
        print(op_choic)
        return 'It\'s a tie'
    
    # r > s, s > p, p > r

    if is_win(user, computer):
        print(op_choic)
        return 'You Won!'
    
    print(op_choic)
    return 'You Lost!'

def is_win(player, opponent):
    #return true if player wins 
     # r > s, s > p, p > r
     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
         or (player == 'p' and opponent =='r'):
        return True
     


print(play())
import random

game=['가위','바위','보']
print('가위바위보 게임 시작')
while True:
    me = input('가위,바위, 보 중 하나를 입력하세요(결과를 확인하려면 0을 입력하세요): ')
    computer_index = random.randint (0,2)
    computer = game[computer_index]
    win =0
    lose = 0
    same = 0
    if me == computer:
        print('무승부')
        
    elif me == '가위' and computer == '바위':
        print('나의 승리')
        
    elif me == '보' and computer == '바위':
        print('나의 승리')
        
    elif me=='바위' and computer == '가위':
        print('나의 승리')
       
    else:
        print('나의 패배')
       
       

    if me == 0:
        print(win,lose,same)
    if print('나의 승리'):
                win +=1
    elif print('나의 패배'):
                lose +=1
    else:
            same +=1

board=[['0','0','0'],['0','0','0'],['0','0','0']]
moves=[]

def showBoard():
    
    print("***********************")
    for i in range(3):
        print(board[i])
    print("***********************")

def enterUser1():
    n=validEnter()
    moveBoard(n,'x')

def enterUser2():
    n=validEnter()
    moveBoard(n,'O')

def winCondition():
        if board[0][0]==board[0][1] and board[0][0]==board[0][2] and board[0][0]!='0':
            return True
        elif board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!='0':
            return True
        elif board[0][0]==board[1][0] and board[0][0]==board[2][0] and board[0][0]!='0':
            return True
        elif board[1][0]==board[1][1] and board[1][0]==board[1][2] and board[1][0]!='0':
            return True
        elif board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!='0':
            return True
        elif board[0][2]==board[1][2] and board[0][2]==board[2][2] and board[0][2]!='0':
            return True
        elif board[2][2]==board[2][1] and board[0][2]==board[2][2] and board[2][2]!='0':
            return True
        elif board[0][1]==board[1][1] and board[0][1]==board[2][1] and board[0][1]!='0':
            return True
        else:
            return False

def main():
    f = open("pastresults.txt", "a")
    n1=input("Enter username for Player1")
    n2=input("Enter username for Player2")
    showBoard()
        
    while(len(moves)<=9):
        
        enterUser1()
        if winCondition():
            showBoard()
            print(n1+" has won")
            f.write(n1+" has won")
            break
        showBoard()
        enterUser2()
        if winCondition():
            showBoard()
            print(n2+" has won")
            f.write(n2+" has won")
            break
        showBoard()
    f.close()
    if len(moves)>9:
        print("Tie is there between "+n1+" between "+n2)

def isNumber(n):
    flag=0
    for i in n:
        if i >='0' and i<='9':
            flag=0
        else:
            flag=1
            break
    if flag==1:
        return False
    else:
        return True



def validEnter():
    num=0
    while True:
        
        print('Moves already done')
        print(moves)
        n=(str(input("Enter Coordinates between 1 and 9: ")))
        if isNumber(n):
            num=int(n)
            if num in moves:
                print("The coordinates are already done")
                continue
            else:
                moves.append(num)
                break
        else:
            print("Enter a number")
            continue
    return num


def moveBoard(n,u):
    print(n)
    print(u)
    if n==1:
        board[0][0]=u
        #print(n)
    elif n==2:
        board[0][1]=u
        #print(n)
    elif n==3:
        board[0][2]=u
        #print(n)
    elif n==4:
        board[1][0]=u
        #print(n)
    elif n==5:
        board[1][1]=u
        #print(n)
    elif n==6:
        board[1][2]=u
        #print(n)
    elif n==7:
        board[2][0]=u
        #print(n)
    elif n==8:
        board[2][1]=u
        #print(n)
    elif n==9:
        board[2][2]=u
        #print(n)

if __name__ == "__main__":
    main()
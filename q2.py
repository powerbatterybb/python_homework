import random
import sys

def updown(x, y, count):
    if x == 1:
      if y == 1:
        print("사용자: 가위/ 컴퓨터: 가위")
        print("무승부")
        count[2] = count[2]+1
        return count
      elif y == 2:
        print("사용자: 가위/ 컴퓨터: 바위")
        print("패배")
        count[1] = count[1]+1
        return count     
      else:
        print("사용자: 가위/ 컴퓨터: 보")
        print("승리")
        count[0] = count[0]+1
        return count
      
    if x == 2:
      if y == 1:
        print("사용자: 바위/ 컴퓨터: 가위")
        print("승리")
        count[0] = count[0]+1
        return count
      elif y == 2:
        print("사용자: 바위/ 컴퓨터: 바위")
        print("무승부")
        count[2] = count[2]+1
        return count     
      else:
        print("사용자: 바위/ 컴퓨터: 보")
        print("패배")
        count[1] = count[1]+1
        return count
      
    else:
      if y == 1:
        print("사용자: 보/ 컴퓨터: 가위")
        print("패배")
        count[1] = count[1]+1
        return count
      elif y == 2:
        print("사용자: 보/ 컴퓨터: 바위")
        print("승리")
        count[0] = count[0]+1
        return count     
      else:
        print("사용자: 보/ 컴퓨터: 보")
        print("무승부")
        count[2] = count[2]+1
        return count

count = [0,0,0]

while True:
    random_number = random.randint(1, 3)

    while True:
      sel = input("가위, 바위, 보 중 하나를 선택하세요: ")
      comp = str(sel)

      if comp == "가위" or comp == "바위" or comp == "보":
        conv_comp = 0
        if comp == "가위":
           conv_comp= 1
        elif comp == "바위":
           conv_comp= 2
        else:
           conv_comp= 3

        count = updown(conv_comp, random_number, count)
        
        result = "승:"+ str(count[0]) + " 패:"+ str(count[1])+" 무:"+ str(count[2])
        print(result)

        regame = input("다시 하시겠습니까?(y/n): ")
        if regame == 'y' or regame == 'Y':
            break
        elif regame == 'n' or regame == 'N':
            sys.exit()        

    
      else:
        print("올바른 범위를 입력해주세요.")
        break

          
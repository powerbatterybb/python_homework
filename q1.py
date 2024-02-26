import random
import sys

def updown(x, y, count):
    if x == y:
        print("정답")
        print("카운트 횟수")
        print(count)
        
        return 0
    elif x > y:
        print("다운")
        return count+1
    else:
        print("업")
        return count+1

while True:
    random_number = random.randint(1, 100)
    count = 1
    while True:
      sel = input("숫자를 입력해주세요(1~100 사이의 자연수): ")
      comp = int(sel)

      if comp > 100 or comp < 1:
        print("올바른 범위를 입력해주세요.")
        break
    
      else:
        count = updown(comp, random_number, count)
        
        if count == 0:
          regame = input("다시 하시겠습니까?(y/n): ")
          if regame == 'y':
             break
          else:
             sys.exit()
          
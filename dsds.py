answer = input('단어를 입력하세요 :')
while True:
    second_answer = input('단어를 입력하세요 : ')    

    if len(second_answer) < 1:
        print('끝말잇기가 끝났습니다')
        break

    if answer.endswith(second_answer[0]):
        answer = second_answer
        continue
    else:
        print('끝말잇기가 끝났습니다')
        break




while True:
    answer = input('낼것(가위, 바위, 보)를 입력하세요 :')
    second_answer = input('두번쨰 낼것(가위, 바위, 보)를 입력하세요 :')

    if second_answer == '가위':
        print('가위:다시, 바위:패배, 보:승리')
    elif second_answer == '바위':
        print('가위:승리, 바위:다시, 보:패배')
    elif second_answer == '보':
        print('가위:패배, 바위:승리, 보:다시')
    else:
        print('잘못된 답변 입니다')
        break

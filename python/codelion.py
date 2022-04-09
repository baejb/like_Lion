menu=["1) 추가 " , "2) 조회 ", "3) 수정 ", "4) 삭제 ", "q) 종료 "]
total_question = {}

while True :
    print("-----------------멋쟁이 사자처럼 전화번호부-----------------")
    print(menu)
    choice_menu = input("원하시는 메뉴를 입력해주세요: ")

    if choice_menu == "q":
        break
    #else:
        #total_question[question]= ""
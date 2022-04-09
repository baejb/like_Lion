total_question = {}
info = {}

while True:
    print("-----------------멋쟁이 사자처럼 전화번호부 -----------------")
    print("-----------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료---------- ")
    print("--------------------------------------------------------")

    choice_menu = input("원하시는 메뉴를 입력해주세요: ")

    if choice_menu == '1':
        name = input("이름을 입력해주세요 :")
        phone_number = input(name + "님의 번호를 입력해주세요 :")
        mail = input(name + "님의 메일을 입력해주세요 :")
        information = {'이름': name, '전화번호': phone_number, '메일': mail}
        info[name] = information
    elif choice_menu == '2':
        name = input("조회를 원하는 이름은 입력해주세요 :")
        if info[name] is None:
            print("찾을 수 없습니다. ")
        else:
            print(info[name])
    elif choice_menu == '3':
        name = input("수정을 원하는 이름을 입력해주세요 : ")
        if info[name] is None:
            print("찾을 수 없습니다. ")
        else:
            key,value =input("수정을 원하는 항목과 내용을 입력해주세요").split()
            if key == "이름":
                info[name].update({'이름':value})
            elif key == "전화번호":
                info[name].update({'전화번호':value})
            elif key == "메일":
                info[name].update({'메일':value})
    elif choice_menu =='4':
        name = input("삭제를 원하는 이름을 입력해주세요 :")
        if info[name] is None:
            print("찾을 수 없습니다.")
        else:
            del info[name]

    elif choice_menu == "q":
        break


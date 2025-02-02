#########################################
#                문제 설명              #
#########################################
# 다음 달에 가장 많은 선물을 받을 친구가 받을 선물의 수를 계산하는 프로그램

# 입력
# 1. friends (문자열 배열): 친구들의 이름 리스트
#    - 조건: 2 ≤ len(friends) ≤ 50
#    - 각 이름은 알파벳 소문자로 구성, 길이 ≤ 10
#    - 이름이 중복되지 않음
# 2. gifts (문자열 배열): 현재까지 주고받은 선물 기록
#    - 조건: 1 ≤ len(gifts) ≤ 10,000
#    - 각 요소는 "A B" 형식 (A가 B에게 선물을 전달)
#    - A와 B는 friends 배열의 원소이며, A != B

# 규칙
# 1. 선물 기록을 기준으로 다음 달에 선물 전달 결정
#    - A가 B보다 더 많은 선물을 준 경우: B가 A에게 선물 1개 받음
#    - 두 사람이 주고받은 선물 수가 같다면:
#      - 선물 지수 비교:
#        - 선물 지수 = (준 선물 수 - 받은 선물 수)
#        - 선물 지수가 큰 사람이 선물을 줌
# 2. 동점일 경우:
#    - 두 사람의 선물 지수도 같다면 선물을 주고받지 않음

# 출력
# - 다음 달에 가장 많은 선물을 받을 친구가 받을 선물의 수를 반환
class friend: 
    def __init__(self):       
        self.name=None
        self.give=0
        self.receive=0
        self.index=0
        self.totalReceive=0
        self.giveGiftName={}
    
    def setGiveGiftName(self, name):
        self.giveGiftName[name] = 0

def solution(friends, gifts):
    answer = 0
    friendNum = len(friends)
    friendList=[]   #리스트에 이름 전부 넣기
    for i in range(friendNum):
        obj = friend()
        obj.name=friends[i]
        friendList.append(obj)
    
    for i in friendList:
        for j in friendList:
            if i.name != j.name:
                i.setGiveGiftName(j.name)

    giftNum = len(gifts)
    for i in range(giftNum):            #give, receive 데이터 입력
        give, receive = gifts[i].split()   # give, receive 이름 분리
        for i in range(friendNum):
            if (friendList[i].name==give):                      #주는 사람일 경우
                friendList[i].give=friendList[i].give+1         #give 증가
                friendList[i].giveGiftName[receive]+=1    #선물 준 사람(receive)의 이름을 리스트에 추가
                friendList[i].index=friendList[i].give-friendList[i].receive
            elif(friendList[i].name==receive):                  # 받는 사람일 경우
                friendList[i].receive=friendList[i].receive+1   # receive 증가
                friendList[i].index=friendList[i].give-friendList[i].receive

    for me in friendList:
        for tarFriend in friendList:
            if me.name==tarFriend.name:
                continue
            else:
                # 대상과 내가 교류를 하지 않았을 때 혹은 주고 받은 선물 개수가 같을 때
                if (tarFriend.giveGiftName[me.name]==0 and me.giveGiftName[tarFriend.name]==0 or tarFriend.giveGiftName[me.name]==me.giveGiftName[tarFriend.name]):
                    if (me.index>tarFriend.index):
                        me.totalReceive+=1
                elif (me.giveGiftName[tarFriend.name]>0):
                    if (me.giveGiftName[tarFriend.name]==tarFriend.giveGiftName[me.name]):  # 지수 같을 때
                        if (me.index<tarFriend.index):
                            me.totalReceive+=1
                    elif (me.giveGiftName[tarFriend.name]>tarFriend.giveGiftName[me.name]):
                        me.totalReceive+=1

    answer = friendList[0].totalReceive
    for i in friendList:
        if (i.totalReceive>answer):
            answer=i.totalReceive
    print(answer)
    return answer

friends=["muzi", "ryan", "frodo", "neo"]
gifts=["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
solution(friends, gifts)
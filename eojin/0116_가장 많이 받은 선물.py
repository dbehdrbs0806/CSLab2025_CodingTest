"""
Programmers 2024 KAKAO WINTER INTERNSHIP 가장 많이 받은 선물
- 알고리즘: 

- 문제
선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다. 당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.

* 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
    * 예를 들어 A가 B에게 선물을 5번 줬고, B가 A에게 선물을 3번 줬다면 다음 달엔 A가 B에게 선물을 하나 받습니다.
* 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
    * 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
    * 예를 들어 A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7입니다. B가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 B의 선물 지수는 1입니다. 만약 A와 B가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면, 다음 달엔 B가 A에게 선물을 하나 받습니다.
    * 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.

위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 당신은 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶습니다.
이때, 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.


- 입력
친구들의 이름을 담은 1차원 문자열 배열 friends 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts가 매개변수로 주어집니다.
friends: ["muzi", "ryan", "frodo", "neo"]
gifts: ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

- 출력
다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 숫자 값으로 반환
result: 2

- 오답노트
    - .find()는 문자열에서만 사용 가능, 리스트나 이외 반복자에서는 .index() 사용
        - .find()와 .index() 둘 다 원소의 위치를 찾은 후 인덱스를 리턴하지만, 원소가 없을 경우 .find는 -1 / .index는 Error 띄움
    - 리스트의 길이 => len(리스트)
"""

def solution(friends, gifts):
    n = len(friends) # 인원 수
    giftindex = [0 for _ in range(n)] # 선물 지수
    member = [[0 for _ in range(n)] for _ in range(n)] # 선물 주고받은 횟수
    receive = [0 for _ in range(n)] # 받을 선물 수
    
    # 각 선물 준/받은 횟수 정리
    for g in gifts:
        fromg, tog = map(friends.index, g.split()) # gitfs의 문자열을 split으로 분리 후 index 함수로 변환
        member[fromg][tog] += 1 # fromg => 준 쪽 / tog => 받은 쪽
    
    # 선물 지수 정리
    for i in range(n):
        for j in range(n):
            giftindex[i] += member[i][j]
            giftindex[j] -= member[i][j]
    
    # 받을 선물의 수 계산
    ## 더 많은 선물을 준 사람이 다음 달에 선물을 받음
    ## 주고받은 선물 수가 같음(+ 서로 주고받은 적 X) 이면 선물 지수 비교해서 선물 지수 큰쪽에 선물
    ## 다 같으면 선물 주고받지 X
    for i in range(n):
        for j in range(n):
            if member[i][j] == member[j][i]:
                if giftindex[i] == giftindex[j]:
                    continue
                else:
                    if giftindex[i] > giftindex[j]:
                        receive[i] += 1
                    else: receive[j] += 1
            elif member[i][j] > member[j][i]:
                receive[i] += 1
            else: receive[j] += 1
            
    return max(receive)/2 # 값이 두배로 나오므로 /2
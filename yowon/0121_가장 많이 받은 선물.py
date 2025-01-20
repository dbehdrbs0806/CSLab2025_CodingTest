def solution(friends, gifts):
    # 각 친구가 다음 달에 받을 선물 수를 저장할 리스트
    received_gifts = [0] * len(friends)

    # 각 친구가 친구들에게 준 선물과 받은 선물을 기록하기 위한 딕셔너리
    gift_counts = {friend: {'given': 0, 'received': 0} for friend in friends}

    # 두 사람 간 선물 횟수를 기록하는 테이블
    gift_table = {friend: {other: 0 for other in friends} for friend in friends}

    # 선물 기록 처리
    for gift in gifts:
        giver, receiver = gift.split()
        gift_counts[giver]['given'] += 1
        gift_counts[receiver]['received'] += 1
        gift_table[giver][receiver] += 1

    # 친구별 선물 지수 계산 (준 선물 - 받은 선물)  
    gift_indices = {friend: gift_counts[friend]['given'] - gift_counts[friend]['received'] for friend in friends}

    # 다음 달 선물 받을 횟수 계산
    for i, friend1 in enumerate(friends):
        for j, friend2 in enumerate(friends):
            if i >= j:
                continue  # 이미 계산된 조합은 건너뜀

            # 친구 사이의 선물 주고받은 횟수 비교
            if gift_table[friend1][friend2] > gift_table[friend2][friend1]:
                received_gifts[i] += 1
            elif gift_table[friend1][friend2] < gift_table[friend2][friend1]:
                received_gifts[j] += 1
            else:  # 선물 주고받은 횟수가 같은 경우 선물 지수 비교
                if gift_indices[friend1] > gift_indices[friend2]:
                    received_gifts[i] += 1
                elif gift_indices[friend1] < gift_indices[friend2]:
                    received_gifts[j] += 1

    # 다음 달 가장 많은 선물을 받을 친구가 받을 선물 수를 반환
    return max(received_gifts)

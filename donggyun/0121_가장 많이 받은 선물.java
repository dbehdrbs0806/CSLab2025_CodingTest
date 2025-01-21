class Solution {
    public int solution(String[] friends, String[] gifts) {         // friends[]: 친구 이름 / gifts[]: 선물 배열
        Map<String, Map<String, Integer>> giftRecords = new HashMap<>();         // giver, receiver 선물 기록을 위한 hashmap
        Map<String, Integer> giftScore = new HashMap<>();                       // 선물지수 기록
        Map<String, Integer> nextMonthGifts = new HashMap<>();                  // 다음달 친구 별 받을 선물횟수

        for (String friend : friends) {                                         // friends 배열의 친구 이름을 각 hashmap에 대입
            giftRecords.put(friend, new HashMap<>());
            giftScore.put(friend, 0);
            nextMonthGifts.put(friend, 0);
        }
        
        for (String gift : gifts) {                                             // gifts 배열의 gitfs개수를 대입
            String[] parts = gift.split(" ");                                   // "선물 받은 사람" , "선물 준 사람"
            String giver = parts[0];
            String receiver = parts[1];

            giftRecords.get(giver).put(receiver, giftRecords.get(giver).getOrDefault(receiver, 0) + 1);
            giftScore.put(giver, giftScore.get(giver) + 1);
            giftScore.put(receiver, giftScore.get(receiver) - 1);

            /*{ giftRecords
                "muzi":   {"frodo": 2},
                "ryan":   {"muzi": 3},
                "frodo":  {"muzi": 1, "ryan": 1},
                "neo":    {"muzi": 1}
            }
            {   giftScore
                "muzi":   -3,
                "ryan":   +2,
                "frodo":  +1,
                "neo":    +1
            }
            {
                "muzi":   3,
                "ryan":   1,
                "frodo":  0,
                "neo":    0
            }

            */
        }
        for (String giver : friends) {
            for (String receiver : friends) {
                if (!giver.equals(receiver)) {      // 자기 자신 제외
                    int giftsFromGiver = giftRecords.get(giver).getOrDefault(receiver, 0);
                    int giftsFromReceiver = giftRecords.get(receiver).getOrDefault(giver, 0);

                    if (giftsFromGiver > giftsFromReceiver) {           // 조건1 선물 횟수가 더 많을 때
                        nextMonthGifts.put(giver, nextMonthGifts.get(giver) + 1);
                    } else if (giftsFromGiver == giftsFromReceiver && giftScore.get(giver) > giftScore.get(receiver)) {         // 조건2 선물 횟수가 같을때는 선물 지수로 확인 giftScore
                        nextMonthGifts.put(giver, nextMonthGifts.get(giver) + 1);
                    }
                }
            }
        }

        return Collections.max(nextMonthGifts.values());            // 최대로 선물 받는 사람의 선물 수 return
    }
}
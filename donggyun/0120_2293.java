import java.io.*;
import java.lang.*;
import java.util.*;
/*
Baekjoon #2644 동전 1
- 알고리즘: DP
- 문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.
사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다. 각 동전을 사용 안해도 된다.

- 입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

- 출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.

예제 입력 1
3 10
1
2
5
예제 출력 1
10
- etc
DP(Dynamic Programming) 동적 계획법
큰 문제를 작은 문제로 나눠서 푸는 알고리즘
동전 가치(원)의 값을 가지는 배열: narray[i]
dp 배열(k) 합인 k원 배열 사용: dp[k]     => 배열의 인덱스: k / 배열의 요소: 인덱스 k를 합으로 가질 수 있는 경우의 수
k >= narray[i] = dp[k] + dp[k - narray[i]]
https://lotuslee.tistory.com/113
 */
public class Main2293 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());                       // n가지 동전 종류
        Integer[] narray = new Integer[n];
        int k = Integer.parseInt(st.nextToken());                       // k 동전의 총 k합

        for (int i = 0; i < n; i++) {
            narray[i] = Integer.parseInt(br.readLine());
        }
        // Arrays.sort(narray, Collections.reverseOrder());                // 내림차순으로 동전 가치 정렬
        //int result = coin(narray, k, 0);                                // 재귀 호출

        int[] dp = new int[k + 1];
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                if (j >= narray[i])
                    dp[j] += dp[j - narray[i]];
            }
        }
        System.out.println(dp[k]);                                     // 결과 출력
    }


    // 재귀 사용 (시간 초과 오류)
    public static int coin(Integer[] narray, int amount, int index) {
        if (amount == 0) return 1;                                           // 종료 조건: 정확히 금액을 맞춘 경우

        if (index >= narray.length || amount < 0) return 0;                  // 종료 조건: 동전이 남아 있지 않거나 amount가 0보다 작아진 경우
        // 경우의 수 계산: 동전을 사용하지 않는 경우 + 동전을 사용하는 경우
        int withoutCurrentCoin = coin(narray, amount, index + 1);       // 현재 동전 사용하지 않음
        int withCurrentCoin = coin(narray, amount - narray[index], index); // 현재 동전 사용

        return withoutCurrentCoin + withCurrentCoin;                   // 두 경우의 수 합산
    }
}

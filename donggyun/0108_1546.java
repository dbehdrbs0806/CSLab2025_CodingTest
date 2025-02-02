import java.io.*;
import java.util.*;
import java.lang.*;

/*
Baekjoon #1546 평균
- 알고리즘: 수학
- 문제
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

- 입력
첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

- 출력
첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.

예제 입력 1
3
40 80 60
예제 출력 1
75.0

- etc
N개의 과목들의 점수를 통해 평균을 구하는 문제
N개의 과목 중 가장 높은 점수를 M이라 할 때, 평균계산은 각 과목 점수 / M * 100 인 점수를 사용함
*/

public class Main1546 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());                // N 과목의 개수
        String[]score_list = br.readLine().split(" ");    // 과목 점수 입력받음
        int temp = 0;
        double all_score = 0;
        double result;

        for(int i = 0; i < N; i++) {                            // temp = M
            int score = Integer.parseInt(score_list[i]);
            if (score >= temp) {
                temp = score;
            }
        }

        for(int j = 0; j < N; j++) {
            int score = Integer.parseInt(score_list[j]);
            all_score = all_score + (((double)score / temp) * 100);
        }
        result = all_score / N;
        System.out.println(result);
    }
}
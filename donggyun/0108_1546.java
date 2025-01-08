import java.io.*;
import java.util.*;
import java.lang.*;

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

/*
Bronze1 1546번 평균
N개의 과목들의 점수를 통해 평균을 구하는 문제
N개의 과목 중 가장 높은 점수를 M이라 할 때, 평균계산은 각 과목 점수 / M * 100 인 점수를 사용함
 */

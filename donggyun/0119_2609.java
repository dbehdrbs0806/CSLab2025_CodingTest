import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
Baekjoon #2609 소수
- 알고리즘: 수학, 유클리드 호제법
- 문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

- 입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

- 출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1
24 18
예제 출력 1
6
72
- etc
최대공약수, 최소공배수 문제는 유클리드 알고리즘을 사용해 해결할 것
GCD(최대공약수)는 a를 b로 나눈 나머지를 n이라 할 때 a % b = n / n 이 0이 아니면 최대공약수

 */

public class Main2609 {
    public static void main(String[] args) throws Exception {
        // GCD 방식 시간 초과로 인한
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int dv = gcd(a, b);
        int mul = (a * b / dv);

        System.out.println(dv);
        System.out.println(mul);
    }
    static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
    /*BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());            // 첫째 줄 입력 자연수

        int a = Integer.parseInt(st.nextToken());           // 첫 입력 자연수 a
        int b = Integer.parseInt(st.nextToken());           // 두번째 입력 자연수 b

        int temp1 = 1;                                         // 임시 최대 공약수
        int dv = temp1;                                        // 최대 공약수 dv
        while (temp1 <= a && temp1 <= b) {
            if ((a % temp1) == 0 && (b % temp1) == 0) {        //  공약수 확인 조건문
                if (dv <= temp1) {
                    dv = temp1;
                }
            }
            temp1+=1;
        }
        int mul = -1;
        int temp2 = 0;
        ArrayList<Integer> array1 = new ArrayList<>();
        ArrayList<Integer> array2 = new ArrayList<>();
        while (true) {
            temp2+=1;
            array1.add(a * temp2);
            array2.add(b * temp2);
            for (int i : array1) {
                if (array2.contains(i)) {
                    mul = i;
                    break;
                }
            }
            if (mul != -1) {
                break;
            }
        }

        System.out.println(dv);
        System.out.println(mul);*/

}
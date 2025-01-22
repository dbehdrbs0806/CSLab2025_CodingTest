"""
Baekjoon #2018 수들의 합 5
- 문제
어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서, 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다. 이때, 사용하는 자연수는 N이하여야 한다.
예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지가 있다.
N을 입력받아 가지수를 출력하는 프로그램을 작성하시오.

- 입력
첫 줄에 정수 N이 주어진다.

- 출력
입력된 자연수 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 출력하시오

예제 입력 1 
15
예제 출력 1 
4
- etc

"""
def count5(N):
    j = 1
    result = 0
    while j != N:
        total = 0
        for i in range(j , N + 1):
            total += i
            if total > N:
                j += 1
                break
            elif total == N:
                result += 1
    return result + 1

if __name__ == "__main__":
    N = int(input())                # 입력 input()
    print(count5(N)) 

"""
public class Main2018 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());            // ex) N = 12

        int total;                                          // 각 자연수를 더한 값 기록 변수 
        int j = 1;                                              // 자연수 flag = j 반복 조건을 위한 flag <= N
        int result = 0;                                             // 결과 result값 
        while (j != N) {
            total = 0;
            for (int i = j; i <= N; i++) {                            // 1 2 3 ~ 12           =>          for ( ; i <= N; i++) 초기값 설정 x 1씩 증가해야 하니까
                total += i;                                     // 1 + 2 + 3 ~
                if (total > N) {                               // 1 + 2 + 3 + 4 + 5 = 15 > 12 => i = 2
                    j++;                                        // 2 부터 연속된 자연수 시작
                    break;
                }
                else if (total == N) {                          // 3 + 4 + 5
                    result += 1;
                }
            }
        }
        System.out.println(result + 1);
    }
    // 몇 개의 연속된 자연수 들의 합을 통해서 N을 만듬
    // 자연수 들은 연속되고 N 이하
    // 출력은 만들 수 있는 가짓 수
    // ex) N = 10 => return 2 (10, 1 + 2 + 3 + 4)
}
"""


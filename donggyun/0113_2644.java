import java.io.*;
import java.lang.*;
import java.util.*;

/*
Baekjoon #2644 촌수계산
- 알고리즘: 그래프 탐색, 너비 우선 탐색
- 문제
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

- 입력
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

예제 입력 1
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
예제 출력 1
3

- 출력
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

- etc
StringTokenizer의 사용
ArrayList 이차원 동적배열 ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
BFS 너비우선탐색
Queue, ArrayList<> graph, visited[] 사용
*/

public class Main2644 {
    public static int BFS(ArrayList<ArrayList<Integer>> graph, int A, int B, int n) {
        boolean[] visited = new boolean[n + 1];                   // 노드들이 방문 했는지 여부 판단 배열 / n + 1: 사람은 1, 2, ~의 숫자 입력이기 때문
        Queue<Integer> queue = new LinkedList<>();                // BFS 계산을 위한 queue 선언
        int[] distance = new int[n+1];                            // 촌수 저장배열

        queue.add(A);                                             // 시작 노드 personA queue에 대입
        visited[A] = true;                                        // 방문 여부 true

        while (!queue.isEmpty()) {                                // queue 빌때까지 반복
            int temp = queue.poll();                              // queue에서 값 반환
            for (int neighbor : graph.get(temp)) {                // queue에서 반환한 temp와 이웃한 노드들
                if (!visited[neighbor]) {                         // 방문하지 않은 노드들
                    visited[neighbor] = true;                     // 방문 여부 true로 변경
                    distance[neighbor] = distance[temp] + 1;      // 현재 노드의 촌수 + 1
                    queue.add(neighbor);                          // 인접 노드를 queue에 대입
                    if (neighbor == B) {
                        return distance[neighbor];
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));                   // 입력을 위한 BufferReader
        StringTokenizer st;                                                                         // 입력을 Tokenizer 나눔 / st 선언

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());                    // 가족 총 인원 n명

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());                           // 각 인덱스에 빈 ArrayList를 추가
        }

        st = new StringTokenizer(br.readLine());                    // 촌수 계산 인원 번호 A, B
        int personA = Integer.parseInt(st.nextToken());
        int personB = Integer.parseInt(st.nextToken());

        int m = Integer.parseInt(br.readLine());                    // 부모 자식 관계의 개수 m개

        for (int i = 0; i < m; i++) {                               // 그래프에 부모 자식 관계 대입
            st = new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            graph.get(parent).add(child);                           // 부모와 자식 양방향
            graph.get(child).add(parent);                           // ex) 1(parent), 2(child)
            // 어차피 관계 상에서 부모 자식이고 촌수 계산 시에는 부모와 자식이 상관 없음
        }

        int result = BFS(graph,  personA, personB, n);

        System.out.println(result);
    }
}

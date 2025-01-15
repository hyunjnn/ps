import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Main {
    static boolean[] visited;
    static HashMap<Integer, Integer> matched;
    static List<List<Integer>> graph;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 직원, 할 일의 수
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        // 작업별 매칭 정보 초기화
        matched = new HashMap<>();
        for (int task = 0; task <= M; task++) {
            matched.put(task, 0);
        }
        // 직원별 가능한 작업 초기화
        graph = new ArrayList();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList());
        }
        
        // 직원별 가능한 일 입력
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int taskCount = Integer.parseInt(st.nextToken());
            for (int j = 0; j < taskCount; j++) {
                int task = Integer.parseInt(st.nextToken());
                graph.get(i).add(task);
            }
        }
        
        // 최대 매칭 수 
        int res = 0;
        for (int employee = 1; employee <= N; employee++) {
            visited = new boolean[M + 1];
            if (isMatching(employee)) {
                res++;
            }
        }
        System.out.println(res);
    }
    
    static boolean isMatching(int employee) {
        for (int task: graph.get(employee)) {
            if (!visited[task]) {
                visited[task] = true;
                if (matched.get(task) == 0 || isMatching(matched.get(task))) {
                    matched.put(task, employee);
                    return true;
                }
            }
        }
        return false;
    }
}
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 테스트 수
        int K = Integer.parseInt(st.nextToken());
        for (int t = 0; t < K; t++) {
            
            // 정점, 간선의 개수
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            
            // 그래프 초기화
            List<List<Integer>> graph = new ArrayList<>(v + 1);
            for (int i = 0; i < v + 1; i++) {
                graph.add(new ArrayList<>());
            }
            
            // 간선 정보 입력
            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph.get(a).add(b);
                graph.get(b).add(a);
            }
            
            // 이분 그래프 판별 결과
            if (isBipartite(graph, v)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
    
    static boolean isBipartite(List<List<Integer>> graph, int N) {
        int[] colors = new int[N + 1];
        Arrays.fill(colors, 0);
        
        for (int start = 1; start <= N; start++) {
            if (colors[start] != 0) continue;
            
            Queue<Integer> q = new ArrayDeque<>();
            q.add(start);
            colors[start] = 1;
        
            while (!q.isEmpty()) {
                int node = q.poll();
                
                for (int neighbor: graph.get(node)) {
                    if (colors[neighbor] == 0) {
                        q.add(neighbor);
                        colors[neighbor] = -colors[node];
                        
                    } else if (colors[neighbor] == colors[node]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
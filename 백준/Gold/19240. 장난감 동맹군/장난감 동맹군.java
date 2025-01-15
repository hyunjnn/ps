import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int T = Integer.parseInt(st.nextToken());
        
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            
            List<List<Integer>> graph = new ArrayList<>(V + 1);
            for (int i = 0; i < V + 1; i++) {
                graph.add(new ArrayList<>());
            }
            
            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int toy1 = Integer.parseInt(st.nextToken());
                int toy2 = Integer.parseInt(st.nextToken());
                graph.get(toy1).add(toy2);
                graph.get(toy2).add(toy1);
            }
            System.out.println(isBipartite(graph, V) ? "YES" : "NO");
        }
    }
    
    static boolean isBipartite(List<List<Integer>> graph, int v) {
        int[] tags = new int[v + 1];
        Arrays.fill(tags, 0);
        
        for (int start = 1; start <= v; start++) {
            if (tags[start] == 0) {
                Queue<Integer> dq = new ArrayDeque<>();
                dq.add(start);
                tags[start] = 1;
                
                while (!dq.isEmpty()) {
                    int node = dq.poll();
                    for (int neighbor: graph.get(node)) {
                        if (tags[neighbor] == 0) {
                            tags[neighbor] = -tags[node];
                            dq.add(neighbor);
                        } else if (tags[neighbor] == tags[node]) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
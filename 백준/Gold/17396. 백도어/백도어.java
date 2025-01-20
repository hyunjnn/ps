import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Edge implements Comparable<Edge> {
    int node, cost;
    
    public Edge(int node, int cost) {
        this.node = node;
        this.cost = cost;
    }
    
    @Override
    public int compareTo(Edge o) {
        return Integer.compare(this.cost, o.cost);
    }
}

public class Main {
    static final long INF = Long.MAX_VALUE;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        
        int[] visible = new int[v];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < v; i++) {
            visible[i] = Integer.parseInt(st.nextToken());
        }
        
        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i < v; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Edge(b, c));
            graph.get(b).add(new Edge(a, c));
        }
        
        System.out.println(findShortestTime(graph, v, visible));
    }
    
    static long findShortestTime(List<List<Edge>> graph, int n, int[] visible) {
        long[] time = new long[n];
        Arrays.fill(time, INF);
        
        time[0] = 0;
        PriorityQueue<Edge> pQ = new PriorityQueue<>();
        pQ.add(new Edge(0, 0));
        
        while (!pQ.isEmpty()) {
            Edge cur = pQ.poll();
            
            if (cur.cost > time[cur.node]) continue;
            
            for (Edge neighbor: graph.get(cur.node)) {
                if (neighbor.node != n - 1 && visible[neighbor.node] == 1) continue;
                long newCost = time[cur.node] + neighbor.cost;
                if (newCost < time[neighbor.node]) {
                    time[neighbor.node] = newCost;
                    pQ.add(new Edge(neighbor.node, (int) newCost));
                }
            }
        }
        return time[n - 1] < INF ? time[n - 1] : -1;
    }
    
}
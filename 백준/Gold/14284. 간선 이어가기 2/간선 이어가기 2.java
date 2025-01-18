import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.PriorityQueue;


class Node implements Comparable<Node> {
    int vertex, cost;
    
    public Node(int vertex, int cost) {
        this.vertex = vertex;
        this.cost = cost;
    }
    
    @Override
    public int compareTo(Node o) {
        return Integer.compare(this.cost, o.cost);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        
        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i < v + 1; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, c));
            graph.get(b).add(new Node(a, c));
        }
        
        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        
        System.out.println(dijkstra(s, t, v, graph));
    }
    
    static int dijkstra(int start, int target, int n, List<List<Node>> graph) {
        int[] costs = new int[n + 1];
        Arrays.fill(costs, Integer.MAX_VALUE);
        PriorityQueue<Node> pQ = new PriorityQueue<>();
        
        costs[start] = 0; 
        pQ.add(new Node(start, 0));
        
        while (!pQ.isEmpty()) {
            Node cur = pQ.poll();
            
            int curNode = cur.vertex;
            int curCost = cur.cost;
            if (curCost > costs[curNode]) continue; 
            
            for (Node neighbor: graph.get(curNode)) {
                int newCost = curCost + neighbor.cost;
                
                if (newCost < costs[neighbor.vertex]) {
                    costs[neighbor.vertex] = newCost;
                    pQ.add(new Node(neighbor.vertex, newCost));
                }
            }
        }
        return costs[target];
    }
}
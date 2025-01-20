import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.Arrays;

class Room implements Comparable<Room> {
    int cost, x, y;
    
    public Room(int cost, int x, int y) {
        this.cost = cost;
        this.x = x;
        this.y = y;
    }
    
    @Override 
    public int compareTo(Room o) {
        return Integer.compare(this.cost, o.cost);
    }
}

public class Main {
    static final int[] dx = {0, 1, -1, 0};
    static final int[] dy = {1, 0, 0, -1};
    static final int INF = Integer.MAX_VALUE;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int problemNum = 1;
        
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            if (n == 0) break;
            
            int[][] maps = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    maps[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            
            Room start = new Room(maps[0][0], 0, 0);
            int minVal = dijkstra(maps, n, start);
            System.out.println(String.format("Problem %d: %d", problemNum, minVal));
            
            problemNum += 1;
        }
    }
    
    static int dijkstra(int[][] maps, int n, Room start) {
        // 각 위치에서의 최소 비용
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], INF);
        }
        dist[0][0] = maps[0][0];
        
        PriorityQueue<Room> pQ = new PriorityQueue<>();
        pQ.add(start);
        
        while (!pQ.isEmpty()) {
            Room cur = pQ.poll();
            
            if (cur.cost > dist[cur.x][cur.y]) continue;
            
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    int newCost = cur.cost + maps[nx][ny];
                    
                    if (newCost < dist[nx][ny]) {
                        dist[nx][ny] = newCost;
                        pQ.add(new Room(newCost, nx, ny));
                    }
                }
            }
        }
        return dist[n - 1][n - 1];
    }
}
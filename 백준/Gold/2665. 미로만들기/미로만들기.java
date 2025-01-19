import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

class Room {
    int x, y;
    
    public Room(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static final int INF = 10_000_000;
    static final int[] dx = {0, 1, 0, -1};
    static final int[] dy = {1, 0, -1, 0};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int[][] graph = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = row.charAt(j) - '0';
            }
        }
        Room startRoom = new Room(0, 0);
        System.out.println(bfs(graph, n, startRoom));
    }
    
    // 바꿔야 할 검은 방의 최소 개수 반환
    static int bfs(int[][] graph, int n, Room start) {
        
        // i, j 위치에 도달하기 위해 바꾸는 검은 방의 수
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], INF);
        }
        // 방문하는 방 관리
        Deque<Room> q = new ArrayDeque<>();
        q.add(start);
        dp[start.x][start.y] = 0;
        
        while (!q.isEmpty()) {
            Room curRoom = q.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = curRoom.x + dx[i];
                int ny = curRoom.y + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    int newCount = dp[curRoom.x][curRoom.y] + (graph[nx][ny] == 0 ? 1 : 0);
                    
                    if (newCount < dp[nx][ny]) {
                        dp[nx][ny] = newCount;
                    
                        if (graph[nx][ny] == 0) {
                            q.addLast(new Room(nx, ny));
                        } else {
                            q.addFirst(new Room(nx, ny));
                        }
                    }
                }
            }
        }
        return dp[n - 1][n - 1];
    }
}
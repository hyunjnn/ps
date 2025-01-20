import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.lang.Math;

public class Main {
    static int INF = 10_000_000;
    static int[] dx = {1, 0};
    static int[] dy = {0, 1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int[][] maps = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(solve(maps, n));
    }
    
    static int solve(int[][] maps, int n) {
        int[][] costs = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(costs[i], INF);
        }
        
        costs[0][0] = 0;
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                // 아래 방향과 오른쪽 방향 두 가지
                for (int k = 0; k < 2; k++) {
                    int nx = dx[k] + x;
                    int ny = dy[k] + y;
                    // 범위를 벗어나지 않는지 확인
                    if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                        if (maps[x][y] <= maps[nx][ny]) { // 버튼 누르는 추가 비용 발생
                            int diff = maps[nx][ny] - maps[x][y] + 1;
                            costs[nx][ny] = Math.min(costs[nx][ny], costs[x][y] + diff);;
                        } else {  
                            costs[nx][ny] = Math.min(costs[nx][ny], costs[x][y]);
                        }
                    }
                }
            }
        }
        
        return costs[n - 1][n - 1];
    }
}
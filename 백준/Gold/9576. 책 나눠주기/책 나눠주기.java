import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int T = Integer.parseInt(st.nextToken());
        
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            
            int[][] requests = new int[M][2];
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                requests[i][0] = Integer.parseInt(st.nextToken());
                requests[i][1] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(requests, (a, b) -> Integer.compare(a[1], b[1]));
            
            boolean[] used = new boolean[N + 1];
            int maxStudents = 0;
            
            for (int[] request: requests) {
                int start = request[0];
                int end = request[1];
                for (int book = start; book <= end; book++) {
                    if (!used[book]) {
                        maxStudents++;
                        used[book] = true;
                        break;
                    }
                }
            }
            System.out.println(maxStudents);
        }
    }
}
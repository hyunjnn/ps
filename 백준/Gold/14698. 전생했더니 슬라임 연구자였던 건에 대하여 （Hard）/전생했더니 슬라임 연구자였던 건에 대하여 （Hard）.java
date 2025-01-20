import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
    
public class Main {
    static final int MOD = 1_000_000_007;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            
            int N = Integer.parseInt(br.readLine());
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            PriorityQueue<Long> pQ = new PriorityQueue<>();
            for (int i = 0; i < N; i++) {
                pQ.add(Long.parseLong(st.nextToken()));
            }
            
            long res = 1;
            while (pQ.size() > 1) {
                long s1 = pQ.poll();
                long s2 = pQ.poll();
                long newCost = (s1 * s2) % MOD;
                res = (res * newCost) % MOD;
                pQ.add(s1 * s2);
            }
            System.out.println(res);
        }
    }
}
    
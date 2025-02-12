import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        
        long window = 0;
        for (int i=0; i<m; i++) {
            window += nums[i];
        }
        
        long max_val = window;
        for (int i=m; i<n; i++) {
            window -= nums[i-m];
            window += nums[i];
            max_val = Math.max(max_val, window);
        }
        
        System.out.println(max_val);
    }
}
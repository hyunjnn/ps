import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Collections;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
            
        int N = Integer.parseInt(st.nextToken());
        
        int[] nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        
        ArrayList<Integer> lis = new ArrayList<>();
        for (int n: nums) {
            int pos = Collections.binarySearch(lis, n);
            if (pos < 0) {
                pos = -(pos+1);
            }
            if (pos == lis.size()) {
                lis.add(n);
            } else {
                lis.set(pos, n);
            }
        }
        
        System.out.println(lis.size());
    }
}
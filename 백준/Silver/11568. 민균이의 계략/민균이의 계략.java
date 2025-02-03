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
        
        ArrayList<Integer> res = new ArrayList<>();
        for (int n: nums) {
            int pos = Collections.binarySearch(res, n);
            
            if (pos < 0) pos = -(pos+1);
            
            if (pos == res.size()) {
                res.add(n);
            } else {
                res.set(pos, n);
            }
        }
        System.out.println(res.size());
    }
}
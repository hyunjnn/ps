import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

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
        int[] index = new int[N];
        int[] pre = new int[N];
        Arrays.fill(pre, -1);
        for (int i=0; i<N; i++) {
            int pos = Collections.binarySearch(lis, nums[i]);
            if (pos < 0) {
                pos = -(pos + 1);
            }
            if (pos == lis.size()) {
                lis.add(nums[i]);
            } else {
                lis.set(pos, nums[i]);
            }
            
            index[pos] = i;
            if (pos > 0) {
                pre[i] = index[pos - 1];
            }
        }
        System.out.println(lis.size());
        
        int idx = index[lis.size() - 1];
        Stack<Integer> stack = new Stack<>();
        while (idx != -1) {
            stack.push(nums[idx]);
            idx = pre[idx];
        }
        
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop()).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    static int N, M;
    static int[] nums;
    static ArrayList<Integer> sequence = new ArrayList<>();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(nums);
        
        backtrack(0);
    }
    
    static void backtrack(int start) {
        if (sequence.size() == M) {
            StringBuilder sb = new StringBuilder();
            for (int i: sequence) {
                sb.append(i).append(" ");
            }
            System.out.println(sb.toString().trim());
            return;
        }
        
        for (int i = start; i < N; i++) {
            sequence.add(nums[i]);
            backtrack(i);
            sequence.remove(sequence.size() - 1);
        }
    }
}
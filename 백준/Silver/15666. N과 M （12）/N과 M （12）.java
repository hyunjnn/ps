import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    static int N, M;
    static int[] sortedNums;
    static ArrayList<Integer> sequence = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        sortedNums = new int[N];
        for (int i = 0; i < N; i++) {
            sortedNums[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(sortedNums);
        
        backtrack(0, 0);
        System.out.println(sb.toString());
    }
    
    static void backtrack(int start, int length) {
        if (length == M) {
            for (int n: sequence) {
                sb.append(n).append(" ");
            }
            sb.append("\n");
            return;
        }
        int pre = -1;
        for (int i = start; i < N; i++) {
            if (pre == sortedNums[i]) continue;
            sequence.add(sortedNums[i]);
            backtrack(i, length + 1);
            sequence.remove(sequence.size() - 1);
            pre = sortedNums[i];
        }
    }
}
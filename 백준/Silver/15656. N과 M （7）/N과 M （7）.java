import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    static int N, M;
    static int[] numbers;
    static List<Integer> sequence = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        numbers = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(numbers);
        backtrack(0, 0);
        System.out.println(sb.toString().trim());
    }
    
    static void backtrack(int start, int count) {
        if (count == M) {
            for (int n: sequence) {
                sb.append(n).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i=start; i<N; i++) {
            sequence.add(numbers[i]);
            backtrack(start, count + 1);
            sequence.remove(sequence.size() - 1);
        }
    }
}
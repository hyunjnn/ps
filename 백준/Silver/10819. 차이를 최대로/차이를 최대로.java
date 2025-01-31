import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.lang.Math;

public class Main {
    static int N;
    static int[] numbers;
    static int maxVal = 0;
    static ArrayList<Integer> sequence = new ArrayList<>();
    static boolean[] used;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        numbers = new int[N];
        used = new boolean[N];
        
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        
        backtrack(0);
        System.out.println(maxVal);
    }
    
    static void backtrack(int level) {
        if (level == N) {
            int total = 0;
            for (int i=0; i<N-1; i++) {
                total += Math.abs(sequence.get(i) - sequence.get(i+1));
            }
            maxVal = Math.max(maxVal, total);
            return;
        }
        for (int i=0; i<N; i++) {
            if (!used[i]) {
                sequence.add(numbers[i]);
                used[i] = true;
                
                backtrack(level+1);
                
                sequence.remove(sequence.size() - 1);
                used[i] = false;
            }
        }
    }
}
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;

public class Main {
    static int maxNum, targetLength;
    static List<Integer> sequence = new ArrayList<>();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        maxNum = Integer.parseInt(st.nextToken());
        targetLength = Integer.parseInt(st.nextToken());
        
        solve(0);
    }
    
    static void solve(int level) {
        if (level == targetLength) {
            StringBuilder sb = new StringBuilder();
            for (int number: sequence) {
                sb.append(number).append(" ");
            }
            System.out.println(sb.toString().trim());
            return;
        }
        
        for (int n = 1; n <= maxNum; n++) {
            if (!sequence.isEmpty() && 
                n <= sequence.get(sequence.size() - 1)) continue;
            sequence.add(n);
            solve(level + 1);
            sequence.remove(sequence.size() - 1);
        }
    }
}
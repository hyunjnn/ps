import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());
        
        for (int i=0; i<t; i++) {
            String line = br.readLine().trim();
            
            int score = 0;
            int total = 0;
            for (char c: line.toCharArray()) {
                if (c == 'O') {
                    score++;
                } else {
                    score = 0;
                }
                total += score;
            }
            System.out.println(total);
        }
    }
}
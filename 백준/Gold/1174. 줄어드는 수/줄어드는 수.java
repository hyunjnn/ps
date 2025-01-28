import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static int N;
    static List<Integer> numbers = new ArrayList<>();
    static List<Long> decreasingNumbers = new ArrayList<>();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        
        for (int k=1; k<=10; k++) {
            getDecreasingNumbers(0, 0, k, 9);
        }
        
        Collections.sort(decreasingNumbers);
        
        if (decreasingNumbers.size() < N) {
            System.out.println(-1);
        } else {
            System.out.println(decreasingNumbers.get(N - 1));
        }
    }
    
    static void getDecreasingNumbers(long curDigit, int level, int targetLevel, int lastDigit) {
        if (level == targetLevel) {
            decreasingNumbers.add(curDigit);
            return; 
        }
        for (int digit = lastDigit; digit>-1; digit--) {
            getDecreasingNumbers(curDigit*10+digit, level + 1, targetLevel, digit - 1);
        }
    }
}
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    static int L, C;
    static char[] data;
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        
        data = new char[C];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            data[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(data);
        backtrack(0, 0, new StringBuilder());
        System.out.println(sb);
    }
    
    static void backtrack(int start, int count, StringBuilder password) {
        if (count == L) {
            if (isValid(password)) {
                sb.append(password).append("\n");
            }
            return;
        }
        for (int i = start; i < C; i++) {
            password.append(data[i]);
            backtrack(i + 1, count + 1, password);
            password.deleteCharAt(password.length() - 1);
        }
    }
    
    static boolean isValid(StringBuilder password) {
        int vowel = 0, consonant = 0;
        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if ("aeiou".indexOf(c) >= 0) {
                vowel++;
            } else {
                consonant++;
            }
        }
        return vowel >= 1 && consonant >= 2;
    }
}
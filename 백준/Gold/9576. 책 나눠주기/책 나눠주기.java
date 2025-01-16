import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class Main {
    static boolean[] visited;
    static HashMap<Integer, Integer> matched;
    static List<List<Integer>> preferredBooks;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int T = Integer.parseInt(st.nextToken());
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int bookCount = Integer.parseInt(st.nextToken());
            int studentCount = Integer.parseInt(st.nextToken());
            
            preferredBooks = new ArrayList<>();
            for (int i = 0; i < studentCount + 1; i++) {
                preferredBooks.add(new ArrayList<>());
            }
            matched = new HashMap<>();
            for (int book = 1; book < bookCount + 1; book++) {
                matched.put(book, 0);
            }
            
            for (int student = 1; student <= studentCount; student++) {
                st = new StringTokenizer(br.readLine());
                int n1 = Integer.parseInt(st.nextToken());
                int n2 = Integer.parseInt(st.nextToken());
                for (int book = n1; book <= n2; book++) {
                    preferredBooks.get(student).add(book);
                }
            }
            
            int maxStudentCount = 0;
            for (int student = 1; student <= studentCount; student++) {
                visited = new boolean[bookCount + 1];
                if (tryMatching(student)) {
                    maxStudentCount++;
                }
            }
            System.out.println(maxStudentCount);
        }
    }
    
    static boolean tryMatching(int student) {
        for (int book: preferredBooks.get(student)) {
            if (!visited[book]) {
                visited[book] = true;
                if (matched.get(book) == 0 || tryMatching(matched.get(book))) {
                    matched.put(book, student);
                    return true;
                }
            }
        }
        return false;
    }
}
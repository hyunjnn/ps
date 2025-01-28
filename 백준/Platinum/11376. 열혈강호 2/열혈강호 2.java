import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;

public class Main {
    static int N, M;
    static List<List<Integer>> options;
    static boolean[] visited;
    static int[] matched;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        options = new ArrayList<>();
        for (int emp = 0; emp <= N; emp++) {
            options.add(new ArrayList<>());
        }
        matched = new int[M + 1];
        
        for (int emp = 1; emp <= N; emp++) {
            st = new StringTokenizer(br.readLine());
            int taskCount = Integer.parseInt(st.nextToken());
            for (int i = 0; i < taskCount; i++) {
                int task = Integer.parseInt(st.nextToken());
                options.get(emp).add(task);
            }
        }
        
        int res = 0;
        for (int emp = 1; emp <= N; emp++) {
            for (int count = 0; count < 2; count++) {
                visited = new boolean[M + 1];
                if (matching(emp)) {
                    res++;
                }
            }  
        }
        System.out.println(res);
    }
    
    static boolean matching(int employee) {
        for (int task: options.get(employee)) {
            if (!visited[task]) {
                    visited[task] = true;
                if (matched[task] == 0 || matching(matched[task])) {
                    matched[task] = employee;
                    return true;
                }
            }
        }
        return false;
    }
}
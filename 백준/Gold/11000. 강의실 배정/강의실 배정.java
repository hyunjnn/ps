import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 수업의 수
        int N = Integer.parseInt(st.nextToken());
        ClassTime[] classes = new ClassTime[N];
        
        // 수업 정보 입력
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            classes[i] = new ClassTime(start, end);
        }
        
        // 시작 시간이 빠른 순으로 정렬
        Arrays.sort(classes, Comparator.comparingInt(p -> p.start));
        
        // 종료 시간 관리 최소힙
        PriorityQueue<Integer> pQ = new PriorityQueue<>();
        for (ClassTime c: classes) {
            if (!pQ.isEmpty() && c.start >= pQ.peek()) {
                pQ.poll();
            }
            pQ.add(c.end);
        }
        
        System.out.println(pQ.size());
    }
    
    static class ClassTime {
        int start, end;
        
        public ClassTime(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}
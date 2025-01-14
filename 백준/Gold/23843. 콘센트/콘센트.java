import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.Collections;
import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 전자기기, 콘센트의 개수 입력
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        // 기기별 충전에 걸리는 시간 입력
        st = new StringTokenizer(br.readLine());
        Integer[] chargingTimes = new Integer[st.countTokens()];
        for (int i = 0; i < chargingTimes.length; i++) {
            chargingTimes[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(chargingTimes, Collections.reverseOrder());
        
        // 충전 시간 관리를 위한 최소 힙
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        // 충전 시작
        for (int t: chargingTimes) {
            if (heap.size() < M) {  
                heap.add(t);  // 빈 자리가 있으면 새로운 기기 추가
            } else {  // 먼저 충전되는 것부터 제거하고 새로운 기기 추가
                int outcome = heap.poll();
                heap.add(outcome + t);
            }
        }
        
        // 최소 충전 시간 출력
        System.out.println(Collections.max(heap));
    }
}
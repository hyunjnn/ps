This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

# 1. 동적 계획법 (Dynamic Programming) 문제 유형 정리

동적 계획법(DP)은 큰 문제를 작은 문제로 나누어 푸는 방식입니다.  
다음은 주요 DP 유형과 그에 해당하는 점화식을 정리한 표입니다.

## 🔹 DP 유형별 점화식 정리

| DP 유형 | 점화식 예시 | 대표 문제 |
|---------|-------------------------------|--------------|
| **기본 DP (피보나치)** | `dp[n] = dp[n-1] + dp[n-2]` | 피보나치 수열 |
| **배낭 문제 (0/1 Knapsack)** | `dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight] + value)` | 배낭 문제 |
| **최소 동전 개수 (동전 거스름돈)** | `dp[i] = min(dp[i], dp[i - coin] + 1)` | 동전 교환 문제 |
| **최장 증가 부분 수열 (LIS)** | `dp[i] = max(dp[j] + 1) (if arr[j] < arr[i])` | LIS 문제 |
| **최단 경로 (플로이드-워셜)** | `dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])` | 플로이드-워셜 알고리즘 |

## 🔹 DP 학습 및 연습 방법
1. **기본적인 DP 문제부터 시작** (점화식 패턴 익히기)
2. **비슷한 유형을 반복적으로 풀면서 점화식 유도 연습**
3. **Top-Down (재귀 + 메모이제이션)과 Bottom-Up (반복문)을 비교하며 연습**
4. **여러 유형을 섞어서 풀면서 응용력 키우기**

---

## 대표적인 DP 문제 풀어보기  
- 배낭 문제: 무게 제한이 있는 상황에서 최적의 가치를 찾는 문제  
- 동전 문제: 특정 금액을 만들기 위한 최소 동전 개수 찾기  
- LIS 문제: 가장 긴 증가하는 부분 수열 찾기  
- 플로이드-워셜 알고리즘: 모든 정점 간 최단 경로 계산  


import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        slimes = list(map(int, input().split()))
        heapify(slimes)
        
        res = 1
        while len(slimes) > 1:
            s1 = heappop(slimes)
            s2 = heappop(slimes)
            new_energy = s1 * s2
            res *= new_energy
            heappush(slimes, new_energy)
            
        print(res % 1000000007)
        
        
if __name__ == "__main__":
    main()
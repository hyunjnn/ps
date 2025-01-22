import sys
from collections import Counter
input = sys.stdin.readline

def calc_consistency(data, n):
    avg = sum(data) / n
    freq = Counter(data)
    
    expected_val = sum(x * (freq[x] / n) for x in freq.keys())
    
    if expected_val == 0:
        return "divide by zero"
    else:
        return f"{avg / expected_val:.2f}"

        
def main():
    n = int(input())
    if n == 0:
        print("divide by zero")
        return
    
    records = list(map(int, input().split()))
    
    print(calc_consistency(records, n))
    
    
if __name__ == "__main__":
    main()
    
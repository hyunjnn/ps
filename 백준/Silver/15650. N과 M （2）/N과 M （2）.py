import sys
input = sys.stdin.readline

def main():
    max_num, target_length = map(int, input().split())
    cur_sequence = []
    
    def generate_sequence(level):
        if level == target_length:
            print(" ".join(map(str, cur_sequence)))
        for n in range(1, max_num + 1):
            if cur_sequence and n <= cur_sequence[-1]:
                continue
            cur_sequence.append(n)
            generate_sequence(level + 1)
            cur_sequence.pop()
            
            
    generate_sequence(0)
    

if __name__ == "__main__":
    main()
from collections import defaultdict

# 책 개수
N = int(input())
# 없는 경우 기본값 0
books = defaultdict(int)

for _ in range(N):
    title = input()
    books[title] += 1
sorted_books = sorted(books.items(), key= lambda x: (-x[1], x[0]))

# 가장 많은 책 제목
print(sorted_books[0][0])
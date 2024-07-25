student = [i for i in range(1, 31)]

for _ in range(28):
    student.remove(int(input().strip())) # remove는 값으로 삭제하는 함수

print(min(student))
print(max(student))
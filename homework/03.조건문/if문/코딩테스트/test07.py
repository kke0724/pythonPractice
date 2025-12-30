def solution(names):
    answer = []
    for i in range(len(names)):
        if i/5 == 0:
            answer.apped(names[i])
    return answer

a = ["nami", "ahri", "jayce", "garen", "ivern","vex", "jinx"]
print(solution(a))
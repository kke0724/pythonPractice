def solution(todo_list,finished):
    todo_list = []
    finished = []
    if finished[0] == True:
        finished.append(todo_list[0])
    return finished
    
todo_list = ['problemsolving','practiceguitar','swim','studygraph']
finished = ['True','false','True','false']
print(solution(todo_list,finished))
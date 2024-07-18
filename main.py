import collections
from collections import deque

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')


student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))


tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"},
    {"type": "fast", "name": "Вивчити тему"}
]

task_queue = deque()

for task in tasks:
    if task in tasks:
        if task["type"] == "fast":
            task_queue.appendleft(task)
            print(f"Додано швидке завдання: {task['name']}")
        else:
            task_queue.append(task)
            print(f"Додано повільне завдання: {task['name']}")
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")
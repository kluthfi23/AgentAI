from core.task.engine import TaskEngine

engine = TaskEngine()

tasks = engine.create_task(
    "buka youtube.com lalu cari python flask lalu screenshot"
)

for task in tasks:

    print(task.to_dict())
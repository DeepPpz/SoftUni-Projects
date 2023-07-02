from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        else:
            return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str) -> str:
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
            task.completed = True
            return f"Completed task {task_name}"
        except StopIteration:
            return f'Could not find task with the name {task_name}'

    def clean_section(self):
        uncompleted_tasks = [task for task in self.tasks if not task.completed]
        num_removed = len(self.tasks) - len(uncompleted_tasks)
        self.tasks = uncompleted_tasks
        return f"Cleared {num_removed} tasks."

    def view_section(self):
        tasks = '\n'.join([t.details() for t in self.tasks])
        return f'Section {self.name}:\n{tasks}'

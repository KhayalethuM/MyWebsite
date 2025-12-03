class Task:
    def __init__(self, title): # Constructor runs whenever a Task is created
        self.title = title # Stores the task title
        self.done = False # Default: task not done
    def mark_done(self): # Behavior (method) of the Task
        self.done = True
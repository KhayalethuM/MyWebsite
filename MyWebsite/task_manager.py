import json
import os
from task import Task  #importing my class file
FILE = "tasks.json"
class TaskManager:
    def __init__(self):
        self.tasks = self.load() #load tasks when object is created
        
    def load(self):
        if not os.path.exists(FILE): #we"re checking if a file exists if not we return an empty list/array indicating that there's currently no files
            
            return []
        with open(FILE) as f: # open the JSON and read its contents 
            data = json.load(f)     
            return [Task(t["title"]) for t in data]  # the title part finds the title stored in json
        #the rest of the code then reconstructs each saved task;
        
    def save(self):
        data = [{"title": t.title, "done": t.done} for t in self.tasks]
        with open(FILE, "w") as f:
            json.dump(data, f, indent = 2)
        def add(self, title):
            self.tasks.append(Task(title))
            self.save()
        def list(self):
            for i, t in enumerate(Self.tasks, start = 1):
                if t.done:
                    status = "✔️" 
                else:
                    "❌"
                print(f"{i}.{t.title} [{status}]")
            def mark_done(self, index):
                if 0 <= index< len(self.tasks):
                    self.tasks[index].mark_done()
                    self.save()
                    
                    
                    
            
            
#!/usr/bin/python
 
import sys
from datetime import date

try:
    if len(sys.argv) == 2:
        if sys.argv[1] == 'help':
            print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
            """)
        elif sys.argv[1] == 'ls':
            todo_file = open('todo.txt', 'r')
            messages = todo_files.read()
            messages = messages.split('\n')
            for sno in range(len(messages)-2, 0, -1):
                print("[" + str(sno) + "]" + messages[sno])
            todo_file.close()
        
        elif sys.argv[1] == 'report':
            todo_file = open('todo.txt', 'r')
            messages = todo_files.read()
            messages = messages.split('\n')
            pending = len(messages)-1
            todo_file.close()
            done_file = open('done.txt', 'r')
            activities = done_file.read()
            activities = activities.split('\n')
            completed = len(activities)-1
            done_file.close()
            print(str(date.today()) + " Pending : " + str(pending) + " Completed : " + str(completed))
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'add':
            todo_file = open('todo.txt', 'a')
            todo_file.write(sys.argv[2])
            todo_file.close()
            print('Added todo: "' + sys.argv[2] + '"')
            
        elif sys.argv[1] == 'done':
            try:
                todo_file = open('todo.txt', 'w+')
                messages = todo_file.read()
                messages = messages.split('\n')
                activity_done = messages[int(sys.argv[2])]
                messages.remove(activity_done)
                messages = '\n'.join(messages)
                todo_file.write(messages)
                todo_file.close()
                
                done_file = open('done.txt', 'a')
                activities = done_file.write(activity_done+"\n")
                done_file.close()
            except:
                print("Error: todo #" + str(sys.argv[2]) + " does not exist.")
        
        elif sys.argv[1] == 'del':
            todo_file = open('todo.txt', 'w+')
            messages = todo_file.read()
            messages = messages.split('\n')[:-1]
            try:
                messages.remove(messages[int(sys.argv[2])-1])
                messages = '\n'.join(messages) + "\n"
                todo_file.write(messages)
            except:
                print("Error: todo #" + str(sys.argv[2]) + " does not exist. Nothing deleted.")
                
    
except:
    print("Incorrect Command")


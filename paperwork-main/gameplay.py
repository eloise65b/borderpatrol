def split(word):
    return [char for char in word]

#get reference number
waitingroom = []
currenttasks = []
importperson()
for i in range (0,5):
  person = importperson()
  waitingroom.append(person)
  
#moved scheduling algorithms
def longestfirst():
    #x = number of tasks waiting
    x = 0
    #timeval = import from main string, time left on task
    for i in range(0,x):
        lowest = 1
        if timeval < lowest:
            lowest = timeval
            todo = x
    return(todo,x)

def shortestfirst():
    #x = number of tasks waiting
    x = 0
    #timeval = import from main string, time left on task
    for i in range(0,x):
        highest = 1
        if timeval > highest:
            highest = timeval
            todo = x
    return(todo,x) #unsure if this is appropriate- run within the func.?

def roundrobin(sleeptime):
    #must be called multiple times using a for statment? probably should run within the function
    x = 0
    for i in range(0,x):
        time.sleep(sleeptime)
        return(x)
        #what the hell is this though

        #TODO: please for the love of god redo these

for i in range (0,5):
  name = waitingroom[i]
  name = str(name)
  name = split(task)
  namedig1 = name[0]
  namedig2 = name[1]
  nameID = str(namedig1 + namedig2)


#get duration
for i in range (0,5):
  task = waitingroom[i]
  task = str(task)
  task = split(task)
  taskdig1 = task[2]
  taskdig2 = task[3]
  taskID = str(taskdig1 + taskdig2)
  taskname = str(["select TaskName from Task where TaskID like", TaskID])
  taskduration = str(["select TaskDuration from Task where TaskID like", TaskID])
  taskscore = str(["select TaskScore from Task where TaskID like", TaskID])
  

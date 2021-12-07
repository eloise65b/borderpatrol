def split(word):
    return [char for char in word]

#get reference number
waitingroom = []
currenttasks = []
importperson()
for i in range (0,5):
  person = importperson()
  waitingroom.append(person)
  
#move scheduling algorithms

#get duration
for i in range (0,5):
  task = waitingroom[i]
  task = str(task)
  task = split(task)
  taskdurdig1 = task[3]
  taskdurdig2 = task[4]
  taskarray = ["select TaskDuration from Task where TaskID like", TaskID]
 

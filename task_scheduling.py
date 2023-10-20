'''
TASK SCHEDULING


Given an array task_memory of n positive integers representing the amount of memory required to process each task, an array task_type 
of n positive integers representing the type of each task, and an integer max_memory. Find the minimum amount of time required for the 
servers to process all the tasks.

Each task takes 1 unit of time to process. The server can process at most two tasks in parallel only if they are of the same type and
together require no more than max_memory units of memory

Example:
Suppose n = 4, task_memory = [7, 2, 3, 9], task_type = [1, 2, 1, 3], and max_memory = 10.
Output = 3


Complete the 'getMinTime' function below.

The function is expected to return an INTEGER, the minmum time required to process all tasks.
The function accepts following parameters:
    1. INTEGER_ARRAY task_memory, the memory required by the tasks
    2. INTEGER_ARRAY task_type, the type of the tasks
    3. INTEGER max_memory, the maximum total memory that can be allocated to the tasks

Constraints:
1 ≤ n ≤ 2*105
1 ≤ max_memory ≤ 109
1 ≤ task_memory[i] ≤ max_memory
1 ≤ task_type[i] ≤ 109
'''


def getMinTime(task_memory, task_type, max_memory):
    tasks_by_type = {}

    # Iterate over the tasks and group them
    for t in range(len(task_memory)):
        memory = task_memory[t]
        type = task_type[t]

        if type not in tasks_by_type:
            tasks_by_type[type] = [] 
        
        tasks_by_type[type].append(memory)

    #Sort the tasks in each type group in descending order of memory requirement
    [tasks_by_type[typ].sort(reverse=True) for typ in tasks_by_type]

    countTime = 0
    
    # Iterate through sorted groups and schedule tasks efficiently
    for tasks in tasks_by_type.values(): 
        i = 0
        while i < len(tasks):
            # Check if there are at least 2 tasks of the same type to process in parallel
            if i + 1 < len(tasks) and tasks[i] + tasks[i + 1] <= max_memory:
                # Process 2 tasks in parallel
                countTime += 1
                i += 2
            else:
                countTime += 1
                i += 1

    # Return the minmum time required to process all tasks            
    return countTime


memory = [7,2,3,9]
type = [1,2,1,3]
max = 10
print(getMinTime(memory,type,max))
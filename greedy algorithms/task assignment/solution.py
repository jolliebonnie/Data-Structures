# O(nlog(n)) time | O(n) space where n is the number of tasks - 
def taskAssignment (k, tasks):
    pairedTasks = []
    taskDurationsToIndices = getTaskDurationsToIndices(tasks)

    sortedTasks = sorted(tasks) # n log n
    for idx in range(k):
        task1Duration= sortedTasks[idx] 
        indicesWithTask1Duration = taskDurationsToIndices[task1Duration]
        task1Index = indicesWithTask1Duration.pop()

        task2SortedIndex = len(tasks) - 1 - idx # to join with the opposite one 
        
        task2Duration= sortedTasks[task2SortedIndex] 
        indicesWithTask2Duration = taskDurationsToIndices[task2Duration]
        task2Index = indicesWithTask2Duration.pop()

        pairedTasks.append([task1Index, task2Index])

    return pairedTasks

def getTaskDurationsToIndices(tasks): 
    taskDurationsToIndices = {}

    for idx, taskDuration in enumerate(tasks): # if the value is already in the dict
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(idx)

        else:
            taskDurationsToIndices[taskDuration] = [idx]

    return taskDurationsToIndices

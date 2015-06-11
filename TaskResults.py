#Module that holds information about all complete tasks

#Dictionary used task.GUID as the key
task_results = {}

#Input a TaskResult, it will be added to the dictionary
def new_task(aResult):
  task_results[aResult.task_guid] = aResult

#Returns result of task associated with guid
def result(guid):
  return task_results[guid]

#Returns result list of task asociated with the guid list
def results(guid_list):
  the_results = []
  for guid in guid_list:
    the_results.append(task_results[guid])
  return the_results
  

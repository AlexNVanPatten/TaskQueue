#A clas that holds information about a completed task
class TaskResult:
  
  def __init__(self, GUID, success, return_code, output, exception, duration):
    #Unique identifier
    self.task_guid = GUID
    #True if task succeded, false if error was thrown
    self.succeeded = success
    #Gives return code if possible, None ohterwise
    self. return_code = return_code
    #Gives ouptut if possible, None otherwise
    self.output = output
    #Gives exception string for failed processes, None for succesful ones
    self.exception = exception
    #Gives the amount of time between the start of the process and it completing
    self.execution_duration = duration
    

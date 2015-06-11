import subprocess
import timeit
from TaskResult import TaskResult
import TaskResults
import uuid

#Class for tasks sent to the command line.
#Strings passed into the command field of the constructor should be
#valid command line code.
class Task:

  #Has fields: description (string) of the task. command (string) that will
  # be run when execute() is called. GUID (uuid), a unique identifier
  def __init__(self, description, command):
    self.description = description
    self.command = command
    self.GUID = uuid.uuid4()

  #Function to execute the command
  def execute(self):
    #The branch where command works.
    try:
      start = timeit.default_timer()
      output = subprocess.check_output(self.command)
      end = timeit.default_timer()
      #(Guid, True for execution worked, 0 for success return_code, the output,
      # no error string, and end - start gives execution duration
      task_result = TaskResult(self.GUID, True, 0, output, None, (end - start))
      TaskResults.new_task(task_result)

    #Branch for a command that throws an error that can be processed.
    except subprocess.CalledProcessError as e:
      end = timeit.default_timer()
      #Guid, False for a failed execution, the failed return code, the
      #normal output, the exception string, and the time it took before failure
      task_result = TaskResult(self.GUID, False, e.returncode, e.output,
                               str(e), (end - start))
      TaskResults.new_task(task_result)

    #Branch for commands that throw errors that cannot be processed
    except Exception as e:
      end = timeit.default_timer()
      #Guid, False for failure, no return code can be salvaged, no output
      #exists, string for the error message, and time before failure.
      task_result = TaskResult(self.GUID, False, None, None,
                               str(e), (end - start))
      print("\nError: Task threw a non-typical error, make sure command is "
            + "valid.\n Command: " + self.command)
      TaskResults.new_task(task_result)
    

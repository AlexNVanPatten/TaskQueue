# TaskQueue
This repository contains a simplistic TaskQueue which stores Tasks, which themselves store command line arguments that can be executed. The aftermath of running a Task is stored in a TaskResult, and all task results in a given session are stored within TaskResults. Next I will explain what functions each file has.

##Task.py
A task is created with Task(description, command) and has fields as follows
* description(string): Statement of what the command does.
* command(string): A command line argument stored in string form.
* GUID: The unique identifier witten in canonical format
  
Task has the following method
* execute(): Executes the command, and stores data in TaskResults
  
##TaskQueue.py
A TaskQueue is created with TaskQueue(), the fields should not be accessed directly.

TaskQueue has the following methods:
 * push(Task): Adds Task to the Queue
 * pop(): Takes away the Task at the queue's end and returns
 * peek_all(): Returns a list of all Tasks in queue
 * peek_next(): Shows the Task at the end of the queue, but does not remove from Queue
 * count(): Returns the number of Tasks left in the Queue

##TaskResult
A TaskResult is created with TaskResult(task\_guid, succeeeded, return_code, output, exception, execution duration) and has the following fields
 * task_guid : GUID of the Task that created this result
 * succeeded : True if task succeded, false if error was thrown
 * return_code: Stores return code from execution, None if execution failed without a return code
 * output: Stores output from execution, None if execution failed without a return code
 * exception: Stores exception string for failed processes, None for succesful ones
 * execution_duration: Time between task starting and either completing or failing
 
A TaskResult has no methods.

##TaskResults
TaskResults is a module, and as such has no constructors, but does have one floating variable
* task_results: A dictionary of all TaskResults, where the key is the tasks GUID

TaskResults has the following methods
* new_task(TestResult): Takes a testResult and inserts it into the dictionary
* result(GUID): returns the task associated with the GUID
* results(GUID list): returns lsit of tasks associated with list of GUIDS

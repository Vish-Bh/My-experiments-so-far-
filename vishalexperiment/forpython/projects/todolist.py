import json
with open('jos.json', 'r') as file:
    tasks=json.load(file)
if __name__=='__main__':
    print(102)

# print(tasks)
def add_task(task_id,task_name,task_status=False):
    tasks[task_id]={"task_name":task_name,"task_status":task_status}
    print(f'Task id:{task_id} task Name:{task_name} Done:{task_status} saved')
def remove_task(task_id, task_name=None, task_status=None):
    if task_id in tasks.keys():
        del tasks[task_id]
        print(f'Task deleted with id {task_id}')
    else:
        print('Error')
def show_tasks():
    for task in tasks:
        print(f' THE ID {task} is given the name of ""{tasks[task]['task_name']}"" and it is {tasks[task]['task_status']}')
i=0
show_tasks()
for i in range(1,3):
    user_input=input('Enter the id')
    task_name=input('NAMe')
    status=input('STATUS')
    add_task(user_input,task_name,status)
    show_tasks()
    i+=1
with open('jos.json', 'w') as idk:
    json.dump(tasks,idk,indent=5)    
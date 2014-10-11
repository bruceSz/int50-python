def parse_arg(str_input):
    lines = str_input('\n')
    first_line = str_input[0]
    number_task = first_line.partition('=')[2]
    dep_dict = {}
    for i in range(1,len(lines)):
        dep = lines[i]
        task_tmp = dep.partition('->')[0]
        depes = dep.partition('->')[2]
        task_list = depes.split(',')
        if not task_tmp in dep_dict:
            dep_dict[task_tmp]=set(task_list)

        else:
            cur_deps = dep_dict[task_tmp]
            for task in task_list:
                if not task in cur_deps:
                    cur_deps.add(task)


    return number_task,dep_dict

class Task:
    def __init__(self,node,root,dep):
        self.node = node
        self.root = root
        self.dep = dep


def findDepRoots(dep_dict):
    for n in dep_dict
    
    

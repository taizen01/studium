import os
import time
os.system('cls')

lst = {1:"Planning", 2:"Design", 3:"Coding", 4:"Testing"}
time_spent = [0,0,0,0]


def log_time(task):
    task = int(task)
    eingabe = float(input("How many hours did you spent on this task? "))
    time_spent[task-1] = time_spent[task-1] + eingabe
    time.sleep(1)
    print(f' task noted for {lst[task]}!\n')
    time.sleep(1)
    return
    

while True:
    try:
        os.system('cls')
        eingabe = input("Choose tasks: 1: Planning  2: Design  3: Coding  4: Testing or type exit: ")
        if eingabe == 0 or eingabe == "exit":
            break
        elif lst[int(eingabe)] in lst:
            print("Zahl zwischen 1-4 eingeben.")
        else:
            log_time(eingabe)
    except KeyError:
        print('Das hast keine Zahl angegeben.')
        continue


        
print("Summary of time spent on tasks: \n")
for i in range(1,len(lst)+1):
    print(f'{lst[i]}: {time_spent[i-1]:.1f} hours spent.')

    
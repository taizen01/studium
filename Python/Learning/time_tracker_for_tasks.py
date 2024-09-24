import os
import time
os.system('cls')

lst = ["Planning", "Design", "Coding", "Testing"]
time_spent = [0,0,0,0]


def log_time(task):
    eingabe = float(input("How many hours did you spent on this task? "))
    time_spent[task-1] = time_spent[task-1] + eingabe
    time.sleep(1)
    print(f' task noted for {lst[task-1]}!\n')
    time.sleep(1)
    return
    

while True:
    try:
        os.system('cls')
        eingabe = int(input("Choose tasks: 1: Planning  2: Design  3: Coding  4: Testing or type exit: "))
        if eingabe == 0:
            break
        elif eingabe < 1 or eingabe > 4:
            print("Zahl zwischen 1-4 eingeben.")
        else:
            log_time(eingabe)
    except ValueError:
        print('Das hast keine Zahl angegeben.')
        continue


        
print("Summary of time spent on tasks: \n")
for i in range(len(lst)):
    print(f'{lst[i]}: {time_spent[i]:.1f} hours spent.')

    
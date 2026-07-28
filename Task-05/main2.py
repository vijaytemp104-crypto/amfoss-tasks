import curses
import os

def get_pids ():
    pids = []
    for item in os.listdir("/proc"):
        if item.isdigit():
            pids.append(int(item))

    pids.sort()

    return pids

def get_process_name(pid):
    try:
        with open("/proc/" + str(pid) + "/comm") as file:
            name = file.read().strip()
        return name
    except(FileNotFoundError, PermissionError):
        return None

        

def get_memory(pid):
    try:
        with open("/proc/" + str(pid)+ "/status") as file:
            for line in file:
                if line.startswith("VmRSS:"):
                    parts = line.split()
                    memory_kb = int(parts[1])

                    return memory_kb / 1024
        return 0


    except(FileNotFoundError, PermissionError):
        return None


def get_total_cpu_time():
    with open("/proc/stat") as file:
        first_line = file.readline()

    values = first_line.split()[1:9]
    
    total_cpu_time = 0

    for value in values:
        total_cpu_time += int(value)

    return total_cpu_time


def get_process_cpu_time(pid):
    try:
        with open(f"/proc/{pid}/stat") as file:
            data = file.read()

        closing_bracket = data.rfind(")")
        values = data[closing_bracket +2:].split()

        user_time = int(values[11])
        system_time = int(values[12])

        return user_time + system_time

    except(FileNotFoundError, PermissionError):
        return None


def get_cpu(process):
    return process["cpu"]


def main(screen):
    try:
        curses.curs_set(0)
    except curses.error:
        pass

    screen.timeout(500)



    previous_total_time = get_total_cpu_time()
    previous_process_times = {}
    
    for pid in get_pids():
        process_time = get_process_cpu_time(pid)

        if process_time is not None:
            previous_process_times[pid] = process_time
    


    while True:

       
        pids = get_pids()

        current_total_time = get_total_cpu_time()
        total_change = current_total_time - previous_total_time
        cpu_percentages = {}
        cpu_count = os.cpu_count()


        
        for pid in pids:
            current_process_time = get_process_cpu_time(pid)

            if current_process_time is None:
                continue
            
            if pid in previous_process_times and total_change > 0:
                process_change = (current_process_time - previous_process_times[pid])

                cpu_percentages[pid] = (process_change/total_change *cpu_count *100)

            else:
                cpu_percentages[pid] = 0

            previous_process_times[pid] = current_process_time


        previous_total_time = current_total_time


       
        processes = []
        for pid in pids:
            name = get_process_name(pid)
            memory = get_memory(pid)

            if name is None or memory is None:
                continue
            cpu = cpu_percentages.get(pid,0.0)
            
            process ={
                    "pid" : pid,
                    "name" : name,
                    "cpu" : cpu,
                    "memory" : memory
                    }
            processes.append(process)
     
            processes.sort(key =get_cpu, reverse = True)



        screen.erase()

        height, width = screen.getmaxyx()
        
        screen.addstr(0,0,"Grand Line Guardian")
        
        screen.addstr(1,0, "Total Process: " + str(len(pids)))
        
        heading =( f"{'PID':<10}"
                   f"{'PROCESS NAME':<30}"
                  f"{'CPU %' : >10}"
                  f"{'MEMORY(MB)':>15}"
                  )
        screen.addstr(3,0, heading)

        row = 4
        for process in processes:
            
            if row >= height -1:
                break

            pid = process["pid"]
            name = process["name"]
            cpu = process["cpu"]
            memory = process["memory"]


            line = (f"{pid:<10}"
            f"{name:30}"
            f"{cpu:>9.1f}%"
            f"{memory:>15.1f}"
            )
            screen.addstr(
                    row,0,line[:width -1]
            )
            row +=1

        controls = "q: Quit"

        screen.addstr(
            height - 1,
            0,
            controls[:width -1]
            )
        screen.refresh()

        key = screen.getch()
        if key == ord("q"):
            break
if __name__ == "__main__":
    curses.wrapper(main)

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


def main(screen):
    try:
        curses.curs_set(0)
    except curses.error:
        pass

    screen.timeout(500)

    while True:
        pids = get_pids()
        screen.erase()

        height, width = screen.getmaxyx()
        
        screen.addstr(0,0,"Grand Line Guardian")
        
        screen.addstr(1,0, "Total Process: " + str(len(pids)))
        
        heading =( f"{'PID':<10}"
                   f"{'PROCESS NAME':<30}"
                  f"{'MEMORY(MB)':>15}"
                  )
        screen.addstr(3,0, heading)

        row = 4
        for pid in pids:
            
            if row >= height -1:
                break

            name = get_process_name(pid)
            memory = get_memory(pid)
            
            if name is None or memory is None :
                continue
            
            line = (f"{pid:<10}"
            f"{name:30}"
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

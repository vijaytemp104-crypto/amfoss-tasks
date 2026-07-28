import curses
import time

import psutil


def get_cpu(process):
    return process["cpu"]


def get_processes():
    processes = list(psutil.process_iter())

    for process in processes:
        try:
            process.cpu_percent()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(0.2)

    process_data = []

    for process in processes:
        try:
            pid = process.pid
            name = process.name()
            cpu_usage = process.cpu_percent()
            memory_usage = process.memory_info().rss / (1024 * 1024)

            process_data.append({
                "pid": pid,
                "name": name,
                "cpu": cpu_usage,
                "memory": memory_usage
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    
    process_data.sort(key=get_cpu, reverse=True)

    return process_data


def display_processes(screen, processes):
    screen.erase()

    height, width = screen.getmaxyx()

    if height < 7 or width < 50:
        message = "Terminal window is too small"
        screen.addstr(0, 0, message[:width - 1])
        screen.refresh()
        return

    screen.addstr(0, 0, "Grand Line Guardian", curses.A_BOLD)
    screen.addstr(1, 0, f"Total Active Processes: {len(processes)}")

    header = (
        f"{'PID':<10}"
        f"{'PROCESS NAME':<30}"
        f"{'CPU %':>10}"
        f"{'MEMORY (MB)':>15}"
    )

    screen.addstr(3, 0, header[:width - 1], curses.A_REVERSE)

    maximum_rows = height - 5

    for index, process in enumerate(processes[:maximum_rows]):
        row = index + 4

        line = (
            f"{process['pid']:<10}"
            f"{process['name'][:29]:<30}"
            f"{process['cpu']:>9.1f}%"
            f"{process['memory']:>15.1f}"
        )

        screen.addstr(row, 0, line[:width - 1])

    screen.addstr(height - 1, 0, "q: Quit", curses.A_BOLD)
    screen.refresh()


def main(screen):
    try:
        curses.curs_set(0)
    except curses.error:
        pass

    
    screen.nodelay(True)

    while True:
        key = screen.getch()

        if key == ord("q"):
            break

        processes = get_processes()
        display_processes(screen, processes)

        time.sleep(0.3)


curses.wrapper(main)

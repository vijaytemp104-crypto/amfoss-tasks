import os
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


# Displays the collected process information as a table.
def display_processes(processes):
    print("Grand Line Guardian")
    print(f"Total Active Processes: {len(psutil.pids())}")
    print()

    print(
        f"{'PID':<10} "
        f"{'PROCESS NAME':<30} "
        f"{'CPU %':<10} "
        f"{'MEMORY (MB)':<12}"
    )

    print("-" * 68)

    for process in processes:
        print(
            f"{process['pid']:<10} "
            f"{process['name'][:29]:<30} "
            f"{process['cpu']:<10.1f} "
            f"{process['memory']:<12.1f}"
        )


try:
    while True:
        processes = get_processes()

        os.system("clear")
        display_processes(processes)

        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nGrand Line Guardian stopped.")

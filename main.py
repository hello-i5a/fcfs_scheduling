class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_fcfs(processes):
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time = process.completion_time

def display_gantt_chart(processes):
    print("\nGantt Chart:")
    print(" " + " -- ".join(p.pid for p in processes))
    time_labels = ["0"]
    current_time = 0
    for process in processes:
        current_time = max(current_time, process.arrival_time) + process.burst_time
        time_labels.append(str(current_time))
    print(" |".join(time_labels))

def print_process_summary(processes):
    print("\nProcess Summary:")
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

def calculate_average_waiting_time(processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    average_waiting_time = total_waiting_time / len(processes)
    return average_waiting_time

def main():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        pid = chr(65 + i)  # Process IDs as A, B, C, ...
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        processes.append(Process(pid, arrival_time, burst_time))

    # Sort processes by arrival time for FCFS
    processes.sort(key=lambda x: x.arrival_time)

    calculate_fcfs(processes)
    display_gantt_chart(processes)
    print_process_summary(processes)

    avg_waiting_time = calculate_average_waiting_time(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f} ms")

if __name__ == "__main__":
    main()

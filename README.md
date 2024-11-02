# CPU Scheduling Algorithm: First-Come-First-Serve (FCFS)

This python program simulates CPU scheduling using the First-Come-First-Serve (FCFS) algorithm. It calculates and displays various metrics for each process, including waiting time and turnaround time, as well as a Gantt chart to visualize the scheduling.

## Features

- Input for process arrival times and burst times.
- Calculation of completion time, turnaround time, and waiting time for each process.
- Display of a Gantt chart showing the order of execution.
- Calculation and display of the average waiting time for all processes.

## Explanation of the Code

1. **Process Class**:

   - Defines a structure to hold information about each process:
     - `pid`: Process ID (character identifier).
     - `arrival_time`: Time at which the process arrives in the ready queue.
     - `burst_time`: Time required by the process for CPU execution.
     - `completion_time`: Time at which the process completes execution.
     - `turnaround_time`: Total time from arrival to completion.
     - `waiting_time`: Total time the process waits in the ready queue.

2. **`calculate_fcfs` Function**:

   - Implements the FCFS scheduling algorithm, updating completion, turnaround, and waiting times based on the processes' burst and arrival times.

3. **`display_gantt_chart` Function**:

   - Displays a Gantt chart representing the order of process execution with corresponding completion times.

4. **`print_process_summary` Function**:

   - Summarizes each process's details, including arrival time, burst time, completion time, turnaround time, and waiting time.

5. **`calculate_average_waiting_time` Function**:

   - Calculates the average waiting time for all processes.

6. **`main` Function**:
   - Manages user interaction, collecting inputs for the number of processes, arrival times, and burst times.

## User Interaction

When the program runs, the user is prompted to enter:

1. The number of processes.
2. For each process:
   - Arrival time
   - Burst time

After entering all processes, the program will display:

- A Gantt chart showing execution order and completion times.
- A summary of each process's metrics.
- The average waiting time for all processes.

## Running the Program

To run the program, follow these steps:

1. **Python Environment**: Ensure you have Python installed. Download it from [python.org](https://www.python.org/).

2. **Create a Python File**:

   - Open a text editor or IDE.
   - Copy the provided code into a new file and save it as `main.py`.

3. **Execute the Program**:

   - Open a terminal or command prompt.
   - Navigate to the directory where you saved `main.py`.
   - Run the program using the command:
     ```bash
     python main.py
     ```
   - Follow the on-screen prompts to enter the number of processes and their respective arrival and burst times.

4. **View Results**: After entering the data, the program will display the Gantt chart, process summary, and average waiting time in the terminal.

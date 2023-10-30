# Advanced Process Manager with Process Synchronization

## Implemented Functionalities

This repository contains an Advanced Process Manager with Process Synchronization. The implemented functionalities include:

1. **Creating and Managing Processes**
   - You can create new processes by calling the `create_process(command)` function, where `command` is the command you want to execute.

2. **Creating and Managing Threads**
   - Threads can be created using the `create_thread(target_function)` function. Specify the target function you want to run as a thread.

3. **Inter-Process Communication (IPC) with Shared Memory**
   - Shared memory communication is achieved using the `ipc_operation(position, value)` function, allowing the modification of the global shared memory in `process_manager.py`.

4. **Process Listing and Termination**
   - You can list all running processes and terminate a specific process using the `list_processes()` and `terminate_process(pid)` functions.

5. **Viewing Process Information**
   - Retrieve information about a specific process using the `view_process_info(pid)` function. It returns process details if the process exists, or None if the process is not found.

6. **Thread Termination**
   - To terminate a thread, use the `terminate_thread(thread)` function, passing the thread object to be terminated.

## Installation Instructions

To use this Advanced Process Manager, follow these installation instructions:

1. Clone the project repository from GitHub.
2. Install the required dependencies (e.g., psutil, subprocess) using pip.
3. Run the main script, `process_manager.py`, in your Python environment.

## Usage

Start the application by running `process_manager.py`. You can modify the main.py script if needed. The menu system in `main.py` allows you to perform various actions, including creating and managing processes, threads, and other functionalities.

The available actions in the menu system include:

1. Creating a New Process
2. Creating a New Thread
3. Inter-Process Communication (IPC)
4. Listing Processes
5. Terminating a Process
6. Viewing Process Information
7. Terminating a Thread
8. Monitoring Running Processes
9. Exit

## Test Results

### 1. Creating a New Process

- **Description**: Created a new process by taking a command.
- **Explanation**: Users can provide a command to start a new process, and the system logs the process creation.

### 2. Creating a New Thread

- **Description**: Create a new thread from taking the name of a function.
- **Explanation**: Users can specify a target function to run in a new thread, and the system logs the thread's start.

### 3. Inter-Process Communication (IPC)

- **Description**: There can be Inter-Process Communication.
- **Explanation**: Processes and threads can gain access to shared memory.

### 4. Listing Processes

- **Description**: Successfully listed active processes.
- **Explanation**: Users can view a list of currently active processes, including their PIDs, names, PPIDs, and statuses.

### 5. Terminating a Process

- **Description**: Process can be successfully terminated knowing their PID.
- **Explanation**: Users can enter a PID to terminate a specific process, and the system logs the termination action.

### 6. Viewing Process Information

- **Description**: Successfully viewed process information.
- **Explanation**: Users can provide a PID to view detailed information about a specific process.

### 7. Terminating a Thread

- **Description**: Successfully terminated a thread.
- **Explanation**: Users can specify a thread to terminate, and the system logs the thread's termination.

### 8. Monitor Running Processes

- **Description**: Successfully monitor running processes.
- **Explanation**: Process activity can be monitored.

## Discussion on Project Results

The menu system can still be refined to improve user-friendliness. It's worth noting that users without programming knowledge may find it challenging to make full use of the program due to its technical nature.

Despite some rough edges, the program can successfully achieve the majority of the intended functions. Further development and user interface improvements could enhance the overall user experience.
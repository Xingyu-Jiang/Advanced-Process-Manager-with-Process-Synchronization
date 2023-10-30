import sys
from process_manager import *


def sampleUserFunction():
    for i in range(10):
        return i


# Define a dictionary to map user input to functions
function_mapping = {
    "sampleUserFunction": sampleUserFunction
    # Add more mappings for other functions
}


# Function to display the main menu
def display_menu():
    print("\nProcess Manager Menu:")
    print("1. Create a new process")
    print("2. Create a new thread")
    print("3. Perform IPC operation")
    print("4. Terminate a process")
    print("5. View process information")
    print("7. Terminate a thread")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        return -1


# Main menu loop
while True:
    choice = display_menu()

    if choice == 1:
        print("Enter the command to start a new process. For example, you can enter 'python your_script.py'")
        cmd = input("Command: ")
        new_process = create_process(cmd)
        if new_process:
            print(f"Process {new_process.get_pid()} started with PID: {new_process.get_pid()}")

    elif choice == 2:
        target_function = input("Enter the name of the target function for the thread: ")
        if target_function in function_mapping:
            function = function_mapping[target_function]
            thread = create_thread(function)
            print(f"Thread {thread.thread.ident} started with PID: {thread.thread.ident}")
        else:
            print("Function not found.")
    elif choice == 3:
        position = int(input("Enter the shared memory position: "))
        value = int(input("Enter the value to set: "))
        ipc_operation(position, value)
    elif choice == 4:
        pid = int(input("Enter the PID of the process to terminate: "))
        terminate_process(pid)
    elif choice == 5:
        pid = int(input("Enter the PID of the process to view information: "))
        process_info = view_process_info(pid)
        if process_info:
            print(f"Process Information: {process_info}")
        else:
            print(f"No such process with PID {pid}")
    elif choice == 6:
        thread = input("Enter the thread terminate: ")
        terminate_thread(thread)
    elif choice == 7:
        print("Exiting Process Manager.")
        sys.exit(0)
    else:
        print("Invalid choice. Please select a valid option.")

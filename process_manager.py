import logging
import multiprocessing
import psutil
import subprocess
import threading
import time

# Global variables for process and thread management
processes = []
threads = []

# A simple synchronization mechanism
thread_lock = threading.Lock()

# Shared memory object for communication
shared_data = multiprocessing.Array('i', [0, 0, 0])  # 'i' is the type code for integers

# Initialize the logger (moved outside the main function for testing)
logging.basicConfig(filename="process_manager.log", level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define semaphores
buffer_mutex = threading.Semaphore(1)  # Mutex for controlling access to the buffer
items = []  # Shared buffer
empty_slots = threading.Semaphore(10)  # Number of available slots in the buffer
items_count = threading.Semaphore(0)  # Number of items in the buffer


# Class definitions for Process
class Process:
    def __init__(self, cmd, shared_data):
        self.process = None
        self.pid = None
        self.cmd = cmd
        self.shared_data = shared_data  # Pass the shared data object

    def start(self):
        self.process = subprocess.Popen(self.cmd)
        self.pid = self.process.pid
        logging.info(f"Process {self.pid} started with command: {self.cmd}")

    def get_pid(self):
        return self.pid

    def access_shared_memory(self, position):
        with self.shared_data.get_lock():
            # Access and modify shared data safely
            self.shared_data[position] = self.pid


# Class definitions for Thread Class
class Thread:
    def __init__(self, target, shared_data):
        self.thread = threading.Thread(target=target)
        self.shared_data = shared_data  # Pass the shared data object

    def start(self):
        self.thread.start()
        logging.info(f"Thread {self.thread.ident} started")

    def join(self):
        self.thread.join()
        logging.info(f"Thread {self.thread.ident} finished")


# Function for creating processes
def create_process(command):
    process = Process(command, shared_data)
    process.start()
    processes.append(process)
    return process


# Function for listing processes
def list_processes():
    process_infos = []  # Changed variable name for clarity
    for process in psutil.process_iter(attrs=["pid", "name", "ppid", "status"]):
        # noinspection PyUnresolvedReferences
        info = process.info
        process_infos.append({
            "PID": info["pid"],
            "Name": info["name"],
            "PPID": info["ppid"],
            "Status": info["status"],
        })
    return process_infos


# Function for terminating a process
def terminate_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        process.wait()
        logging.info(f"Process {pid} terminated")
        return True
    except psutil.NoSuchProcess:
        logging.warning(f"Attempted to terminate a non-existent process with PID {pid}")
        return False  # The Process doesn't exist


# Function for monitoring processes
def monitor_processes(interval=10):
    while True:
        processes = list_processes()
        for process in processes:
            print(
                f"PID: {process['PID']}, Name: {process['Name']}, PPID: {process['PPID']}, Status: {process['Status']}")
        time.sleep(interval)


# Function for viewing process information
def view_process_info(pid):
    try:
        process = psutil.Process(pid)
        info = process.as_dict(attrs=["pid", "name", "ppid", "status", "cpu_percent", "memory_percent"])
        return info
    except psutil.NoSuchProcess:
        return None  # The Process doesn't exist


# Function for creating a thread
def create_thread(target_function):
    thread = Thread(target_function, shared_data)
    thread.start()
    threads.append(thread)
    return thread


# Function for terminating a thread
def terminate_thread(thread):
    try:
        thread.join()  # Wait for the thread to finish
        logging.info(f"Thread {thread.thread.ident} terminated")
        return True
    except Exception as e:
        logging.error(f"Error terminating thread: {str(e)}")
        return False


def ipc_operation(position, value):
    with shared_data.get_lock():
        shared_data[position] = value
    logging.info(f"Set shared memory position {position} to {value}")

import unittest
from process_manager import *
import time


class ProcessManagerTestCase(unittest.TestCase):
    def test_create_and_list_process(self):
        # Create a process
        command = ["ping", "localhost", "-n", "100"]
        process = create_process(command)

        # Get the PID of the created process
        created_pid = process.get_pid()

        # Add a delay to allow the process to start
        time.sleep(1)  # Wait for 1 second

        # List processes
        processes = list_processes()

        # Diagnostic information
        print("Expected PID:", created_pid)
        print("List of PIDs:", [p["PID"] for p in processes])

        # Check if the created process is in the list
        found = False
        for process_info in processes:
            if process_info["PID"] == created_pid:
                found = True
                break

        # Assert the result
        self.assertTrue(found, f"Process with PID {created_pid} not found in the list of processes.")

    def test_terminate_process(self):
        # Create a process
        command = ["ping", "localhost", "-n", "100"]
        process = create_process(command)

        # Get the PID of the created process
        created_pid = process.get_pid()

        # Add a delay to allow the process to start
        time.sleep(1)  # Wait for 1 second

        # Terminate the process
        result = terminate_process(created_pid)

        # Add a delay to ensure the process is terminated
        time.sleep(1)

        # List processes
        processes = list_processes()

        # Check if the process is terminated
        found = False
        for process_info in processes:
            if process_info["PID"] == created_pid:
                found = True
                break

        # Assert the results
        self.assertTrue(result, f"Process termination failed for PID {created_pid}.")
        self.assertFalse(found, f"Terminated process with PID {created_pid} is still in the list of processes.")

    def test_view_process_info(self):
        # Create a process
        command = ["ping", "localhost", "-n", "5"]
        process = create_process(command)

        # Get the PID of the created process
        created_pid = process.get_pid()

        # Add a delay to allow the process to start
        time.sleep(1)  # Wait for 1 second

        # View detailed information about the process
        process_info = view_process_info(created_pid)

        # Assert that the process information is not None
        self.assertIsNotNone(process_info, f"Process information not available for PID {created_pid}.")

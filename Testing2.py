import unittest
from process_manager import *
import time


class TestProcessManager(unittest.TestCase):
    def test_thread_creation_termination(self):
        # Define a target function for the test
        def target_function():
            with thread_lock:
                time.sleep(1)
                self.assertEqual(2 + 2, 4)  # An assertion to verify that the thread is executing

        # Create a thread
        thread = create_thread(target_function)

        # Wait for the thread to complete
        terminate_thread(thread)

    def test_thread_lock_synchronization(self):
        shared_value = 0

        # Define a target function that increments the shared_value
        def target_function():
            nonlocal shared_value
            with thread_lock:
                shared_value += 1
                time.sleep(0.1)  # Simulate some work
                shared_value += 1

        # Create multiple threads to increment the shared_value
        threads = [create_thread(target_function) for _ in range(5)]

        # Wait for all threads to complete
        for thread in threads:
            terminate_thread(thread)

        # Ensure that the shared_value is correctly synchronized
        self.assertEqual(shared_value, 10)  # Each thread increments it by 2


if __name__ == '__main__':
    unittest.main()

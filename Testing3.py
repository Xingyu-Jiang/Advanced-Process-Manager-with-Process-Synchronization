import unittest
from process_manager import *


class TestSharedMemoryIPC(unittest.TestCase):
    def test_shared_memory_access(self):
        # Create a test process
        test_command = ["python", "-c", "import time; time.sleep(1)"]
        process = Process(test_command, shared_data)
        process.start()
        process.access_shared_memory(0)

        # Wait for a short period to allow the process to access shared memory
        time.sleep(2)  # Wait for 2 seconds to ensure the process has time to run and access shared memory

        # Check if the process has modified the shared memory
        self.assertEqual(shared_data[0], process.pid)

        # Clean up - terminate the test process
        process.process.terminate()
        process.process.wait()


if __name__ == '__main__':
    unittest.main()

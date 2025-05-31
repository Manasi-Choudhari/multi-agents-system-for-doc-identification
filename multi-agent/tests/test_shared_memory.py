import os
import json
from shared_memory import SharedMemory

def test_log_and_retrieve():
    test_db = "test_memory.db"
    if os.path.exists(test_db):
        os.remove(test_db)

    mem = SharedMemory(test_db)
    thread_id = "test-thread-1"
    mem.log("TestSource", "TestType", "Test info", thread_id)
    mem.save_extracted(thread_id, "field1", "value1")
    mem.save_extracted(thread_id, "field2", "value2")

    logs = mem.get_thread_logs(thread_id)
    extracted = mem.get_extracted_values(thread_id)

    assert len(logs) == 1
    assert logs[0]["source"] == "TestSource"
    assert extracted == {"field1": "value1", "field2": "value2"}

    os.remove(test_db)

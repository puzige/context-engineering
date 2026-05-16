from task_tracker.main import create_task

def test_create_task():
    result = create_task("Buy milk")
    assert "Buy milk" in result
    assert "success" in result.lower()

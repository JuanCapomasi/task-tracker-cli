import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(task.name, "Test task")
        self.assertEqual(task.status, "todo")
        self.assertEqual(task.id, 0)

    def test_delete_task_valid(self):
        task = self.manager.add_task("Delete me")
        deleted = self.manager.delete_task(str(task.id))
        self.assertEqual(deleted.id, task.id)

    def test_update_task(self):
        task = self.manager.add_task("Old name")
        self.manager.update_task(f"{task.id} New name")
        self.assertEqual(self.manager.tasks[0].name, "New name")

    def test_mark_task_done(self):
        task = self.manager.add_task("Mark test")
        self.manager.mark_task(f"{task.id} done")
        self.assertEqual(task.status, "done")

    def test_list_tasks(self):
        self.manager.add_task("One")
        self.manager.add_task("Two")
        tasks = self.manager.tasks
        self.assertEqual(len(tasks), 2)

    def test_delete_invalid_id(self):
        deleted = self.manager.delete_task("999")
        self.assertIsNone(deleted)

    def test_mark_invalid_status(self):
        task = self.manager.add_task("Invalid mark")
        self.manager.mark_task(f"{task.id} bananas")
        self.assertEqual(task.status, "todo")  # Should be unchanged

    def test_update_invalid_id(self):
        result = self.manager.update_task("999 NewName")
        self.assertIsNone(result)

    def test_mark_invalid_id(self):
        result = self.manager.mark_task("999 done")
        self.assertIsNone(result)

    def test_id_continues_after_delete(self):
        task1 = self.manager.add_task("First")
        self.manager.delete_task(str(task1.id))
        task2 = self.manager.add_task("Second")
        self.assertEqual(task2.id, task1.id + 1)

        def test_add_empty_task(self):
            task = self.manager.add_task("")
            self.assertIsNone(task)

    def test_delete_non_integer_id(self):
        deleted = self.manager.delete_task("abc")
        self.assertIsNone(deleted)

    def test_update_task_no_args(self):
        result = self.manager.update_task("")
        self.assertIsNone(result)

    def test_mark_task_no_args(self):
        result = self.manager.mark_task("")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
from django.test import TestCase, client
from .models import Todo
import json
# Create your tests here.

class ToDoTestCase(TestCase):

    def setUp(self) -> None:
        Todo.objects.create(title="test_case_1")
        self.c = client.Client()
    
    def test_api(self):
        response = self.c.get("/api/")
        data = response.content.decode("utf-8")
        data = json.loads(data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["data"][0]["title"], "test_case_1")
    
    def test_index(self):
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '''<div id="all">''')
    
    def test_add(self):
        response = self.c.post("/add/", {"title": "test_case_2"}, content_type="application/json")
        data = response.content.decode("utf-8")
        data = json.loads(data)
        self.assertEqual(data["todo_title"], "test_case_2")

        response = self.c.get("/api/")
        data = response.content.decode("utf-8")
        data = json.loads(data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["data"][1]["title"], "test_case_2")
        

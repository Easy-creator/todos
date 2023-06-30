from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from tools.models import Todo

# Create your tests here.
class TodoAPITeastCase(APITestCase):
    def create_todo(self):
        sampletodo = {'title':'Hello', 'desc': 'Test'}
        return self.client.post(reverse('create_details'), sampletodo)

    def authenticate(self):
        self.client.post(reverse('register'), {'username': 'username', 'email':'email@gmail.com', 'password': 'password1'})
        response = self.client.post(reverse('login'), {'email':'email@gmail.com', 'password': 'password1'})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

class TestListCreateTodos(TodoAPITeastCase):

    def test_create_todo_with_no_header(self):
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_create_todo_with_header(self):
        self.authenticate()
        previous_todo_count = Todo.objects.all().count()
        response = self.create_todo()
        self.assertEqual(Todo.objects.all().count(), previous_todo_count +1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Test')

    def test_retrieve_all_todo(self):
        self.authenticate()
        response = self.client.get(reverse('create_details'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list )

        self.create_todo()

        res = self.client.get(reverse('create_details'))
        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)

class TestTodoUpdate(TodoAPITeastCase):

    def test_retrieve_item(self):
        self.authenticate()
        res = self.create_todo()

        resp = self.client.get(reverse("update", kwargs={"id": res.data["id"]}))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        todo = Todo.objects.get(id=res.data['id'])
        self.assertEqual(todo.title, res.data['title'])

    def test_updateitem(self):
        self.authenticate()
        res = self.create_todo()
         
        response = self.client.patch(reverse("update", kwargs={"id": res.data["id"]}), {'title':'new Title', 'is_complete': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        update_todos = Todo.objects.get(id=response.data["id"])
        self.assertEqual(update_todos.is_complete, True)
        self.assertEqual(update_todos.title, 'new Title')

    def test_delete_item(self):
        self.authenticate()
        res = self.create_todo()

        previous_db = Todo.objects.all().count()
        self.assertGreater(previous_db, 0)
        self.assertEqual(previous_db, 1)

        response = self.client.delete(reverse("update", kwargs={"id": res.data["id"]}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.all().count(), 0)
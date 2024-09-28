from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from todo.serializers import TodoSerializer

from todo.models import Todo
from todo import views


# Create your tests here.

class UserTest(TestCase):

    def setUp(self) -> None:

        Todo.objects.create(title ="Java", description = 'Java Tutorials', completed = 1)
        Todo.objects.create(title ="Python", description = 'Python Tutorials', completed = 1)

    
    def test_get_user(self):
        user1 = Todo.objects.get(title ='Java')
        user2 = Todo.objects.get(title ='Python')
        self.assertEqual(user1.getTitle(), user1.title)
        self.assertEqual(user2.getTitle(), user2.title)

    # def test_get_all_users(self):

    #     client = Client()
    #     # get API response
    #     response = client.get(reverse('list-users'))

    #     # get data from DB
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    # def test_create_user(self):

    #     client = APIClient()

    #     input_data = {
    #     "name": "Abhi kkk",
    #     "age": 24,
    #     "gender": "Male"
    #     }

    #     res = client.post(reverse('create-user'), data=input_data)
    #     self.assertEqual(res.data['name'], 'Abhi kkk')
    #     self.assertEqual(res.status_code, 201)

    # def test_post_user(self):

    #     input_data = {
    #     "name": "Amitkumar",
    #     "age": 24,
    #     "gender": "Male"
    #     }

    #     factory = APIRequestFactory()
    #     request = factory.post(reverse('create-user'), input_data, format='json')
    #     response = views.create_user(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    # def test_get_single_user(self):

    #     mohan = User.objects.create(name ="Mohan", age = 30, gender='Male')
    #     client = APIClient()
    #     response = client.get(reverse('single-user'), args= {'pk' :mohan.pk})

    #     user = User.objects.get(pk=mohan.pk)
    #     serializer = UserSerializer(user)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_get_invalid_user(self):

    #     client = APIClient()

    #     response = client.get(reverse('single-user'), args={'pk': 30})
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        










        


        

        
       
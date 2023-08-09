from django.test import TestCase, Client
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post
from blog.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, post


class PostModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a post for testing
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
    
    def test_str_representation(self):
        self.assertEqual(str(self.post), 'Test Post')
    
    def test_absolute_url(self):
        expected_url = '/post/1/'.format(self.post.pk)
        self.assertEqual(self.post.get_absolute_url(), expected_url)

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
        self.post_id = self.post.id
        

    def test_post_list_view(self):
        request = self.factory.get(reverse('post-home'))
        response = PostListView.as_view()(request)
        response2 = self.client.get(reverse('post-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response2, 'blog/post_home.html')

    def test_post_detail_view(self):
        request = self.factory.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        response = PostDetailView.as_view()(request, pk=self.post.pk)
        response2 = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response2, 'blog/post_detail.html')

    def test_post_create_view(self):
        data = {'title': 'New Post', 'content': 'This is a new post.', 'author': self.user.id}
        self.client.login(username = 'testuser', password = 'testpassword')
        response = self.client.post(reverse('post-create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post-detail', args = [self.post_id +1]))

    def test_post_update_view(self):
        data = {'title': 'Updated Post', 'content': 'This post has been updated.', 'author': self.user.id}
        self.client.login(username = 'testuser', password = 'testpassword')
        response = self.client.post(reverse('post-update',args = [self.post_id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post-detail', args = [self.post_id]))
       
    def test_post_delete_view(self):
        self.client.login(username = 'testuser', password = 'testpassword')
        response = self.client.post(reverse('post-delete',args = [self.post_id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post-home'))
    



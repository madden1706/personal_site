from django.test import TestCase
from .models import BlogPost
import datetime
from django.utils import timezone
from django.urls import reverse

# Create your tests here.


def create_post(title, date, post, publishable):
    """
    :param title: Title of a blog post.
    :param date: Date of the blog post.
    :param post: Content of a blog post.
    :return: A blog post with a specified date, +int for future (days) and -int for past.
    """

    time = timezone.now() + datetime.timedelta(days=date)
    return BlogPost.objects.create(title_of_post=title, date_of_post=time, blog_post=post, publish=publishable)


class BlogPostTests(TestCase):

    def test_future_post(self):
        """
        Test to see if posts from a future date are hidden from the BlogHomepage view.
        :return:
        """
        create_post("Title", 10, "Post text", True)
        response = self.client.get(reverse('blog:blog'))
        self.assertContains(response, "No blog posts are available.")
        self.assertQuerysetEqual(response.context['blog_home_list'], [])

    def test_future_post_in_archive(self):
        """
        Test to see if posts from a future date are hidden from the BlogArchive view.
        :return:
        """
        post = create_post("Title", 10, "Post text", True)
        year = post.date_of_post.year
        response = self.client.get(reverse('blog:blog_archive', args=[year]))
        #self.assertContains(response, "No blogs are available.")
        self.assertEqual(response.status_code, 404)

    def test_future_post_in_blog_archive_list(self):
        """
        Test to see if posts from a future date are hidden (the year of the post) from the BlogArchiveList view.
        :return:
        """
        post = create_post("Title", 10, "Post text", True)
        year = post.date_of_post.year
        response = self.client.get(reverse('blog:blog_archive_list'))
        self.assertNotContains(response, year)
        self.assertQuerysetEqual(response.context['years'], [])

    def test_past_post(self):
        """
        Test to see if posts from a past date are in the BlogHomepage view.
        :return:
        """
        post = create_post("Title", -10, "Post text", True)
        response = self.client.get(reverse('blog:blog'))
        self.assertContains(response, post.title_of_post)
        self.assertQuerysetEqual(response.context['blog_home_list'], ["<BlogPost: Title>"])

    def test_past_post_in_archive(self):
        """
        Test to see if posts from a past date are in the BlogArchive view.
        :return:
        """
        post = create_post("Title", -10, "Post text", True)
        year = post.date_of_post.year
        response = self.client.get(reverse('blog:blog_archive', args=[year]))
        #self.assertContains(response, "No blogs are available.")
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['posts'], ["<BlogPost: Title>"])

    def test_past_post_in_blog_archive_list(self):
        """
        Test to see if posts from a past date (the year of the post) are in the BlogArchiveList view.
        :return:
        """
        post = create_post("Title", -10, "Post text", True)
        year = post.date_of_post.year
        response = self.client.get(reverse('blog:blog_archive_list'))
        self.assertContains(response, year)
        self.assertQuerysetEqual(response.context['years'], [str(year)])

    def test_publishable_post(self):
        test_post = create_post("Title", -10, "Post text", True)
        url = reverse('blog:blog_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_post.title_of_post)   

    def test_not_publishable_post(self):
        test_post = create_post("Title", -10, "Post text", False)
        url = reverse('blog:blog_post', kwargs={'pk': test_post.id, 'slug': test_post.slug })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

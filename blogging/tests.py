from django.test import TestCase
from django.contrib.auth.models import User

from blogging.models import Post, Category
import datetime
from django.utils.timezone import utc


class PostTestCase(TestCase):
    fixtures = ["blogging_test_fixture.json"]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a post"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = "A category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    fixtures = ["blogging_test_fixture.json"]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count, text="foo", author=author)
            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get(
            "/"
        )  # self.client comes with TestCase, allows you to get the output you would've gotten with a web browser
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("New Blog Post Title" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get("/posts/%d/" % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)

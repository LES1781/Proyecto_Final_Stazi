from django.test import TestCase

from post.models import Post, Comment
class PostTests(TestCase):

    def test_post_has_an_name(self):
        post = Post.objects.create(title="Titulo de prueba")
        hola = Comment.objects.create(name="hola", post="Titulo de prueba")
        chau = Comment.objects.create(name="chau", post="Titulo de prueba")
        post.comment.set([hola.pk, chau.pk])
        self.assertEqual(post.comment.count(), 2)

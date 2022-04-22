from django.test import TestCase
from django.contrib.auth import get_user_model

from news import models


def sample_user(username="Testuser", password="Testpass"):
    """Create a sample user"""
    return get_user_model().objects.create_user(username, password)


class ModelTests(TestCase):
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "Testadmin", "Testpass123"
        )

        self.assertTrue(user.is_superuser)

    def test_article_str(self):
        article = models.Article.objects.create(
            author="Test author",
            title="Test title",
            description="Test description",
            body="Test body",
            location="Test location",
            publication_date="2000-01-01",
            active="True",
            created_at="2000-01-01",
            updated_at="2001-01-01",
        )
        self.assertEqual(str(article), f"{article.author} {article.title}")

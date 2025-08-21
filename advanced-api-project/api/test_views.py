from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):
    def setUp(self):
        # User setup
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Author and Book setup
        self.author = Author.objects.create(name="George Orwell")
        self.book1 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Animal Farm", publication_year=1945, author=self.author
        )

        # URLs
        self.list_url = reverse("book-list")   # from DRF router or ListView
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))
        self.assertIn("Animal Farm", str(response.data))

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Keep the Aspidistra Flying",
            "publication_year": 1936,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id,
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=1945")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Animal Farm", str(response.data))
        self.assertNotIn("1984", str(response.data))

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_order_books(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(
            response.data[0]["publication_year"], response.data[1]["publication_year"]
        )

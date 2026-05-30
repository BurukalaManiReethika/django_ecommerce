from django.test import TestCase

from store.models import Category


class StoreModelTest(TestCase):

    def test_category_creation(self):

        category = Category.objects.create(
            name="Books",
            slug="books"
        )

        self.assertEqual(
            category.name,
            "Books"
        )

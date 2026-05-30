from django.core.management.base import BaseCommand

from store.models import Category
from store.models import Product


class Command(BaseCommand):

    help = "Seed Sample Products"

    def handle(self, *args, **kwargs):

        electronics, _ = Category.objects.get_or_create(
            name="Electronics",
            slug="electronics"
        )

        Product.objects.get_or_create(
            category=electronics,
            name="Laptop",
            slug="laptop",
            description="Powerful Laptop",
            price=50000,
            stock=10
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Products seeded successfully."
            )
        )

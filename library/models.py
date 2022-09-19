from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['title', 'author']
        constraints = [
            UniqueConstraint(fields=["title", "author"],
                             name="unique_title_author")
        ]

    def __str__(self):
        return f'{self.title} by {self.author}'


class SavedBook(models.Model):
    NOT_READ = 'NRD'
    READING = 'RDG'
    READ = 'YRD'
    STATUS = [
        (NOT_READ, 'Not read'),
        (READING, "Reading"),
        (READ, 'Read'),
    ]
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='saved')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='saved')
    status = models.CharField(max_length=3, choices=STATUS, default=NOT_READ)

    def __str__(self):
        return f'{self.status} {self.book}'


class MarkUp(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='markup')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='markup')
    note = models.TextField(max_length=1000)
    page_number = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.book}, page {self.page_number} note: {self.note}'

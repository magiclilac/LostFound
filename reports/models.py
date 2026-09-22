from django.db import models


class Report(models.Model):

    REPORT_TYPE_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Returned', 'Returned'),
    ]

    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Documents', 'Documents'),
        ('Accessories', 'Accessories'),
        ('Books', 'Books'),
        ('Clothing', 'Clothing'),
        ('Other', 'Other'),
    ]

    student_name = models.CharField(max_length=100)

    enrollment_number = models.CharField(max_length=50)

    phone_number = models.CharField(max_length=15)

    report_type = models.CharField(
        max_length=10,
        choices=REPORT_TYPE_CHOICES
    )

    item_name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    location = models.CharField(max_length=200)

    date_time = models.DateTimeField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Open'
    )

    returned_date = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.item_name} - {self.report_type}"
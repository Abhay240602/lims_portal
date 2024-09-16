from django.db import models

class Reader(models.Model):
    """
    Represents a library reader.

    Attributes:
        reference_id (int): A unique reference identifier for the reader.
        reader_name (str): The name of the reader.
        reader_contact (str): The contact information for the reader.
        reader_address (str): The address of the reader.
        active (bool): A flag indicating whether the reader is active.
        books (ManyToManyField): A many-to-many relationship with `Book`, indicating which books the reader has.
    """

    def __str__(self):
        """
        Returns a string representation of the Reader instance.

        Returns:
            str: The name of the reader.
        """
        return self.reader_name

    reference_id = models.IntegerField(
        max_length=200,
        help_text="A unique reference identifier for the reader."
    )
    reader_name = models.CharField(
        max_length=200,
        help_text="The name of the reader."
    )
    reader_contact = models.CharField(
        max_length=200,
        help_text="The contact information for the reader."
    )
    reader_address = models.TextField(
        help_text="The address of the reader."
    )
    active = models.BooleanField(
        default=True,
        help_text="A flag indicating whether the reader is active."
    )
    books = models.ManyToManyField(
        'Book',
        related_name='readers',
        help_text="The books associated with the reader."
    )

class Book(models.Model):
    """
    Represents a book in the library system.

    Attributes:
        name (str): The name of the book.
        isbn (int): The ISBN number of the book.
        author (str): The author of the book.
        category (str): The category of the book, default is 'education'.
    """

    name = models.CharField(
        max_length=30,
        help_text="The name of the book."
    )
    isbn = models.PositiveIntegerField(
        help_text="The ISBN number of the book."
    )
    author = models.CharField(
        max_length=40,
        help_text="The author of the book."
    )
    category = models.CharField(
        max_length=30,
        default='education',
        help_text="The category of the book, default is 'education'."
    )

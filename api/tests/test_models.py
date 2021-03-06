from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import Note

class ModelTestCase(TestCase):
    """This class defines the test suite for the note model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.text = "Write world class code"
        self.category_tags = ['django', 'testing']
        self.note = Note(text=self.text, category_tags = self.category_tags, creator=user) 

    def test_model_can_create_a_note(self):
        """Test the note model can create a note."""
        old_count = Note.objects.count()
        self.note.save()
        new_count = Note.objects.count()
        self.assertNotEqual(old_count, new_count)

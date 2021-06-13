from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=date.today, null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def past(self):
        try:
            return date.today() > self.due_date
        except TypeError:
            return None

    @property
    def today(self):
        return date.today() == self.due_date

    @property
    def coming(self):
        try:
            return date.today() < self.due_date
        except TypeError:
            return self.due_date == None

    def mark_as_completed(self):
        self.completed = not self.completed
        self.completed_date = date.today()
        self.save()
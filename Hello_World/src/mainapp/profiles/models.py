from django.db import models

PREFIX_CHOICES = {
    ('Mr.','Mr.'),
    ('Mrs.','Mrs.'),
    ('Ms.','Ms.'),
    ('Miss','Miss'),
}


class Profile(models.Model):
    Prefix = models.CharField(max_length=5, blank=True, choices=PREFIX_CHOICES)
    FirstName = models.CharField(max_length=45, null=False)
    LastName = models.CharField(max_length=45, null=False)
    Email = models.EmailField(max_length=255, null=False)
    Username = models.CharField(max_length=45, null=False)

    objects = models.Manager()

    def __str__(self):
        return ((self.FirstName) + " " + (self.LastName))
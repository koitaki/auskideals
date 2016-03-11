from __future__ import unicode_literals

from django.db import models

class ProspectiveUser(models.Model):

    email_address = models.EmailField(null=False, primary_key=True)

from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _



class User(AbstractUser):

    """ User Model """

    name = models.CharField(_("Name of User"), blank=True, max_length=255)


# coding: utf8
from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="Date de création"
    )
    modified = models.DateTimeField(
        auto_now = True, 
        verbose_name="Date de modification"
    )

    class Meta:
        abstract = True
        ordering = ("-created", )

class UserProfile(AbstractUser, BaseModel):
    displayed_name = models.TextField(
        verbose_name = "Nom d'affichage",
        help_text = "Ce nom sera affiché en tant qu'auteur des articles",
        null = True, 
        blank = True,
    )

    def __str__(self):
        if self.displayed_name:
            return "%s, %s" % (self.displayed_name, self.username)
        else:
            return "NOT DEFINED, %s" % (self.username)


            
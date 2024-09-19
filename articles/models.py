from django.db import models
from django.utils.text import slugify
from users.models import UserProfile, BaseModel

class Article(BaseModel):
    author = models.ForeignKey(
        UserProfile,
        verbose_name = "Auteur de l'article",
        on_delete=models.CASCADE,
    )
    title = models.TextField(
        verbose_name = "Titre de l'article",
        help_text = "Ce titre sera affiché en haut en h1 et sera en title de la page. Garder 50-60 caractères si possible.",
        max_length = 100,
    )
    subtitle = models.TextField(
        verbose_name = "Sous-titre de l'article",
        max_length = 100,
    )
    content = models.TextField(
        verbose_name = "Contenu de l'article",
        help_text = "Le contenu de l'article est en HTML",
    )
    slug = models.TextField(
        verbose_name = "Sous-URL de l'article",
        help_text = "Ce champ sera présent dans l'URL de l'article pour aider le référencement et donner du sens à l'URL.",
    )
    is_display = models.BooleanField(
        verbose_name = "Article visible ?",
        help_text = "Définit si l'article doit être consultable",
        default = True,
    )
    is_index = models.BooleanField(
        verbose_name = "Article indéxé ?",
        help_text = "Définit si l'article doit être indexé et affiché sur la liste des articles",
        default = True,
    )

    def __str__(self):
        return "%s (%s)" % (self.title, self.author)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
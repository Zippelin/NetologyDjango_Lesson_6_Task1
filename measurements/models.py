from django.db import models


def generate_file_path(instance, filename):
    return f'{instance.project.name}/{instance.created_at.strftime("%Y-%d-%m")}/{filename}'


class CommonAbstract(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Project(CommonAbstract):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Measurement(CommonAbstract):
    """Измерение температуры на объекте."""
    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to=generate_file_path)
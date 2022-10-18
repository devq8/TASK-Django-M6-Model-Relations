from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)


class Lecture(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Slide(models.Model):
    lecture = models.OneToOneField(
        Lecture,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=30)
    link = models.URLField()

    def __str__(self):
        return self.name


class Assignment(models.Model):
    lecture = models.OneToOneField(
        Lecture,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=30)
    link = models.URLField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    courses = models.ManyToManyField(
        Course,
        related_name="tags",
    )
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

from django.db import models


class touch(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.EmailField(max_length=40)
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=150)

    def __str__(self):
        return self.first_name


class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title


class data(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class reg(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
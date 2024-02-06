from django.db import models

class Task(models.Model):

	title = models.CharField(
		verbose_name = "Titre",
		max_length = 50,
		default = "Tâche sans titre"
	)

	description = models.CharField(
		verbose_name = "Description",
		max_length = 500,
		null = True,
		blank = True
	)

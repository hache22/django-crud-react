from django.db import models


# clase con el nombre de la tabla a crear en la base de datos SQLITE3
class Task(models.Model):
    # titulo de la tarea
    title = models.CharField(max_length=100)
    # descripcion de la tarea
    description = models.TextField(blank=True)
    # mostrar si se encuentra realizada o no
    done = models.BooleanField(default=False)

    # esto muestra el nombre de la tarea dentro del panel admin
    def __str__(self):
        return self.title

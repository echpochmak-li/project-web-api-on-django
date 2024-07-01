from django.db import models

# Create your models here.
class Serials(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    genres = models.CharField(max_length=40)   
    info = models.CharField(max_length=1500) 
    
    #используем замечательный метод
    def __str__(self):
        return f'{self.pk}{self.name}'
    
    def clean(self):
        super().clean()
        if len(self.name) > 50:
            raise ValueError('Название сериала слишком длинное. Оно не должно превышать 50 символов.')
        if len(self.genres) > 40:  # Пример ограничения для жанров (установите желаемое значение)
            raise ValueError('Список жанров слишком длинный. Измените его.')
        if len(self.info) > 1500:
            raise ValueError('Описание сериала слишком длинное. Оно не должно превышать 1500 символов.')

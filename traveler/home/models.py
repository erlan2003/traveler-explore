from django.db import models


class AttractionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'attraction_types'

    def __str__(self):
        return self.name


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'regions'

    def __str__(self):
        return self.name


class Attraction(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    region_id = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='attractions'
    )
    attraction_type_id = models.ForeignKey(
        AttractionType,
        on_delete=models.CASCADE,
        related_name='attractions'
    )
    info = models.TextField()
    image_path = models.ImageField(upload_to='attractions/', blank=True, null=True)

    class Meta:
        db_table = 'attractions'



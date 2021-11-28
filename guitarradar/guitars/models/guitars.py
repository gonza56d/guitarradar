
from django.db import models

from guitarradar.utils.fields import DescriptiveCharField
from guitarradar.utils.models import BaseModel


class Guitar(BaseModel):

    class NeckShapes(models.TextChoices):
        CS = 'CS', 'C'
        CC = 'CC', 'C Chunky'
        DS = 'DS', 'D'
        VH = 'VH', 'V Hard'
        VS = 'VS', 'V Soft'
        AS = 'AS', 'Asymmetrical'
        US = 'US', 'U'

    class Materials(models.TextChoices):
        ALDER = 'AD', 'Alder'
        ASH = 'AS', 'Ash'
        MAHOGANY = 'MG', 'Mahogany'
        EBONY = 'EB', 'Ebony'
        ROSEWOOD = 'RW', 'Rosewood'
        MAPLE = 'MP', 'Maple'
        ROASTED_MAPLE = 'RM', 'Roasted Maple'
        FLAMED_MAPLE = 'FM', 'Flamed Maple'
        QUILTED_MAPLE = 'QM', 'Quilted Maple'
        POPLAR = 'PO', 'Poplar'
        BASSWOOD = 'BW', 'Basswood'
        OTHER = 'OT', 'Other'
    
    class Strings(models.IntegerChoices):
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TWELVE = 12
    
    class FretsQuantities(models.TextChoices):
        NINETEEN = 'NT', '19'
        TWENTY = 'TW', '20'
        TWENTY_ONE = 'TO', '21'
        TWENTY_TWO = 'TT', '22'
        TWENTY_FOUR = 'TF', '24'
        OTHER = 'OT', 'Other'

    class FretsTypes(models.TextChoices):
        MEDIUM_JUMBO = 'RMJ', 'Medium Jumbo'
        JUMBO = 'RJJ', 'Jumbo'
        EXTRA_JUMBO = 'RXJ', 'Extra Jumbo'
        STAINLESS_MEDIUM_JUMBO = 'SMJ', 'Stainless Medium Jumbo'
        STAINLESS_JUMBO = 'SJJ', 'Stainless Jumbo'
        STAINLESS_EXTRA_JUMBO = 'SXJ', 'Stainless Extra Jumbo'

    brand = models.ForeignKey('guitars.Brand', on_delete=models.PROTECT, null=False)
    model_name = models.CharField(max_length=300)
    url = models.CharField(max_length=5000)
    origin = models.CharField(max_length=300)
    bridge_pickup = models.ForeignKey('guitars.Pickup', on_delete=models.SET_NULL, null=True, related_name='bridge_pickup')
    middle_pickup = models.ForeignKey('guitars.Pickup', on_delete=models.SET_NULL, null=True, related_name='middle_pickup')
    neck_pickup = models.ForeignKey('guitars.Pickup', on_delete=models.SET_NULL, null=True, related_name='neck_pickup')
    bridge = models.ForeignKey('guitars.Bridge', on_delete=models.PROTECT, null=False)
    body_material = DescriptiveCharField(max_length=2, choices=Materials.choices)
    neck_material = DescriptiveCharField(max_length=2, choices=Materials.choices)
    fingerboard_material = DescriptiveCharField(max_length=2, choices=Materials.choices)
    fingerboard_radius = models.CharField(max_length=5)
    neck_shape = models.CharField(max_length=2, choices=NeckShapes.choices)
    strings = models.IntegerField(choices=Strings.choices, null=False)
    frets_quantity = models.CharField(max_length=2, choices=FretsQuantities.choices)
    frets_type = models.CharField(max_length=3, choices=FretsTypes.choices)
    scale_length = models.FloatField(null=False)

    class Meta:
        unique_together = ['brand', 'model_name']

    def __str__(self) -> str:
        return f'{self.brand} {self.model_name}'


class GuitarPicture(BaseModel):

    guitar = models.ForeignKey('guitars.Guitar', on_delete=models.CASCADE, related_name='guitar_picture')
    picture = models.ImageField(upload_to='guitarradar/guitars/pictures')

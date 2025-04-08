from django.db import models

class Equipment (models.Model):
    equipment= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.equipment
# Create your models here.
class Car(models.Model): 
    Engine_Types = [
        ("benzyna", "Benzynowy"),
        ("disel", "Disel"),
        ("elekryczny", "Elektryczny"),
        ("hybryda", "Hybrydowy"),
        
    ]

    GEARBOX_TYPES = [
        ("manual", "manualna"),
        ("automat", "automatyczna"),
    ]

    BODY_TYPES = [
        ("hatchback", "hatchback"),
        ("sedan", "sedan"),
         ("combi", "combi"),
        ("suv", "SUV"),
    ]
    CAR_CLASSES = [
        ("a", "male i mini"),
        ("b", "miejskie"),
         ("c", "komapktowe"),
        ("d", "rodzine"),
        ("e", ""),
        ("f", "luksusowe"),
         ("g", "sportowe"),
        ("h", "kabriolet"),
        ("i", "terenowe"),
        ("m", "van"),
    ]
    

    brand = models.CharField(max_length =  50)
    model = models.CharField(max_length = 50)
    engine_type= models.CharField(max_length=50, choices=Engine_Types)
    gearbox_type = models.CharField(max_length=50, choices =GEARBOX_TYPES)
    engine_power = models.PositiveSmallIntegerField()
    engine_capacity = models.PositiveSmallIntegerField()
    seats_count = models.PositiveSmallIntegerField()
    dors_count = models.PositiveSmallIntegerField()
    trunk_capacity= models.PositiveBigIntegerField()
    color = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50, choices=BODY_TYPES) 
    category = models.CharField(max_length=50, choices=CAR_CLASSES) 
    fuel_usage = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits =10 , decimal_places=2)
    mileage_limit = models.PositiveIntegerField()
    value = models.PositiveBigIntegerField()
    availability =models.BooleanField()
    insurance_expiry_date = models.DateField()
    equipment =models.ManyToManyField(Equipment)
    image = models.ImageField()
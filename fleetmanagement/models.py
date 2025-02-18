from django.db import models

# Create your models here.

STATUSES = [
    ('BESTELLT', 'Bestellt'),
    ('EINGETROFFEN', 'Eingetroffen'),
    ('IN_REPARATUR', 'In Reparatur'),
    ('FAHRBEREIT', 'Fahrbereit'),
]


class Auto(models.Model):
    hersteller = models.CharField(max_length=40)
    modell = models.CharField(max_length=40)
    nummernschild = models.CharField(blank=True, max_length=10)
    status = models.CharField(choices=STATUSES, max_length=30)

    def __str__(self):
        return f"{self.hersteller}  {self.modell}"


if len(Auto.objects.all()) == 0:
    print("DATABASE IS EMPTY; GENERATING FAKE ENTRIES")
    Auto(hersteller="Tesla", modell="Model S", nummernschild="ME-MS-12", status=STATUSES[3][0]).save()
    Auto(hersteller="Tesla", modell="Model 3", nummernschild="ME-ME-63", status=STATUSES[3][0]).save()
    Auto(hersteller="Tesla", modell="Model X", nummernschild="ME-MX-08", status=STATUSES[2][0]).save()
    Auto(hersteller="Tesla", modell="Model Y", nummernschild="", status=STATUSES[0][0]).save()
    Auto(hersteller="Volkswagen", modell="ID.3", nummernschild="", status=STATUSES[0][0]).save()

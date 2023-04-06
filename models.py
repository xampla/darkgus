from django.db import models

class Dork(models.Model):
    dork = models.TextField(primary_key=True)
    category = models.TextField(blank=True, null=True)
    total_results = models.IntegerField(blank=True, null=True)
    results_gathered = models.IntegerField(blank=True, null=True)
    last_executed = models.DateField(blank=True, null=True)

    def str(self):
        return self.dork


class Result(models.Model):
    url = models.TextField()
    dork = models.ForeignKey(Dork, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    all_info = models.TextField(blank=True, null=True)
    last_detected = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('url', 'dork')

    def str(self):
        return self.url
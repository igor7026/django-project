from django.db import models

# Create your models here.


class Customer(models.Model):
    lead = models.ForeignKey("leads.Lead", on_delete=models.CASCADE)
    contract = models.ForeignKey("contracts.Contract", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        created = not self.pk  # проверяем, создается ли новый объект
        super().save(*args, **kwargs)
        if created:
            self.lead.status = "customer"
            self.lead.save()

    def __str__(self):
        return self.lead.first_name + " " + self.lead.last_name

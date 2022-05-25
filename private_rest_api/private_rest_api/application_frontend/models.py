from django.db import models

# Model for the SIPRI files:
class SIPRIData(models.Model):
    """A generic database model that allows for the uploading and retrieving of
    SIPRI data, typiclaly in the form of .xlsx, csv and rft files.

    Its main fields are File Upload Fields that allow admin uses to upload the
    datasets that the frontend makes use of.

    """
    total_arms_sales = models.FileField(blank=True, null=True, upload_to="SIPRI_data/")
    top_hundred_companies = models.FileField(blank=True, null=True, upload_to="SIPRI_data/")
    date_uploaded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"SIPRI_DATASETS-{self.date_uploaded}"

    class Meta:
        verbose_name_plural = "SIPRI Datasets"

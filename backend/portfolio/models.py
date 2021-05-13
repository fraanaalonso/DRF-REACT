from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

class Skill(models.Model):
    uid = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Name', max_length=150)
    progresion = models.CharField(verbose_name='Progresion', max_length=3)


    def __str__(self):
        return self.name
    
class Project(models.Model):
    uid = models.UUIDField(_('ID'), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=150)
    code_url = models.URLField(_("URL Code"), max_length=250)
    host_url = models.URLField(_('URL Page'), max_length=250)

    def __str__(self):
        return self.name
         
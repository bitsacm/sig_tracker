from django.db import models


"""This is the class for the list of SIGs in ACM.
It has three attributes- name, coordinator, SIG members

"""
class SIG(models.Model):
    sig_name = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=50)
    members = models.CharField(max_length=500)
    
    def __str__(self):
        return self.sig_name


"""Classes for individual SIGs will come here
"""




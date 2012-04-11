from django.db import models
import datetime
# Create your models here.


CATEGORY_CHOICES = (
	(u'Ambiental', u'Problema Ambiental'), 
	(u'Seguranca', u'Problemas de seguranca'), 
	(u'Transito', u'Problemas relacionados ao transito'), 

)



class Problem(models.Model):
	"""
	Modelo das Foto-Problemas

	"""
	# Titulo do Problema
	title       = models.CharField(max_length=512, blank=False)
	#Descricao do problema
	description = models.TextField(default="Descricao do problema")
	#Nome do usuario autor do problema -> vai ter que referenciar o usuario depois
	author      = models.CharField(max_length=512, blank = False)
	category    = models.CharField(max_length=200, choices=CATEGORY_CHOICES, blank = False)
	solved      = models.BooleanField(default=False)
	
	address     = models.CharField(max_length=512, blank=False)
	
	pub_date    = models.DateTimeField('date published')

	def __unicode__ (self):
		return self.title

	def problem_solved(self):
		return self.solved

		
		
class Comment(models.Model):
	problem      = models.ForeignKey(Problem)
	author       = models.CharField(max_length=512, blank = False)
	comment_text = models.TextField(default="Comentario basico")
	

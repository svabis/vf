from django.db import models


# !!! Grafiks !!!
class Grafiks(models.Model):
    class Meta():
        db_table = "grafiks"

    sakums = models.DateTimeField()
#    ilgums = 
    nodarbiba = models.ForeignKey(  ) # Nodarbiba
    treneris = models.ForeignKey( ) # Treneris

    telpa = models.ForeignKey( ) # Telpa

 = models.CharField( max_length = 100 )
    kamera_slug = models.SlugField( unique = True, default=rand_slug() )
    kamera_apraksts = models.TextField( default = 'kameras apraksts' )
    kamera_img_dir = models.CharField( max_length = 50, default = 'username' )
    kamera_email = models.CharField( max_length = 30, blank = True )
    kamera_type = models.CharField( max_length=10, choices=KAMERA_TYPE, default="PUB" )

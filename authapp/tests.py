from django.test import TestCase

# Create your tests here.

# when we run program
# first we intialize application
# after intialize  the url for the local host we include authapp.urls 
# it will jump from urls.py to urls.py from authapp that we created
# then see which one is path the  he will jump to views function
# and it will search for home function
# in function  return render index.html page
# after that we need to intialize the template page in setting that is the directory of templates
from django.db import models
from django.urls import reverse

class Post(models.Model):
    #foreign key
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE, )
   #for list view on home
    title = models.CharField(max_length=200)
    description = models.TextField()
    #resume fields for detailed view

     #contact us area

    name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    address = models.TextField()
    #Education x xii grad- graduation pg post graduation
        #x xii
    x_board = models.CharField(max_length=200)
    x_percentage = models.CharField(max_length=200)

    xii_board = models.CharField(max_length=200)
    xii_percentage = models.CharField(max_length=200)
    #grad
    grad_university = models.CharField(max_length=200)
    grad_college = models.CharField(max_length=200)
    grad_course = models.CharField(max_length=200)
    grad_specialisation= models.CharField(max_length=200)
    grad_percentage = models.CharField(max_length=200)
    grad_year_of_passing = models.CharField(max_length=200)

    #pg
    pg_university = models.CharField(max_length=200)
    pg_college = models.CharField(max_length=200)
    pg_course = models.CharField(max_length=200)
    pg_specialisation = models.CharField(max_length=200)
    pg_percentage = models.CharField(max_length=200)
    pg_year_of_passing = models.CharField(max_length=200)

    #skills
    technical_skills = models.TextField()
    non_technical_skills = models.TextField()

    def __str__(self):
        return self.title
            
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])
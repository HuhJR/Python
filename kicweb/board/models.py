from django.db import models

# Create your models here.

class Board(models.Model) :
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pass1 = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=4000)
    regdate = models.DateTimeField(auto_now_add=True, blank=True)
    readcnt = models.IntegerField(default=0)
    file1 = models.CharField(max_length=300)

    def __str__(self):
        return str(self.num) + ":" + self.subject

class Comment(models.Model) :
    ser = models.AutoField(primary_key=True)
    num = models.IntegerField(default=0)
    content = models.CharField(max_length=4000)
    regdate = models.DateTimeField(auto_now_add=True, blank=True) # 오늘날짜 적용
    
    def __str__(self):
        return str(self.ser) + "\t" + str(self.num) +"\t" + self.content













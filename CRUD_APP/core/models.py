from django.db import models



class Table(models.Model):
  name = models.CharField(max_length=20, default='')
  coulumn_header_1 = models.CharField(max_length=20, default='')
  coulumn_header_2 = models.CharField(max_length=20, default='')
  coulumn_header_3 = models.CharField(max_length=20, default='')
  coulumn_header_4 = models.CharField(max_length=20, default='')

  def __str__(self) -> str:
    return self.name


class DataInTable(models.Model):
  #4
  table_that_data_in = models.ForeignKey(Table, on_delete=models.CASCADE)
  coulumn1 = models.CharField(max_length=20, default='')
  coulumn2 = models.CharField(max_length=20, default='')
  coulumn3 = models.CharField(max_length=20, default='')
  coulumn4 = models.CharField(max_length=20, default='')
  
  def __str__(self):
    return str(self.table_that_data_in)


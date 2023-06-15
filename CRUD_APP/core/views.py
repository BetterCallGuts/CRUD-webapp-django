from django.shortcuts import render, redirect
from .models import DataInTable, Table
from django.http.request  import HttpRequest



def view_CRUD_APP(request, pk=None):
  
    if pk is not None:
      
      TABLES   = Table.objects.all() 
      TABLE    = Table.objects.get(pk=pk)
      DATA     = DataInTable.objects.filter(table_that_data_in=TABLE)
      var = {
        'data'     : DATA,
        'tables'   : TABLES,
        'table'    : TABLE,
      }
    else:
      table  = Table.objects.first()
      data = DataInTable.objects.filter(table_that_data_in=table)
      tables = Table.objects.all()
      print(table)
      var = {
        'table' : table,
        'data'  : data,
        'tables': tables
      }
    # print(TABLE.pk  ==  TABLES[0].pk)
    
    return render(request, 'core/show_values.html', var)



def edit_table_or_data(request, table_or_data, pk=None):
  if pk is None:
    return render(request, 'core/show_values.html')
  if request.method == 'POST':
    first = request.POST['first']
    second = request.POST['second']
    third = request.POST['third']
    fourth = request.POST['fourth']
    if table_or_data == 'table':
      table = Table.objects.get(pk=pk)
      table.coulumn_header_1 = first
      table.coulumn_header_2 = second
      table.coulumn_header_3 = third
      table.coulumn_header_4 = fourth
      table.save()
      return redirect('core:show_CRUD', f'{str(table.pk )}')
    elif table_or_data == 'data':
      first = request.POST['first']
      second = request.POST['second']
      third = request.POST['third']
      fourth = request.POST['fourth']
      
      item = DataInTable.objects.get(pk=pk)
      table = item.table_that_data_in
      
      item.coulumn1 = first
      item.coulumn2 = second
      item.coulumn3 = third
      item.coulumn4 = fourth
      item.save()
      return redirect('core:show_CRUD', f'{str(table.pk)}')
    
    
  else:
    if table_or_data == 'table':
      table = Table.objects.get(pk=pk)
      
      
      var = {
        'table' : table,
        'op'    : 'table'
      }
    elif table_or_data == 'data':
      the_data = DataInTable.objects.get(pk=pk)
      table    = the_data.table_that_data_in
      var      = {
        "table"    : table,
        'the_data' : the_data,
        'op'       : 'data',
        
        }
    return render(request, 'core/edit_value.html', var)

  # return render(request, )


# def view_table(request, pk):
#   pass

def delete(request, table_or_data,pk):
  if table_or_data == 'table':
    table = Table.objects.get(pk=pk)
    all_data = DataInTable.objects.filter(table_that_data_in=table)
    table.delete()
    all_data.delete()
    return redirect('core:show_CRUD')
    
  elif table_or_data == 'data':
    data = DataInTable.objects.get(pk=pk)
    data.delete()
    return redirect('core:show_CRUD')
  

def add_value(request:HttpRequest,pk=None):
  if pk is None:
    return render(request, 'core/show_values.html')
  table = Table.objects.get(pk=pk)
  
  if request.method == 'POST':
    first = request.POST['first']
    second = request.POST['second']
    third = request.POST['third']
    fourth = request.POST['fourth']
    item = DataInTable.objects.create(table_that_data_in=table, coulumn1=first, coulumn2=second, coulumn3=third, coulumn4=fourth)
    item.save
    
    return redirect('core:show_CRUD')
  else:
    var = {
      'table' : table,
      'op'    : 'add_value'
    }
    return render(request,'core/edit_value.html', var)

def add_table(request):
  
  
  if request.method == 'POST':
    name = request.POST['name']
    first = request.POST['first']
    second = request.POST['second']
    third = request.POST['third']
    fourth = request.POST['fourth']

    table = Table.objects.create(name=name, coulumn_header_1=first,
                        coulumn_header_2=second,
                        coulumn_header_3=third, 
                        coulumn_header_4=fourth
                        )
    table.save()
    return redirect('core:show_CRUD')
  else:
    var = {
      'op'    : 'add_table'
    }
    return render(request,'core/edit_value.html', var)

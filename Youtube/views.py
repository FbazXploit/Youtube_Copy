from django.shortcuts import render

def about(req):
  context = {
    'title' : 'About Developer',
  }
  
  return render(req, 'aboutDev.html', context)

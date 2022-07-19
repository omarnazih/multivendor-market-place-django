from django.shortcuts import render

# Start Views
def home(request):
  return render(request, 'index.html')
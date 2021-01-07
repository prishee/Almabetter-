from django.shortcuts import render
from studentApp.forms import StudentMarksForm
from studentApp.models import Mark

# Create your views here.
def index(request):
  return render(request,'index.html')

def studentMarksView(request):
  form = StudentMarksForm()
  if request.method=='POST':
    form=forms.StudentMarksForm(request.POST)
    if form.is_valid():
      form.save()
    return index(request)
  return render(request,'marks.html',{'form':form})
    

def leaderBoardView(request):
  studentList=Mark.objects.all()
  return render(request,'leaderboard.html',{'studentList':studentList})

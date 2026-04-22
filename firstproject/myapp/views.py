from django.shortcuts import render
<<<<<<< HEAD

from .models import Student 



def marks_tracker(request):
    result = None
    error = None 

    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        maths = request.POST.get('maths')
        science = request.POST.get('science')
        english = request.POST.get('english')

        if maths < 0 or maths > 100:
            error = "Maths marks must be between 0 and 100."
        elif science < 0 or science > 100:
            error = "Science marks must be between 0 and 100."
        elif english < 0 or english > 100:
            error = "English marks must be between 0 and 100."
        else:
            total = maths + science + english
            percentage =  round((total / 3), 2)

            if percentage >= 90:
                grade = 'A+'
            elif percentage >= 75:
                grade = 'A'
            
            elif percentage >= 60:
                grade = 'B'
            
            elif percentage >= 45:
                grade = 'C'
            
            elif percentage >= 35:
                grade = 'D'
            else:
                grade = 'F'
            

            student = Student.objects.create(
                name=name,
                roll_number=roll_number,
                maths=maths,
                science=science,
                english=english,
                total=total,
                percentage=percentage,
                grade=grade
            )
            
            result = Student
    history  = Student.objects.all().order_by('-start')[:5]

    return render(request,'myapp.html',{
        'result': result,
        'error': error,
        'history': history
    })
=======
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, World! from django app")
>>>>>>> d017417b8cfd1d58a32f9a6c1a751174891f1854

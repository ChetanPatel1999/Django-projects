from django.shortcuts import render

# Create your views here.
# def student_detail(request):
#     return render(request,"student/home.html",{"name":"ranveer","age":24,"collage":"DPGU"})


# def student_detail(request):
#     name="rydham"
#     age=21
#     collage="holker"
#     return render(request,"student/home.html",{"name":name,"age":age,"collage":collage})


# def student_detail(request):
#     data={
#         'name':"yuvraj",
#         'age':25,
#         'collage':"HSCL"
#     }
#     return render(request,"student/home.html",data)


class product:
    def __init__(self, color,price):
        self.color=color
        self.price=price



def student_detail(request):

    name="yuvraj"
    p1=product("red",40000)
    l1=["hindi","english","math"]
    a=12
    b=5
    c=a+b
    data={
        'name':name,
        'age':25,
        'collage':"holker science collage",
        'subjects':l1,
        'marks':{'hindi':50,'english':28,'math':12},
        "product": p1,
        "sum":c,
        "mysum":"",
        "intro":"hello everyone my name is chetan patel i am teacher",
        "message":"<h1>this is safe syntax</h1>",
        "d":False
    }

    return render(request,"student/home.html",data)

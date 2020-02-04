from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")

def showresult(request):
    n1 = request.POST.get("t1")
    n2 = request.POST.get("t2")
    n3 = request.POST.get("t3")
    n4 = request.POST.get("t4")
    n5 = request.POST.get("t5")
    n6 = request.POST.get("t6")
    n7 = request.POST.get("t7")
    n8 = request.POST.get("t8")
    n9 = request.POST.get("t9")
    n10 = request.POST.get("t10")

    if n1 == "idly":
        n1 = 42
    else:
        n1 = 0

    if n2 == "dosa":
        n2 = 63
    else:
        n2 = 0
    if n3 == "poori":
        n3 = 63
    else:
        n3 = 0
    if n4 == "vada":
        n4 = 60
    else:
        n4 = 0
    if n5 == "upma":
        n5 = 40
    else:
        n5 = 0
    if n6 == "bajji":
        n6 = 53
    else:
        n6 = 0
    if n6 == "setdosa":
        n7 = 68
    else:
        n7 = 0
    if n8 == "tamtobath":
        n8 = 47
    else:
        n8 = 0
    if n9 == "paseratu":
        n9 = 68
    else:
        n9 = 0
    if n10 == "plaindosa":
        n10 = 50
    else:
        n10 = 0
    total1 = n1+n2+n3+n5+n6+n7+n8+n9+n10
    total = total1+18

    return render(request,"index.html",{"data":total1,"data2":total})
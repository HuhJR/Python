from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect
import time
from django.contrib import auth

from decorator.decorator import loginchk
from decorator.decorator import loginadmin
# Create your views here.
"""
Created on Thu Feb 22 12:15:26 2024
1) __init__ 폴더 확인한다
2)  views.py에   
    from decorator.decorator  import loginchk, loginadmin 추가 한다
3) !!!!!!  장고 리쎗한다

 1)path("info/<str:id>/", views.info, name="info"), 
 2)def info(request, id):  
 3) def loginchk(func):
     def check(request,id):  
 
         
 
    3개의 파라메타가 맞아야 한다 



"""
def index(request) :
    return render(request, 'head.html') #templates


def join(request) :
    if request.method != 'POST':
        return render(request,'member/join.html')
    else :
        member = Member(id = request.POST["id"],\
                        pass1 = request.POST["pass"],\
                        name = request.POST["name"],\
                        gender = request.POST["gender"],\
                        tel = request.POST["tel"],\
                        email = request.POST["email"],\
                        picture = request.POST["picture"])
        member.save() #insert, update(같은 id) 문장 실행.
        return HttpResponseRedirect("/member/login/")

def login(request):
    if request.method != 'POST':
        return render(request, 'member/login.html')
    else :
        id1 = request.POST["id"]
        pass1 = request.POST["pass"]
        try:
            member = Member.objects.get(id=id1) #select 문장 실행
        except:
            context = {"msg" : "아이디를 확인하세요.", "url" : "/member/login/"}
            return render(request, "alert.html",context)
        
        else:
            if member.pass1 == pass1 :
                request.session["id"]=id1
                time.sleep(1)
                return HttpResponseRedirect("/member/index")
            else : 
                context = {"msg" : "비밀번호가 틀립니다.", "url" : "/member/login/"}
                return render(request, "alert.html",context)
            
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/member/login/")

@loginchk
def info(request):
    id1 = request.session["id"]
    member = Member.objects.get(id=id1)
    return render(request, "member/joinInfo.html", {"mem":member})


def update(request):
    id1 = request.session["id"]
    member = Member.objects.get(id=id1)
    
    if request.method != 'POST':
        id1 = request.session["id"]
        return render(request, 'member/memberUpdateForm.html', {"mem":member})
    
    else :
        if request.POST["pass"] == member.pass1 :
            member = Member(id = request.POST["id"],\
                            pass1 = request.POST["pass"],\
                            name = request.POST["name"],\
                            gender = request.POST["gender"],\
                            tel = request.POST["tel"],\
                            email = request.POST["email"],\
                            picture = request.POST["picture"])
            member.save() #insert, update(같은 id) 문장 실행.
            return HttpResponseRedirect("/member/joinInfo/")
        else : 
            context = {"msg" : "비밀번호가 틀립니다.", "url" : "/member/memberUpdate/"}
            return render(request, "alert.html",context)
    
    
def delete(request):
    id1 = request.session["id"]
    member = Member.objects.get(id=id1)
    
    if request.method != 'POST':
        return render(request, 'member/memberDeleteForm.html')
    
    else :
        if request.POST["pass"] == member.pass1 :
           # 삭제코드
            member.delete()
            auth.logout(request)
            return HttpResponseRedirect("/member/login/")
    
        else:
            context = {"msg" : "비밀번호가 틀립니다.", "url" : "/member/memberDelete/"}
            return render(request, "alert.html",context)
"""
def passchg(request):
    id1 = request.session.get("id")  # get() 사용으로 KeyError 방지
    try:
        member = Member.objects.get(id=id1)
    except Member.DoesNotExist:
        # 회원이 존재하지 않을 경우 처리
        return HttpResponseRedirect("/member/login/")
    
    if request.method == 'POST':
        pass1 = request.POST.get("pass")  # 현재 비밀번호 입력값
        pass2 = request.POST.get("chgpass")   # 새 비밀번호 입력값

        # 현재 비밀번호 확인
        if pass1 == member.pass1:
            if pass2:
                # 새 비밀번호 설정
                member.pass1 = pass2
                member.save()
                auth.logout(request)  # 로그아웃 처리
                return HttpResponseRedirect("/member/login/")
            else:
                context = {"msg": "새 비밀번호를 입력해주세요.", "url": "/member/memberPass/"}
                return render(request, "alert.html", context)
        else:
            context = {"msg": "현재 비밀번호가 틀립니다.", "url": "/member/memberPass/"}
            return render(request, "alert.html", context)
    else:
        return render(request, 'member/memberPassForm.html')
"""
def passchg(request, id):
    if request.method != 'POST':
        return render(request, 'member/memberPassForm.html')
    
    
def picture(request):
    if request.method != 'POST':
        return render(request, 'member/pictureimgForm.html')
    
    else :
        filename = request.FILES["picture"].name
        handle_upload(request.FILES["picture"])
        return render(request,"member/picturePro.html",{"filename":filename})

def handle_upload(f) :
    with open("file/picture/"+f.name, "wb+") as dest:
        for ch in f.chunks():
            dest.write(ch)
@loginadmin
def list1(request):
    if request.method != 'POST':
        mlist = Member.objects.all()
        return render(request, 'member/memberList.html',{"mlist":mlist})

        





































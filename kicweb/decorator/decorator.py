# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:06:23 2024

@author: KITCOOP
"""

from django.shortcuts import render


def loginchk(func):
    def check(request):
        print("deco")
        try:
            login = request.session["id"]
        except:
            context={"msg":"로그인 하세요","url":"/member/login/"}
            return render(request, "alert.html",context)
        return func(request)
    return check



def loginadmin(func):
    def check(request):
        try:
            login = request.session["id"]
        except:
            context={"msg":"로그인 하세요","url":"/member/login/"}
            return render(request, "alert.html",context)
        else:
            if login != 'admin' :
                context = {"msg":"접근불가합니다.","url":"/member/index/"}
                return render(request, "alert.html",context)
        return func(request)
    return check
    











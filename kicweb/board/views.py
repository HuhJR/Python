from django.shortcuts import render
from .models import Board, Comment
from django.http import HttpResponseRedirect, HttpResponse


from django.utils import timezone

from django.core import serializers
# Create your views here.

def handle_upload(f) :
    with open("file/picture/"+f.name, "wb+") as dest:
        for ch in f.chunks():
            dest.write(ch)

def write(request) :
    if request.method != 'POST':
        return render(request,'board/boardForm.html')
    else :
        try:
            filename = request.FILES["file1"].name
            handle_upload(request.FILES["file1"])
        except:
            filename=""
            
        b = Board(name = request.POST["name"],
                  pass1 = request.POST["pass"],
                  subject = request.POST["subject"],
                  content = request.POST["content"],
                  regdate = timezone.now(),
                  readcnt = 0,
                  file1=filename )
        b.save()
        print(b)
        return HttpResponseRedirect("/board/list/")

def list1(request) :
    all_boards = Board.objects.all().order_by("-num")
    limit = 3 #page당 게시물 갯수
    bottomLine = 3 # 하단 page 갯수
    totalcount = len(all_boards) # 게시물 등록 건수
    # pageNum 파라미터값이 없는 경우 1로 리턴
    pageNum = int(request.GET.get("pageNum",1))
    #pageging
    start = (pageNum-1)*limit + 1#
    end = start + limit -1
    print(start,":",end)
    blist = all_boards[start-1:end]
    maxcount = len(all_boards)-(pageNum-1)*limit
    print(maxcount,"===maxcount")
    startpage = int((pageNum - 1)/bottomLine) * bottomLine + 1
    endpage = startpage + bottomLine - 1
    maxpage = (int)(totalcount/limit)
    
    if totalcount % limit != 0:
        maxpage = maxpage + 1
    if endpage > maxpage :
        endpage = maxpage
    
    # 1~3 1,2,3  4,5,6
    pagelist = list(range(startpage, endpage+1))
    
    content = {
        "blist": blist,
        "maxcount": maxcount,
        "totalcount": totalcount,
        "bottomLine": bottomLine,
        "startpage": startpage,
        "endpage": endpage,
        "pageNum": pageNum,
        "pagelist": pagelist,
        "maxpage": maxpage
        }
    
    return render(request,'board/boardList.html', content)
    

def restlist1(request) :
    all_boards = Board.objects.all().order_by("-num")
    limit = 3 #page당 게시물 갯수
    bottomLine = 3 # 하단 page 갯수
    totalcount = len(all_boards) # 게시물 등록 건수
    # pageNum 파라미터값이 없는 경우 1로 리턴
    pageNum = int(request.GET.get("pageNum",1))
    #pageging
    start = (pageNum-1)*limit + 1#
    end = start + limit -1
    print(start,":",end)
    blist = all_boards[start-1:end]
    maxcount = len(all_boards)-(pageNum-1)*limit
    print(maxcount,"===maxcount")
    startpage = int((pageNum - 1)/bottomLine) * bottomLine + 1
    endpage = startpage + bottomLine - 1
    maxpage = (int)(totalcount/limit)
    
    if totalcount % limit != 0:
        maxpage = maxpage + 1
    if endpage > maxpage :
        endpage = maxpage
    
    # 1~3 1,2,3  4,5,6
    pagelist = list(range(startpage, endpage+1))
    
    blistjson = serializers.serialize("json", blist)
    print(type(blistjson))
    
    content = {
        "blist": blistjson,
        "maxcount": maxcount,
        "totalcount": totalcount,
        "bottomLine": bottomLine,
        "startpage": startpage,
        "endpage": endpage,
        "pageNum": pageNum,
        "pagelist": str(pagelist),
        "maxpage": maxpage
        }
    print(type(content))
    return HttpResponse(str(content),content_type="text/json")


def info(request, num) :
    print(num)
    board = Board.objects.get(num=num)
    print("board.num:", board.num)
    board.readcnt += 1
    board.save()    
    
    commentLi = Comment.objects.all().filter(num=num).order_by("-ser")
    count = len(commentLi)
    print(board)
    
    content = {"board":board, 'commentLi':commentLi, 'count':count}
    return render(request, 'board/boardInfo.html',content)



def update(request, num) :
    board = Board.objects.get(num=num)
    print(board.pass1, ":pass1")
    if request.method != 'POST':
        return render(request,'board/boardUpdateForm.html',{'board':board})
    else:
        try:
            filename=request.FILES["file2"].name
            handle_upload(request.FILES["file2"])
            board.file1=filename
        except:
            pass
    
    print(board.pass1, request.POST["pass"],"==========")
    if board.pass1 == request.POST["pass"]:
        board.name =request.POST["name"]
        board.subject =request.POST["subject"]
        board.content =request.POST["content"]
        board.save()
        return HttpResponseRedirect("/board/info/"+str(board.num))
    else:
        context = {"msg":"비밀번호 오류입니다.", "url":"/board/update/"+str(board.num)}
        return render(request,"alter.html",context)


def delete(request, num) :
    board = Board.objects.get(num=num)
    if request.method != 'POST':
        return render(request,'board/boardDeleteForm.html',{'num':num})
    else:
        print(board.pass1)
        if board.pass1 == request.POST["pass"]:
            board.delete()
            return HttpResponseRedirect("/board/list")
        else:
            context = {"msg":"비밀번호 오류입니다.","url":"/board/delete/"+str(board.num)}
            return render(request, "alert.html",context)
    
    print(board.pass1, request.POST["pass"],"==========")
    if board.pass1 == request.POST["pass"]:
        board.name =request.POST["name"]
        board.subject =request.POST["subject"]
        board.content =request.POST["content"]
        board.save()
        return HttpResponseRedirect("/board/info/"+str(board.num))
    else:
        context = {"msg":"비밀번호 오류입니다.", "url":"/board/update/"+str(board.num)}
        return render(request,"alter.html",context)



def commentpro(requeest, comment, num):
    com = Comment(num=num, content=comment, regdate=timezone.now())
    com.save()
    
    commentLi = Comment.objects.all().filter(num=num)
    if commentLi:
        count = len(commentLi)
    else:
        count=0
    print(count)
    line='<div class="row"><div class="col-sm-1">&nbsp;</div>'+\
         '<div class="col-sm-1">'+str(count)+'</div>'+\
         '<div class="col-sm-5">'+com.content+'</div>'+\
         '<div class="col-sm-5">&nbsp;</div></div>'
    return HttpResponse(line)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
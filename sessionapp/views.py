from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.

def mainFunc(request):
    return render(request, 'main.html') # forwarding

def setOsFunc(request):
    if "favorite_os" in request.GET:
        # print(request.GET.get("favorite_os")) 밑에 꺼를 더 많이 사용
        print(request.GET["favorite_os"])
        
        # "f_os"라는 키로 세션을 생성
        request.session["f_os"] = request.GET["favorite_os"]
        # return render() 형식은 forwarding이기 때문에 클라이언트를 통한 요청 불가
        # 다시 말해 메인 urls.py를 만날 수 없다.
        
        # forwarding말고 redirect 방식을 사용한다면 가능하다. redirect해서 -> showOsFunc에 요청이 들어감
        return HttpResponseRedirect("/showos")
        
    else:
        return render(request, 'selectos.html') # 요청값에 "favorite_os"이 없는 경우
        
        
        
        
def showOsFunc(request):
    # print("여기까지 도착")
    dict_context = {}
    
    
    if "f_os" in request.session:   # 세션 값 중에 "f_os"가 있으면 처리
        print("유효 시간 : ", request.session.get_expiry_age())
        dict_context['sel_os'] = request.session["f_os"]
        dict_context['message'] = "너가 선택한 os는 %s 악깡버"%request.session["f_os"]
    else:
        dict_context['sel_os'] = None
        dict_context['message'] = "빨리 선택해"
        
    # del request.session["f_os"] # 특정 세션 삭제
    request.session.set_expiry(5) # 5초 후 세션 삭제
    # set_expiry(0) 브라우저가 닫힐 때 세션이 해제됨
        
        
    return render(request, 'show.html', dict_context)
        
        
        
        
        

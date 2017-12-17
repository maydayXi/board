from django.shortcuts import render, redirect
from boardapp import forms, models
import math
from django.contrib import auth
from django.contrib.auth import authenticate

page = 0                            # 初始頁數為 0

# <summary> 首頁 Function </summary>
# <param name='page_index'> 跳頁操作參數 </param>
# <return> 留言板首頁 </return>
def index(request, page_index=None):
    global page
    board_all = models.BoardUnit.objects.all().order_by('-id')
    page_size = 3                                                   # 每頁資料數
    total_size = len(board_all)                                     # 總資料數
    total_page = math.ceil(total_size/page_size)                    # 總頁數

    if page_index == None:
        page = 0
        board_records = models.BoardUnit.objects.all().order_by(
            '-id')[:page_size]                                      # 取出前三筆資料

    elif page_index == 'pre':                                       # 上一頁操作
        start = (page-1) * page_size                                # 上一頁第一筆資料
        if start >= 0:                                              # 如果上一頁有資料就顯示
            board_records = models.BoardUnit.objects.all().order_by(
                '-id')[start:(start+page_size)]
            page -= 1

    elif page_index == 'next':                                      # 下一頁操作
        start = page * page_size                                    # 下一頁第一筆資料
        if page < total_size:                                       # 如果下一頁有資料就顯示
            board_records = models.BoardUnit.objects.all().order_by(
                '-id')[start:(start+page_size)]
            page += 1

    print(board_records)

    current_page = page + 1
    return render(request, 'index.html', locals())

# <summary> 新增留言 Function </summary>
# <return> 依據表單驗證導向不同頁面 </return>
def post(request):

    if request.method == 'POST':                                    # 如果是前端表單傳送
        postform = forms.PostForm(request.POST)                     # 取得前端表單傳送資料 建立 Form Class

        if postform.is_valid():                                     # 如果前端表單通過驗證
            human = True
            title = postform.cleaned_data['board_title']            # 取得表單輸入標題
            name = postform.cleaned_data['board_name']              # 取得標單輸入姓名
            content = postform.cleaned_data['board_content']        # 取得表單輸入留言
            boo = postform.cleaned_data['board_gender']             # 取得表單輸入性別

            if boo:
                gender = 'm'
            else:
                gender = 'f'
                                                                    # 新增資料
            record = models.BoardUnit.objects.create(b_name=name, b_title=title,
                b_gender=gender, b_content=content, b_response='')
            record.save()                                           # 儲存資料
            message = '留言已新增......'
            postform = forms.PostForm()                             # 清空表單資料

            return redirect('/index/')                              # 重新導向首頁
        else:
            message = '驗證碼錯誤！'
    else:
        message = '標題、姓名、內容及驗證碼必須輸入！'
        postform = forms.PostForm()

    return render(request, 'post.html', locals())

# <summary> 登入 Function </summary>
# <return> 登入成功導向管理首頁 </summary>
# <return> 登入失敗重新導向登入畫面 </summary>
def login(request):
    message = ''

    if request.method == 'POST':                                    # 取得表單帳號密碼
        name = request.POST['username'].strip()
        password = request.POST['password']

        user1 = authenticate(username=name, password=password)      # 登入帳密驗證

        if user1 is not None:                                       # 如果有這個使用者
            if user1.is_active:                                     # 且帳號有效
                auth.login(request, user1)                          # 使用者登入
                return redirect('/adminmain/')                      # 導向管理首頁
            else:                                                   # 如果帳號無效
                message = '帳號尚未啟用！'
        else:                                                       # 未通過登入驗證
            message = '登入失敗！'

    return render(request, 'login.html', locals())

# <summary> 登出 Function </summary>
# <return> 留言版首頁 </summary>
def logout(request):
    auth.logout(request)

    return redirect('/index/')

# <summary> 管理首頁 Function </summary>
# <param name='page_index'> 操作參數 </param>
# <return> 導向管理首頁 </summary>
def adminmain(request, page_index=None):
    global page
    board_all = models.BoardUnit.objects.all().order_by('-id')      # 所有資料
    page_size = 3                                                   # 每頁資料數
    total_size = len(board_all)                                     # 資料總數
    total_page = math.ceil(total_size/page_size)                    # 總頁數

    if page_index == None:
        page = 0
        board_records = models.BoardUnit.objects.all().order_by(
            '-id')[:page_size]                                      # 取出前三筆資料

    elif page_index == 'pre':                                       # 上一頁操作
        start = (page-1) * page_size                                # 上一頁第一筆資料
        if start >= 0:                                              # 如果上一頁有資料就顯示
            board_records = models.BoardUnit.objects.all().order_by(
                '-id')[start:(start+page_size)]
            page -= 1

    elif page_index == 'next':                                      # 下一頁操作
        start = page * page_size                                    # 下一頁第一筆資料
        if start < total_size:                                      # 如果下一頁有資料就顯示
            board_records = models.BoardUnit.objects.all().order_by(
                '-id')[start:(start+page_size)]
            page += 1

    elif page_index == 'back':                                      # 確定修改完成後操作
        start = page * page_size
        board_records = models.BoardUnit.objects.all().order_by(    # 取出修改完的資料
            '-id')[start:(start+page_size)]

    else:                                                           # 修改
        record = models.BoardUnit.objects.get(id=page_index)        # 取得要修改的資料
        record.b_title = request.POST.get('board_title', '')        # 取得修改後的標題
        record.b_content = request.POST.get('board_content', '')    # 取得修改後的留言
        record.b_response = request.POST.get('board_response', '')  # 取得回覆
        record.save()                                               # 儲存修改後的資料

        return redirect('/adminmain/back/')                         # 返回管理首頁

    current_page = page + 1
    return render(request, 'adminmain.html', locals())

# <summary> 刪除 Function </summary>
# <param name='board_id'> 要刪除的資料 id </param>
# <param name='delete_type'> 刪除操作參數 </param>
# <return>
def delete(request, board_id=None, delete_type=None):
    record = models.BoardUnit.objects.get(id=board_id)              # 取出要刪除的資料
    if delete_type == 'del':                                        # 刪除資料
        record.delete()
        return redirect('/adminmain/')                              # 導向管理首頁

    return render(request, 'delete.html', locals())                 # 導向刪除頁面

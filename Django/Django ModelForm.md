# Django Form, ModelForm

# Django Form Class
## Form Class 선언
- forms 라이브러리의 Form 클래스 상속받음
- form에는 model field와 달리 TextField가 존재하지 않음
```python 
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField()
```
- view 업데이트

![image](https://user-images.githubusercontent.com/122726684/226626351-dce48c71-6ccb-442e-950e-a198482f0b59.png)

- create 템플릿 업데이트

![image](https://user-images.githubusercontent.com/122726684/226626454-3135cb02-5aef-4a76-9653-77515eead51d.png)

### Rendering options
- label, input 쌍에 대한 3가지 출력 옵션
1. as_p()
  - 각 필드가 p 태그으로 감싸져서 렌더링
2. as_ul()
  - 각 필드가 목록(li 태그) 항목으로 감싸져서 렌더링
  - ul 태그는 직접 작성해야 함
3. as_table()
  - 각 필드가 테이블(tr 태그)행으로 감싸져서 렌더링

## Widget
- HTML input element의 표현을 담당
- 단순히 HTML 렌더링을 처리하는 것이며 유효성 검증과 아무런 관계가 없음

![image](https://user-images.githubusercontent.com/122726684/226633924-490a945b-c111-4cd7-ae68-138abec97c42.png)

### Textarea 위젯 적용
```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField(widget=forms.Textarea)
```

# Django ModelForm
## ModelForm 선언
- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
- fields 속성에 `__all__`를 사용하여 모델의 모든 필드를 포함할 수 있거나 exclue 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음
```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'
```
## Model Form 구현하기
### Create
1. 유형성 검사를 통과하면 데이터 저장 후 상세 페이지로 리다이렉트
- save() method: ModelForm의 하위클래스는 인자 instance 여부를 통해 생성할 지, 수정할 지 를 결정함
  - 제공되지 않는 경우 save()는 지정된 모델을 새 인스턴스를 만듦(CREATE)
  - 제공되면 해당 인스턴스를 수정(UPDATE)
2. 통과하지 못하면 작성 페이지로 리다이렉트
```python
def create(request):
  if request.method == "POST":
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()
  context = {'form':form}
  return render(request, 'articles/create.html', context)
```

### Update
- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
1. request.POST
- 사용자가 form을 통해 전송한 데이터(새로운 데이터)
2. instance
- 수정이 되는 대상
```python
def update(request):
  article = Article.objects.get(pk=pk)
  if request.method == "POST":
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm(instance=article)
  context = {'form':form, 'article':article}
  return render(request, 'articles/update.html', context)
```

## Form과 ModelForm
### Form
- 사용자의 입력을 필요로 하며 직접 입력 데이터가 DB저장에 사용되지 않거나 일부 데이터만 사용 될 때
- 예시: 로그인 시, 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음
### ModelForm
- 사용자의 입력을 필요로 사며 입력을 받을 것을 그대로 DB 필드에 맞춰 저장할 때
- 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할 지 이미 알고 있기 때문에 곧바로 save()호출 가능

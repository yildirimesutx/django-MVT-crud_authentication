# DJANGO MVT-CRUD-AUTHENTICATION 


- Bu projemiz içerisinde aşağıda bulunan app bulunmaktadır.

    - app (temel kurulum adımları)
    - student (CRUD islemleri)
    - userapp   (DJ.User model ile AUTH islemleri)
    - customize_user (DJ. User model customizEe ek field tanımlama )
    - base_user (DJ. User modelini polymorphism ederek ek field tanımlama ayrıca defaul gelen username => email adresine cevirme )


    
    
    
    
    
    
    
    
    
    ***MEDIA YUKLENMESI***

avatar = models.ImageField("resim", upload_to="media/", blank=True, null=True)

#null db kaydetmiyor, blank boş bırakılabiliyor
#media yüklemelerinde pillow yüklenmeli

python -m pip install Pillow 
MEDIA_URL = "media/"

# View Static/Media Files: MAIN URLS.PY
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


blank = True form ile ilgili. Bunu forma aktırdığımız zaman formdan boş veri gelebilir
null = True database ile ilgili. Diyelim integer tipinde bir field'ımız var. Bu frontend tarafından boş geldi. O zaman bu alan database'de NULL olarak kayıt ediliyor. Demezsek formdan boş gelirse o zaman database kayıt ederken hata alırız


on_delete properties:
#! CASCAADE  - parent silinince silinir
#! SET_NULL  - parent silinince null yapar
#! PROTECT   - parent silinince hata verir
#! DO_NOTHING - parent silinince hiçbir şey yapmaz
#! SET_DEFAULT - parent silinince default değer atar


#! Database
#1https://docs.djangoproject.com/en/4.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
#1 $ pip install psycopg2 # alternative -> $ pip install psycopg2-binary
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangotest', # database_name
        'USER': 'postgres', # login_user_name
        'PASSWORD': '1234', # login_user_pass (setted on install)
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

-----------------------------------------------------------

#!  Template oluşturulması 


- base.html : html yapyı üzerine oturtduğumuz yer,
  - projede kullanılacak ana html yapısı
  - body kısmında {% block container %} yapısı tanımlıyoruz
  - proje sayfamızdaki navbar, footer gibi değişmeyen yapıları direk alıyoruz, örneğin register/new post/detail gibi sayfalarımız var. onları block container içerisine tanımlıyoruz.
  - register.html içinde {% extends 'student/base.html' %} ilgili base.html çağırdık 


#! form.py oluşturulması  


- Model yapımızda oluşurduğumuz tabloyu client a form ile sunduğumuzda kullanılıyor.

- Form iki türlü oluşturulabilir bir kendimiz fieldlarını yazarız, modelden bağımsız olur, 
- diğeri modelimiz import ederiz ve model field larının hepsi yada istenilenleri kullanılır.
- formu kendimiz oluşturduğumuzda db tanıtma işlemlerinde de ek kodyazılması gerekir


```
--forms.py
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
     class Meta:
        model = Student
        fields = "__all__"



---views.py
def student(request):

    form = StudentForm()
    context = {
      "form": form
   }


    return render(request, "student/student.html", context)


---student.html
{% extends 'student/base.html' %}

{% block container %}

<form action="" method="POST" enctype="multipart/form-data">
    
    {% csrf_token %}
    {{ form.as_p}}
    <input type="submit" value="OK"/>

</form>
    
{% endblock container %}


--buradaki enctype="multipart/form-data"  form içinde media istenildiği zaman

-- burada csrf token formun içine eklenmesli, gönderilen formdaki bilgileri güvenliğinin alınması maksadıyla


```

- print(request.POST) views içinde post sorgusu 






# AUTH

- AUTH-1

- Djangonun default gelen USER modelini kullanacağız.

- Default gelen USER modelinin attributes leri:

    - username
    - password
    - email
    - first_name
    - last_name


- Django kurulduğunda gelen Auth sistemi, aşağıdaki yapılar default gelmektedir.    

```
INSTALLED_APPS = [
    ...
    'django.contrib.auth',  # Core authentication framework and its default models.
    'django.contrib.contenttypes',  # Django content type system (allows permissions to be associated with models).
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages sessions across requests
    ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',  #  Associates users with requests using sessions.
    ....

```    
    
<img src="DjangoAuthModels.png"  alt="auth_model" width="600"/>






- User 3 farklı sekilde oluşturulur,
   - admin sayfası ile
   - shell ile
   - views ile


- shell ile 

```
python manage.py shell
from django.contrib.auth.models import User
user2 = User.objects.create_user('john', email='john@mail.com')
 user2
 user2.email
```




- Views ile auth

- https://docs.djangoproject.com/en/4.0/topics/auth/default/#using-the-views-1


```
ana urls.py ekledik,

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    ### And using some urls which Django give us about authentication:
    path('accounts/', include('django.contrib.auth.urls'))
]

```


- accounts path eklediğimizde default olrak aşapıdaki endpointler gelmektedir.


```
accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']
```

- LOGIN

- yukarıda accounts/ login/ yaptığımızda login.html istedi

- bu html sayfasını dokumanda default olrak faydalanambilmek icin registration/login.html folder, oluşturup icine login.html eklememiz gerekmektedir.

```
default page 

<h1>Login Page</h1>


<form action="" method="POST">
{% csrf_token %}

{{form.as_p}}

<a href="{% url 'home' %}">
<input type="submit" value="LOGIN"/>
</a>

</form>

```




- yukarıdaki islemleri yaptigimizda login olunca default olarak profile sayfasına yönlendiriyor.

- Bu yönlendirmeyi LOGIN_REDIRECT_URL = "home" settings ekleyerek gönlendirme yapıyoruz.



- REGISTER


```
from django.contrib.auth.forms import UserCreationForm

register olurken login olma aşamasında import ettik
from django.contrib.auth import authenticate, login

user kaydı oluşturabilmek icin views.py da import ettik

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    # bu bölüma kadar olan kısımda register islemi tamam bundan sonraki kisim register olduktan sonra login olmak maksadıyla 

    # asagida belirtilen kod bolumu register olurken aynı anda login olabilmesi icin   
    # cleaned_data bize form yapısı içindeki yazılan ifadeyi çekti, get ile, sayfa yapisini incele dedigimizde p tagi icinde gözükmektedir. username ve password1, import edilecek yapilar unutulmamali         
            
           username = form.cleaned_data.get("username")
           password = form.cleaned_data.get("password1")


           user = authenticate(username=username,
          password=password)
           login(request, user)
           return redirect("home") 


    context = {
        "form":form
        }

    return render(request, "registration/register.html", context)




register.html=>

<h1>Register Page</h1>


<form action="" method="POST">
{% csrf_token %}

{{ form.as_p }}

<input type="submit" value="REGISTER"/>


</form>



```


- CHANGE / RESET PASSWORD

```
urls.py=>
 path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),
    name='change-password'),

change-password.html =>
<h1>Password Change Page</h1>


<form action="" method='POST'>
 {% csrf_token %}

 {{form.as_p}}

 <a href="{% url 'home'  %}">

 <input type="submit" value='change'>
</a>
</form>

```

```
urls.py=>
path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html'), name='reset-password'),

settings.py =>
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

reset-password.html =>
<h1>Password Reset Page</h1>


<form action="" method="POST">

    {% csrf_token %}
    {{ form.as_p }}
    <br>
    <input type="submit" value="Reset Password">

</form>


terminalden sifirlama bağlantısı gönderiyor
```

```

 accounts/logout komutu ile ana sayfaya yönlendirmesi için

settings.py
LOGOUT_REDIRECT_URL = "/"
```



- decorators

```

login olunca izin verilecek sayfalar iicin kullandık



from django.contrib.auth.decorators import login_required
```

- AUTH-2

  - bu AUTH-2 de default gelen user tablosunu customize yapacağız

   - default gelen User tablo
       - username
       - email
       - first_name
       - last_name
       - password
       - last_login
       - date_joined
       - is_superuser
       - is_active
       - is_staff


- default gelen tablo dısinda ihtiyacımız olan profile pic, adres, portofolio vb attiributlere ihtiyacımız olduğunda One to One iliski kurularak yeni tabloya bu ihtiyacları yazıyoruz.


<img src="auth_customize_user.png"  alt="auth_model" width="600"/>




- AUTH-2-2

- Djangonun default gelen User modelini abstraction ile düzenledik, user modelini inherit edip ekstra fieldler düzenledik => abstraction,
- yukarıda Auth-2 de user model dışında ihtiyac olan fieldları farklı tablo ile alıp birleştirmiştik,
- bu app de User modeli aldık ve abstraction sayesinde yeni fieldlar tanımladık, ve tek tabloda devam edeceğiz.

- settinds de default user i değiştiriyoruz.

- `AUTH_USER_MODEL = 'users.User'`

- AbstractUser ile User field lar aynı, user modelde olmayan yeni field ekliyoruz, az field ekleuyeceksek bu yöntem daha kolay ve kullanışlı, fieldlar çoğalırsa tablo uzunluğundan dolayı db cevap verme süresi artar

- user modelde kullanıcıdan default olarak username alınıyordu, güncel olarak email adresi kullanıldığından, override ederek emaşl adresi tanımladık.



















#! virtualenv kurulumu
# Macos => python3 -m venv env
# Windows => python -m venv env

#+ activate komutu
# MAC/Linux => source env/bin/activate
# bash  => source env/Scripts/Activate
# windows  => env\Scripts\Activate

#& django yüklemesi
# pip install django
#? pip freeze > requirements.txt(yüklü paketleri txt dosyasına kaydettik)(bunu yapmamızın sebebi prjeyi sunduğumuzda kullanndığımız paketleri gösermesi için)

#& django projesi oluşturma
# django-admin startproject main .
#+ app olusturma
# python manage.py startapp courses

#? appi ekleme

# proje klasörümüz olan main klasörünün içinde settings.py yi açıyoruz
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #my Apps
    'courses',
]
"""


# yine aynı dizinde yer alan urls.py klasörüne app imizn içinde oluşturacağımız ursl.py ye gitmesini declare edeceğiz (best practice olarak)

"""
# main.urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("course/", include("courses.urls")),
    #burada dedik ki ana url den sonra courses endpointi geldiğinde courses.urls klasörünün içindeki urls.py klasörünü çağır ve oradaki pathleri çalıştır
]
 """

# şimdi courses klasörüne gidip urls.py mizi oluşturalım ve içi şimdilik boş kalsın 
"""
from django.urls import path

urlpatterns = [
    
]

"""

# şimdi gelelim database işlemlerine bizim yani database işlemlerini yapacağımız, databse ile iletişim kuracağımız kısım yani databse tablolarını oluşturup sileceğimiz güncelleyeceğimiz kısım bizim appimizin klasöründe yer alan models.py dosyamız 

# models.Model classından inherit alrak her bir modelimizi oluştururuz

#her bir model databsede bir tabloya işarettir
# databse tabloları proje başlamadan belirlenir bunuda yapan kişi senior developerdır

#models lerde her ekleme çıkarma da mutlaka 
# *python manage.py makemigrations ve 
#? python manage.py migrate 
# komutlarını kullanırız.

#*orm sorguları yazabileceğimiz bir yapı olan ORM(object relational mapper) yani ORM ile veritabanına veri ekleme ve çıkarma yapıyoruz. ve bunu ya viewsten yapacaz yada shellden yapabiliriz 

#models.TextField(null=True, blank=True) null =true null olabilir demiş oluyoruz ve blank form vs için zorunlu olup olmadığını belirlemek için kullanılır
#models.CharField(max_length=255) max_length = 255 karakterlik alan oluşturur

#tarih
#models.DateTimeField(auto_now_add=True) (kayıt olduğu an ki tarih ve sabit)
#update_date= models.DateTimeField(auto_now=True) (bu da işlem yapıldığında değişiyor)

#!imagefield
#pip install pillow
#models.ImageField(upload_to='media/', null=True, blank=True) upload_to='media/', image eklendiği zaman eklemek gerekiyor
#resimleri açmak için yapmamız gerekenler proje dizinine git
#1settingse git=>MEDIA_URL='media/' bunu ekle
#2.urls.py ye gidip=>urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#models relations
#!onetomany- manytoone
#models.ForeignKey(to='', on_delete=models.CASCADE) ForeignKey ile bir modeli bağlı tutabiliriz. on_delete=models.CASCADE ile silinen modelin bağlı olduğu modeli siler
#models.ManyToManyField(to='', blank=True) ManyToManyField ile birden fazla modeli bağlayabiliriz. blank=True ile boş bırakılabilir
#models.OneToOneField(to='', on_delete=models.CASCADE) OneToOneField ile bir modeli bağlayabiliriz. on_delete=models.CASCADE ile silinen modelin bağlı olduğu modeli siler

# onetoone ilişkisi bir hastanın bir aile hekimi olabilir hasta ile doktor arasında onetoone ilşki var ama bir aile hekiminin birden fazla hastası olabilir yani doktor ile hastalar arasında one to many bir ilişki var.

# şimdi bizim bir kursumuz var ve kursumuzda kategoriler var işte frontend backend gibi ve kategorilerin altında kurslar var

# kursları bir kategoriye bağlayabiliriz ama kategorilerin altında birden fazla kurs olabilir

#models relations on_delete=
#! CASCAADE  - parent silinince silinir
#! SET_NULL  - parent silinince null yapar
#! PROTECT   - parent silinince hata verir
#! DO_NOTHING - parent silinince hiçbir şey yapmaz
#! SET_DEFAULT - parent silinince default değer atar

# şimdi gidelim models.py dosyamıza

# önce kategori tablomuzu oluşturacağız



""" 
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
 """

#  şimdi artık course tablomuuz oluşturabiliriz
"""
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
"""



# şimdi oluşturduğumuz tabloları admin panelde görebilmek için yine aynı dizinde bulunan admin.py e girip tablolarımızı tanıtmamız lazım ayrıca burası bizim admin panelde yapmayı istediğimiz değişiklikleri yaptığımız kısım
"""
from django.contrib import admin
from .models import Course,Category

admin.site.register(Category)
admin.site.register(Course)
"""
#models lerde her ekleme çıkarma da mutlaka 
# *python manage.py makemigrations ve 
#? python manage.py migrate 
# komutlarını kullanırız.
# şimdi admninpanel için bir superuser oluşturalım

# python manage.py createsuperuser

# artık projeyi ayağa kaldırıp admin panele giriş yapabiliriz
# python manage.py runserver
# şimdi admin panele girebiliriz

# şimdi geldik bizim projelerimizdeki asıl kısma yani logic kısmına, database ile iletişim kuracağımız,database deki tablolarda crud işlemlerini yapabilceğimiz yani orm sorgularını yazacağımız ksııma geldik.

#views.py
# buradki her bir function veya class farketmez her bir yapı ile urls te bağlantı kuryoruz 
# yani belirttiğimiz end pointe bir istek geldiğinde views taki hangi functionu çalıştıracağımızı belirtiyoruz

# views.py import edebilceğimiz yapılar var 
# mesela 
# HttpResponse bu bize string bir ifade döndürür.

# render => buda bize belirteceğimiz bir html sayfası döndürür

# views ta oluşturacağımız her bir function bir request alır yani bir istek alır

"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import Course #orm sorgusu yapacağımız için modeli import etmemiz gerekiyor

def index(request):
    return return render(request,'index.html')#karşılama sayfamız


def home(request):
    courses=Course.objects.all() #orm sorgusu yazdık ve databaseden tüm kurs bilgilerini çektik
    return render(request, "home.html", {'courses': courses}) # render ettik ve databseden bize dönen veriyi html syafamıza ilettik mantık olarak navigate state gibi düşünülebilir

def course_detail(request, id):
    course=Course.objects.get(id=id) # tek bir eleman çekmek için get kullanırız
    return render(request, "detail.html", {'course': course})   
 """

#  şimdi de gidelim hrml lerimiz oluşturalım

# django template dosyalarını default olarka app dizinindeki templates klasöründe arar bunun için gidelim appimize templates dizini oluşturalım

# içine viewste belirttiğimiz home.html i ve detail.html i belirtelim

# template sytanxi

# for döngüleri süslü içinde {% for i in data %} {% endfor %} şeklinde kullanılır

# if else döngüleri süslü içinde {% if data %} {% else %} {% endif %} şeklinde kullanılır

# değişkenleri kullanmak için {{}} şeklinde kullanılır

# link vermemizi sağlayan a tagini href kısmına "{% url 'urlde belirttiğimiz name patternini veririz' %}" eğer id gibi specific bir veri de yollamamız gerkiyorsa bunu da "{% url 'urlde belirttiğimiz name patternini veririz' id %}" bu şekilde kullanılır

#index.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
    <div class="container">
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="https://i.picsum.photos/id/0/5616/3744.jpg?hmac=3GAAioiQziMGEtLbfrdbcoenXoWAW-zlyEAMkfEdBzQ" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="https://i.picsum.photos/id/1029/4887/2759.jpg?hmac=uMSExsgG8_PWwP9he9Y0LQ4bFDLlij7voa9lU9KMXDE" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="https://i.picsum.photos/id/1060/5598/3732.jpg?hmac=31kU0jp5ejnPTdEt-8tAXU5sE-buU-y1W1qk_BsiUC8" class="d-block w-100" alt="...">
          </div>
        </div>
      </div>
      <div class="card text-center">
        <div class="card-header">
          Clarusway Bootcamp
        </div>
        <div class="card-body">
          <h5 class="card-title">Full Stack Development</h5>
          <p class="card-text">Frontend and Backend Course</p>
          <a href="{% url 'home' %}" class="btn btn-primary">Go Course Details</a>
        </div>
        <div class="card-footer text-muted">
          2 days ago
        </div>
      </div>
    </div>

    <!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
"""

#şimdi gidelim ana url imize karşılama sayfamızı eklyelim örnek amaçlı
"""
from django.contrib import admin
from django.urls import path,include

from courses.views import index #aynı dizinde olmadığımız için hangi app teki viewsi çağırdığımız belli ettik 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path("courses/", include("courses.urls")),
]

"""

# home.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Courses</h1>
    {% for i in courses %}
        <h2><a href="{% url 'course_detail' i.id %}">{{ i.name }}</a></h2>
        <p>{{ i.description }}</p>
        <p>{{ i.category }}</p>
        <p>{{ i.publish_date }}</p>
        <p>{{ i.update_date }}</p>
    {% endfor %}
</body>
</html>
"""
# detail.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Course Detail</h1>
    <h2>{{ course.name }}</h2>
    <p>{{ course.description }}</p>
    <p>{{ course.category }}</p>
    <p>{{ course.publish_date }}</p>
    <p>{{ course.update_date }}</p>
</body>
</html>
"""

# urllerimiizi belirtme zmanı 

# urls.py
"""
from django.urls import path
from .views import home, course_detail

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>', course_detail, name='course_detail'),
]
"""

# artık projemiz hazır hale geldi

# Happy Coding 
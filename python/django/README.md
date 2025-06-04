# DJANGO

- [x] What is Django
- [x] Django project structure
- [x] How to create a project and application
- [x] Models
- [x] Serializers
- [ ] Admin Interface
- [ ] Templates
- [x] CRUD Operations (Create, Read, Update, Delete)

---

### Django

Django is a high-level Python web framework used to build secure, scalable, and maintainable web applications quickly.

_Its gives you everything you need out of the box_

**Key Features**
- Built-in routing system  
- Database connection and ORM  
- User authentication and permissions  
- Admin panel  
- Forms handling and validation  
- REST API support via Django REST Framework  

**Real-World Use Cases**
- Blogs  
- Booking systems  
- APIs for mobile apps  
- Admin dashboards  
- Social networks  

**Why Django**
- **Fast** – You can build a prototype in hours or days  
- **Secure** – Follows best practices  
- **Scalable** – Used by companies like Instagram and Pinterest  
- **Extensible** – You can plug in tools like Django REST Framework, Celery, etc.

---

## Setting Up Django and Folder Structure

**To start a project:**

1. Create a directory with the project name and `cd` into it
    ```bash
    mkdir example_project
    cd example_project
    ```

2. Create a virtual environment and activate it
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install Django and Django REST Framework
    ```bash
    pip install django djangorestframework
    ```

4. Set up a new project with a single application
    ```bash
    django-admin startproject example_project .
    python manage.py startapp example_app
    ```

5. Sync the database for the first time
    ```bash
    python manage.py migrate
    ```

6. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts.

---

## File Structure

(To be filled later – includes `manage.py`, `example_project/settings.py`, etc.)

---

## Models

Defines the database structure.  
Each class is a database table.  
Each attribute is a column (field) in that table.

### Common Field Types

| Field                  | Used For                        |
|------------------------|---------------------------------|
| `TextField`            | Long text (content, description)|
| `IntegerField`         | Whole numbers                   |
| `CharField`            | Short strings (name, title)     |
| `FloatField`/`DecimalField` | Decimal numbers (prices, rates) |
| `BooleanField`         | True/False values               |
| `DateTimeField`        | Timestamps                      |
| `EmailField`, `URLField`| Emails and website URLs        |
| `ForeignKey`           | One-to-many relations           |
| `ManyToManyField`      | Many-to-many relations          |
| `OneToOneField`        | One-to-one relation             |

**After defining models:**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Example of a Model

```python
# example_app/models.py

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.score)
```

In the model class, the `__str__` method tells Django how to represent the object as a string:

```python
return f"{self.title} by {self.author}"
return f"{self.task} - {'Done' if self.complete else 'Pending'}"
```

---

## Serializers

The heart of Django REST Framework.  
Think of serializers as translators between Python objects and JSON.

**Purpose**
- Convert model instances to JSON (for response)
- Convert JSON to Python objects (for create/update)
- Define what fields are visible/editable

### Common Types of Serializers

#### 1. `ModelSerializer` (used 90% of the time)

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = '__all__'
```

#### 2. Manual Serializers

```python
from rest_framework import serializers
from .models import Post

class ManualPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
```

| Method        | When it Runs                     | Purpose                  |
|---------------|----------------------------------|---------------------------|
| `create()`    | `.save()` after POST             | Creates a new object     |
| `update()`    | `.save()` after PUT or PATCH     | Updates an existing one  |
| `validated_data` | Cleaned input from request    | Used like `**kwargs`     |

#### Custom Validation

```python
def validate_title(self, value):
    if "badword" in value.lower():
        raise serializers.ValidationError("Title is not allowed.")
    return value
```

#### Field Control

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at']
        read_only_fields = ['id', 'created_at']
```

#### Full Example with Validation

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def validate_title(self, value):
        if "spam" in value.lower():
            raise serializers.ValidationError("No spam allowed.")
        return value

    def validate(self, data):
        if data['title'] == data['content']:
            raise serializers.ValidationError("Title and content cannot be the same.")
        return data
```

**Note:**  
`class Meta` is a special inner class Django looks for to configure the serializer.  
Use naming like `PostSerializer`, `UserSerializer`, etc.

---

## Views and Routers

They connect your models to the outside world (API endpoints).

- **Views** – Define logic for GET, POST, PUT, DELETE  
- **Routers** – Automatically generate URLs for views

### Steps (Views + Routers)

1. Create ViewSet

```python
# example_app/views.py

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

2. Create Router and Register ViewSet

```python
# example_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

3. Include in Project's `urls.py`

```python
# example_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('example_app.urls')),
]
```

To run the server:

```bash
python manage.py runserver
```
# DJANGO

- [x] What is django
- [ ] Django project sturcture
- [ ] How to create a project and application
- [ ] Models
- [ ] Serializers
- [ ] Admin Interface
- [ ] Templates
- [ ] CRUD Operations (create, Read, update, Delete)


### Django
This is a high-level Python web framework which is used in building a secure, scallable and maintainable web applications quickly

_Its gives you everything you need out of the box_

**Key Features**
- Routing system builty in 
- Database connection and ORM
- User authentication and permissions
- Admin panel 
- Forms handling and validation
- REST API support with Django REST Framework

**Real World use cases**
- Blogs
- Booking systems
-  APIs for mobile apps
- Admin dashboards
- Social networks 

**Why Django**
- Fast - You can build a prototype in hours or days
- Secure - Follows best practices
- Scalable - used by companies like Instagram and Pinterest 
- Extensible - you can plug in tools like Django REST Framework, Celery, etc



## Setting up Django and Folder Structure
**To start a project**

1. create a directory with the project name and cd into it
    
    `mkdir example_project`

    `cd example_project`

2. Create a virtual environment and activate it 
    
    `python3 -m venv venv`
    
    `source venv/bin/activate`

3. Install Django and Django REST Framework 
    
    `pip install django`
    
    `pip install djangorestframework`

4. Set up a new project with a single application
    
    `django-admin startproject example_project`
    
    `cd exapmle_project`
    
    `django-admin startapp example_app`
    
    `cd example_app`

5. Sync database for the first time 
    `python manage.py migrate`

6. Create super user
    
    `python createsuperuser`
    
    follow the prompt 


## File Structure


## Models
Defines the database structure
Each class is a database table
Each attribute is  column(field) in that table 

### Common Fields Types 
|Fields| Used For|
|------|-------------|
|`TexField`| Long text(content, description)|
|`IntegerField`| Whole numbers |
|`CharField`| Short string(name, title)|
|`FloatField`, `DecimalField`| Decimals(prices, rates)|
|`BooleanField`| Yes/No, True/False|
|`DateTimeField`| Timestamps|
|`EmailField`, `URLField`| Email and websites URLs|
|`ForeignKey`| Link to another model 1:N|
|`ManyToManyField`| Many-to-many relations|
|`OneToOneField`| One-to-one relation|

After you define a model you need to:
* `python manage.py makemigrations` - Creates migration file 
* `python manage.py migrate` - Applies them to the db  


## Example of a Model
```Python
# example_app/models.py

import django.db import models

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=model.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Rating(models.Model):
    post = model.ForeignKey(Post, on_delete=models.CASCADE, related_name="rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.score
```
In the model calss you can define `__Str__` method
This tells Django how to represent the object as a string. You can return anything. 
eg 
```python
return f"{self.title} by {self.author}.
return f"{self.task} - {"Done" if sefl.complete else "Pending"}
```

## Serializers 
The heart beat of Django REST Framework 
* More like a translator between python objects e.g., Django model and JSON(used in APIs)

**Uses**
- Converts model instance to JSON(for reponse)
- Converts JSON input to Python objects(for creating/updating)
- Define what fields are visible or editable

### Two Common Type of Serializers 
1. **ModelSerializer (used 90% of the time)**:
e.g.,
```Python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = '__all__' # This list specific fields in the model 
```

Adding validation and control to Serialization class
```python
from rest_framework import serializers
from .models import Post

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
            raise serializers.ValidationError("Title and content cannot be the same")
        return data
```
DRF runs these automatically when you call .is_valid() on the serializer. 


2. **Manual Serializers**
```Python
class ManualPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializer.CharField()
    created_at = serializer.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance 
```
- With this you have full controll 
- Good for custom validation
- APIs are not tied to a model
`validated_data` is a dictionary of all the cleanded, validated data from the request
`**validated_data` unpacks the dictionary like: `Post(title=".....", content="...")`
`instance` is the current model object being updated
`validated_data` contains the new data
`.save()` persist the data after updating fields by call this

|Method| When it Runs | Purpose|
|------|--------------|--------|
|create()|`serializer.save()` after `POST`| Creates a new object|
|`update()| `serializer.save()` after `PUT/PATCH`| Updates an existing object|
|**validated_data| cleaner data from request| Used like kwargs in model creation|

**You can also add Custom Validation**
```Python
def validate_title(self, value):
    if "badword" in value.lower():
        raise serializers.ValidationError("Title is not allowed.")
    return value 
```
**You can Control Fields**
```Python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at']
        read_only_fields = ['id', 'created']
```
Note:
`PostSerializer` is a custome nameing  it follows 
`Post` = `PostSerializer`
`User` = `UserSerializer`

`class Meta` - Special Built-in Inner Class
- Django look for it
- It tells the seriliazer how to behave
- Inside is where you specify the model use, which fiels to include etc.
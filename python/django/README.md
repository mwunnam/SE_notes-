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
To start a project
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
```text
example_project/ |--Javascript/ |-- variables 

```
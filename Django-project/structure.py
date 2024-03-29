"""
URL-https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files
1. Project Root Directory:
At the root level of your Django project, you’ll find several essential files and directories:

/my_django_project/
|-- manage.py
|-- my_django_project/
    |-- settings.py
    |-- urls.py
    |-- asgi.py
    |-- wsgi.py
|-- requirements.txt
|-- apps/
|-- static/
|-- media/
|-- templates/


manage.py: This is a command-line utility to interact with the Django project.
my_django_project/: The inner directory with the same name as the project will hold the main settings and configurations.
requirements.txt: It contains a list of project dependencies that can be installed using pip.

Another example:
    # ...\my_clubproject
    \env_myclub
    \myclub_site        <= This is your Django project
        \myclub_site    <= This is a Django app
        db.sqlite3      <= Your project database
        manage.py       <= Django project management utility

2. The “apps” Directory:
Django projects are often composed of multiple apps, each serving a specific functionality. Grouping these apps within a dedicated “apps” directory keeps the project well-organized:

/my_django_project/
|-- apps/
    |-- blog/
    |-- user_management/
    |-- ecommerce/
	
	
3. App Directory Structure:
Each app within the “apps” directory follows a structured layout. Here’s an example for the “blog” app:

/blog/
|-- migrations/
|-- static/
|-- templates/
|-- admin.py
|-- apps.py
|-- models.py
|-- views.py
|-- urls.py
|-- tests/
|-- forms.py (Optional)

migrations/: Contains database migration files generated by Django for model changes.
static/: Holds static files like CSS, JavaScript, and images specific to the app.
templates/: Contains HTML templates associated with this app.
admin.py: Configures the Django admin interface for managing app models.
apps.py: App configuration and metadata.
models.py: Defines the app's data models.
views.py: Contains the views or controller functions for handling HTTP requests.
urls.py: Defines the app's URL patterns.
tests/: Houses unit tests for the app (optional but highly recommended).
forms.py (Optional): Includes form classes if the app requires custom forms.

4. The “static” Directory:
The global “static” directory holds project-wide static files, like CSS, JavaScript, and images used across different apps:

/my_django_project/
|-- static/
    |-- css/
    |-- js/
    |-- images/
	
5. The “media” Directory:
The “media” directory is used to store user-uploaded files:
/my_django_project/
|-- media/
    |-- user_uploads/


6. The “templates” Directory:
The “templates” directory stores project-wide templates and base templates that are extended by app-specific templates:
/my_django_project/
|-- templates/
    |-- base.html
    |-- header.html
    |-- footer.html
    |-- blog/
    |-- user_management/
    |-- ecommerce/
	
Common Patterns:
In addition to the above structure, some common patterns and practices include:

Creating a separate “utils” directory for utility functions and helper modules.
Using an “api” directory for housing REST API-related files if your project includes APIs.
Using version control, such as Git, to track changes and collaborate with a team.
Organizing your Django project with a well-thought-out folder and directory structure is essential for long-term maintainability and codebase clarity.
 By following the best practices and adopting the examples mentioned above, you can ensure a clean and scalable Django project that remains easy to understand 
 and expand as your application grows.

"""
"""
In Django, middleware is a way to process requests and responses globally before they reach the view or after they leave the view. Middleware components are implemented as classes, and they provide hooks into the Django request/response processing.

Middleware components can perform various tasks such as modifying request or response objects, performing authentication, handling exceptions, adding or modifying headers, and more. Each middleware class defines one or more methods that are executed at different stages of the request-response processing.

Here are some key points about middleware in Django:

    Execution Order:
        Middleware components are executed in the order they are defined in the MIDDLEWARE setting. The order matters because each middleware can potentially modify the request or response before passing it to the next middleware or view.

    Example Middleware Class:
        A basic example of a middleware class might look like this:

    python

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed before the view is called
        response = self.get_response(request)
        # Code to be executed after the view is called
        return response

Middleware Methods:

    Middleware classes typically define one or more of the following methods:

    __init__(self, get_response): The constructor where you can set up any necessary state. get_response is a function that takes a request and returns a response.

    __call__(self, request): The method that is called for each request. This is where you can perform actions before and after the view is called.

    Example:

    python

    class MyMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Code to be executed before the view is called
            response = self.get_response(request)
            # Code to be executed after the view is called
            return response

    Additional methods include process_view, process_template_response, process_exception, and more, depending on the specific needs of the middleware.

Built-in Middleware:

    Django comes with a set of built-in middleware that can be enabled or disabled in the MIDDLEWARE setting. Examples include:
        django.middleware.security.SecurityMiddleware
        django.contrib.sessions.middleware.SessionMiddleware
        django.middleware.common.CommonMiddleware
        django.contrib.auth.middleware.AuthenticationMiddleware
        ...

Custom Middleware:

    Developers can create custom middleware to add project-specific functionality. For example, logging requests, modifying headers, or implementing custom authentication.

Middleware Configuration:

    Middleware is configured in the MIDDLEWARE setting in the settings.py file. The order of middleware classes is crucial, as it determines the order in which they are executed.

python

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        # ... other middleware ...
    ]

Middleware is a powerful feature in Django that allows developers to intervene in the request-response cycle and perform actions at various stages. It provides a flexible mechanism for extending and customizing the behavior of Django applications.

"""
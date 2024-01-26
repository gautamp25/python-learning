# What is Alembic?
"""
Alembic is a database migration tool for SQLAlchemy, which is a popular SQL toolkit and Object-Relational Mapping (ORM) library for Python. In the context of SQLAlchemy, Alembic provides a mechanism for managing database schema changes over time. It enables developers to version control database schemas, create and apply database migrations, and automate the process of updating the database schema as the application evolves.

Key features and concepts of Alembic include:

    Migration Scripts:
        Alembic generates migration scripts that describe changes to the database schema.
        These scripts capture alterations such as adding or removing tables, modifying columns, and other schema-related operations.

    Versioning:
        Alembic introduces the concept of versioning to the database schema.
        Each migration script is associated with a version number, allowing Alembic to track the current state of the database schema and apply changes in the correct order.

    Autogeneration:
        Alembic can automatically generate migration scripts by comparing the current state of the database with the SQLAlchemy models defined in the application.
        This feature simplifies the process of creating migration scripts for common schema changes.

    Command-Line Interface (CLI):
        Alembic provides a command-line interface that developers can use to interact with the tool.
        Common commands include creating a new migration, applying migrations to the database, and managing the migration history.

    Integration with SQLAlchemy:
        Alembic is designed to work seamlessly with SQLAlchemy.
        It leverages the SQLAlchemy model definitions to generate migration scripts and apply changes to the database.

    Multiple Database Support:
        Alembic supports multiple database backends, allowing developers to use it with different relational database systems like PostgreSQL, MySQL, SQLite, and others.

Typical Workflow with Alembic:

    Initialization:
        Developers initialize Alembic in their project, creating an initial migration script that captures the initial state of the database.

    Model Changes:
        As the application evolves, developers make changes to the SQLAlchemy models to reflect the desired database schema.

    Autogenerate:
        Developers use Alembic's autogenerate feature to automatically create migration scripts based on the changes to the SQLAlchemy models.

    Migration Execution:
        Alembic commands are used to apply the generated migration scripts to the database, updating the schema.

    Version Control:
        Alembic maintains a version history of applied migrations, ensuring that each database instance is at the correct version.

By using Alembic in conjunction with SQLAlchemy, developers can manage database schema changes in a systematic and version-controlled manner, making it an essential tool for projects that rely on SQLAlchemy for database interactions.

- Create Migration:
    alembic revision -m "create account table

    alembic revision -m "Add a column"

    alembic history --verbose

    # revision identifiers, used by Alembic.
    revision = '1975ea83b712'
    down_revision = None
    branch_labels = None

    from alembic import op
    import sqlalchemy as sa

    def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

    def downgrade():
        op.drop_table('account')

- Run Migration:
        alembic upgrade head

"""

# What is 'g' object in flask?
"""
In Flask, the g object is a global object that can be used to store data during the lifetime of a request. 
It provides a way to share data across different parts of the application without having to pass it explicitly through function parameters.

Key characteristics of the g object in Flask:

    Lifetime:
        The g object is specific to each request and is created when a request begins processing and is discarded when the request is complete.
        It is part of the Flask application context, and its lifespan is tied to the duration of a single request.

    Storage:
        It is a simple namespace object that can store arbitrary data.
        Data stored in the g object is available to all functions and methods that are part of the same request context.

    Usage:
        Developers can use the g object to store information that needs to be accessed by multiple functions during the processing of a request.
        Common use cases include sharing database connections, storing user information, or passing information between different parts of a request-handling pipeline.

    Thread Safety:
        The g object is designed to be thread-safe within the context of a single request. Each request has its own g object, so there is no risk of data interference between concurrent requests.

Example:

python

from flask import Flask, g

app = Flask(__name__)

# Example of using g to store and access data during a request
@app.before_request
def before_request():
    g.user = get_current_user()

@app.route('/profile')
def profile():
    # Accessing data stored in g
    user = g.user
    return f'User Profile: {user.username}'

def get_current_user():
    # Example function to retrieve the current user from the database
    # In a real application, this function would perform database queries or other operations
    # to determine the current user for the request.
    return User(username='john_doe')

class User:
    def __init__(self, username):
        self.username = username

if __name__ == '__main__':
    app.run()

In this example, the before_request function is executed before each request, and it sets the current user in the g object. Later, the profile route accesses the user information from the g object. This allows data to be shared between different parts of the request-handling process.
"""

"""
Flask is a popular web framework for Python, and interview questions for Flask can cover a range of topics from basic concepts to more advanced features. Here are some commonly asked Flask interview questions:

    What is Flask?
        Flask is a micro web framework for Python that is lightweight and modular. It is designed to be easy to use and extend, allowing developers to build web applications quickly.

    How does routing work in Flask?
        Flask uses the @app.route() decorator to define routes. For example:

        python

    @app.route('/')
    def index():
        return 'Hello, World!'

Explain the concept of a Flask Blueprint.

    Blueprints are a way to organize and group related routes, templates, and static files in a Flask application. They allow for modular application development.

What is the difference between render_template and render_template_string in Flask?

    render_template is used to render HTML templates stored in separate files, while render_template_string renders templates provided as strings directly in the code.

How does error handling work in Flask?

    Flask provides the @app.errorhandler() decorator to handle specific HTTP errors or exceptions. For example:

    python

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

Explain Flask request and response objects.

    The request object in Flask provides access to incoming request data, while the response object is used to build and modify the outgoing response.

What is Flask-WTF, and why would you use it?

    Flask-WTF is a Flask extension for working with web forms. It integrates with the WTForms library and simplifies form handling in Flask applications.

How can you handle file uploads in Flask?

    File uploads are handled using the request.files object. The FileStorage object in Flask provides access to uploaded files, and you can use it to save or process the files.

Explain Flask SQLAlchemy and its role in Flask applications.

    Flask SQLAlchemy is an extension for Flask that adds support for SQLAlchemy, a popular Object-Relational Mapping (ORM) library. It simplifies database interactions in Flask applications.

How do you handle authentication in Flask?

    Authentication in Flask can be implemented using various methods, such as Flask-Login or JWT (JSON Web Tokens). Flask-Login provides user session management, while JWT can be used for token-based authentication.

Explain Flask context.

    Flask has two contexts: application context and request context. The application context is created when the application starts, while the request context is created for each incoming request. The g object and the current_app object are examples of objects that exist within the context.

What is Flask-SocketIO, and how does it enable real-time communication in Flask?

    Flask-SocketIO is an extension for Flask that adds support for Socket.IO, a real-time bidirectional communication library. It allows for real-time updates and interactions between the server and clients.
"""

# Advanced interview questions
"""
    Explain the role of Flask Blueprints in large-scale applications. Provide examples of when and how you would use them.

    How would you implement token-based authentication in a Flask application? Discuss the advantages and potential security considerations.

    Describe the use of Flask Middleware. Provide examples of scenarios where you might use middleware in a Flask application.

    Explain the concept of Flask Signals and how they can be utilized for event-driven programming in a web application.

    Discuss different methods of handling database migrations in Flask applications. How do tools like Alembic contribute to this process?

    Explain the purpose of Flask's before_request and after_request decorators. Provide use cases where these might be beneficial.

    How would you optimize a Flask application for performance and scalability? Discuss caching strategies, load balancing, and other techniques.

    Describe how you would implement RESTful APIs in Flask. Discuss the use of Flask-RESTful or other extensions for building APIs.

    Explain the use of Flask Testing. How would you write unit tests and integration tests for a Flask application?

    Discuss the role of Flask's current_app object and the context stack. How does it contribute to managing the application's state?

    Explain how you would implement WebSocket communication in a Flask application. Discuss the integration of Flask-SocketIO or alternative approaches.

    Discuss security best practices in Flask development. How do you protect against common vulnerabilities, such as SQL injection and Cross-Site Scripting (XSS)?

    Explain the concept of Flask Factory Patterns. How can it be used to create scalable and modular Flask applications?

    Describe your experience with RESTful API versioning in Flask. Discuss different strategies for versioning APIs and their implications.

    Discuss Flask's integration with OAuth. How would you implement OAuth-based authentication in a Flask application?

    Explain how you would handle asynchronous tasks in Flask. Discuss the use of Celery or other asynchronous task queues.

    Describe your experience with Flask extensions. Provide examples of extensions you have used and how they contributed to your projects.

    How would you handle CORS (Cross-Origin Resource Sharing) in a Flask application? Discuss the challenges and solutions related to cross-origin requests.

    Discuss your experience with Flask and microservices architecture. How would you design and implement microservices using Flask?

    Explain the Flask Testing Pyramid. How do you balance unit tests, integration tests, and end-to-end tests in a Flask project?
""" 


"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""

def splitStr(mystr):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    strlen = len(mystr) # o(1)
    mid = int(strlen/2)
    a = mystr[0:mid]
    b = mystr[mid:]
    print(a,b)
    a_count = 0
    b_count = 0
    for i in a:
        if i in vowels:
            a_count+=1
    for j in b:
        if j in vowels:
            b_count+=1
    if a_count == b_count:
        return True
    else:
        return False 






print(splitStr("&o1234gsot"))

# List of test cases
#1. 
#2.len > 0
#3. len is even
O(n)+ o(m)
O(n+m) 


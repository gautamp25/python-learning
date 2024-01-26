
"""Brief introduction - Technoogy & experty, project description
Day to day activities
React-
    State Management-state & props
    Promise
    pure function
    DOM and Virtual DOM
    Have you worked on Redux
    Design pattern in react

Python:
    Best pactices followed in Django project
    Authentication and Authorization django.
    which library to use for JWT?
    Diff in List & Tuple
    Lambda function
    Try, Except and finally block- if we got exception then where it will go, in finally block which object will pass.

    Which AWS services you used- Moitoring services

Database:
    Postgres advantages and disadvantages?
    ==>
        PostgreSQL is a feature-rich, open-source database with strong community support. 
        Its advantages, such as SQL compliance, extensibility, and scalability, make it suitable for a wide range of applications. 
        However, users should be aware of potential challenges, including a learning curve and considerations around memory usage. 
        The choice of a database depends on the specific needs and goals of a project.
"""

#Behavior Quesions.
#How u r going to handle client if there is any issue and it impacting business.
"""
    Handling a production bug that is impacting the business requires a systematic and prompt response to minimize the impact and resolve the issue as quickly as possible.
    Here's a general guide on how to handle such a situation:

    Acknowledge and Assess:
        Acknowledge the issue and assess its severity. Understand the impact on users and the business.
        Prioritize fixing critical issues that have a significant impact on functionality, data integrity, or user experience.

    Alert and Notify:
        If your system has monitoring and alerting in place, it might have already triggered alerts for the issue. Ensure that relevant stakeholders, including development, operations, and business teams,
        are notified about the problem.

    Create a Incident Response Team:
        Assemble a cross-functional incident response team that includes developers, operations, and relevant stakeholders. This team should collaborate to diagnose and resolve the issue.

    Isolate and Rollback:
        If possible, identify the cause of the issue and consider rolling back the recent changes that might have introduced the bug. This could involve reverting to a previous version of the code or configuration.

    Temporary Fix or Mitigation:
        If a complete fix is not immediately available, consider implementing a temporary fix or mitigation to reduce the impact on users and the business. 
        This might involve disabling specific features, adjusting configurations, or implementing workarounds.

    Communicate Proactively:
        Keep stakeholders informed about the progress in resolving the issue. Provide regular updates on what is being done, expected resolution time, and any temporary measures in place. 
        Open and transparent communication helps manage expectations.

    Test and Validate:
        Before deploying any fix to production, thoroughly test it in a staging environment to ensure it doesn't introduce new issues. Automated tests, if available, can be invaluable during this phase.

    Deploy the Fix:
        Once you have a fix or workaround, deploy it to the production environment. Ensure that the deployment process is well-tested and does not introduce new problems.

    Post-Incident Review:
        Conduct a post-incident review (post-mortem) to analyze the root cause of the issue and identify areas for improvement. This includes understanding why the bug occurred, 
        how it went unnoticed, and how to prevent similar issues in the future.

    Documentation and Knowledge Sharing:
        Document the incident, its resolution, and the lessons learned. Share this information with the team to improve overall system resilience and to avoid similar issues in the future.

Remember, a quick and well-coordinated response is crucial in handling production issues. Having incident response plans, monitoring systems, and well-defined communication channels in place can help streamline the process.
"""

# Django best project practices
"""
Best practices for Django projects encompass a range of considerations, including
project structure, coding conventions, security, performance, and maintainability. 
Here are some key best practices for Django projects:
1. Project Structure:

    Follow Django Conventions:
        Adhere to Django's project structure conventions, including the use of apps for modular components and the manage.py file for management commands.

    Use a Virtual Environment:
        Always use a virtual environment (venv or virtualenv) to isolate project dependencies.

    Separate Settings for Different Environments:
        Use separate settings files for development, testing, and production environments. Use tools like python-decouple or django-environ for managing environment variables.

2. Code Organization:

    Modular Apps:
        Organize your project into reusable apps, each serving a specific functionality. This promotes code reusability and maintainability.

    Thin Views, Fat Models:
        Keep views lightweight by moving business logic to models. Follow the "Fat models, thin views" principle for better separation of concerns.

    DRY (Don't Repeat Yourself):
        Avoid code duplication by adhering to the DRY principle. Reuse code using mixins, decorators, and utility functions.

3. Security:

    Use django.contrib.auth for Authentication:
        Leverage Django's built-in authentication system (django.contrib.auth) for user authentication. Avoid rolling your authentication system unless absolutely necessary.

    Keep Secrets Secure:
        Store sensitive information, such as secret keys and credentials, in a secure manner. Use environment variables or a configuration management tool. Never hardcode secrets in the code.

    SSL for Production:
        Ensure that your production site uses SSL to encrypt data in transit. Configure your web server (e.g., Nginx or Apache) to enforce HTTPS.

    Security Middleware:
        Enable Django's security middleware (django.middleware.security.SecurityMiddleware) to add security-related headers to HTTP responses.

Performance:

    Use Django Debug Toolbar Carefully:
        While Django Debug Toolbar is a powerful debugging tool, use it sparingly in production to avoid unnecessary performance overhead.

    Caching:
        Implement caching for expensive operations using Django's caching framework. Consider using a caching backend like Redis or Memcached.

Database:

    Optimize Database Queries:
        Use the Django Debug Toolbar or other profiling tools to identify and optimize slow database queries. Leverage the Django ORM efficiently.

    Database Indexing:
        Add appropriate indexes to database tables for columns involved in frequent query conditions. This improves query performance.

Testing:

    Write Tests:
        Write comprehensive tests for your code using Django's testing framework. Include unit tests, integration tests, and functional tests.

    Automated Testing:
        Set up automated testing using tools like pytest or Django's built-in test runner. Run tests automatically as part of your CI/CD pipeline.

Version Control:

    Use Version Control:
        Use a version control system (e.g., Git) for your project. Regularly commit changes, write meaningful commit messages, and follow a branching strategy.

Documentation:

    Document Code:
        Write clear and concise comments in your code. Additionally, maintain external documentation, especially for APIs and project setup.

    README File:
        Include a well-documented README file that provides information on how to set up, configure, and run the project.

Deployment:

    Automate Deployment:
        Use automated deployment tools (e.g., Ansible, Fabric) to streamline and automate the deployment process.

    Containerization:
        Consider using containerization (e.g., Docker) for consistent and reproducible deployments across different environments.

Monitoring and Logging:

    Monitoring:
        Set up monitoring for your application, including error tracking, performance monitoring, and log aggregation.

    Logging:
        Implement proper logging in your application to capture important events and errors. Use tools like django-request-logging for HTTP request logging.

Community Best Practices:

    Follow PEP 8:
        Adhere to PEP 8 style guidelines for Python code. Consistent and clean code improves readability and maintainability.

    Stay Updated:
        Keep your Django version and dependencies up to date to benefit from the latest features, improvements, and security patches.

    Contribute to the Community:
        Contribute to the Django community by sharing reusable apps, reporting issues, and participating in discussions.

By following these best practices, you can build maintainable, secure, and efficient Django projects that are easier to develop, deploy, and maintain over time.
"""
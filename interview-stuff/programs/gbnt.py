"""
What is api throttling?
method of REST?
serverless computing and benefits of Lambda?
What is lambda function
security groups in AWS
context manager in python
abstract class?
Instance method,staticmethod & class methods in python?
Can we update class variable in static method?

"""

my_string = 'ab@c/def$ij'
opt='ji@f/edc$ba'
for i in range(len(my_string)-1):
  print(my_string[i])


  my_dict = {1:'a', 2:[],3:{4: {5: {}}}}
  print(len(my_dict))
# count = 0

d = {1:'a', 2:[],3:{4: {5: {}}},4:'qbc'}

# correct way
def count_nested_dicts(d):
    count = 0
    for value in d.values():
        if isinstance(value, dict):
            count += 1
            count += count_nested_dicts(value)
    return count

print(count_nested_dicts(d))

# =========================
my_string = 'ab@c/def$ij'

# Convert string to list of characters
my_list = list(my_string)

# Initialize variables for start and end indices of alphabetic characters
start = 0
end = len(my_list) - 1

# Loop over the characters in the list
while start < end:
    # If start character is not alphabetic, move to the next character
    if not my_list[start].isalpha():
        start += 1
    # If end character is not alphabetic, move to the previous character
    elif not my_list[end].isalpha():
        end -= 1
    # If both start and end characters are alphabetic, swap them
    else:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1
    print(my_list)

# Convert list of characters back to string
my_string = ''.join(my_list)

# Print the reversed string
print(my_string)  # Output: ji@c/fed$ba
# ----------------------------------------
import re

my_string = 'ab@c/def$ij'

# Use regular expression to match alphabetic characters
matches = re.findall(r'[a-zA-Z]', my_string)

# Reverse the order of the matches
matches.reverse()
print(matches)
print(lambda m: matches.pop(0), my_string)

# Replace the alphabetic characters in the string with the reversed characters
my_string = re.sub(r'[a-zA-Z]', lambda m: matches.pop(0), my_string)

# Print the reversed string
print(my_string) 

# ===================================


# def decorator_fuc(func,a):
#   def wrapper_func():
#     print(a)
#     print("In wrapper func")
#     return func()
#   return wrapper_func 

# # @decorator_fuc
# def greet():
#   print("Hello there Good Afternoon")

# my_decorator = decorator_fuc(greet,a=3)
# my_decorator()


class Employee:
  
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
  @staticmethod
  def display():
    print()

  
  def display(self):
    print("")
  @classmethod
  def display_details(cls):
    print(f"My name is {cls.name}")
    


obj1 = Employee("Shyam",20)
Employee.display_details()

my_string = 'ab@c/def$ij'
opt='ji@f/ed'
for i in range(len(my_string)-1):
  print(my_string[i])




  # =======================
  """
  API throttling, also known as rate limiting, is a technique used by API providers to control the rate at which clients can make requests to their APIs. Throttling is implemented to prevent abuse, ensure fair usage, and protect the server from being overwhelmed by a high volume of requests. The goal is to maintain a balance between providing access to the API for legitimate users and preventing misuse.

Key aspects of API throttling include:

    Request Rate Limits:
        API providers set limits on the number of requests a client can make within a specified time period. For example, an API might allow 1000 requests per hour for a particular user or API key. Exceeding this limit results in throttling.

    Types of Throttling:
        There are various ways to implement throttling. Some common types include:
            Fixed Window Throttling: Limits are enforced within fixed time windows (e.g., 100 requests per minute).
            Token Bucket Throttling: Tokens are added to a bucket at a fixed rate, and clients consume tokens for each request. Once the bucket is empty, further requests are delayed.
            Leaky Bucket Throttling: Similar to token bucket, but requests are released at a fixed rate, creating a leaky bucket effect.

    HTTP Status Codes:
        When a client exceeds the allowed rate, the API server responds with HTTP status codes indicating the throttling status. Common status codes include 429 Too Many Requests and 503 Service Unavailable.

    Retry-After Header:
        The API server may include a Retry-After header in the response, indicating the amount of time a client should wait before making additional requests.

    Quotas and Plans:
        Throttling limits may vary based on the user's subscription plan or API key. Paid plans might have higher rate limits than free plans.

    Preventing Abuse and DDoS Attacks:
        Throttling helps mitigate the risk of abuse, unintentional spikes in traffic, and Distributed Denial of Service (DDoS) attacks by limiting the rate at which requests are processed.

    Developer Experience:
        APIs often provide mechanisms for developers to monitor their usage, check rate limits, and handle throttling gracefully in their applications.

API throttling is a crucial component of API management and helps maintain the availability, reliability, and performance of APIs. It is commonly used by both public APIs and internal APIs to ensure a fair and secure environment for all users.
  
  """

  """
  In REST (Representational State Transfer), which is an architectural style for designing networked applications, there are several common HTTP methods (also known as HTTP verbs) that are used to perform different operations on resources. These methods define the actions that can be performed on a resource and correspond to CRUD (Create, Read, Update, Delete) operations. The primary HTTP methods used in RESTful APIs are:

    GET:
        The GET method is used to retrieve information or data from a specified resource. It should not have any side effects on the server or the resource.

    POST:
        The POST method is used to submit data to be processed to a specified resource. It is often used to create a new resource or initiate a background process.

    PUT:
        The PUT method is used to update a resource or create a new resource if it does not exist. It replaces the entire resource or creates it if it doesn't exist.

    PATCH:
        The PATCH method is used to apply partial modifications to a resource. It is typically used when you want to update only a portion of the resource, leaving the rest unchanged.

    DELETE:
        The DELETE method is used to request the removal of a resource. It indicates that the client wants the resource identified by the URI to be removed.

    OPTIONS:
        The OPTIONS method is used to describe the communication options for the target resource. It can be used to check the allowed methods or other information about a server's capabilities.

    HEAD:
        The HEAD method is similar to GET but is used to request the headers of a resource without the actual body content. It can be used to check for the existence of a resource or to get metadata about it.

    TRACE:
        The TRACE method is used to perform a message loop-back test along the path to the target resource. It can be used for diagnostic purposes.

These HTTP methods are fundamental to the RESTful architecture and are used to perform various operations on resources. The choice of the appropriate method depends on the action you want to perform and the semantics of the operation. In a well-designed RESTful API, these methods are mapped to the corresponding CRUD operations on resources.
  """
  
    


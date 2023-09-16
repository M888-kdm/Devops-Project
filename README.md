# devopsProjetClasse
Projet de classe devops
The main of this project is to develop a simple Django application that is deployed using a Continuous Integration/Continuous Deployment (CI/CD) pipeline. The pipeline will be implemented using GitHub Actions, Docker, and Kubernetes.


# 1-Django App:
## 1-1 How to run the django App ?

To run the django app first clone the repository with `git clone https://github.com/M888-kdm/devopsProjetClasse.git` on your terminal.
Then go on your IDE terminal on the clone project directory then to build the project run `docker-compose build `:

<img width="1680" alt="Screenshot 2023-09-16 at 13 43 05" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/82677158-0866-4892-997c-5d8fd2dcb1ab">

Then run the `docker-compose up -d ` to start containers:

<img width="1680" alt="Screenshot 2023-09-16 at 13 43 37" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/e41b6860-e89d-48d2-82ad-ca0bcc219250">

 ## 1-2 Deep dive into django app :
 We have 2 endpoints : 
### The first endpoint (`localhost:8000/users` on the web browser)
It returns the list of users in the databases (username, email, first name and last name) : 
 
<img width="1658" alt="Screenshot 2023-09-16 at 16 32 27" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/76d419a7-270a-4d24-8b3e-3b80bddab215">


 To go into details in the implementation, this is the views.py where i will explain the function behind each endpoint.
 About the view function of  the `local:8000/users` endpoint :
 
<img width="660" alt="Screenshot 2023-09-16 at 14 35 44" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/248bb147-5ae7-4aa9-8649-2a175fce834e">

This function counts and stores the number of visits to a web page while displaying a list of users from a database in a web application using Django.
Let's break down what this function does step by step:

`def user_list(request):` This line defines a function named user_list that takes a request object as its parameter. In Django, view functions are responsible for handling incoming HTTP requests and returning HTTP responses.

`visits = cache.get('visits')`: This line attempts to retrieve a value named 'visits' from a cache. Caching is a technique used to store and retrieve data efficiently, often used to reduce the load on a database or other data source. In this case, it's trying to get the number of visits from the cache.

`if(visits is None):` This conditional checks if the visits value obtained from the cache is None. If it's None, it means there are no visits stored in the cache, so it sets visits to 1.

else: If the visits value is not None, this block is executed.

visits += 1: Here, the number of visits is incremented by 1, indicating that a new visit has occurred.

`cache.set('visits', visits, timeout=3600)`: After updating the visit count, this line sets the 'visits' value in the cache to the new value of visits. It also specifies a timeout of 3600 seconds (1 hour) for this cache entry. This means that after 1 hour, the cached value will expire and need to be recomputed.

`users = Utilisateur.objects.all()`: This line queries the database to retrieve all records from the Utilisateur model (presumably a Django model representing users). It retrieves all user objects from the database.

`return render(request, 'formulaire/user_list.html',{'users': users })`: Finally, this line renders an HTML template named 'formulaire/user_list.html' and passes the users data obtained from the database as a context variable to the template. The render function generates an HTTP response containing the HTML content, which is sent back to the client's web browser.

About the tests.py,the one for this previous view function is below :

<img width="706" alt="Screenshot 2023-09-16 at 15 00 12" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/83920664-b6a1-4d07-b3f2-052a2dc38183">
What we do above is break down as follow:
`setUp(self):` This function is called before each test method and is used to set up any necessary data or conditions for the tests. In this case, it creates a sample user in the database with some predefined attributes.

`test_user_list_view(self):` This function is a test method that checks if the user list view returns a 200 status code when accessed. It sends a GET request to the view and asserts that the response status code is 200 (indicating a successful request).

`test_user_list_view_context(self):` This test method verifies if the user list view contains user data in its context. It sends a GET request to the view, extracts the "users" variable from the response context, and checks if there is exactly one user in the context.

`test_user_list_view_template(self):` This function tests if the user list view uses the correct template for rendering. It sends a GET request to the view and asserts that the response uses the specified template, "formulaire/user_list.html."

### The second endpoint `localhost:8000/visit_count`:
It check count the number of visits of the website.
A glance is presented below: 
<img width="1680" alt="Screenshot 2023-09-16 at 16 33 10" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/c54c4780-e212-48b8-9fbb-456f8adccd66">



About the view function :

<img width="660" alt="Screenshot 2023-09-16 at 14 36 04" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/69e19f85-89c1-4a35-914b-78b54e050ed7">

Here is the keys of this function:

`def get_visit_count(request)`: This defines the view function and takes a request object as a parameter, which represents an HTTP request made to this view.

`visits = cache.get('visits')`: This line attempts to retrieve a value called 'visits' from the cache. In Django, the cache is a storage mechanism that allows you to store and retrieve data quickly, often used to store frequently accessed data temporarily.

`return render(request, 'formulaire/visit_count.html', {'visits': visits})`: This line renders an HTML template named 'formulaire/visit_count.html' and passes a context variable 'visits' to that template. The 'visits' variable contains the value retrieved from the cache.
**NB:**__ the cache was stored every time we access the `localhost:8000/users` in a cache variable named cache.

For the unit test of this function:
<img width="1146" alt="Screenshot 2023-09-16 at 15 25 43" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/c243e738-ecf2-4036-89a7-fd33a1db00c9">

Class Definition:
`class GetVisitCountViewTest(TestCase):` - This defines a test case class named GetVisitCountViewTest, which inherits from Django's TestCase class. Test case classes are used to group related test methods.
setUp Method:

`setUp(self):` - This is a special method that gets executed before each test method in the test case. In this method:
Sample user data is created in the database for testing purposes. This data includes a user with attributes like username, email, first name, and last name.
test_get_visit_count_view Method:

`test_get_visit_count_view(self):` - This is a test method responsible for testing the get_visit_count view.
It first simulates a visit count (in this case, 42) in the cache using cache.set('visits', 42).
Then, it sends an HTTP GET request to the get_visit_count view using self.client.get(reverse("formulaire:visit_count")).
Finally, it asserts that the HTTP response status code is 200, indicating a successful response.
test_get_visit_count_view_context Method:

`test_get_visit_count_view_context(self):` - This test method checks the behavior of the get_visit_count view when there are no visits in the cache.
It simulates the absence of visits in the cache by deleting the 'visits' key with cache.delete('visits').
Then, it sends an HTTP GET request to the get_visit_count view.
It checks if the 'visits' variable in the view's context is None to verify that no visits are cached.

**`test_get_visit_count_view_template Method:`**

`test_get_visit_count_view_template(self):` - This test method checks if the get_visit_count view uses the correct HTML template.
It simulates a visit count (in this case, 42) in the cache using cache.set('visits', 42).
Then, it sends an HTTP GET request to the get_visit_count view.
It asserts that the view uses the expected template named "formulaire/visit_count.html" by calling self.assertTemplateUsed.

**ALL TEST IS OK :**
When we go on the terminal of the docker-container of the app and run the command `python manage.py test`

<img width="950" alt="Screenshot 2023-09-16 at 15 38 19" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/7f65da6e-652b-4265-bff8-6dfd4ad78620">

# 2- Docker:
We create our docker image in Dockerfile:
This screen below is self-explanatory 
<img width="530" alt="Screenshot 2023-09-16 at 15 41 54" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/d9cd4ea3-af82-48ff-8258-8c98b39fcd7e">

Our application uses a Postgres database and Redis to store the cache so we write containers as services as the facility is provided by `docker-compose.yml`:

<img width="530" alt="Screenshot 2023-09-16 at 16 27 00" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/15fa4f7e-068d-4487-accd-0ba41d3372b4">



 
 






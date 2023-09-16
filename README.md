# devopsProjetClasse
Projet de classe devops
The main of this project is to develop a simple Django application that is deployed using a Continuous Integration/Continuous Deployment (CI/CD) pipeline. The pipeline will be implemented using GitHub Actions, Docker, and Kubernetes.


# 1-Django App:
## 1-1 How to run the django App ?

To run the django app first clone the repository with `git clone https://github.com/M888-kdm/devopsProjetClasse.git` on your terminal.
Then go on your IDE terminal on the clone project directory then to build the project run `docker-compose build `:

<img width="1680" alt="Screenshot 2023-09-16 at 13 43 05" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/79c55535-79d8-46df-b936-33dfcb576fb5">

Then run the `docker-compose up -d ` to start containers:

<img width="1680" alt="Screenshot 2023-09-16 at 13 43 37" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/e41b6860-e89d-48d2-82ad-ca0bcc219250">

To start the app go on your web browser on the url : `localhost:8000`


<img width="1680" alt="Screenshot 2023-09-16 at 14 24 21" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/9780fa7e-6aa1-45b3-9c16-8011b756b8fc">

 ## 1-2 Deep dive into django app :
 We have 2 endpoints : 
 The first one (`localhost:8000/users` on the web browser) returns the list of users in the databases (username, email, first name and last name) : 
 
 <img width="1680" alt="Screenshot 2023-09-16 at 13 24 20" src="https://github.com/M888-kdm/devopsProjetClasse/assets/108241621/a35642f2-d974-4d5b-ab42-ebbcb9e2d4a6">

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

The url of this view is 



 
 






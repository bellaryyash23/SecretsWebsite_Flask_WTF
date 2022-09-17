# 🤫Secrets Website🔐 using Flask, WTForms, Bootstrap, Jinja of Python

🌟A website that holds some secrets. Only with the right username and password can you access the page with my secrets. Built forms using a Flask extension called 
Flask-WTF. Designed the Website using the Flask-Bootstrap extension & used templating with Jinja, along with basic HTML & CSS to create this website.

👉In the 'main.py' the class i.e. the template for the form is created using the Flask-WTF quickstart. This allows us to create Flask Forms which are easy to design and
can be added with features like validators, error message responder & Field separator depending on the input we want.

👉Next, the Flask app and server is created. The various routes and functions are setup using Flask decorator functions.

👉For the designinig of the website and maintaining consistency over all webpages the use of Bootstrap and Jinja is done. The base template for each webpage is defined 
in the 'base.html' file. This template is then inherited to all other webpages using the Jinja '{% extends %}' method. 

👉The Home page is designed and rendered as follows:

![Home Page of Website](https://github.com/bellaryyash23/SecretsWebsite_Flask_WTF/blob/master/samples/home.jpg?raw=true)

👆Home Page of Website👆

👉Next, the login page where the WTForms magic is implemented is created. Using the Jinja 'render_template()' method, the WTForm object created earlier is passed as an
argument to render the HTML file. This is caught in the respective file and form is rendered. 

👉One of the main reasons why we're using Flask-Bootstrap in this project is because it has one of the most convenient methods for generating forms with WTForms.
Literally, in 1 line of code, we can create your form. It's as simple as typing this '{‌{ wtf.quick_form(form) }}' and the form in its entirety along with styling and
labels and validators gets created.

![Login Page of Website](https://github.com/bellaryyash23/SecretsWebsite_Flask_WTF/blob/master/samples/login.jpg?raw=true)

👆Login Page of Website👆

👉With WTForms it is easier to get hold of the form data. Just use the notation '<form_object>.<form_field>.data' and the form data from a POST reqquest can be accessed.
Also, inorder to check if the request is GET or POST we can use 'validate_on_submit()' method. 

👉With this when a user enters wrong credentials they get directed to the 'denied.html' page and are not allowed the access of the Secrets of Website. 

![Access Denied Page of Website](https://github.com/bellaryyash23/SecretsWebsite_Flask_WTF/blob/master/samples/denied.jpg?raw=true)

👆Access Denied Page of Website👆

👉But, when a user enters the correct credentials in the login form and gets validated then, they are directed to the Top Secret page hidden in the website.
This valdation being done using WTForms.

![Secrets Page of Website](https://github.com/bellaryyash23/SecretsWebsite_Flask_WTF/blob/master/samples/success.jpg?raw=true)

👆Secrets Page of Website👆

🌟Thus, in this way the complete website is programmed and designed. And we can see it in action as follows:

![The Sectets Website](https://github.com/bellaryyash23/SecretsWebsite_Flask_WTF/blob/master/samples/site.gif?raw=true)

👆The Sectets Website👆

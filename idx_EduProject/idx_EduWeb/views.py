from django.shortcuts import render, redirect
from .models import Course, Student
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def index(request, lesson_num):
    # courses = Course.objects.all()  # Getting all the courses from database
    try:
        each = Course.objects.get(pk=lesson_num)
        if not request.user.is_authenticated:
            return redirect('/login/')
        return render(request, 'idx_EduWeb/index.html/', {'courses': each})
    except Course.DoesNotExist:
        raise HttpResponseBadRequest("File does not exist")

def enrollCourse(request):
    if request.method == 'GET':
           course_id = request.GET['course_id']
           selectedCourse = Course.objects.get(pk=course_id) #getting the course of specified id
           m = Student(courseEnrolled=selectedCourse) # Creating Like Object
           m.save()  # saving it to store in database
           return HttpResponse("Success!") # Sending an success response
    else:
           return HttpResponse("Request method is not a GET")

def allCourses(request):
    courses = Course.objects.all()
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'idx_EduWeb/courses.html', {'courses': courses})

# Define a view function for the login page
def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'Invalid Username')
			return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('/')
	
	# Render the login page template (GET request)
	return render(request, 'idx_EduWeb/login.html')

# Define a view function for the registration page
def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		# Creates a student instance - so that they can be validated 
		student = Student(userName=username, firstName=first_name, lastName=last_name, courseEnrolled=0, cid=0, valid=0)
		student.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('/login/')
	
	# Render the registration page template (GET request)
	return render(request, 'idx_EduWeb/register.html')

def profile(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None

    profileInfo = username
    return render(request, 'idx_EduWeb/profile.html', {'profile': profileInfo})

def logoutView(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None

    if username != None:
        logout(request)
        return redirect('/login/')
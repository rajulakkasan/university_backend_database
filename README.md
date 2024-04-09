# university_management_system_backend_django

Project Specification

Teams will design and implement a web-based university management system. The system will make use of the university database that you have been working on since the beginning of this semester, but with some extension as part of this project. The system will utilize the Django web framework to connect to MySQL and to hold together all components of the system: loading data from the database, representing the data as Python objects, and dynamically creating a web page for displaying the data. The user interface will be built using Django templates.



Your system will provide functionalities/features to support three kinds of users (admins, profs, and students), as follows:

Admin can do the following: 
F1. Roster: Create a list of professors. In addition, the admin must have the option to sort the list by one of the following criteria: 
(1) by name 
(2) by dept, or 
(3) by salary. 
F2. Salary: Create a table of min/max/average salaries by dept.
F3. Performance: Given a professor's name, an academic year, and a semester, show the following for the professor: 
(1) the number of course sections taught during the semester, 
(2) the number of students taught, 
(3) the total dollar amount of funding the professor has secured, and 
(4) the total number of papers the professor has published.
Professors can do the following:
F4. Create the list of course sections and the number of students enrolled in each section that the professor taught in a chosen semester
F5. Create the list of students enrolled in a chosen course section and semester the professor taught 
Students can do the following:
F6. Query the list of course sections offered by a chosen dept in a chosen year and semester.
Deliverables, deadlines and grading criteria:



0. Team formation: Appoint a team leader; The team lead must email me names of all team members by 5pm, Friday April 5.



1. Create a project github repository with instructor (git ID: daqinghou) invited. This will allow instructor to review your source code: noon, April 9 TU



Review Git & GitHub by Watching this Crash Course on Youtube

Review of initial design and impl. for feedback: April 10 & 12, Wed/Friday, in class  1%


2. Draft user manual and design manual for feedback (noon, April 16 TU);

    second demo of design and impl. for feedback: April 17 & 19, Wed/Friday, in class 1%



3. Project showcase presentation:  April 24 &26 Wed/Friday, in class  2%

(5 minutes each team, 1 minute for Q&A)

Overview of system goal and required functionality 

Design process & challenges encountered
Status of each functionality supported with screenshots

What remain to be done and how well team has worked



4. System source code as well as user manual & design manual: 5pm May 1 Wednesday 16%

The implementation of each feature F1 to F6 except F3 is worth of 1%. F3 3%.
User manual is worth of 2%
Design manual is worth of 6% (design overview 3%, E-R diagram and database schemas 2%, and description of security assurance process 1%)
-----------------------------------------------------

Prep: 

1. start off with Lab11: Installing and using Django with mysql

2. study Django tutorials:

1. An Overview of Django Framework - video

Python Django Explained In 8 Minutes

2. Text: https://docs.djangoproject.com/en/3.0/intro/tutorial01/

3. Video: https://www.youtube.com/watch?v=zuxzE7--RYM

Models and databases:

https://docs.djangoproject.com/en/4.2/topics/db/

Setting up legacy MySQL DB (our case):

https://docs.djangoproject.com/en/4.2/howto/legacy-databases/

Making queries via models:

https://docs.djangoproject.com/en/4.2/topics/db/queries/

Performing raw SQL queries:

To perform queries that involve composite primary keys, directly execute raw SQL queries: https://docs.djangoproject.com/en/4.2/topics/db/sql/#executing-custom-sql-directly

https://docs.djangoproject.com/en/4.2/topics/db/sql/

Django Templates (pass a a dictionary object or a list of dictionaries from views to template via context):

video: Django Tutorial - Templates & Custom HTML

https://docs.djangoproject.com/en/3.0/topics/templates/

The Django template language:

https://docs.djangoproject.com/en/dev/topics/templates/#the-django-template-language

Working with forms:

https://docs.djangoproject.com/en/3.0/topics/forms/

HTML tutorials:

https://www.w3schools.com/html/default.asp

https://www.w3schools.com/html/html_tables.asp

https://dev.mysql.com/doc/index-connectors.html
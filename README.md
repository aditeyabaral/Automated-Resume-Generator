# Automated-Resume-Generator
Automated Resume Generator is an application made using SQL and Python as a part of the Database Management Systems course (UE18CS252) at PES University. The application takes in user details from a command line interface and transforms this unstructured data into a well formatted resume. 

The application was built using Python3 with Microsoft SQL as the backend server for the database to execute transactions. The application has a simple command line interface (CLI) and requires the user to type out their details one after the other. Python’s ODBC API, pyodbc was used to perform the SQL transactions and its MIME libraries were used to send emails. The Google backend script was written and deployed as a web app connected to the template which was in turn created on Google Docs. The web app is deployed as a URL containing a link to the google script and a query string containing the details of the users.

## How to run it?
All the scripts required to run the application can be found in [Source Code](https://github.com/aditeyabaral/Automated-Resume-Generator/tree/master/Source%20Code). 
* Firstly, run all the commands in ```TableCreation.sql```
* Make the following changes to the scripts - 

    * Swap the connection strings present with your database server connection in ```Main.py``` and ```Dependencies.py```
    * Modify the email address fields to your email in ```ResumeGenerator.py```
* Finally, execute the application with ```python3 Main.py```

## Folder Descriptions
* [Source Code](https://github.com/aditeyabaral/Automated-Resume-Generator/tree/master/Source%20Code): Contains the scripts required to execute the application
* [Lossless Joins](https://github.com/aditeyabaral/Automated-Resume-Generator/tree/master/Lossless%20Joins): Contains CSV files displaying lossless join of relations
* [Automated Scripts](https://github.com/aditeyabaral/Automated-Resume-Generator/tree/master/Automated%20Scripts): Contains 2 python scripts - one of them to generate random data for relations and another to generate resumes for all users in database

## More about the Application
A resume or portfolio is an extremely important tool in today’s world. It is used by employees and university graduates all over the world to market themselves and display their skills and achievements and serves as a documentation of one’s professional life. Whether you are a professional with over 20 years of experience or a freshman from University, having an up to date and polished resume is of utmost importance to help you stand out and be a cut above the competition.

As students who are constantly on the lookout for internships, it is very crucial for us to have a professionally written and laid out resume to attract attention from employers. It helps other employers identify talent and find the right people for their company – people who are skilled and can bring a change in the company. However, many students find it difficult to create a good resume, since building a resume is also an art that must be perfected in today’s world. Hence, to solve this issue and help students build professional resumes, we need an Automated Resume Generator.

As the name suggests, the application takes in all user details and creates a user profile from the unstructured data it is fed in. It then creates a well-structured resume out of these details by invoking a call to a web app – a Google script linked to a resume template to format the resume and personalise the template for the said user. It finally not only backs up a version of the resume on the cloud, but also emails the candidate a version of their resume. The application also possesses basic features such as modifying of inserted details and displaying a candidate’s details.

A detailed report on the same can be found [here](https://github.com/aditeyabaral/Automated-Resume-Generator/blob/master/DBMS%20Project%20Report%20-%20PES1201800366.pdf).

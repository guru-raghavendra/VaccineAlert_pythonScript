# VaccineAllert_pythonScript

the API used form : https://apisetu.gov.in/ <br>
pip install requests   #to send api request <br>

email,smtplib libraries to send mail. <br>

<h5>To run the script: </h5> python3 VaccineAllert.py <br>


<h2>NOTE!</h1>
if you get error like <b>smtplib.SMTPAuthenticationError: </b> 

read this:  https://support.google.com/accounts/answer/6010255 

In a nutshell, google is not allowing to log in via smtplib because it has flagged this sort of login as "less secure", so go to this link while you're logged in to your google account, and allow the access:

https://www.google.com/settings/security/lesssecureapps

I am attaching the screenshot below<br>
![image](https://user-images.githubusercontent.com/51516878/119986099-1113f700-bfe1-11eb-8043-c09775acf158.png)





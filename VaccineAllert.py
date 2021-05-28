import requests
from datetime import datetime, timedelta
import time

import email
import smtplib



num_days = 2
age=int(input("Enter your age: "))
pincodes=[]
p=int(input("How many pincode you want to check? "))
for i in range(0,p):
    pincodes.append(input("enter pincode: "))
    


print_flag = 'Y'
mail_flag=input("Do you want to receive mail about the details (Y/N) ")

if(mail_flag=="y" or mail_flag=="Y" ):
    to=input("enter your mail id: ")

#print(mail_flag[0])



print("Starting search for Covid vaccine slots for next two days!")

actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

content=""

while True:
    counter = 0   

    for pincode in pincodes:   
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, given_date)
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
            
            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()
                if response_json["centers"]:
                    if(print_flag.lower() =='y'):
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                    print('Pincode: ' + pincode)
                                    print("Available on: {}".format(given_date))
                                    print("\t", center["name"])
                                    print("\t", center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Availablity : ", session["available_capacity"])

                                    content=content+'Pincode: '+pincode +"\n"
                                    content=content+"Available on: {}".format(given_date) +"\n"
                                    content=content+"\t" + center["name"] +"\n"
                                    content=content+"\t"+ center["block_name"] +"\n"
                                    content=content+"\t Price: " + center["fee_type"] +"\n"
                                    content=content+"\t Availablity : " + str(session["available_capacity"]) +"\n"
                                   



                                    if(session["vaccine"] != ''):
                                        print("\t Vaccine type: ", session["vaccine"])
                                        content=content+"\t Vaccine type: " + session["vaccine"] +"\n"
                                    content=content+"\n\n"
                                    print("\n")
                                    counter = counter + 1
            else:
                print("No Response!")
                
    if counter==0:
        print("No Vaccination slot available!")
        content=content+"No Vaccination slot available!" +"\n"
    else:
        content="The slots for next two days are:\n\n" + content
        print("Search Completed!")
    break

if(mail_flag=="y" or mail_flag=="Y" ):
    
    email_msg = email.message.EmailMessage()
    email_msg["Subject"] = "Vaccination Slot Details"
    email_msg["From"] = "hguru1005@gmail.com"
    email_msg["To"] = to
    email_msg.set_content(content)

    with smtplib.SMTP(host='smtp.gmail.com', port='587') as server:
        server.starttls()
        server.login("hguru1005@gmail.com", "Guru@1729")
        server.send_message(email_msg, "hguru1005@gmail.com", to)



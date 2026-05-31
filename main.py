from datetime import datetime
import pandas
import smtplib
import random

##################### Extra Hard Starting Project ######################

MY_EMAIL = "zynx.official.mail@gmail.com"
my_password = "terl odoj kofs xzlm"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv(r"C:\Users\wazie\OneDrive\Desktop\UDEMY\birthday-wisher-extrahard-start\birthday.csv")
birthdays_dict = {(data_row['month'], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"C:\\Users\\wazie\\OneDrive\\Desktop\\UDEMY\\birthday-wisher-extrahard-start\\letter_templates\\letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, my_password)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject: Happy Birthday!\n\n{contents}"
            )

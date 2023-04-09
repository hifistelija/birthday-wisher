import pandas as pd
import datetime as dt
import random
import smtplib

today = dt.datetime.now()
today_month = today.month
today_day = today.day
today_tuple = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    name = str(birthday_person["name"])
    email = str(birthday_person["email"])
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as file:
        letter_contents = file.read()
        letter_contents = letter_contents.replace("[NAME]", name)
        file.close()

    my_email = "enteremail@yahoo.com"
    my_password = "yourpassword"
    smtp_server = "smtp.mail.yahoo.com"
    port = 587

    with smtplib.SMTP(smtp_server, port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{letter_contents}")
        connection.close()

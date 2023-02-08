import smtplib

# now =dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(month)
# date_of_birth = dt.datetime(year=1996, month=9, day=6)

import datetime as dt
import time
import random

my_email = "busjackson37@gmail.com"
password = "yqhpkksgkiwllbob"



now = dt.datetime.now()
year = now.year
weekday = now.weekday()
quotes_list = []
with open(file="quotes.txt",mode="r") as file:
    for lines in file:
        quotes_list.append(lines)

if weekday == 0 and year < 2030:
    random_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dmorin9696@yahoo.com",
                            msg=f"Subject:Motivational Monday! \n\n{random_quote}")
    time.sleep(60*60*24)





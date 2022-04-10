import datetime
import pandas
import random
import smtplib

user = "sachnboora@gmail.com"
password = "abcd@1234"

today = (datetime.datetime.now().month, datetime.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        replaced_text = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user, password)
        connection.sendmail(
            from_addr=user,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{replaced_text}"
        )

import smtplib
import datetime as dt
import random

MY_EMAIL = "swarupspacetech@gmail.com"
MY_PASSWORD ="ewpatfmieiueskpk"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).strip()

    print(quote)
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="aasiandme@gmail.com",
                        msg=f"Subject: Monday Motivation\n\n{quote}".encode('utf-8')
    )
    connection.close()



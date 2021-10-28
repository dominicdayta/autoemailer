import smtplib, ssl, os
import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

port = os.getenv("SMTP_PORT")
smtp_server = os.getenv("SMTP_SERVER")
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SMTP_PASSWORD")

content_df = pd.read_excel(r'data/current_grading_sheet.xlsx', sheet_name='Grades')
base_message = """\
Subject: {subject} {requirement}

Good morning,

I have completed evaluating your input to the requirement {requirement}. You scored {score} points,  which is equivalent to a percentage grade of {percent}. Please see my full feedback and score breakdown below:

{feedback}

This is a system generated e-mail. Please do not reply. Any and all feedback/inquiry should be coursed through my official UP email at dbdayta@up.edu.ph.

This message, included thread, and any attachments therein are privileged and confidential. No part of this message may be reproduced or exhibited in any form or manner without the consents of the sender and the University of the Philippines Diliman. In case of wrongful receipt of or unauthorized access to this message, please immediately inform the sender and permanently delete all wrongfully received copies. Your access to this message subjects you to the UP Diliman Message and Communication Policy and relevant data privacy regulations. 
"""

context = ssl.create_default_context()
i = 1
total = len(content_df.index)

for index, row in content_df.iterrows():

    print("Sending email {num}/{total}".format(num = i, total = total))
    
    new_message = base_message.format(
        subject=row['Class'],
        requirement=row['Requirement'],
        score = row['Grade'],
        percent = round(100 * row['Percent'],1),
        feedback = row['Remarks']
    )
    
    receiver_email = row['Email']

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, new_message)

    i = i + 1

print("All emails sent!")
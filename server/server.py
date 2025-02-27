import imaplib
import email
import time
import dotenv

# BASE_URL
mail = imaplib.IMAP4_SSL('mail.lernsax.de')
# EMAIL_ADRESS
# EMAIL_PASSWORD
mail.login('<name>@<school>.lernsax.de', '<password>')
# mail.select('inbox')

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'mikolajpindera2@gmail.com'
email_password = 'wwalnnbrcohqkgvk'
email_receiver = 'mikolajpindera2@gmail.com'

subject = 'Check out'

username = 'John Doe'
bialko = '100g'
tluszcz = '50g'

button_url = 'https://example.com'
button_text = 'Click Here'

body = f"""
<html>
<body>
<p><strong>Hello, It's email from: {username}</strong></p>
<p>Here are your nutritional requirements:</p>
<p><a href="{button_url}" style="background-color: #007bff; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 4px;">{button_text}</a></p>

<ul>
  <li>Protein: {bialko}</li>
  <li>Fat: {tluszcz}</li>
</ul>
</body>
</html>
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.add_alternative(body, subtype='html')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

# <p><strong>Hello, It's email from: {username}</strong></p>
# <ul>
# <li>Protein: {bialko}</li>
# <li>Fat: {tluszcz}</li>
# </ul>

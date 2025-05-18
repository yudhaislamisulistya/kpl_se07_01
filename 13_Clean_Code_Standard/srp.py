# ❌ => Bad, SRP (Single Responsibility Principle)
# This function violates the Single Responsibility Principle (SRP) by handling both user creation and email sending.
def save_user_and_send_email(user):
    database.save(user)
    email.send_welcome(user.email)
    
# ✅ => Good, SRP (Single Responsibility Principle) -> Mematuhi Prinsip Tanggung Jawab Tunggal
# This function adheres to the Single Responsibility Principle (SRP) by focusing only on user creation.
def save_user(user):
    database.save(user)

def send_welcome_email(email_address):
    email.send_welcome(email_address)
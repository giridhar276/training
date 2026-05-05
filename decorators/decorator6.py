
#Validate email before registration

def validate_email(func):
    def wrapper(email):
        if "@" in email and "." in email:
            return func(email)
        else:
            print("Invalid email address")
    return wrapper

@validate_email
def register_user(email):
    print(f"User registered with email: {email}")

register_user("test@gmail.com")
register_user("wrongemail")
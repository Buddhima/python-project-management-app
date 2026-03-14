from app.auth import pwd_context

# In a real app, this would be in a database service
users_db = {
    "admin": {"pw": pwd_context.hash("secret"), "role": "manager"},
    "staff": {"pw": pwd_context.hash("secret"), "role": "staff"}
}

def get_login_user(user_name: str):
    return users_db.get(user_name)

def is_admin(user):
    return user.profile.role == 'ADMIN'

def is_customer(user):
    return user.profile.role == 'CUSTOMER'

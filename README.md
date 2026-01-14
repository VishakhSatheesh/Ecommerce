## Basic Usage Guide
```
1.Register new customer: /register/
2.Login to get JWT: /login/
3.Use JWT token for all requests (Authorization → Bearer <token>)
4.Admin can create products, view all orders, update order status
5.Customer can view products, create orders, view own orders
```


## Setup Instructions

1. Clone project
```bash
git clone <repo-url>
cd ecommerce
```
2.Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate 
```
3.Install requirements
```bash
pip install django djangorestframework djangorestframework-simplejwt

```
4. Migrate database
```bash
   python manage.py makemigrations
   python manage.py migrate
```
5.Run server
```bash
python manage.py runserver
```





## DjangoFormAndRoles

#### _This project is already live, I've hosted it on Google Cloud Compute engine with my domain and I've sent the address to same HR I've got assignment from. There was one instruction on email please do check it out_

### _How to Run_

- Clone project and move to project root directory. 
- Activate python environment .
- Update your pip to latest version otherwise installing requirements will give you error.
- Upgrade pip by running ```pip install --upgrade pip``` . 
- Then run ```pip install -r requirments.txt``` .
- From project root run ```python manage.py makemigrations``` then ```python manage.py makemigrations chat``` and ```python manage.py migrate```.
- Then Finally run ```python manage.py runserver```.

## Features
- Visit ```http://localhost:8000/Project/```.
- Create new user. There Check the manager box if you want to increase the level of user (Create,Edit,Delete and list deleted records) or create simple user as viewer and Creater.
- If you are an Manager you are going to see three card Create, View and Deleted otherwise you are going to only two card View and Create
- If you press view and you are an manager you are going to get two extra button (Edit and Delete) otherwise you are going to only see list of name.
- There's so much please check everything on role security , Bootstrap and jQuery ajax.
- Anyone can create manager account because I didn't add enough security due to lack of time.
- Thank You

### If you get any issues please email me balwantdod223@gmail.com .


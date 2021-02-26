# welcome to django react based dashboard and authentication system

in this app u can see an authentication system which uses django for api and react as front end and tailwind for styling
authentication follows cookies and id and its protected by csrf token so its safe

# here is what u should do to run django api 

### `pip install -r requirements.txt`

It installs all dependencies on your system

### `python manage.py makemigrations`

It gathers all table datas from ORM and prepare them to be applied on your database

### `python manage.py migrate`

It correctly applies all changes and makes tables from your models.

### `python manage.py createsuperuser`
It creates a user with full-access to admin panel and api

### `python manage.py runserver`

It runs the api in the development mode.\
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.


**Note: this project uses sqlite db but dont worry u can change it to anything u want like postgress in less than a minute!**

# here is what u should do to run react frontend 

### `npm install`

It installs all dependencies on your system

### `npm start`

It runs the api in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm run build`

It exports front end for deployment.\

* [here is postman json](https://github.com/m-moein98/dashboard/blob/main/backend/postman.json) All api urls are documented and ready for test in postman and u only need to import this in the app!

**Note: this project uses tailwind css but dont worry u can change it to anything u want like pure css in few minutes!**

If you are satisfied with the project and idea behind it, I will be so happy to apply changes u want to this project so send your pull requests or dm me on my gmail or in my website leave a message at hire me tab https://moein98.ir

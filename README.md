პროექტში გამოყენებული ტექნოლოგიები
Python 3.11
Django
HTML
SQLite
ძირითადი ფუნქციონალი
მონაცემების დამატება HTML ფორმების საშუალებით
forms.Form-ის გამოყენება
forms.ModelForm-ის გამოყენება
ველების დამატებითი ვალიდაცია clean_<field_name>() მეთოდით
GET და POST მოთხოვნების დამუშავება
is_valid() მეთოდის გამოყენება
მონაცემების შენახვა მონაცემთა ბაზაში
CSRF დაცვის გამოყენება ({% csrf_token %})
პროექტის სტრუქტურა
project/
│
├── app/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── manage.py
└── db.sqlite3
პროექტის გაშვება
1. პროექტის კლონირება
git clone <repository-url>
2. პროექტის საქაღალდეში გადასვლა
cd project-folder
3. ვირტუალური გარემოს შექმნა და გააქტიურება

Windows

python -m venv .venv
.venv\Scripts\activate

Linux / macOS

python3 -m venv .venv
source .venv/bin/activate
4. საჭირო ბიბლიოთეკების ინსტალაცია
pip install -r requirements.txt
5. მიგრაციების გაშვება
python manage.py migrate
6. სერვერის გაშვება
python manage.py runserver

შემდეგ ბრაუზერში გახსენით:

http://127.0.0.1:8000/
შესრულებული მოთხოვნები
✅ მოდელის შექმნა (models.py)
✅ forms.Form-ის გამოყენება
✅ forms.ModelForm-ის გამოყენება
✅ clean_<field_name>() მეთოდის გამოყენება
✅ GET და POST მოთხოვნების დამუშავება
✅ is_valid() მეთოდის გამოყენება
✅ მონაცემების მონაცემთა ბაზაში შენახვა
✅ HTML Templates-ის გამოყენება
✅ csrf_token-ის გამოყენება ფორმების დასაცავად

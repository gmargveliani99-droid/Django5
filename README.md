# Django Forms პროექტი

## პროექტის აღწერა

ეს პროექტი შექმნილია Django Framework-ის გამოყენებით და წარმოადგენს HTML ფორმებთან მუშაობის მაგალითს.

მომხმარებელს შეუძლია ფორმების საშუალებით მონაცემების დამატება. მონაცემები გადის ვალიდაციას და წარმატების შემთხვევაში ინახება მონაცემთა ბაზაში.

პროექტში გამოყენებულია როგორც `forms.Form`, ასევე `forms.ModelForm`. დამატებით გამოყენებულია `clean_<field_name>()` მეთოდი ველების ვალიდაციისთვის.

## ფუნქციონალი

- Django forms (`forms.Form`)
- Django ModelForm (`forms.ModelForm`)
- ველების ვალიდაცია `clean_<field_name>()` მეთოდით
- GET და POST მოთხოვნების დამუშავება
- `is_valid()` მეთოდის გამოყენება
- მონაცემების შენახვა მონაცემთა ბაზაში
- HTML ფორმები
- CSRF დაცვა

## გამოყენებული ტექნოლოგიები

- Python 3.11
- Django
- HTML
- SQLite

## პროექტის სტრუქტურა


Django5/
│
├── app/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│
├── manage.py
└── db.sqlite3


## ინსტალაცია და გაშვება

### 1. რეპოზიტორიის კლონირება

```bash
git clone https://github.com/gmargveliani99-droid/Django5.git
2. პროექტის საქაღალდეში გადასვლა
cd Django5
3. ვირტუალური გარემოს შექმნა
python -m venv .venv
4. ვირტუალური გარემოს გააქტიურება

Windows:

.venv\Scripts\activate

Linux / macOS:

source .venv/bin/activate
5. ბიბლიოთეკების დაყენება
pip install -r requirements.txt
6. მიგრაციების გაშვება
python manage.py migrate
7. სერვერის გაშვება
python manage.py runserver

შემდეგ გახსენით ბრაუზერში:

http://127.0.0.1:8000/

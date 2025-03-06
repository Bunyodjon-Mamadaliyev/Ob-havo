# Ob-havo 🌦️

### Bu loyiha ob-havo ma'lumotlarini saqlash va boshqarish uchun ishlab chiqilgan Django veb-ilovasi.

## 📋 Mundarija

- [Texnologiyalar](#texnologiyalar)
- [O'rnatish](#ornatish)
- [Foydalanish](#foydalanish)
- [Tahlillar](#Tahlillar)
- [Loyiha tuzilishi](#loyiha-tuzilishi)
- [Loyiha asoschisi](#Loyiha_asoschisi)



## 🛠️ Texnologiyalar

- **Django** - Veb-ilovalar uchun Python freymvorki
- **Python 3.13** - Eng so'nggi Python versiyasi
- **SQLite** - Standart ma'lumotlar bazasi (ishlab chiqish uchun)


## 🚀 O'rnatish

Loyihani ishga tushirish uchun quyidagi bosqichlarni bajaring:

### 1. Loyihani klonlash

```shellscript
git clone https://github.com/Bunyodjon-Mamadaliyev/Ob-havo.git
cd Ob-havo
```

### 2. Virtual muhitni yaratish

```shellscript
python -m venv .venv
```

### 3. Virtual muhitni faollashtirish
Windows:
```shellscript
.venv\Scripts\activate
```
Linux/Mac:
```shellscript
source .venv/bin/activate
```

### 4. Talab qilingan kutubxonalarni o'rnatish

```shellscript
pip install -r requirements.txt
```

### 5. Ma'lumotlar bazasini yaratish

```shellscript
python manage.py makemigrations
python manage.py migrate
```

### 6. Admin panelga kirish uchun superuser yaratish

```shellscript
python manage.py createsuperuser
```

### 7. Serverni ishga tushirish

```shellscript
python manage.py runserver
```

Brauzeringizda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) manziliga o'ting.

## 🖥️ Foydalanish

- Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Bosh sahifa: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Forecast sahifa: [http://127.0.0.1:8000/api/forecasts/](http://127.0.0.1:8000/api/forecasts/)
- Location sahifa: [http://127.0.0.1:8000/api/locations/](http://127.0.0.1:8000/api/locations/)
- WeatherData sahifa: [http://127.0.0.1:8000/api/weather-data/](http://127.0.0.1:8000/api/weather-data/)

## 🖥️ Analytics (Tahlillar)

- O'rtacha harorat sahifa: [http://127.0.0.1:8000/api/analytics/temperature-avg/](http://127.0.0.1:8000/api/analytics/temperature-avg/)
- Umumiy yog'ingarchilik miqdori sahifa: [http://127.0.0.1:8000/api/analytics/precipitation-sum/](http://127.0.0.1:8000/api/analytics/precipitation-sum/)
- Maksimal shamol tezligi sahifa: [http://127.0.0.1:8000/api/analytics/wind_speed-max/](http://127.0.0.1:8000/api/analytics/wind_speed-max/)

### Ob-havo Loyiha Tuzilmasi 📁

```plaintextOb-havo/                      # Loyiha asosiy papkasi
│
├── .venv/                    # Virtual muhit (Python paketlari saqlanadi)
│
├── config/                   # Konfiguratsiya fayllari
│   ├── __init__.py
│   ├── settings.py           
│   ├── urls.py               
│   └── wsgi.py               
│
├── Forecast/                 # Ob-havo bashorati ilovasi
│   ├── __init__.py
│   ├── apps.py               
│   ├── admin.py              
│   ├── models.py             
│   ├── tests.py              
│   ├── urls.py              
│   ├── views.py              
│
├── Location/                 # Joylashuv ilovasi
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── WeatherData/              # Ob-havo ma'lumotlari ilovasi
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── .gitignore                
├── db.sqlite3                
├── manage.py                 
├── README.md                
└── requirements.txt          
```

## 🖥️ Loyiha asoschisi
## Bunyodjon Mamadaliyev
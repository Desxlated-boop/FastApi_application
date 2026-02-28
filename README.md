# Как запустить

## 1. Скачайте репо
git clone https://github.com/Desxlated-boop/FastApi_application

## 2. Создайте виртуальное окружение
python -m venv venv

## 3. Активируйте виртуальное окружение
### Для PowerShell:
.\venv\Scripts\Activate.ps1
### ИЛИ для CMD:
venv\Scripts\activate

## 4. Установите зависимости
pip install fastapi[all] uvicorn[standard] pydantic

## 5. Запустите сервер
uvicorn app:app --reload

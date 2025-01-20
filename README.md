# How to run this script?
> You should have python installed.

> Create .env file with correct MONGODB_URL
## Create virtual env
```
python -m venv env
```
## Activate virtual env
```
.\env\Scripts\Activate.ps1
```
## Install dependencies
```
pip install -r requirements.txt
```
## Run scripts
- View all codes generated
```
python app.py
```
- Create new code for investor
```
python app.py --create --name "Investor Name" --info "Additional info here"
```
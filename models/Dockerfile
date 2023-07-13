FROM python:3.8
WORKDIR C:\Docs\Python\automating-security\models
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5500
CMD [ "python", "app.py" ]
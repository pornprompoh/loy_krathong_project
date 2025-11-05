import os

# หาตำแหน่งที่แท้จริงของไฟล์ config นี้
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SECRET_KEY จำเป็นมากสำหรับ Flask session
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_very_secret_key_12345'
    
    # ตั้งค่าฐานข้อมูล SQLite ให้เก็บไว้ในโฟลเดอร์ instance/
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
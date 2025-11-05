from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # สร้างโฟลเดอร์ instance ถ้ายังไม่มี
    instance_path = os.path.join(app.root_path, '..', 'instance')
    os.makedirs(instance_path, exist_ok=True)
    
    db.init_app(app)

    # Import routes หลังจากสร้าง app แล้ว
    from app import routes, models

    # สร้างตารางฐานข้อมูล (ถ้ายังไม่มี)
    with app.app_context():
        db.create_all()

    return app
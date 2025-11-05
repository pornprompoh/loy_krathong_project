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

    # --- ส่วนที่แก้ไข ---
    # Import models เพื่อให้ db.create_all() รู้จัก
    from app import models 
    
    # Import Blueprint จาก routes.py
    from app.routes import main_bp
    # จดทะเบียน Blueprint กับ app
    app.register_blueprint(main_bp)
    # --- สิ้นสุดส่วนที่แก้ไข ---

    # สร้างตารางฐานข้อมูล (ถ้ายังไม่มี)
    with app.app_context():
        db.create_all()

    return app
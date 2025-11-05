from app import db
from datetime import datetime

class KrathongEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ชื่อที่กรอกจากหน้าแรก
    name = db.Column(db.String(100), nullable=False)
    # เก็บว่าเลือกกระทงแบบไหน (เช่น "premade1", "premade2", หรือ "diy")
    krathong_design = db.Column(db.String(50), default='premade1')
    # คำอธิษฐานจากหน้าลอย
    wish = db.Column(db.Text, nullable=True)
    # เวลาที่สร้าง
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<KrathongEntry {self.id} - {self.name}>'
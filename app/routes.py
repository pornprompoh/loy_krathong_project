from flask import render_template, request, redirect, url_for, session, flash
from app import db
from app.models import KrathongEntry
from flask import current_app as app # ใช้ app context

# ===== หน้า 1: หน้าต้อนรับ + ใส่ชื่อ =====
@app.route('/', methods=['GET', 'POST'])
def index():
    # ถ้ากดปุ่ม "เริ่มประกอบกระทง" (POST)
    if request.method == 'POST':
        name = request.form.get('name')
        
        if not name:
            # ไม่กรอกชื่อ
            flash('กรุณาใส่ชื่อก่อนนะครับ 💖')
            return redirect(url_for('index'))

        # สร้าง Entry ใหม่ในฐานข้อมูล
        new_entry = KrathongEntry(name=name)
        db.session.add(new_entry)
        db.session.commit()
        
        # เก็บ ID ของกระทงนี้ไว้ใน session เพื่อใช้ในหน้าต่อไป
        session['entry_id'] = new_entry.id
        
        # ไปหน้าเลือกกระทง
        return redirect(url_for('build'))

    # ถ้าเข้าหน้าเว็บเฉยๆ (GET)
    return render_template('index.html')

# ===== หน้า 2: เลือกกระทง (หรือประกอบเอง) =====
@app.route('/build', methods=['GET', 'POST'])
def build():
    # ตรวจสอบว่ามี session จากหน้าแรกหรือไม่
    if 'entry_id' not in session:
        return redirect(url_for('index'))
    
    entry_id = session['entry_id']
    entry = db.session.get(KrathongEntry, entry_id)

    if not entry:
        # ถ้าหา entry ไม่เจอ (อาจจะนานไป) ให้กลับไปหน้าแรก
        session.pop('entry_id', None)
        return redirect(url_for('index'))

    # ถ้ากดปุ่ม "เสร็จแล้ว ไปปล่อยกระทงกัน" (POST)
    if request.method == 'POST':
        # รับค่า 'krathong_design' จาก hidden input ใน form
        design = request.form.get('krathong_design')
        
        # อัปเดตฐานข้อมูล
        entry.krathong_design = design
        db.session.commit()
        
        return redirect(url_for('launch'))

    # ถ้าเข้าหน้าเว็บ (GET)
    # ส่ง 'current_design' ไปให้ template รู้ว่าเคยเลือกอะไรไว้
    return render_template('build.html', current_design=entry.krathong_design)

# ===== หน้า 3: ปล่อยกระทง + เขียนคำอธิษฐาน =====
@app.route('/launch', methods=['GET', 'POST'])
def launch():
    if 'entry_id' not in session:
        return redirect(url_for('index'))
    
    entry_id = session['entry_id']
    entry = db.session.get(KrathongEntry, entry_id)

    if not entry:
        session.pop('entry_id', None)
        return redirect(url_for('index'))

    # ถ้ากดปุ่ม "ลอยกระทง" (POST)
    if request.method == 'POST':
        wish_text = request.form.get('wish')
        
        # อัปเดตคำอธิษฐานลงฐานข้อมูล
        entry.wish = wish_text
        db.session.commit()
        
        # ไปหน้าสุดท้าย
        return redirect(url_for('final'))

    # ถ้าเข้าหน้าเว็บ (GET)
    # ส่ง design ไปให้ template แสดงผลกระทงที่ถูกต้อง
    return render_template('launch.html', design=entry.krathong_design)

# ===== หน้า 4: ข้อความถึงแฟน =====
@app.route('/final')
def final():
    if 'entry_id' not in session:
        return redirect(url_for('index'))
    
    entry_id = session['entry_id']
    entry = db.session.get(KrathongEntry, entry_id)

    if not entry:
        session.pop('entry_id', None)
        return redirect(url_for('index'))
    
    # ส่งชื่อ (name) และ คำอธิษฐาน (wish) ไปแสดงผล
    return render_template('final.html', name=entry.name, wish=entry.wish)
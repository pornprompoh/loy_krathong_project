from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app import db  # Import db จาก __init__.py
from app.models import KrathongEntry

# 1. สร้าง Blueprint ชื่อ 'main'
main_bp = Blueprint('main', __name__)

# 2. เปลี่ยน @app.route ทั้งหมดเป็น @main_bp.route
@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        
        if not name:
            flash('กรุณาใส่ชื่อก่อนนะครับ 💖')
            # 3. แก้ url_for ให้มี prefix ของ blueprint (เช่น 'main.index')
            return redirect(url_for('main.index')) 

        new_entry = KrathongEntry(name=name)
        db.session.add(new_entry)
        db.session.commit()
        
        session['entry_id'] = new_entry.id
        
        # 3. แก้ url_for
        return redirect(url_for('main.build'))

    return render_template('index.html')

@main_bp.route('/build', methods=['GET', 'POST'])
def build():
    if 'entry_id' not in session:
        return redirect(url_for('main.index'))
    
    entry_id = session['entry_id']
    entry = db.session.get(KrathongEntry, entry_id)

    if not entry:
        session.pop('entry_id', None)
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        design = request.form.get('krathong_design')
        entry.krathong_design = design
        db.session.commit()
        
        # 3. แก้ url_for
        return redirect(url_for('main.launch'))

    return render_template('build.html', current_design=entry.krathong_design)

@main_bp.route('/launch', methods=['GET', 'POST'])
def launch():
    if 'entry_id' not in session:
        return redirect(url_for('main.index'))
    
    entry_id = session['entry_id']
    entry = db.session.get(KrathongEntry, entry_id)

    if not entry:
        session.pop('entry_id', None)
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        wish_text = request.form.get('wish')
        entry.wish = wish_text
        db.session.commit()
        
        # 3. แก้ url_for
        return redirect(url_for('main.final'))

    return render_template('launch.html', design=entry.krathong_design)

@main_bp.route('/final')
def final():
    if 'entry_id' not in session:
        return redirect(url_for('main.index'))
    
    entry_id = session['entry_id']
    entry = db.session.get(KrathongEntry, entry_id)

    if not entry:
        session.pop('entry_id', None)
        return redirect(url_for('main.index'))
    
    return render_template('final.html', name=entry.name, wish=entry.wish)
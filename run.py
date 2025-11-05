from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # debug=True เพื่อให้เห็นข้อผิดพลาดง่ายๆ ตอนพัฒนา
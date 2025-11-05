// รอให้หน้าเว็บโหลดเสร็จก่อน
document.addEventListener('DOMContentLoaded', function() {

    // --- Logic สำหรับหน้า 2 (Build) ---
    const buildForm = document.getElementById('build-form');
    if (buildForm) {
        const designInput = document.getElementById('krathong_design_input');
        const choices = document.querySelectorAll('.krathong-choice');

        choices.forEach(choice => {
            choice.addEventListener('click', function() {
                // ลบ .selected ออกจากทุกอัน
                choices.forEach(c => c.classList.remove('selected'));
                
                // เพิ่ม .selected ให้อันที่คลิก
                this.classList.add('selected');
                
                // อัปเดตค่าใน hidden input
                designInput.value = this.dataset.design;
            });
        });
    }


    // --- Logic สำหรับหน้า 3 (Launch) ---
    const launchForm = document.getElementById('launch-form');
    if (launchForm) {
        const btnLaunch = document.getElementById('btn-launch');
        const krathong = document.getElementById('krathong-to-launch');
        const fireworks = document.getElementById('fireworks'); // หาพลุ

        btnLaunch.addEventListener('click', function(event) {
            // 1. หยุดการ submit form ตามปกติ
            event.preventDefault();

            // 2. ซ่อนปุ่มและช่องกรอก (กันกดย้ำ)
            document.querySelector('.wish-box').style.display = 'none';

            // 3. เริ่ม Animation ลอยกระทง (เปลี่ยนจาก .floating เป็น .animating)
            if (krathong) {
                krathong.classList.add('animating');
            }

            // 4. แสดงพลุ (ถ้าหาเจอ)
            if (fireworks) {
                fireworks.style.display = 'block';
            }

            // 5. หน่วงเวลา 7 วินาที (ให้ตรงกับ animation-duration ใน CSS)
            setTimeout(function() {
                // 6. พอ animation จบ ค่อย submit form จริงๆ เพื่อไปหน้า 4
                launchForm.submit();
            }, 10000); // 10000ms = 10 วินาที
        });
    }

});
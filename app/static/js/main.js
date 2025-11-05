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
        const fireworks = document.getElementById('fireworks');

        btnLaunch.addEventListener('click', function(event) {
            // 1. หยุดการ submit form ตามปกติ
            event.preventDefault();

            // 2. ซ่อนปุ่มและช่องกรอก (กันกดย้ำ)
            document.querySelector('.wish-box').style.display = 'none';

            // 3. เริ่ม Animation ลอยกระทง (โดยการเพิ่ม class 'floating')
            if (krathong) {
                krathong.classList.add('floating');
            }

            // 4. แสดงพลุ
            if (fireworks) {
                fireworks.style.display = 'block';
            }

            // 5. หน่วงเวลา 4 วินาที (ให้กระทงลอย + พลุแตก)
            setTimeout(function() {
                // 6. พอ animation จบ ค่อย submit form จริงๆ เพื่อไปหน้า 4
                launchForm.submit();
            }, 4000); // 4000ms = 4 วินาที
        });
    }

});
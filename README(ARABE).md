
---

# Removing-Undesirable-Objects-MRCNN

يهدف هذا المشروع إلى إزالة الأشياء غير المرغوب فيها من الصورة. يتيح للمستخدمين اختيار كائن في الصورة وإزالته تلقائيًا باستخدام تقنيات متقدمة مثل التقسيم المتجسد (**Mask R-CNN**) والتعبئة باستخدام تقنية **Inpainting**.

---

## الوصف

يستخدم المشروع **Mask R-CNN** لاكتشاف وتقسيم الكائنات في الصورة. بمجرد تحديد الكائن، يتم إزالته تلقائيًا ويتم ملء المنطقة الفارغة باستخدام تقنية **Inpainting**.

### التقنيات المستخدمة:

- **التقسيم المتجسد (Mask R-CNN)**
- **Inpainting** لملء المناطق التي تم إزالتها.

---

## المتطلبات

1. **Python 3.7**: تأكد من تثبيت هذه النسخة.
2. **Git**: لتحميل الملفات المطلوبة.
3. **مستودع Mask R-CNN**: يعتمد المشروع على مكتبة Mask R-CNN المتاحة على GitHub.

---

## تعليمات التثبيت والتنفيذ

### 1. استنساخ وإعداد مستودع Mask R-CNN

- قم بتحميل مستودع **Mask R-CNN** من الرابط التالي:
  [https://github.com/matterport/Mask\_RCNN.git](https://github.com/matterport/Mask_RCNN.git)

- قم بفك ضغط محتويات المستودع وضعها **في نفس المكان** الذي يوجد فيه ملف `rcnn.py` الخاص بمشروعك.

### 2. تحميل النموذج المدرب مسبقًا COCO

- قم بتحميل ملف **mask\_rcnn\_coco.h5** من الرابط التالي:
  [https://github.com/matterport/Mask\_RCNN/releases](https://github.com/matterport/Mask_RCNN/releases)

- ضع ملف **mask\_rcnn\_coco.h5** في مجلد المشروع.

### 3. تثبيت Python 3.7 وإعداد البيئة الافتراضية

1. **تثبيت Python 3.7**: قم بتحميل وتثبيت Python 3.7 من الموقع الرسمي.

   - تأكد من إضافة Python إلى PATH أثناء التثبيت.

2. **إنشاء بيئة افتراضية**:

   - افتح PowerShell أو CMD.
   - نفذ الأوامر التالية:
     ```bash
     python -m venv myenv
     ```

3. **إعداد أذونات التنفيذ على Windows**:

   - في PowerShell، اكتب:
     ```bash
     Get-ExecutionPolicy
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```
   - اختر **"نعم للجميع"** إذا تم سؤالك.

4. **تفعيل البيئة الافتراضية**:

   - نفذ الأمر التالي:
     ```bash
     .\myenv\Scripts\Activate
     ```
   - بمجرد تفعيلها، يجب أن يظهر في الطرفية شيء مشابه لـ:
     ```bash
     (myenv)
     ```

### 4. تثبيت المتطلبات

- بمجرد تفعيل البيئة، قم بتثبيت المتطلبات الضرورية إما من خلال ملف `requirements.txt` أو يدويًا:
  ```bash
  pip install tensorflow keras opencv-python numpy matplotlib
  ```

### 5. تشغيل المشروع

- قم بتشغيل السكربت الرئيسي `rcnn.py` وتأكد من أنك في البيئة الافتراضية.
- ![WhatsApp Image 2024-12-17 at 14 29 10_e63babfa](https://github.com/user-attachments/assets/47639c2a-1da7-410a-8e4a-9c2eb04758e2)

  ```bash
  python rcnn.py
  ```

---

## ملاحظات هامة

- تأكد من أن مستودع **Mask R-CNN** وملف **mask\_rcnn\_coco.h5** تم وضعهم بشكل صحيح.
- يعتمد ملف `rcnn.py` بشكل كبير على ملفات Mask R-CNN لكي يعمل بشكل صحيح.
- يجب تشغيل المشروع في بيئة Python 3.7.

---

## الروابط المفيدة

- **مستودع Mask R-CNN**: [https://github.com/matterport/Mask\_RCNN](https://github.com/matterport/Mask_RCNN)
- **النموذج المدرب مسبقًا COCO**: [https://github.com/matterport/Mask\_RCNN/releases](https://github.com/matterport/Mask_RCNN/releases)

---

## الاتصال

لأي استفسارات أو مساعدة، لا تتردد في الاتصال بي عبر GitHub أو عبر البريد الإلكتروني.
zakariae.khayi@uit.ac.ma

---

شكرًا لاستخدامك **Removing-Undesirable-Objects-MRCNN**!

---

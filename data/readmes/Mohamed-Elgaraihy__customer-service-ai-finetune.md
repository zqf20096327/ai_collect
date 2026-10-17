# تدريب نموذج ذكاء اصطناعي لخدمة العملاء | Customer Service AI Fine-Tuning

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mohamed-Elgaraihy/customer-service-ai-finetune/blob/main/train.ipynb)

هذا المستودع يحتوي على أكواد وبيانات لتدريب (Fine-Tuning) نموذج الذكاء الاصطناعي **Qwen 2.5** ليكون مساعداً ذكياً لخدمة العملاء، باستخدام **Unsloth** ولغة **Python**.

## 🎥 الشرح المرئي (YouTube)
يمكنك مشاهدة الشرح الكامل لكيفية تدريب الموديل عبر Google Colab و Unsloth من خلال الرابط التالي:
[اضغط هنا لمشاهدة الفيديو على يوتيوب](https://www.youtube.com/watch?v=cnkNQlqxg18)

## 📁 ملفات المشروع
* `dataset.json`: يحتوي على بيانات التدريب (أسئلة وإجابات).
* `train.ipynb`: نسخة نوتبوك (Colab Notebook) جاهزة للتشغيل المباشر.
* `train.py`: ملف الأكواد الرئيسي لتدريب الموديل واختباره وحفظه.

## 🚀 كيفية التشغيل السريع

1. قم بالضغط على زر **Open In Colab** الموجود بالأعلى.
2. **تنبيه هام**: الكود مبرمج ليقوم بسحب ملف `dataset.json` (بيانات تجريبية) من هذا المستودع تلقائياً. لتدريب الموديل على بياناتك الخاصة، قم بفتح أيقونة الملفات 📁 في يسار شاشة Colab، وافتح ملف `dataset.json` الذي تم تحميله، ثم قم بتعديل الأسئلة والإجابات بما يناسب مشروعك واحفظ الملف قبل إكمال باقي خطوات التدريب.
3. قم بتشغيل الخلايا داخل Colab واحدة تلو الأخرى لبدء عملية التدريب.
4. لرفع الموديل إلى منصة **HuggingFace** بعد انتهاء التدريب، ستحتاج إلى الحصول على `MY_HF_TOKEN`. يمكنك إنشاء التوكن (Token) الخاص بك مجاناً من هذا الرابط: [HuggingFace Tokens](https://huggingface.co/settings/tokens). تأكد من لصق التوكن واسم حسابك `username` في الخلية الأخيرة الخاصة بالرفع قبل تشغيلها.

## 🤝 شكر خاص ودعم
تم إعداد وتطوير هذا المشروع بواسطة المهندس **محمد الجرايحي**.

إذا استفدت من هذا المشروع، لا تنسَ دعمنا بعمل **Star ⭐** للمستودع!
يسعدني تواصلكم ومتابعتكم على منصة إكس (تويتر):
[حسابي على إكس (EngMoElgaraihy)](https://x.com/EngMoElgaraihy)

---

# Customer Service AI Fine-Tuning

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mohamed-Elgaraihy/customer-service-ai-finetune/blob/main/train.ipynb)

This repository contains the code and dataset to fine-tune the **Qwen 2.5** AI model to serve as a smart customer service assistant, utilizing **Unsloth** and **Python**.

## 🎥 Video Tutorial (YouTube)
You can watch the full tutorial on how to train the model via Google Colab and Unsloth using the following link:
[Click here to watch the video on YouTube](https://www.youtube.com/watch?v=cnkNQlqxg18)

## 📁 Project Files
* `dataset.json`: Contains the training data (questions and answers).
* `train.ipynb`: A Jupyter Notebook version ready for Google Colab.
* `train.py`: The main script for training, testing, and saving the model.

## 🚀 Quick Start Guide

1. Click on the **Open In Colab** button above.
2. **Important Note**: The notebook will automatically download a sample `dataset.json` file. To train the model on your own data, click the Files icon 📁 on the left sidebar in Colab, double-click the downloaded `dataset.json`, and edit it with your custom questions and answers. Save the file before continuing with the training.
3. Run the cells inside Colab sequentially to start the training process.
4. To upload the trained model to **HuggingFace**, you will need a `MY_HF_TOKEN`. You can generate your free API token from this link: [HuggingFace Tokens](https://huggingface.co/settings/tokens). Make sure to replace `Your_Token` and your `username` in the final upload cell before running it.

## 🤝 Acknowledgements & Support
This project was developed by Engineer **Mohamed Elgaraihy**.

If you found this project helpful, please don't forget to **Star ⭐** the repository!
I would be happy to connect with you on X (Twitter):
[My X Account (EngMoElgaraihy)](https://x.com/EngMoElgaraihy)

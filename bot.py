import os
import time
from instagrapi import Client

print("Starting Instagram bot worker...")

cl = Client()

# خواندن متغیرها از گیت‌هاب (IG_USERNAME و IG_PASSWORD)
USERNAME = os.getenv("IG_USERNAME")
SESSION_ID = os.getenv("IG_PASSWORD") # در این بخش مقدار sessionid را در گیت‌هاب قرار دهید

try:
    # لاگین امن با Session ID بدون نیاز به پسورد و چالش اینستاگرام
    cl.login_by_sessionid(SESSION_ID)
    print("با موفقیت به اینستاگرام متصل شد!")
except Exception as e:
    print("خطا در لاگین:", e)
    exit(1)

while True:
    try:
        threads = cl.direct_threads(amount=3)
        for thread in threads:
            last_message = thread.messages[0]
            if str(last_message.user_id) != str(cl.user_id):
                # شرط بررسی کلمه «قیمت» یا پاسخ خودکار
                text = last_message.text.lower() if last_message.text else ""
                
                if "قیمت" in text:
                    reply_text = "سلام! خوش آمدید. برای مشاهده قیمت‌ها لطفا در سایت ما ثبت‌نام کنید."
                else:
                    reply_text = "سلام! پیام شما خودکار دریافت شد."
                    
                cl.direct_send(reply_text, thread.id)
                print("Auto-reply sent!")
        
        # بررسی هر ۱ دقیقه یا ۲ دقیقه یک‌بار
        time.sleep(60)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)

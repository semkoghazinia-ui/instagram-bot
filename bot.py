import os
from instagrapi import Client

print("Starting Instagram bot worker...")

cl = Client()

USERNAME = os.getenv("IG_USERNAME")
SESSION_ID = os.getenv("IG_PASSWORD")

try:
    cl.login_by_sessionid(SESSION_ID)
    print("با موفقیت به اینستاگرام متصل شد!")
except Exception as e:
    print("خطا در لاگین:", e)
    exit(1)

try:
    # بررسی دایرکت‌ها فقط یک بار در هر بار اجرا
    threads = cl.direct_threads(amount=3)
    for thread in threads:
        last_message = thread.messages[0]
        if str(last_message.user_id) != str(cl.user_id):
            text = last_message.text.lower() if last_message.text else ""
            
           # بررسی کلمه «سمکو» در پیام کاربر
            if "سمکو" in text:
                reply_text = "سلام! خوش آمدید. پیام شما با کلمه کلیدی سمکو دریافت شد."
            else:
                reply_text = "سلام! پیام شما خودکار دریافت شد."
                
                
            cl.direct_send(reply_text, thread.id)
            print("Auto-reply sent!")
            
    print("بررسی دایرکت‌ها به اتمام رسید.")
except Exception as e:
    print("Error:", e)

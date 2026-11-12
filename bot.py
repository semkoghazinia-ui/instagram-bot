import os
import time
from instagrapi import Client

print("Starting Instagram bot worker...")

cl = Client()
# شبیه‌سازی مشخصات اپلیکیشن موبایل برای کاهش حساسیت اینستاگرام
cl.set_user_agent("Instagram 269.0.0.18.75 Android (31/12; 480dpi; 1080x2240; Samsung; SM-G991B; o1s; exynos2100; en_US)")

USERNAME = os.getenv("IG_USERNAME")
SESSION_ID = os.getenv("IG_PASSWORD")

try:
    cl.login_by_sessionid(SESSION_ID)
    print("با موفقیت به اینستاگرام متصل شد!")
except Exception as e:
    print("خطا در لاگین یا انقضای Session ID:", e)
    exit(1)

# مکث کوتاه برای پایداری اتصال
time.sleep(3)

try:
    threads = cl.direct_threads(amount=3)
    print(f"تعداد {len(threads)} گفتگو با موفقیت دریافت شد.")
    
    for thread in threads:
        if thread.messages:
            last_message = thread.messages[0]
            if str(last_message.user_id) != str(cl.user_id):
                text = last_message.text.lower() if last_message.text else ""
                
                # بررسی کلمه «سمکو» در دایرکت
                if "سمکو" in text:
                    reply_text = "سلام! خوش آمدید. پیام شما با کلمه کلیدی سمکو دریافت شد."
                    cl.direct_send(reply_text, thread.id)
                    print("Auto-reply sent for keyword!")
                    
    print("بررسی دایرکت‌ها به اتمام رسید.")
except Exception as e:
    print("خطای موقت از طرف سرور اینستاگرام (احتمال محدودیت IP گیت‌هاب):", e)

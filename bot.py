import os
import time
from instagrapi import Client

print("Starting Instagram bot worker...")

cl = Client()
# شبیه‌سازی دقیق مرورگر موبایل برای عبور از فیلترهای امنیتی اینستاگرام
cl.set_user_agent("Instagram 300.0.0.32.109 Android (33/13; 420dpi; 1080x2400; Samsung; SM-S911B; kalama; qcom; en_US)")

USERNAME = os.getenv("IG_USERNAME")
SESSION_ID = os.getenv("IG_PASSWORD")

try:
    cl.login_by_sessionid(SESSION_ID)
    print("با موفقیت به اینستاگرام متصل شد!")
except Exception as e:
    print("خطا در لاگین یا انقضای Session ID:", e)
    exit(1)

# مکث ۵ ثانیه‌ای برای طبیعی جلوه دادن درخواست
time.sleep(5)

try:
    # استفاده از متد امن‌تر برای دریافت چت‌ها
    threads = cl.direct_threads(amount=2, selected_filter="unread")
    print(f"تعداد {len(threads)} گفتگوی خوانده‌نشده دریافت شد.")
    
    for thread in threads:
        if thread.messages:
            last_message = thread.messages[0]
            if str(last_message.user_id) != str(cl.user_id):
                text = last_message.text.lower() if last_message.text else ""
                
                # بررسی کلمه «سمکو»
                if "سمکو" in text:
                    reply_text = "سلام! خوش آمدید. پیام شما با کلمه کلیدی سمکو دریافت شد."
                    cl.direct_send(reply_text, thread.id)
                    print("Auto-reply sent for keyword!")
                    
    print("بررسی دایرکت‌ها به اتمام رسید.")
except Exception as e:
    print("خطای موقت از طرف سرور اینستاگرام (محدودیت IP دیتاسنتر):", e)

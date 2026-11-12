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
    # دریافت گفتگوهای اخیر
    threads = cl.direct_threads(amount=5)
    print(f"تعداد {len(threads)} گفتگو دریافت شد.")
    
    for thread in threads:
        if thread.messages:
            last_message = thread.messages[0]
            print(f"آخرین پیام در چت: ID کاربر = {last_message.user_id}")
            
            # بررسی اینکه پیام متعلق به خودمان نباشد
            if str(last_message.user_id) != str(cl.user_id):
                text = last_message.text.lower() if last_message.text else ""
                print(f"متن پیام دریافتی: {text}")
                
                # بررسی وجود کلمه سمکو
                if "سمکو" in text:
                    reply_text = "سلام! خوش آمدید. پیام شما با کلمه کلیدی سمکو دریافت شد."
                    cl.direct_send(reply_text, thread.id)
                    print("Auto-reply sent for keyword!")
                else:
                    print("کلمه سمکو در پیام یافت نشد.")
            else:
                print("آخرین پیام متعلق به خود ربات است.")
            
    print("بررسی دایرکت‌ها به اتمام رسید.")
except Exception as e:
    print("Error in checking threads:", e)

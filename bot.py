import time
from instagrapi import Client

print("Starting Instagram bot worker...")

cl = Client()
# حتماً از اکانت تستی استفاده کنید
cl.login("YOUR_USERNAME", "YOUR_PASSWORD")

while True:
    try:
        threads = cl.direct_threads(amount=3)
        for thread in threads:
            last_message = thread.messages[0]
            if last_message.user_id != cl.user_id:
                cl.direct_send("سلام! پیام شما خودکار دریافت شد.", thread.id)
                print("Auto-reply sent!")
        
        # بررسی هر ۲ دقیقه یک‌بار
        time.sleep(120)
    except Exception as e:
        print("Error:", e)
        time.sleep(120)
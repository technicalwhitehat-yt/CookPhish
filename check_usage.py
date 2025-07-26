import os, json, requests
from datetime import datetime

# Paths
is_termux = os.path.exists("/data/data/com.termux")
log_path = "/data/data/com.termux/files/usr/bin/.cplog" if is_termux else "/usr/bin/.cplog"
limit = 1

# ✅ Get real date from your hosted API
try:
    res = requests.get("https://timeapi-73f7.onrender.com/", timeout=5)
    json_data = res.json()
    real_now = datetime.fromisoformat(f"{json_data['date']}T{json_data['time']}")
except Exception as e:
    print("⚠️ Failed to fetch real time. Check your internet or API.")
    exit(1)

# Read or initialize log
if os.path.exists(log_path):
    try:
        with open(log_path, "r") as f:
            data = json.load(f)
        last = datetime.fromisoformat(data.get("date", real_now.isoformat()))
        if last.date() != real_now.date():
            data["count"] = 0
    except:
        data = {"date": real_now.isoformat(), "count": 0}
else:
    data = {"date": real_now.isoformat(), "count": 0}

# Enforce limit
if data["count"] >= limit:
    print("🚫 Daily Free Limit Reached (2 runs/day). Try again tomorrow.")
    exit(1)

# Save updated log
data["count"] += 1
data["date"] = real_now.isoformat()
try:
    with open(log_path, "w") as f:
        json.dump(data, f)
except Exception as e:
    print(f"❌ Failed to save log: {e}")
    exit(1)

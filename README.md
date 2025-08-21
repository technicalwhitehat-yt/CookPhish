<h1 align="center">🚀 COOKPHISH - Advanced Instagram Hacking Framework</h1>

<p align="center">
  <a href="https://github.com/technicalwhitehat-yt"><img src="https://img.shields.io/badge/MADE%20IN-India-success?style=for-the-badge"></a>
  <a href="https://youtube.com/@technicalwhitehat"><img src="https://img.shields.io/badge/Tool-CookPhish-blueviolet?style=for-the-badge"></a>
  <a href="https://github.com/technicalwhitehat-yt/CookPhish"><img src="https://img.shields.io/github/v/release/technicalwhitehat-yt/CookPhish?style=for-the-badge"></a>
  <a href="https://github.com/technicalwhitehat-yt"><img src="https://img.shields.io/badge/Maintained%3F-Yes-brightgreen?style=for-the-badge"></a>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=technicalwhitehat-yt.CookPhish" alt="visitor badge"/>
</p>

<p align="center">
  <img width="100%" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEewMSMzXt5M1EICO8xvveC7-1Qr9gg2SOfHkfUX_7AeNpy_4FjM80JYrniMz47fukQNsvXzBmvU9kGuNAuy_DMGnnZ4i_AL3zzqJZhLpVaWDeTpoBUcymj675l59RXEqi0HKfkK0tvkyQbjLpA7vAugMW61dwZuf0dYMOVplqQ3pns5xcwmkHck49B290/s1280/twh.png" alt="CookPhish Screenshot"/>
</p>

---

## 🔍 About CookPhish

**CookPhish** is a modern and powerful phishing simulation framework developed by **Technical White Hat (TWH)**. It creates highly realistic fake login pages (like Instagram), logs victim data (IP, device, time), simulates 2FA, and runs in a stunning terminal interface.

> ⚠️ **Made strictly for ethical hacking training, CTFs, and cybersecurity education. Do not use illegally.**

---

## ⚙️ Features

- 🎨 Colorful dynamic gradient banner
- 📸 Realistic Instagram-style phishing simulation
- 🌐 Logs IP, user-agent, and timestamps
- 🔐 Simulates 2FA (TOTP / WhatsApp / SMS)
- 🔁 GitHub-based auto-update system
- 🚀 Fast Flask-based setup (no Apache needed)
- ☁️ Cloudflared and Tunnelmole tunneling support
- 🧾 Logs saved in `output/` directory

---

## 🧪 Tested Platforms

- Termux on Android
- Kali Linux
- Debian-based Linux distros

---

## 🔥 Why Choose CookPhish?

| Feature                 | Regular Tools     | CookPhish             |
|-------------------------|-------------------|------------------------|
| Dynamic Gradient Banner | ❌                | ✅ Yes                |
| 2FA Clone Pages         | ❌                | ✅ Yes                |
| Tunneling Support       | ❌                | ✅ Cloudflared/Tunnelmole |
| Auto Update             | ❌                | ✅ Git-based          |
| Android/Linux Support   | Limited           | ✅ Termux + Linux     |

---
## 🛠️ Installation

## How to setup cookphish in termux full partical video (Android) 📱
<p align="center">
  <a href="https://twhtube.blogspot.com/2025/08/cookphish-termux.html" target="_blank">
    <img width="100%" src="https://raw.githubusercontent.com/technicalwhitehat-yt/CookPhish/refs/heads/main/cookphish.png" alt="CookPhish Termux Setup"/>
  </a>
</p>


## 📱 Termux (Android)
```
pkg update && pkg upgrade -y
pkg update && pkg upgrade -y
pkg install git
git clone https://github.com/technicalwhitehat-yt/CookPhish.git
cd CookPhish
bash CookPhish
```
## Termux apk
👉 **If you don’t have Termux, you can click on “Click to Download” here to download Termux’s APK.** The latest version of Termux is v0.118.3.
[📥 Click to Download Termux.apk](https://github.com/termux/termux-app/releases/download/v0.118.3/termux-app_v0.118.3+github-debug_universal.apk)

---
## 🛠️ Installation

## How to setup & use cookphish on kali Linux full partical video (Computer) 💻
<p align="center">
  <a href="https://twhtube.blogspot.com/2025/08/cookphish-partical-video-for-kali-linux.html" target="_blank">
    <img width="100%" src="https://raw.githubusercontent.com/technicalwhitehat-yt/CookPhish/refs/heads/main/cookphish%202.png" alt="CookPhish kali linux Setup"/>
  </a>
</p>

## 💻 Kali Linux / Debian-based Linux
```
sudo apt-get update && upgrade -y
apt-get install git
git clone https://github.com/technicalwhitehat-yt/CookPhish.git
cd CookPhish
sudo bash CookPhish
```


> 🔁 **Note:** You must clone the repo via Git to enable auto-update functionality.

---

## 📦 Requirements

```bash
pip install -r requirements.txt
````

> ⚠️ **IMPORTANT:** If you start facing any errors while running Cookphish, then run this command. This will solve the problem. If it doesn’t, contact us. 📩

---


## 🚀 Usage

1. Start the tool using `./CookPhish`.
2. Colorful UI will load, followed by GitHub update check.
3. Local phishing server starts on port `8080`.
4. Use `cloudflared` or `tunnelmole` to expose online.
5. Logs:

   * IP/User Agent → `output/ip_agent.log`
   * Correct credentials → `output/correct_pass_user.log`
   * Wrong credentials → `output/wrong_pass.log`

> Web interface uses `web_app.py` with support for 2FA and logging.

---

## 📲 Recommended Browser for Mobile (Cookie Editor Support)

If you're testing **CookPhish** on Instagram using a mobile device, you'll need a browser that supports extensions like **Cookies Editor**.

👉 **Download the recommended browser app (.apk)** that supports cookie injection and browser extensions:  
[📥 Click to Download (.apk)](https://play.google.com/store/apps/details?id=com.lemurbrowser.exts)


## 🔧 How to Use (With Cookies Editor Extension)

1. Install the browser using the link above.
2. Open the browser and visit the **Chrome Web Store**.
3. Search and install the [**Cookies Editor**](https://chromewebstore.google.com/detail/cookie-editor/gigiddbkofmmehoipndncpadfopebjfh?utm_source=item-share-whatsapp) extension.
4. Launch the phishing page hosted by CookPhish (e.g. via `cloudflared` or `tunnelmole`).
5. Open **Cookies Editor** and find important cookies like:
   - `sessionid`
6. Modify or inject the cookies to simulate an authenticated session.

## 📸 Screenshots

<p align="center">
  <img width="100%" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlFtZwaTVfEPsleUX9c6KgDagIkKpDiTegF3ed6ZHsTPsqPUGUJnAL3EHdHkn_9rw1cfvdKxUAnelCtmWnSKD5TjdlAcinEFXFwNZOC637KGkSABhomCrDttbBHmnaE0rak8bTces5W6f2jDCg2hckbSvJcQnu2Kt5EljIzHEeEtidKbErKW19eUKFKur1/s1920/Untitled%20design.png"/>
</p>

---

## 🌐 Connect With Me

[![YouTube](https://img.shields.io/badge/YouTube-Everything%20is%20Free%20Tech-red?style=for-the-badge\&logo=youtube)](https://youtube.com/@technicalwhitehat)
[![Instagram](https://img.shields.io/badge/Instagram-Follow-blueviolet?style=for-the-badge\&logo=instagram)](https://instagram.com/technicalwhitehat)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge\&logo=telegram)](https://t.me/technicalwhitehat)
[![GitHub](https://img.shields.io/badge/GitHub-technicalwhitehat--yt-black?style=for-the-badge\&logo=github)](https://github.com/technicalwhitehat-yt)
[![Email](https://img.shields.io/badge/Email-Contact-green?style=for-the-badge\&logo=gmail)](mailto:technicalwhitehat@protonmail.com)

---

## ❤️ Support My Work

* 🌟 Star the repository
* 📢 Share it with friends
* 🧠 Use it in your cyber education events
* 🍀 Stay ethical, stay curious!

---

## ⚠️ Legal Disclaimer

> This tool is created strictly for **educational** and **ethical testing** purposes.
> Using CookPhish on unauthorized targets is **illegal**.
> The author is not responsible for any misuse or damage caused by this tool.
> Always get proper authorization before testing.

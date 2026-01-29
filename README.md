# TrackMyRupee
## Privacy-First Personal Finance Tracker & Expense Tracking App (No SMS, No Bank Access)

**TrackMyRupee** is a privacy-first personal finance tracker and expense tracking app built for people who want complete control over their money — without giving away their data.

Unlike most money management apps, TrackMyRupee does not read SMS, connect to bank accounts, or sell user data.
You manually track expenses, analyze spending, manage budgets, and stay in control — on your terms.

🌐 Live App: https://trackmyrupee.com  
🔓 Open Source · Self-Hosted · Django

![Django](https://img.shields.io/badge/Django-4.x-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Privacy First](https://img.shields.io/badge/Privacy-First-brightgreen)

---

## Why TrackMyRupee?

TrackMyRupee follows strict privacy principles:

-  ❌ No SMS reading
-  ❌ No bank account access
-  ❌ No selling or sharing financial data
-  ✅ Full data export and account deletion
-  Your money. Your data. Your control.

---

## Personal Finance Tracking Without Surveillance

Most expense tracking apps rely on:
- Reading SMS messages
- Connecting to bank accounts
- Sharing financial insights with third parties

**TrackMyRupee is different.**

It is a **privacy-first expense tracker** that gives you:
- Complete ownership of your financial data
- Manual and bulk expense tracking
- Transparent analytics with zero hidden tracking

---

## Features – Expense Tracking & Money Management

TrackMyRupee includes all the essential features expected from a modern **expense tracker and budget management app**:

✔ Daily expense tracking (manual entry)  
✔ Excel-based bulk expense import  
✔ Budget vs actual spending analysis  
✔ Visual dashboards and charts  
✔ Subscription and recurring payment tracking  
✔ Category-based expense filtering  
✔ Multi-currency support  
✔ Export your financial data anytime  

This makes TrackMyRupee ideal for:
- Individuals managing personal expenses
- Freelancers tracking income and costs
- Privacy-conscious users avoiding SMS-based apps

---

## Who Should Use TrackMyRupee?

TrackMyRupee is designed for:

- Users looking for a **simple expense tracker**
- People who want a **budget tracker without bank access**
- Anyone avoiding SMS-reading finance apps
- Developers looking for an **open source finance tracker**
- Users who want a **self-hosted personal finance app**

---

## Standout Features

### 1. Interactive Budget Dashboard
Visualize your monthly spending against your budget goals. Get instant alerts when you're nearing your limits.
![Budget Dashboard Screenshot](misc/dashboard2.png)

### 2. Smart Excel Import
Bulk upload your expenses with intelligence. The system automatically enforces the selected year and handles various date formats.
![Upload Page Screenshot](misc/upload.png)

### 3. Comprehensive Filtering
Slice and dice your financial data. Filter by **Year**, **Month**, **Category**, and **Date Range** to get the insights you need.

### 4. Recurring Transactions
Set it and forget it. Automate your regular income and expenses (like rent or subscriptions) so you never miss an entry.
![Recurring Transactions Screenshot](misc/subscriptions.png)

### 5. Category Management & Limits
Create custom categories and set monthly spending limits. The dashboard visualizes your progress against these limits.

### 6. Multi-Currency Support
Work with your preferred currency. Update your profile settings to display your local currency symbol across the app.

### 7. Smart Category Prediction 🧠
Typing descriptions manually? Let the app do the work.
- **Personalized Learning**: Recognizes your custom habits (e.g., "Momos" → "Street Food") from your history.
- **Rule-Based Instant Match**: Instantly detects common terms like "Uber", "Netflix", "Zomato", etc.
- **Generative AI (Optional)**: Connect Google Gemini AI for advanced context-aware categorization.

### 8. Smart Notifications & Email Reminders 🔔
Stay on top of your bills with a multi-channel notification system:
- **In-App Notifications**: Get alerts for upcoming payments directly in the dashboard.
- **Web Push Notifications**: Receive timely reminders on your device (supports both Desktop and Mobile).
- **Consolidated Email Summaries**: Get a single daily email listing all recurring payments due in 3 days (Exclusive to **Plus** and **Pro** users).
- **Auto-Cleanup**: Old notifications are automatically removed after 90 days to keep your list clean.

---

### 🚀 Quick Start – Self-Hosted Expense Tracker (Docker)

Run your own self-hosted personal finance tracker in minutes:

```bash
git clone https://github.com/OmkarPathak/django-finance-tracker
cd django-finance-tracker
docker-compose up
```

Open 👉 http://localhost:8000

### Manual Setup (Django)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

Detailed steps can be found in `SETUP.md`

## Contributing to TrackMyRupee

TrackMyRupee is an open-source personal finance tracker.
Contributions are welcome — features, bug fixes, documentation, and UI improvements.

👉 See `CONTRIBUTING.md`

## 💬 What users say

> “Finally a finance app that doesn’t read my SMS.”  
> — Early user

> “Simple, clean, and private.”  
> — Indie Hacker

## 📝 License

TrackMyRupee is licensed under the MIT License.

# TrackMyRupee
# Privacy-First Personal Finance Tracker & Expense Tracking App (No SMS, No Bank Access)

![Django](https://img.shields.io/badge/Django-4.x-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Privacy First](https://img.shields.io/badge/Privacy-First-brightgreen)

**TrackMyRupee** is an open-source **personal finance tracker** and **expense tracking app** built for people who want full control over their money **without sacrificing privacy**.

Unlike traditional money management apps, TrackMyRupee does **not read SMS, connect to bank accounts, or sell user data**.

🌐 Live App: https://trackmyrupee.com  
🔓 Open Source · Self-Hosted · Django  
📱 Android & iOS apps coming soon

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
![Budget Dashboard Screenshot](misc/dashboard1.png)
![Budget Dashboard Screenshot](misc/dashboard2.png)

### 2. Smart Excel Import
Bulk upload your expenses with intelligence. The system automatically enforces the selected year and handles various date formats.
![Upload Page Screenshot](misc/upload.png)

### 3. Comprehensive Filtering
Slice and dice your financial data. Filter by **Year**, **Month**, **Category**, and **Date Range** to get the insights you need.
![Filtering Screenshot](misc/filters.png)

### 4. Recurring Transactions
Set it and forget it. Automate your regular income and expenses (like rent or subscriptions) so you never miss an entry.
![Recurring Transactions Screenshot](misc/subscriptions.png)

### 5. Category Management & Limits
Create custom categories and set monthly spending limits. The dashboard visualizes your progress against these limits.
![Category Limits Screenshot](misc/limits.png)

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

## Manual Setup

-   Python 3.8+
-   pip (Python package manager)

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd django-finance-tracker
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```
5.  **Setup Demo User** (Optional but recommended):
    ```bash
    python manage.py setup_demo_user
    ```

    **Note**: This command populates the database with sample data for the demo mode.


## 🚀 Quick Start – Self-Hosted Expense Tracker (Docker)

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd django-finance-tracker
    ```

2.  **Create `.env` file**:
    Create a file named `.env` in the root directory. Fill in the values:
    ```env
    SECRET_KEY=''
    DEBUG=True
    EMAIL_HOST='smtp.gmail.com' # if you want to use gmail for sending emails
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=''
    EMAIL_HOST_PASSWORD=''
    ```
    **Note**: The application will not run correctly without this file.

3.  **Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```
    **Note**: The container defaults to running migrations and setting up the demo user automatically on startup.

4.  **Access the application**:
    Open your browser and navigate to `http://localhost:8000`.


### Getting Started

1.  **Sign Up**: Create a new account.
2.  **Add Expenses**: Manually add expenses or use the "Upload More" button.
3.  **View Dashboard**: authenticating will take you to the dashboard where you can filter and analyze your spending.

### Bulk Upload Format

To upload expenses via Excel, ensure your file follows this format:

-   **File Type**: `.xlsx`
-   **Sheets**: You can have multiple sheets (e.g., "Jan", "Feb").
-   **Columns**: The following columns are strictly required (headers are case-insensitive):
    -   `Date`: Supported formats: `DD MMM YYYY` (e.g., 01 Jan 2025), `YYYY-MM-DD`.
    -   `Amount`: Numeric value.
    -   `Description`: Text description.
    -   `Category`: Expense category (e.g., Food, Travel).

**Note**: When uploading, you will be asked to select a "Target Year". This year will override the year in the Excel dates to ensure data consistency.

## Privacy-First by Design

TrackMyRupee follows strict privacy principles:

-  ❌ No SMS reading
-  ❌ No bank account access
-  ❌ No selling or sharing financial data
-  ✅ Full data export and account deletion
-  Your money. Your data. Your control.

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

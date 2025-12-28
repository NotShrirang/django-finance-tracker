# Django Finance Tracker

A personal finance application to track expenses, analyze spending trends, and visualize data.

## Features

-   **Dashboard**: Visualize spending with category distribution charts and monthly/daily trend graphs.
-   **Expense Management**: Add, edit, and delete expenses.
-   **Bulk Upload**: Upload Excel files with multiple sheets to import expenses.
-   **Advanced Filtering**: Filter expenses by Year, Month, Category, and Search by description.
-   **Data Privacy**: Each user sees only their own data.

## Prerequisites

-   Python 3.8+
-   pip (Python package manager)

## Installation

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

## Usage

### Running the Server

Start the development server:

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

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

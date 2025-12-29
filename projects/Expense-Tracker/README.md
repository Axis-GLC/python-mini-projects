# Simple Expense Tracker

A lightweight web application built with Python and Streamlit to track personal expenses. Users can add items with costs and categories, and visualize their spending.

## Features

- Add expenses with a name, amount, and category.
- View a history table of all transactions.
- See the total amount spent.
- View a bar chart breakdown of spending by category.
- Data persists temporarily while the script is running (in-memory session state).

## Prerequisites

You need Python installed on your machine.

## Installation

1. **Download the files**: Ensure `app.py` and `requirements.txt` are in the same folder.

2. **Create a Virtual Environment (Recommended)**:
   `python -m venv venv`
      `# Windows`
         `venv\Scripts\activate`
            `# Mac/Linux`
               `source venv/bin/activate`

3. **Install Dependencies**:
                  Run the following command in your terminal to install Streamlit and Pandas:
                     `pip install -r requirements.txt`

## How to Run

1. Open your terminal/command prompt in the project folder.
2. Run the app using this command:
                        `streamlit run app.py`
3. The application will open automatically in your default web browser (usually at `http://localhost:8501`).

## Usage

1. Enter an **Item Name** (e.g., "Lunch").
2. Enter the **Amount** in dollars.
3. Select a **Category** (e.g., "Food").
4. Click **Add Expense**.
5. View the updates in the table and the chart below.


**Pull Requests and Issues are welcomed :)**
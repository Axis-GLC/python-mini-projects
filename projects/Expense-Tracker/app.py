import streamlit as st
import pandas as pd

# --- Configuration ---
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="centered")

# --- Session State Initialization ---
# We use session_state to keep data even when the app reruns (which happens on every click)
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

    # --- Header ---
    st.title("💰 Simple Expense Tracker")
    st.markdown("Keep track of your daily spending easily.")

    # --- Input Form ---
    st.subheader("Add New Expense")
    with st.form("expense_form", clear_on_submit=True):
        # Create 3 columns for input layout
            col1, col2, col3 = st.columns(3)
                
                    with col1:
                            item_name = st.text_input("Item Name", placeholder="e.g. Coffee")
                                
                                    with col2:
                                            amount = st.number_input("Amount ($)", min_value=0.0, step=0.01, format="%.2f")
                                                
                                                    with col3:
                                                            category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Other"])
                                                                
                                                                    submitted = st.form_submit_button("Add Expense")

                                                                        # Logic to add expense
                                                                            if submitted and item_name and amount > 0:
                                                                                    new_expense = {
                                                                                                "Name": item_name,
                                                                                                            "Amount": amount,
                                                                                                                        "Category": category
                                                                                                                                }
                                                                                                                                        st.session_state.expenses.append(new_expense)
                                                                                                                                                st.success(f"Added '{item_name}' to your list!")

                                                                                                                                                # --- Display Section ---
                                                                                                                                                if st.session_state.expenses:
                                                                                                                                                    # Convert list of dictionaries to a DataFrame for easier display/manipulation
                                                                                                                                                        df = pd.DataFrame(st.session_state.expenses)

                                                                                                                                                            st.divider()
                                                                                                                                                                st.subheader("📊 Expense History")
                                                                                                                                                                    
                                                                                                                                                                        # Show the dataframe
                                                                                                                                                                            st.dataframe(df, use_container_width=True)

                                                                                                                                                                                # Metrics
                                                                                                                                                                                    col_a, col_b = st.columns(2)
                                                                                                                                                                                        total_spent = df['Amount'].sum()
                                                                                                                                                                                            num_items = len(df)
                                                                                                                                                                                                
                                                                                                                                                                                                    with col_a:
                                                                                                                                                                                                            st.metric("Total Spent", f"${total_spent:.2f}")
                                                                                                                                                                                                                with col_b:
                                                                                                                                                                                                                        st.metric("Number of Items", num_items)

                                                                                                                                                                                                                            # Chart
                                                                                                                                                                                                                                st.subheader("Spending by Category")
                                                                                                                                                                                                                                    category_group = df.groupby('Category')['Amount'].sum()
                                                                                                                                                                                                                                        st.bar_chart(category_group, use_container_width=True)

                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                            st.info("No expenses recorded yet. Add one above to get started!")
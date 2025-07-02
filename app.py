import streamlit as st
import pandas as pd

st.title("DAILY EXPENSE TRACKER")

username = st.text_input("Enter the username: ")

if username:
    options = ["Transport","Food","Stationary","Shopping"]
    category = st.selectbox("Where you spend: " , options,None)

    amount = st.number_input("Money spended: ",0)

    date = st.date_input("ON which day: ",)

    st.write(f"On {date} You spended {amount} Rupess on {category}",)

    add = st.button("Add Expense: ")

    if add and category is not None:
        new_data = {"category":category ,"amount":amount, "date":date}

        try:
            df = pd.read_csv(f"{username}.csv")
        except FileNotFoundError:
            df = pd.DataFrame([new_data])

        new_row_df = pd.DataFrame([new_data])
        df = pd.concat([df,new_row_df], ignore_index=True)

        df.to_csv(f"{username}.csv",index=False)

        st.success("Expense added successfully")

    df = pd.read_csv(f"{username}.csv")
    st.dataframe(df)

    st.bar_chart(df,x="category", y="amount")

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.strftime("%B")

    monthly_total = df.groupby("month")["amount"].sum()
    st.line_chart(monthly_total)

    df = pd.read_csv(f"{username}.csv")
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=f"Download {username}'s expense report ",
        data=csv_data,
        file_name=f"{username}.csv",
        mime='text/csv'
    )
else:
    st.write("Enter a valid username")
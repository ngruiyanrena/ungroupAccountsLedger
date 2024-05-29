import streamlit as st
import pandas as pd


def process_GL(GL_file):
    GL_data = pd.read_excel(GL_file, header=5)
    GL_cleaned = GL_data.drop(columns=['Running Balance (SGD)'])
    GL_cleaned = GL_cleaned.dropna(subset=['Transaction Type'])
    GL_cleaned = GL_cleaned.reset_index(drop=True)
    return GL_cleaned

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def main():

    st.title('[TEMP] Ungroup Accounts Ledger')

    GL_file = st.file_uploader("Upload General Ledger", type=['xlsx'])

    if GL_file is not None:
        processed_data = process_GL(GL_file)
        st.write("Processed Data", processed_data)
        csv = convert_df_to_csv(processed_data)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Transactions.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Business Data Visualization App")

    # File uploader allows user to add their own CSV
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Display the dataframe
        st.write(df)

        # Basic stats of the dataframe
        if st.button("Show Summary Statistics"):
            st.write(df.describe())

        # Select box for choosing column to visualize
        column_to_plot = st.selectbox('Select column to visualize', df.columns)

        # Plotting
        if st.button("Generate Plot"):
            # Create a simple plot
            fig, ax = plt.subplots()
            df[column_to_plot].hist(bins=20, ax=ax)
            ax.set_xlabel(column_to_plot)
            ax.set_ylabel("Frequency")
            ax.set_title(f"Distribution of {column_to_plot}")
            st.pyplot(fig)

if __name__ == "__main__":
    main()

import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")

    st.write("Enter three numbers:")
    num1 = st.number_input("Number 1", value=0)
    num2 = st.number_input("Number 2", value=0)
    num3 = st.number_input("Number 3", value=0)

    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()

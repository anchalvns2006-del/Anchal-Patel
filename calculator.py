
import streamlit as st
st.title(' Calculator')
st.header('my first web based application')




c1,c2 =st.columns(2)
fnum = c1.number_input('Enter first number' , value=0)
snum = c2.number_input('Enter second number' , value=0)

options = ['Addition' , 'Subtraction' , 'Multiplication' , 'Division','Exponentiation']
choice =st.radio('Select an operation' , options)

button =st.button('Calculate')

result = 0
if button:
    if choice == 'Addition':
        result = fnum + snum
    elif choice == 'Subtraction':
        result = fnum - snum
    elif choice == 'Multiplication':
        result = fnum * snum
    elif choice == 'Division':
        if snum != 0:
            result = fnum / snum
        else:
            st.error('Cannot divide by zero')
    elif choice == 'Exponentiation':
        result = fnum ** snum

    st.success(f'The result is: {result}')

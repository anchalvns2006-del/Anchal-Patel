# pip install streamlit
import streamlit as st
st.title(' Calculator')
st.header('my first web based application')


# columns
c1,c2 =st.columns(2)
fnum = c1.number_input('Enter first number' , value=0)
fnum = c2.number_input('Enter second number' , value=0)

options = ['Addition' , 'Subtraction' , 'Multiplication' , 'Division','Exponentiation']
choice =st.radio('Select an operation' , options)

button =st.button('Calculate')

result = 0
if button:
    if choice == 'Addition':
        result = fnum + fnum
    if choice == 'Subtraction':
        result = fnum - fnum
    if choice == 'Multiplication':
        result = fnum * fnum
    if choice == 'Division':
        if fnum != 0:
            result = fnum / fnum
        else:
            st.error('Cannot divide by zero')
    elif choice == 'Exponentiation':
        result = fnum ** fnum
#  if choice=='Square Root':
#      result =math.sqrt(fnum)

    st.success(f'The result is: {result}')

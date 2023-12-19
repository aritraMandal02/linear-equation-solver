import streamlit as st
import numpy as np
from numpy.linalg import LinAlgError

st.title('nxn Linear Equation Solver:')
number = st.number_input(
    'Enter the number of the linear equations', step=1, min_value=2, value=3)

cols = st.columns(number+1)

A = []
B = []
key = 1
count = 1

if cols:
    for col in cols:
        if count == number+1:
            with col:
                for i in range(number):
                    col1, col2 = st.columns(2)
                    col1.text('=')
                    b = col2.number_input('b', key=key)
                    B.append(b)
                    key += 1
            continue
        with col:
            row = []
            for i in range(number):
                a = st.number_input('a', key=key)
                row.append(a)
                key += 1
            A.append(row)
        count += 1

clicked = st.button('Solve')

if clicked:
    A = np.array(A).T
    try:
        X = np.linalg.solve(A, B)
        for i, val in enumerate(X):
            st.text(f'x{i+1} = {round(val, 3)}')
    except LinAlgError as e:
        st.text(f'{e}: Invalid system of equations')

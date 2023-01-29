import streamlit as st
with st.form(key='or'): #重要！これないとFormが起動せず。Fileのオープン→処理→クローズまで。1セットで事項する便利なコード

    name= st.text_input('ばまえ')
    name= st.text_input('ば')
    name= st.text_input('rr')

    submit_btn=st.form_submit_button('送信')
    cancel_btn=st.form_submit_button('No')

    if submit_btn:
        st.text(f'ようこそ{name}san') 
        
    print(f'submit_btn: {submit_btn}')
    print(f'submit_btn: {cancel_btn}')

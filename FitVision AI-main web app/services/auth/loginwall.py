import streamlit as st 
from services.persistence.exercise_repository import get_or_create_user



def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    

    st.title("FitVision-Ai")
    st.write("### Welcome back! Continue your fitness journey.")

    with st.form("Login_form", clear_on_submit=False):
        username = st.text_input("Username", placeholder="username eg. Harsh Liftts")
        submit_button = st.form_submit_button("Stat Session")

    if submit_button:
        if not username:
            st.error("Username cannot be blank.")
            return False

        user = get_or_create_user(username)

        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]


        st.rerun()

    return False
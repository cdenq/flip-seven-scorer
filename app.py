import streamlit as st
from flip7_scorer.pages import scorer, advisor

PAGES = {
    "Scorer": scorer.show,
    "Advisor": advisor.show,
}


def main():
    st.set_page_config(page_title="Flip7 Scorer", layout="wide")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[page]()


if __name__ == "__main__":
    main()
from datetime import datetime

import streamlit as st

DATE_FORMAT = "%Y-%m-%d"
UMNICHKA = "Умничка"
RAPUNTSEL = "Рапунцель"

KITSUSYA = "КИЦУСЯ"
KOTYONOCHEK = "КОТЁНОЧЕК"

BEGIN_DATE = "2023-05-16"
TODAY_YOU_ARE = "Значит сегодня ты"


def main():
    choose_you = st.selectbox(
        "Кто ты?",
        (
            UMNICHKA,
            RAPUNTSEL,
        ),

    )
    begin_date = datetime.strptime(BEGIN_DATE, DATE_FORMAT).date()
    today = datetime.today().date()
    days_done = (today - begin_date).days
    if (choose_you == UMNICHKA and days_done % 2) or (choose_you == RAPUNTSEL and days_done % 2 == 0):
        st.write(TODAY_YOU_ARE)
        st.write(KOTYONOCHEK)
    else:
        st.write(TODAY_YOU_ARE)
        st.write(KITSUSYA)


if __name__ == "__main__":
    main()

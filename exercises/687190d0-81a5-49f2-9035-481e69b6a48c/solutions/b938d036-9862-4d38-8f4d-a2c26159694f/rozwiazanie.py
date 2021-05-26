def niepowtarzalne(st):
    
    try:
        st = str(st)
    except TypeError:
        return 'blad wprowadzenia'

    st = st.lower().split()
    res = {i : st.count(i) for i in set(st) if st.count(i)>1}
    return f"zawiera {list(res.keys())}" if len(res) != 0 else "nie zawiera"
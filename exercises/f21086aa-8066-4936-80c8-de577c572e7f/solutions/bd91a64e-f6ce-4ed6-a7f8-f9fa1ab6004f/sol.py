def niepowtarzalne(st):

    try:
        st = str(st).lower().split()
    except TypeError:
        return 'blad wprowadzenia'

    res = {i : st.count(i) for i in set(st) if st.count(i)>1}
    return 'zawiera' if len(res) != 0 else 'nie zawiera'
    #return f"zawiera {list(res.keys())}" if len(res) != 0 else "nie zawiera"
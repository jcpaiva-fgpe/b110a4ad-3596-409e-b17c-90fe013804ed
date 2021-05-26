st = input().lower().split()
res = {i : st.count(i) for i in set(st) if st.count(i)>1}
print(f"zawiera {list(res.keys())}" if len(res) != 0 else "nie zawiera")
from collections import deque
N,M,Q = map(int,input().split())
st = deque(range(N))
for a in map(int,input().split()):
    st.rotate(((-1)**((a&1)+1))*a)
    st.popleft()
print("\n".join("1" if q in st else "0" for q in map(int,input().split())))

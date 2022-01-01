#Speedtest
from speedtest import Speedtest
st=Speedtest()
print("Your connection's Download Speed in Bytes:",st.download())
print("Your connection's Upload Speed in Bytes:",st.upload())

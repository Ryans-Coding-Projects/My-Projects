#Simple internet speedtest

import speedtest

st = speedtest.Speedtest()

print("Testing internet speed please wait....\n")

download = (st.download()) / 1000000
upload = (st.upload()) / 1000000



print(f"Download Speed: {download} \nUpload Speed: {upload}")


import numpy
import pandas
from PIL import Image
import time
import streamlit


streamlit.write('Start')
latest_iteration = streamlit.empty()
bar = streamlit.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
else:
    streamlit.write("Install has finished!")


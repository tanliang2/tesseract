
from PIL import Image
import datetime
import pytesseract
import time
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()
    text = pytesseract.image_to_string( image= Image.open('/Users/a123/Downloads/test2.png'),lang='chi_sim')
    print('cost_time:'+str(time.time() - start_time) +'ms')
    print(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

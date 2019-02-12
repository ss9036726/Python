import webbrowser
import time

total_break = 3
break_count = 0



while(break_count < total_break):
    print ("The Program started on " + time.ctime())
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=dcEP7YXUC6o")
    break_count = break_count + 1


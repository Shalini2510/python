#'finally' is executed always. It gurantees execution of block. Usually used for freeing up resourcesv
import time

try:
    count = 0
    while True:
        count += 1
        print("hello")
        if count==5:
            break
        else:
            time.sleep(2)
except KeyboardInterrupt:
    print("ctrl and c pressed")
finally:
    print("executed always")
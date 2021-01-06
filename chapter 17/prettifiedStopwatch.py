import time

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
    while(True):

        input()
        lapTime = str(round(time.time() - lastTime , 2)).rjust(7)
        totalTime = str(round(time.time() - startTime , 2)).rjust(8)

        print("Lap # {}:{} ({})".format(lapNum,totalTime,lapTime , end = ""))
        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    print("\nDone!")





# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys


if __name__ == "__main__":
    file = open('./input/data.txt', 'r')
    lines = file.readlines()

    n = int(lines[0])

    def hourToMin(hour):
        return (hour-8)*60+1

    def dayToMin(day):
        return (day-1)*600

    parsed = []
    for i in range(1, n+1):
        day = int(lines[i][0])
        start = dayToMin(day)+hourToMin(int(lines[i][2:4]))+int(lines[i][5:7])
        end = dayToMin(day)+hourToMin(int(lines[i][8:10]))+int(lines[i][11:13])
        parsed.append([start, end])

    sortedList = sorted(parsed, key=lambda x: x[0])
    uniques = []

    current = sortedList[0]
    for i in range(1, n):
        curb = sortedList[i][0]
        cure = sortedList[i][1]
        if curb <= current[1]:
            current[1] = max(current[1], cure)
        else:
            uniques.append([current[0], current[1]])
            current = sortedList[i]

    res = 1
    for i in range(len(uniques)):
        if res+59 < uniques[i][0]:
            break
        res = uniques[i][1] + 1

    beg = res
    end = res + 59

    day = (beg-1) // 600

    hour = ((beg - 1 - (day*600)) // 60)
    minute = beg - 1 - (day*600) - (hour*60)

    houre = ((end - 1 - (day*600)) // 60)
    minutee = end - 1 - (day*600) - (houre*60)

    def countToString(hour):
        if hour < 10:
            return "0"+str(hour)
        else:
            return str(hour)

    print(str(day+1)+" "+countToString(hour+8)+":"+countToString(minute) +
          "-"+countToString(houre+8)+":"+countToString(minutee))

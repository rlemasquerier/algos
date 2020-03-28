from minizinc import Instance, Model, Solver, Status
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
def prep_data():
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
    return parsed, n

def solve():
    times, n = prep_data()
    nqueens = Model("./model.mzn")
    # Find the MiniZinc solver configuration for Gecode
    solver = Solver.lookup("chuffed")
    # Create an Instance of the n-Queens model for Gecode
    instance = Instance(solver, nqueens)
    # Assign 4 to n
    instance["N_slot"] = n
    instance["min_time"] = 0
    instance["max_time"] = 7*60*24
    instance["max_duration_meeting"] = max([s[1]-s[0]+1 for s in times])
    instance["duration_meeting"] = 59
    instance["array_meeting"] = [s[0] for s in times]
    instance["array_duration"] = [s[1]-s[0]+1 for s in times]
    from datetime import timedelta
    result = instance.solve(timeout=timedelta(seconds=3600))
    # Output the array q
    opt: Status = result.status
    print(result.__dict__)
    time = result["time_meeting"]

    beg = time
    end = time + 59

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
if __name__ == "__main__":
    solve()
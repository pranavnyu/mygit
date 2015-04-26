__author__ = 'pranavrajtyagi'

class Window(object):

    def __init__(self,window_string):
        self.window  = window_string


def get_enclosing_rectangle(windows):

    recs = []
    for item in windows:
        x,y,w,h = item.split(" ")
        x1 = ''.join(a for a in x if a.isdigit())
        y1 = ''.join(a for a in y if a.isdigit())
        w1 = ''.join(a for a in w if a.isdigit())
        h1 = ''.join(a for a in h if a.isdigit())
        x2 = int(x1)+int(w1)
        y2 = int(y1)+int(h1)
        x1 = int(x1)
        y1 = int(y1)
        rec = (x1,y1,x2,y2)
        recs.append(rec)

    recs = zip(*recs)
    results = []
    for i in range(0,4):
        if i == 0 or i == 1:
            minX = min(recs[i])
            results.append(minX)
        elif i==2 or i == 3:
            maxY = max(recs[i])
            results.append(maxY)
    x1 = results[0]
    y1 = results[1]
    x2 = results[2]
    y2 = results[3]

    w = int(x2) - int(x1)
    h = int(y2) - int(y1)

    output = "X=" + str(x1) + " " + "Y="+str(y1)+ " " + "W="+str(w)+" "+"H="+str(h)
    return output


if __name__ == '__main__':
    for windows in ['X=5 Y=9 W=10 H=40' , 'X=16 Y=16 W=10 H=40'],['X=0 Y=0 W=1 H=5' , 'X=0 Y=8 W=1 H=9']:

        print get_enclosing_rectangle(windows)


import sys
from PySide.QtCore import*
from PySide.QtGui import*
import turtle as t


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("image/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("image/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(250, 50, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("image/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(0, 150, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("image/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(100, 400, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(110, 450, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Disk:
    def __init__(self, name, x, y, h, w):
        self.name = name
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.color = 'black'

    def showdisk(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        #t.color(self.color)
        #t.begin_fill()
        t.fd(self.width/2)
        t.lt(90)
        t.fd(self.height)
        t.lt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.height)
        t.lt(90)
        t.fd(self.width/2)
        #t.end_fill()

    def newpos(x, y):
        self.x = x
        self.y = y

    def cleardisk(self):
        t.pencolor("white")
        self.showdisk()
        t.pencolor('black')

class Pole:
    def __init__(self, n, x, y):
        self.name = n
        self.stack = []
        self.top_position = 0
        self.x = x
        self.y = y
        self.thickness = 20
        self.length = 200
        self.color = 'pink'

    def showpole(self):
        t.pu()
        t.goto(self.x, self.y)
        t.pd()
        t.color(self.color)
        t.begin_fill()
        t.fd(self.thickness/2)
        t.lt(90)
        t.fd(self.length)
        t.lt(90)
        t.fd(self.thickness)
        t.lt(90)
        t.fd(self.length)
        t.lt(90)
        t.fd(self.thickness/2)
        t.end_fill()

    def pushdisk(self, disk):
        disk.x = self.x
        disk.y = self.y + self.top_position
        disk.showdisk()
        self.top_position += 40
        self.stack.append(disk)

    def popdisk(self):
        self.stack[len(self.stack)-1].cleardisk()
        self.top_position -= 40
        return self.stack.pop()

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)*30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s,d)
            self.move_tower(n-1, w ,d ,s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)





def main():
    app = QApplication(sys.argv)

    t.speed(5)
    h = Hanoi()
    h.solve()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

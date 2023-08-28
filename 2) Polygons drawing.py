import turtle


p = turtle.Pen()
l=35
n = 3
while n < 11:
    l=l*1.2
    p.down ()
    p.left ((n-2)*180/(2*n))

    for i in range (n):
        p.left (180-((n-2)*180/n))
        p.forward (l)

    p.up()
    p.right ((n-2)*180/(2*n))
    p.forward (15)
    n+=1   #or n = n + 1

turtle.done()
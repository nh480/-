Web VPython 3.2


dou = box(pos=vec(-12.15, -21, -5), length=4, height=10, width=1)
re = box(pos=vec(-8.1, -21, -5), length=4, height=10, width=1)
mi = box(pos=vec(-4.05, -21, -5), length=4, height=10, width=1)
fa = box(pos=vec(0, -21, -5), length=4, height=10, width=1)
sol = box(pos=vec(4.05, -21, -5), length=4, height=10, width=1)
la = box(pos=vec(8.1, -21, -5), length=4, height=10, width=1)
si = box(pos=vec(12.15, -21, -5), length=4, height=10, width=1)


rep = box(pos=vec(-10.15, -19, -4.5), length=2, height=6, width=1, color=color.black)
mip = box(pos=vec(-6, -19, -4.5), length=2, height=6, width=1, color=color.black)
solp = box(pos=vec(2, -19, -4.5), length=2, height=6, width=1, color=color.black)
lap = box(pos=vec(6, -19, -4.5), length=2, height=6, width=1, color=color.black)
sip = box(pos=vec(10.15, -19, -4.5), length=2, height=6, width=1, color=color.black)




h = sphere(size = vec(0.9,0.9,0.9))
er = sphere(pos = vec(-0.3,0.36,0), size = vec(0.2,0.2,0.2))
ea = sphere(pos = vec(0.3,0.36,0), size = vec(0.2,0.2,0.2))
erp = sphere(pos = vec(-0.3,0.36,0.04), size = vec(0.15,0.15,0.15),color = vec(255/255,204/255,229/255))
eap = sphere(pos = vec(0.3,0.36,0.04), size = vec(0.15,0.15,0.15),color = vec(255/255,204/255,229/255))
ey = sphere(color = color.black, pos = vec(0.15,0.1,0.4), size = vec(0.07,0.07,0.07))
ee = sphere(color = color.black, pos = vec(-0.15,0.1,0.4), size = vec(0.07,0.07,0.07))
nos = sphere(color = color.black, pos = vec(0,0,0.45), size = vec(0.07,0.07,0.07))


bear = compound([h, er, ea, erp, eap, ey, ee, nos])




b = sphere(make_trail = True)


while True :
    rate(100)
    if scene.mouse.pick == dou :
        b.pos.x = b.pos.x + 0.1
    if scene.mouse.pick == re :
        b.pos.x = b.pos.x + -0.1
    if scene.mouse.pick == mi :
        b.pos.y = b.pos.y + 0.1

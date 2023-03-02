from vpython import *
#GlowScript 3.0 VPython
# adapted from code
# simulation of projectile motion
# Written for Phy 235
# Frank Wolfs, Univ. of Rochester, September 2017.
# Example problem 2.7
g = 9.81
cd = 0.22
cl = 0.00
p = 1.2
r = 0.11
A = r * r * pi
m = 0.43
a = 0.0 * pi/ 180.0

# Define the scene.
width = 5.0E4   # Horizontal range.
height = 5.0E4  # Vertical range.

scene.title = "Projectile motion"
scene.background = color.white
scene.up = vector(0.,0.,1.)
scene.forward = vector(0.,1.,0.)
scene.width=700
scene.height=400
scene.range=0.5*width
scene.center=vector(scene.range,0.,0.)

# Define the surface (the green ground).
ground = box(pos=vector(0,0,-1.0E2), length = 4*width, height = 0.1*width,\
             width = 2.0E2, color=color.green)

# Create a run button so that the user can decide when to start the program.
# An empty scene is displayed with a "fire" button.
# When the user presses the "fire" button the simulation starts.
run = False
def Runbutton(r):
    global run
    run = not run
    if run:
        r.text = "Pause"
    else:
        r.text = "Fire"

button(text='Fire', bind=Runbutton)

listcl = []
listcd = []
listx = []
listz = []
listv = []

proj_x = []
proj_z = []
proj_xv = []
proj_zv = []
i = 0

lt1 = 0
lt2 = 0
lt3 = 0
lt4 = 0
lt5 = 0
lt6 = 0
lt7 = 0

while (cd < 0.29):
    
    x0 = 0.0
    y0 = 0.0
    z0 = 0.0
    initialPosition = vector(x0, y0, z0)

    v0 = 30.0
    angle0 = 45.0

    v0x = v0 * cos(angle0 * pi/ 180.0)
    v0y = 0.0;
    v0z = v0 * sin(angle0 * pi/ 180.0)
    initialVelocity = vector(v0x, v0y, v0z)

    proj =  sphere(color=color.blue, radius=50,\
                     pos=vector(x0,y0,z0),\
                     velocity=vector(v0x,v0y,v0z),\
                     make_trail=True, trail_type="curve",\
                     trail_color=color.blue,interval=1)
                   
    accel_g = vector(0.0, 0.0, -g)

    accel_p = accel_g

    dt = 0.005
    t = 0.0

    time = []

    while (proj.pos.z >= 0.0):
        
        kd = (p * A * cd)/(2 * m)
        kl = (p * A * cl)/(2 * m)
    
        rate(1000)
    
        if not run: continue
    
        time.append(t)
        proj_x.append(proj.pos.x)
        proj_z.append(proj.pos.z)
        proj_xv.append(proj.velocity.x)
        proj_zv.append(proj.velocity.z)
    
        t = t + dt
        
        accel_x = -mag(proj.velocity) * (kd * proj.velocity.x + kl * proj.velocity.z)
        accel_y = 0.0;
        accel_z = -g - mag(proj.velocity) * (kd * proj.velocity.z - kl * proj.velocity.x)
        accel_p = vector(accel_x, accel_y, accel_z)
        
        dv = dt * accel_p
        
        proj.velocity = proj.velocity + dv
        
        proj.pos = proj.pos + proj.velocity*dt
    
    n = len(proj_x) - 1
    listcl.append(cl)
    listcd.append(cd)
    listx.append(proj_x[n])
    listz.append(proj_z[n])
    listv.append(sqrt(pow(proj_xv[n], 2) + pow(proj_zv[n], 2)))
    #cl = cl + 0.01
    cd = cd + 0.01
    i = i + 1
    if i == 1: lt1 = len(time)
    if i == 2: lt2 = len(time)
    if i == 3: lt3 = len(time)
    if i == 4: lt4 = len(time)
    if i == 5: lt5 = len(time)
    if i == 6: lt6 = len(time)
    if i == 7: lt7 = len(time)

for i in range(0, len(listcl)):
    print(listcl[i], listv[i])
    print(listx[i], listv[i]);
    
scene2 = gdisplay(x = 0, y = 0, title = "Trajectory of Ball from Side View", xtitle = "x (m)", ytitle = "z (m)")

f1 = gcurve(color = color.red)
f2 = gcurve(color = color.orange)
f3 = gcurve(color = color.yellow)
f4 = gcurve(color = color.green)
f5 = gcurve(color = color.blue)
f6 = gcurve(color = color.purple)
f7 = gcurve(color = color.black)
for i in range(0, lt1):
    f1.plot(pos=(proj_x[i], proj_z[i]))
for i in range(0, lt2):
    f2.plot(pos=(proj_x[i + lt1], proj_z[i + lt1]))
for i in range(0, lt3):
    f3.plot(pos=(proj_x[i + lt1 + lt2], proj_z[i + lt1 + lt2]))
for i in range(0, lt4):
    f4.plot(pos=(proj_x[i + lt1 + lt2 + lt3], proj_z[i + lt1 + lt2 + lt3]))
for i in range(0, lt5):
    f5.plot(pos=(proj_x[i + lt1 + lt2 + lt3 + lt4], proj_z[i + lt1 + lt2 + lt3 + lt4]))
for i in range(0, lt6):
    f6.plot(pos=(proj_x[i + lt1 + lt2 + lt3 + lt4 + lt5], proj_z[i + lt1 + lt2 + lt3 + lt4 + lt5]))
for i in range(0, lt7):
    f7.plot(pos=(proj_x[i + lt1 + lt2 + lt3 + lt4 + lt5 + lt6], proj_z[i + lt1 + lt2 + lt3 + lt4 + lt5 + lt6]))
    

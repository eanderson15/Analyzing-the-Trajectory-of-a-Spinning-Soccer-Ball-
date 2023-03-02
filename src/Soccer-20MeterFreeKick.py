from vpython import *
#GlowScript 3.0 VPython
# adapted from code
# simulation of projectile motion
# Written for Phy 235
# Frank Wolfs, Univ. of Rochester, September 2017.
# Example problem 2.7
g = 9.81
cd = 0.25
cl = 0.23
p = 1.2
r = 0.11
A = r * r * pi
m = 0.43
a = 62.5 * pi/ 180.0

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
listy = []
listz = []

while (cl < 0.3):
    
    x0 = 0.0
    y0 = 0.0
    z0 = 0.0
    initialPosition = vector(x0, y0, z0)

    v0 = 25.0
    angle0 = 15.0

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

    dt = 0.001
    t = 0.0

    time = []
    proj_x = []
    proj_y = []
    proj_z = []

    while (proj.pos.x <= 20):
        
        kd = (p * A * cd)/(2 * m)
        kl = (p * A * cl)/(2 * m)
    
        rate(1000)
    
        if not run: continue
    
        time.append(t)
        proj_x.append(proj.pos.x)
        proj_y.append(proj.pos.y)
        proj_z.append(proj.pos.z)
    
        t = t + dt
        
        accel_x = -mag(proj.velocity) * (kd * proj.velocity.x + kl * (sin(a) * proj.velocity.z + cos(a) * proj.velocity.z))
        accel_y = -mag(proj.velocity) * (kd * proj.velocity.y - kl * sin(a) * proj.velocity.x)
        accel_z = -g - mag(proj.velocity) * (kd * proj.velocity.z - kl * cos(a) * proj.velocity.x)
        accel_p = vector(accel_x, accel_y, accel_z)
        
        dv = dt * accel_p
        
        proj.velocity = proj.velocity + dv
        
        proj.pos = proj.pos + proj.velocity*dt
    
    scene2 = gdisplay(x = 0, y = 0, title = "Trajectory of Ball from Side View", xtitle = "x (m)", ytitle = "z (m)")
    
    f1 = gcurve(color = color.blue)
    for i in range(0, len(proj_z)):
        f1.plot(pos=(proj_x[i], proj_z[i]))
        
    scene3 = gdisplay(x = 0, y = 0, title = "Trajectory of Ball from Top View", xtitle = "x (m)", ytitle = "y(m)")
    
    f2 = gcurve(color = color.blue)
    for i in range(0, len(proj_y)):
        f2.plot(pos=(proj_x[i], proj_y[i]))
    
    scene4 = gdisplay(x = 0, y = 0, title = "Trajectory of Ball from Kicker View", xtitle = "y (m)", ytitle = "z (m)")
    
    f3 = gcurve(color = color.blue)
    for i in range(0, len(proj_z)):
        f3.plot(pos=(-proj_y[i], proj_z[i]))
    
    n = len(proj_x) - 1
    listcl.append(cl)
    listcd.append(cd)
    listx.append(proj_x[n])
    listz.append(proj_z[n])
    listy.append(proj_y[n])
    cl = cl + 0.01
    cd = cd + 0.01

for i in range(0, len(listcl)):
    print(listcl[i])
    print(listx[i], listy[i], listz[i]);

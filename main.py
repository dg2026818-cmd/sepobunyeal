Web VPython 3.2
t=sphere(color=color.purple, opacity=0.3)
u=sphere(color=color.blue, size=vec(1.5,1.5,1.5),opacity=0.2)
a=box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(-0.3,0.4,0), axis=vec(1,1,0))
b=box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(-0.3,0.4,0), axis=vec(1,-1,0))
c=box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(0.1,0.1,0), axis=vec(1,-1,0))
d=box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(0.1,0.1,0), axis=vec(1,1,0))
e=box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(0.5,-0.1,0), axis=vec(1,1,0))
f=box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(0.5,-0.1,0), axis=vec(1,-1,0))
g=box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(-0.1,-0.5,0), axis=vec(1,1,0))
h=box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(-0.1,-0.5,0), axis=vec(1,-1,0))
m=compound([a,b])
n=compound([c,d])
p=compound([e,f])
q=compound([g,h])


ab=curve(pos=[vec(0,-0.6,0), vec(-0.1, 0, 0)], color=color.white, visible = False)
bc=curve(pos=[vec(0,-0.6,0), vec(0.14, 0, 0)], color=color.white, visible = False)
cd=curve(pos=[vec(0,-0.6,0), vec(-0.3, 0, 0)], color=color.white, visible = False)
df=curve(pos=[vec(0,-0.6,0), vec(0.5, 0, 0)], color=color.white, visible = False)
fg=curve(pos=[vec(0,0.6,0), vec(-0.1, 0, 0)], color=color.white, visible = False)
gh=curve(pos=[vec(0,0.6,0), vec(0.14, 0, 0)], color=color.white, visible = False)
hi=curve(pos=[vec(0,0.6,0), vec(-0.3, 0, 0)], color=color.white, visible = False)
ij=curve(pos=[vec(0,0.6,0), vec(0.5, 0, 0)], color=color.white, visible = False)


while True:
    rate(100)
    k=keysdown()
    if '1'in k:
       m.pos.y=0
       n.pos.y=0
       p.pos.y=0
       q.pos.y=0
       box(color=color.red, size=vec(0.05,0.05,0.05), pos=vec(0.,-0.6,0))
       box(color=color.red, size=vec(0.05,0.05,0.05), pos=vec(0,0.6,0))
    if '2' in k:
       ab.visible = True
       bc.visible = True
       cd.visible = True
       df.visible = True
       fg.visible = True
       gh.visible = True
       hi.visible = True
       ij.visible = True
       u.visible=False
       
    if '3' in k:
       box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(-0.3,0.4,0), axis=vec(1,1,0))
       box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(0.1,0.4,0), axis=vec(1,1,0))
       box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(-0.3,-0.4,0), axis=vec(1,1,0))
       box(color=color.orange, size=vec(0.05,0.3,0.05), pos=vec(0.1,-0.4,0), axis=vec(1,1,0))
       box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(0,0.4,0), axis=vec(1,1,0))
       box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(0.4,0.4,0), axis=vec(1,1,0))
       box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(0,0.4,0), axis=vec(1,1,0))
       box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(-0.1,-0.5,0), axis=vec(1,1,0))
       box(color=color.green, size=vec(0.03,0.2,0.03), pos=vec(0.4,-0.5,0), axis=vec(1,1,0))
       m.visible = False
       n.visible = False
       p.visible = False
       q.visible = False
       aa=curve(pos=[vec(0,-0.6,0), vec(-0.3, -0.4, 0)], color=color.white)
       bb=curve(pos=[vec(0,-0.6,0), vec(0.1, -0.4, 0)], color=color.white)
       cc=curve(pos=[vec(0,-0.6,0), vec(-0.1, -0.5, 0)], color=color.white)
       dd=curve(pos=[vec(0,-0.6,0), vec(0.4, -0.5, 0)], color=color.white)
       ee=curve(pos=[vec(0,0.6,0), vec(0.4, 0.4, 0)], color=color.white)
       ff=curve(pos=[vec(0,0.6,0), vec(0.1, 0.4, 0)], color=color.white)
       gg=curve(pos=[vec(0,0.6,0), vec(0, 0.4, 0)], color=color.white)
       hh=curve(pos=[vec(0,0.6,0), vec(-0.3, 0.4, 0)], color=color.white)
       ab.visible=False
       bc.visible=False
       cd.visible=False
       df.visible=False
       fg.visible=False
       gh.visible=False
       hi.visible=False
       ij.visible=False
    
    if '4' in k:
          sphere(color=color.purple, opacity=0.3, size=vec(1, 1, 1), pos=vec(1,0,0))
          sphere(color=color.purple, opacity=0.3, size=vec(1, 1, 1), pos=vec(-1,0,0))
          z=compound([t,u,aa,bb,cc,dd,ee,ff,gg,hh])
          z.visible=False
           
       
       
     
       

from evaluator import *
import math
vx=[]
vy=[]
m =[]
rx=[]
ry=[]
def new_move():
   global vx
   global vy
   global m
   global rx
   global ry
   inp=get_data()
   t=inp[1]
   g=inp[0]
   if m==[]:
        for item in inp[2:]:
         vx.append(item[3])
         vy.append(item[4])
         m.append(item[0])
         rx.append(item[1])
         ry.append(item[2])

   dx = [i * t for i in vx]
   dy = [a * t for a in vy]
   i = 0
   dr = []
   while i < (len(dx)):
       dr.append([dx[i],dy[i]])
       i += 1

   for a in range(len(rx)):
        rx[a]=rx[a]+dx[a]
        ry[a]=ry[a]+dy[a]

   for i in range(len(m)):
      crx = rx[i]
      cry = ry[i]
      new_m = m[:i] + m[i + 1:]
      new_rx = rx[:i] + rx[i + 1:]
      new_ry = ry[:i] + ry[i + 1:]
      ax = 0
      ay = 0
      for a in range(len(new_rx)):
         cos=float((new_rx[a]-crx))/float(math.sqrt(float(float((new_rx[a]-crx))**2)+float(float((new_ry[a]-cry))**2)))
         ax += float((g*new_m[a]*cos))/float((float((new_rx[a]-crx))**2)+(float((new_ry[a]-cry))**2))
      vx[i] = vx[i] + (ax * t)
      for b in range(len(new_ry)):
         sin=float((new_ry[b]-cry))/float(math.sqrt(float((new_rx[b]-crx))**2+float((new_ry[b]-cry))**2))
         ay += float((g*new_m[b]*sin))/float((float((new_rx[b]-crx))**2+float((new_ry[b]-cry)**2)))
      vy[i] = vy[i] + (ay * t)

   return dr
   



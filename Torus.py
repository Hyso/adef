from myobject import myobject
from numpy import sin, cos, pi, mgrid, zeros_like, ones_like

class Torus(myobject):
	def __init__(self,rx,ry,rz):
		myobject.__init__(self)
                #############################################################################
                #parameter fuer die flaeche
## 		u, v = mgrid[-pi:mypi:0.01, -pi:mypi:0.01]
## 		r1, r2 = 1, 0.3
		r1, r2 = 1, 0.3
		self.u_f, self.v_f = mgrid[0:2*pi:180j,0:2*pi:180j]
                #alle funktionen fuer die flaeche
		self.x = lambda u,v: rx*(r1+r2*cos(u))*sin(v)
		self.y = lambda u,v: ry*(r1+r2*cos(u))*cos(v)
		self.z = lambda u,v: rz*r2*sin(u)
		#############################################################################
                #zeros_like = einfach die arraywerte in 0 umschreiben.
                #ones_like = einfach die arraywerte in 1 umschreiben.
                #dxu,dxv sind die Werte der ersten Patielenableitung
                self.dxu = lambda u,v: rx*r2*(-sin(u))*sin(v)
                self.dxv = lambda u,v: rx*(r1+r2*cos(u))*cos(v)
                
                self.dyu = lambda u,v: ry*r2*(-sin(u))*cos(v)
                self.dyv = lambda u,v: ry*(r1+r2*cos(u))*(-sin(v))
                
                self.dzu = lambda u,v: rz*r2*cos(u)
                self.dzv = lambda u,v: zeros_like(v)
                
                self.dxuu = lambda u,v: rx*r2*(-cos(u))*sin(v)
                self.dxvu = lambda u,v: rx*r2*(-sin(u))*cos(v)
                self.dxuv = lambda u,v: rx*r2*(-sin(u))*cos(v)
                self.dxvv = lambda u,v: rx*(r1+r2*cos(u))*(-sin(v))
                
                self.dyuu = lambda u,v: ry*r2*(-cos(u))*cos(v)
                self.dyvu = lambda u,v: ry*r2*(-sin(u))*(-sin(v))
                self.dyuv = lambda u,v: ry*r2*(-sin(u))*(-sin(v))
                self.dyvv = lambda u,v: ry*(r1+r2*cos(u))*(-cos(v))
                
                self.dzuu = lambda u,v: rz*r2*(-sin(u))
                self.dzvu = lambda u,v: zeros_like(v)
                self.dzuv = lambda u,v: zeros_like(v)
                self.dzvv = lambda u,v: zeros_like(v)
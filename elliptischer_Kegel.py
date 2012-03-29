from myobject import myobject
from numpy import sin, cos, pi, mgrid, zeros_like, ones_like

class elliptischer_Kegel(myobject):
	def __init__(self,rx,ry,rz):
		myobject.__init__(self)
                #############################################################################
                #parameter fuer die flaeche
##                 self.u, self.v = mgrid[-pi:pi:180j,0:1:180j]
		self.u_f, self.v_f = mgrid[0:2*pi:180j,0:1:180j]
                #alle funktionen fuer die flaeche
		self.x = lambda u,v: rx*cos(u)*v
		self.y = lambda u,v: ry*sin(u)*v
		self.z = lambda u,v: rz*v
                #zeros_like = einfach die arraywerte in 0 umschreiben.
                #ones_like = einfach die arraywerte in 1 umschreiben.
                #dxu,dxv sind die Werte der ersten Patielenableitung
                self.dxu = lambda u,v: rx*(-sin(u))*v
                self.dxv = lambda u,v: rx*cos(u)
                
                self.dyu = lambda u,v: ry*cos(u)*v
                self.dyv = lambda u,v: ry*sin(u)
                
                self.dzu = lambda u,v: zeros_like(u)
                self.dzv = lambda u,v: rz*ones_like(v)
                
                self.dxuu = lambda u,v: rx*(-cos(u))*v
                self.dxvu = lambda u,v: rx*(-sin(u))
                self.dxuv = lambda u,v: rx*(-sin(u))
                self.dxvv = lambda u,v: zeros_like(v)
                
                self.dyuu = lambda u,v: ry*(-sin(u))*v
                self.dyvu = lambda u,v: ry*cos(u)
                self.dyuv = lambda u,v: ry*cos(u)
                self.dyvv = lambda u,v: zeros_like(v)
                
                self.dzuu = lambda u,v: zeros_like(u)
                self.dzvu = lambda u,v: zeros_like(u)
                self.dzuv = lambda u,v: zeros_like(v)
                self.dzvv = lambda u,v: zeros_like(v)
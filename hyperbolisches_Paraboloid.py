from myobject import myobject
from numpy import sin, cos, pi, mgrid, zeros_like, ones_like

class hyperbolisches_Paraboloid(myobject):
	def __init__(self,rx,ry,rz):
		myobject.__init__(self)
                #############################################################################
                #parameter fuer die flaeche
## 		self.u, self.v = mgrid[0:2*pi:180j,0:2*pi:180j]
## 		self.u, self.v = mgrid[-pi:pi:180j,-pi:pi:180j]
		self.u_f, self.v_f = mgrid[-1:1:180j,-1:1:180j]
                #alle funktionen fuer die flaeche
		self.x = lambda u,v: rx*u
		self.y = lambda u,v: ry*v
		self.z = lambda u,v: rz*(u**2-v**2)
		#############################################################################
                #zeros_like = einfach die arraywerte in 0 umschreiben.
                #ones_like = einfach die arraywerte in 1 umschreiben.
                #dxu,dxv sind die Werte der ersten Patielenableitung
                self.dxu = lambda u,v: rx*ones_like(u)
                self.dxv = lambda u,v: zeros_like(v)
                
                self.dyu = lambda u,v: zeros_like(u)
                self.dyv = lambda u,v: ry*ones_like(v)
                
                self.dzu = lambda u,v: rz*2*u
                self.dzv = lambda u,v: rz*(-2)*v
                
                self.dxuu = lambda u,v: zeros_like(u)
                self.dxvu = lambda u,v: zeros_like(u)
                self.dxuv = lambda u,v: zeros_like(v)
                self.dxvv = lambda u,v: zeros_like(v)
                
                self.dyuu = lambda u,v: zeros_like(u)
                self.dyvu = lambda u,v: zeros_like(u)
                self.dyuv = lambda u,v: zeros_like(v)
                self.dyvv = lambda u,v: zeros_like(v)
                
                self.dzuu = lambda u,v: rz*2
                self.dzvu = lambda u,v: zeros_like(u)
                self.dzuv = lambda u,v: zeros_like(v)
                self.dzvv = lambda u,v: rz*(-2)
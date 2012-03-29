from myobject import myobject
from numpy import sin, cos, sinh, cosh, pi, mgrid, zeros_like, ones_like

class hyperbolischer_Zylinder(myobject):
	def __init__(self,rx,ry,rz):
		myobject.__init__(self)
                #############################################################################
                #parameter fuer die flaeche
		self.u_f, self.v_f = mgrid[-pi:pi:180j,0:1:180j]
                #alle funktionen fuer die flaeche
		self.x = lambda u,v: rx*cosh(u)
		self.y = lambda u,v: ry*sinh(u)
		self.z = lambda u,v: rz*v
		#############################################################################
                #zeros_like = einfach die arraywerte in 0 umschreiben.
                #ones_like = einfach die arraywerte in 1 umschreiben.
                #dxu,dxv sind die Werte der ersten Patielenableitung
                self.dxu = lambda u,v: rx*sinh(u)
                self.dxv = lambda u,v: zeros_like(v)
                
                self.dyu = lambda u,v: ry*cosh(u)
                self.dyv = lambda u,v: zeros_like(v)
                
                self.dzu = lambda u,v: zeros_like(u)
                self.dzv = lambda u,v: rz*ones_like(v)
                
                self.dxuu = lambda u,v: rx*cosh(u)
                self.dxvu = lambda u,v: zeros_like(u)
                self.dxuv = lambda u,v: zeros_like(v)
                self.dxvv = lambda u,v: zeros_like(v)
                
                self.dyuu = lambda u,v: ry*sinh(u)
                self.dyvu = lambda u,v: zeros_like(u)
                self.dyuv = lambda u,v: zeros_like(v)
                self.dyvv = lambda u,v: zeros_like(v)
                
                self.dzuu = lambda u,v: zeros_like(u)
                self.dzvu = lambda u,v: zeros_like(u)
                self.dzuv = lambda u,v: zeros_like(v)
                self.dzvv = lambda u,v: zeros_like(v)

from myobject import myobject
from numpy import sin, cos, sinh, cosh, pi, mgrid, zeros_like, ones_like

class einschaliges_Hyperboloid(myobject):
	def __init__(self,rx,ry,rz):
		myobject.__init__(self)
                #############################################################################
                #parameter fuer die flaeche
##                 u, v = mgrid[-pi:mypi:0.01, -1:1:0.01]
		self.u_f, self.v_f = mgrid[0:2*pi:180j,-1:1:180j]
                #alle funktionen fuer die flaeche
		self.x = lambda u,v: rx*cos(u)*cosh(v)
		self.y = lambda u,v: ry*sin(u)*cosh(v)
		self.z = lambda u,v: rz*sinh(v)
		#############################################################################
                #zeros_like = einfach die arraywerte in 0 umschreiben.
                #ones_like = einfach die arraywerte in 1 umschreiben.
                #dxu,dxv sind die Werte der ersten Patielenableitung
                self.dxu = lambda u,v: rx*(-sin(u))*cosh(v)
                self.dxv = lambda u,v: rx*cos(u)*sinh(v)
                
                self.dyu = lambda u,v: ry*cos(u)*cosh(v)
                self.dyv = lambda u,v: ry*sin(u)*sinh(v)
                
                self.dzu = lambda u,v: zeros_like(u)
                self.dzv = lambda u,v: rz*cosh(v)
                
                self.dxuu = lambda u,v: rx*(-cos(u))*cosh(v)
                self.dxvu = lambda u,v: rx*(-sin(u))*sinh(v)
                self.dxuv = lambda u,v: rx*(-sin(u))*sinh(v)
                self.dxvv = lambda u,v: rx*cos(u)*cosh(v)
                
                self.dyuu = lambda u,v: ry*(-sin(u))*cosh(v)
                self.dyvu = lambda u,v: ry*cos(u)*sinh(v)
                self.dyuv = lambda u,v: ry*cos(u)*sinh(v)
                self.dyvv = lambda u,v: ry*sin(u)*cosh(v)
                
                self.dzuu = lambda u,v: zeros_like(u)
                self.dzvu = lambda u,v: zeros_like(u)
                self.dzuv = lambda u,v: zeros_like(v)
                self.dzvv = lambda u,v: rz*sinh(v)
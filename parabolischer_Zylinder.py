from myobject import myobject
from numpy import sin, cos, pi, mgrid, zeros_like, ones_like

class parabolischer_Zylinder(myobject):
	def __init__(self,rx,ry,rz):
		myobject.__init__(self)
                #############################################################################
                #parameter fuer die flaeche
		self.u_f, self.v_f = mgrid[-1:1:180j,-1:1:180j]
                #alle funktionen fuer die flaeche
		self.x = lambda u,v: rx*u
		self.y = lambda u,v: ry*u**2
		self.z = lambda u,v: rz*v
		#############################################################################
                #x,y,z sind die Koordinaten im dreidimensionalem euklidischen Raum
                #TODO: ueberlegung, ob ich die brauche oder x_f,y_f,z_f reichen
##                 self.x = lambda u,v: rx*cos(u)*sin(v)
##                 self.y = lambda u,v: ry*sin(u)*sin(v)
##                 self.z = lambda u,v: rz*cos(v)
                #ones_like = einfach die arraywerte in 1 umschreiben.
                #dxu,dxv sind die Werte der ersten Patielenableitung
                self.dxu = lambda u,v: rx*ones_like(u)
                #zeros_like = einfach die arraywerte in 0 umschreiben.
                self.dxv = lambda u,v: zeros_like(v)
                self.dyu = lambda u,v: ry*2*u
                self.dyv = lambda u,v: zeros_like(v)
                self.dzu = lambda u,v: zeros_like(u)
                self.dzv = lambda u,v: rz*ones_like(v)
                self.dxuu = lambda u,v: zeros_like(u)
                self.dxvu = lambda u,v: zeros_like(u)
                self.dxuv = lambda u,v: zeros_like(v)
                self.dxvv = lambda u,v: zeros_like(v)
                
                self.dyuu = lambda u,v: ry*2
                self.dyvu = lambda u,v: zeros_like(u)
                self.dyuv = lambda u,v: zeros_like(v)
                self.dyvv = lambda u,v: zeros_like(v)
                self.dzuu = lambda u,v: zeros_like(u)
                self.dzvu = lambda u,v: zeros_like(u)
                self.dzuv = lambda u,v: zeros_like(v)
                self.dzvv = lambda u,v: zeros_like(v)
from myobject import myobject
from numpy import sin, cos, pi, mgrid, zeros_like, ones_like

class elliptischer_Zylinder(myobject):
	def __init__(self,rx,ry,rz):
		myobject.__init__(self)
                #############################################################################
                #parameter fuer die flaeche
		self.u_f, self.v_f = mgrid[0:2*pi:180j,-1:1:180j]
                #alle funktionen fuer die flaeche
		self.x = lambda u,v: rx*cos(u)
		self.y = lambda u,v: ry*sin(u)
		self.z = lambda u,v: rz*v
## 		self.x_f_werte = x_f(myobj.u_f,myobj.v_f)
## 		self.y_f_werte = y_f(myobj.u_f,myobj.v_f)
## 		self.z_f_werte = z_f(self.u_f,myobj.v_f)
		#############################################################################
##                 #alle funktionen fuer die kurve und die dazugehoerigen funktionen
##                 self.u = lambda t,tckp : splev(t,tckp,0)[0]
##                 self.v = lambda t,tckp : splev(t,tckp,0)[1]
##                 #du,dv sind die ersten Ableitungen der Flaechenparameter.
##                 self.du = lambda t,tckp : splev(t,tckp,1)[0]
## 		self.dv = lambda t,tckp : splev(t,tckp,1)[1]
                #x,y,z sind die Koordinaten im dreidimensionalem euklidischen Raum
                #TODO: ueberlegung, ob ich die brauche oder x_f,y_f,z_f reichen
##                 self.x = lambda u,v: rx*cos(u)*sin(v)
##                 self.y = lambda u,v: ry*sin(u)*sin(v)
##                 self.z = lambda u,v: rz*cos(v)
                #ones_like = einfach die arraywerte in 1 umschreiben.
                #dxu,dxv sind die Werte der ersten Patielenableitung
                self.dxu = lambda u,v: rx*(-sin(u))
                #zeros_like = einfach die arraywerte in 0 umschreiben.
                self.dxv = lambda u,v: zeros_like(v)
                self.dyu = lambda u,v: ry*cos(u)
                self.dyv = lambda u,v: zeros_like(v)
                self.dzu = lambda u,v: zeros_like(u)
                self.dzv = lambda u,v: rz*ones_like(v)
                self.dxuu = lambda u,v: rx*(-cos(u))
                self.dxvu = lambda u,v: zeros_like(u)
                self.dxuv = lambda u,v: zeros_like(v)
                self.dxvv = lambda u,v: zeros_like(v)
                
                self.dyuu = lambda u,v: ry*(-sin(u))
                self.dyvu = lambda u,v: zeros_like(u)
                self.dyuv = lambda u,v: zeros_like(v)
                self.dyvv = lambda u,v: zeros_like(v)
                self.dzuu = lambda u,v: zeros_like(u)
                self.dzvu = lambda u,v: zeros_like(u)
                self.dzuv = lambda u,v: zeros_like(v)
                self.dzvv = lambda u,v: zeros_like(v)
                
##                 self.duu = lambda t,tckp : splev(t,tckp,2)[0]
##                 self.duv = lambda t,tckp : zeros_like(duu(t,tckp))
##                 self.dvu = lambda t,tckp : zeros_like(dvv(t,tckp))
##                 self.dvv = lambda t,tckp : splev(t,tckp,2)[1]

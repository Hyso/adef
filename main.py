################################################################################
# Create a set of points, with given density
#zweite zeile brauche ich damit ich lib beim picker aufrufen kann als np.lib
import numpy as np
from numpy import *
from enthought.mayavi import mlab
from scipy.interpolate import splprep, splev
from extentDialog import ExtentDialog
from myutil import ebene, punkt
from calculation import * #K,dKt,dKtt,normalisiere,kreuzprodukt
from myobject import myobject

myobj = myobject()

## myobj.fig = mlab.figure(1,bgcolor=(1,1,1))
## mlab.clf()
## myobj.index_u = array([0,0,0,0])
## myobj.index_v = array([0,0,0,0])
## myobj.global_i = 0

## myobj.u_f, myobj.v_f = mgrid[0:pi:180j,0:2*pi:180j]

#brauche ich um den picker zu benutzen
## myobj.x_f_werte = x_f(myobj.u_f,myobj.v_f)
## myobj.y_f_werte = y_f(myobj.u_f,myobj.v_f)
## myobj.z_f_werte = z_f(myobj.u_f,myobj.v_f)

# A first plot in 3D
## myobj.fig = mlab.figure(1,bgcolor=(1,1,1))
## mlab.clf()
#Das ist die gekruemmte Flaeche.
## myobj.mesh = mlab.mesh(myobj.x_f_werte,myobj.y_f_werte,myobj.z_f_werte,color=(0.6,0.6,0.6))
#aenderung mode='axes' zu mode='point' oder 'sphere'
## cursor3d = mlab.points3d(0., 0., 0., mode='sphere',
##                                 color=(0, 0, 0),
##                                 scale_factor=0.03)

#Methode die, die Kurve und Tangente berechnet und anzeigt.
## def my_test_plod3d():
##     """Generates a pretty set of lines."""
#parameterwerte der selektierten punkte ueber ihre indizes
#parameter von 0-pi und 0-2pi
## u_f4 = [u_f[69][36], u_f[73][32], u_f[81][36], u_f[92][32]]
## v_f4 = [v_f[69][36], v_f[73][32], v_f[81][36], v_f[92][32]]
#TODO: kurz auskommentiert
#ist nur statisch, bauch ich nicht
## u_f4 = [myobj.u_f[67][106], myobj.u_f[80][109], myobj.u_f[96][107], myobj.u_f[106][111]]
## v_f4 = [myobj.v_f[67][106], myobj.v_f[80][109], myobj.v_f[96][107], myobj.v_f[106][111]]
#
#koordinaten der punkte
#punkte von 0-pi und 0-2pi
## x_p = array([0.33560251, 0.25743358, 0.14167357, -0.03954295])
## y_p = array([0.8921692, 0.86397454, 0.94261526, 0.90064444])
## z_p = array([0.30233271, 0.43275392, 0.30233271, 0.43275392])
#ist nur statisch brauch ich nicht
## myobj.x_p = array([-0.21056481, -0.10493242, 0.0656097, 0.19562368])
## myobj.y_p = array([-0.50521065, -0.62350292, -0.57262213, -0.65653392])
## myobj.z_p = array([-0.83691377, -0.77474725, -0.81718986, -0.72848787])
#
## myobj.kurvenpunkte_4 = mlab.points3d(myobj.x_p, myobj.y_p, myobj.z_p, mode='sphere',color=(0, 0, 0),scale_factor=0.02)
# s und k koennen auch statisch sein, weil die kurve immer mit den werden berechnet wird
## s=3.0
## k=3
#tckp: beinhaltet die Knotenpunkte, Koeffizienten und den Grad der 
#interpolierten Splinekurve.
#nix: enthaelt den rest was nicht gebraucht wird.
## tckp, nix = splprep([u_f4,v_f4],s=s,k=k,nest=-1)

## def kurve_berechnen(u_werte, v_werte, grad, glaettung):
## 	print 'test'
## 	tckp, nix = splprep([u_werte,v_werte],k=grad, s=glaettung, nest=-1)
## 	print 'Kurve wurde berechnet'
## 	return tckp

#TODO: u_f4 aendern in index_u
## tckp = kurve_berechnen(myobj.index_u,myobj.index_v,3,3)
## myobj.tckp = kurve_berechnen(u_f4,v_f4,3,3)
#r_ = arange
#t ist der Kurvenparameter, selbst bei 300 punkten ist die aenderung der haupnormalen grad mal zu sehen.
## myobj.t = r_[0:1:101j]
#Fuer einfache Funktionen, kann die lambda-Funktion benutz werden, dadurch
#muss die Funktion nicht erst definiert werden.
#Der Funktionswert wird bei der lambda-Funktion sofort zurueckgeliefert.
#u,v sind die Flaechenparameter

## dKtt = lambda t: (array((dxuu(u(t),v(t)),dyuu(u(t),v(t)),dzuu(u(t),v(t))))*du(t)
## 		+array((dxu(u(t),v(t)),dyu(u(t),v(t)),dzu(u(t),v(t))))*duu(t)
## 		+array((dxvu(u(t),v(t)),dyvu(u(t),v(t)),dzvu(u(t),v(t))))*dv(t)
## 		+array((dxv(u(t),v(t)),dyv(u(t),v(t)),dzv(u(t),v(t))))*dvu(t)
## 		+array((dxuv(u(t),v(t)),dyuv(u(t),v(t)),dzuv(u(t),v(t))))*du(t)
## 		+array((dxu(u(t),v(t)),dyu(u(t),v(t)),dzu(u(t),v(t))))*duv(t)
## 		+array((dxvv(u(t),v(t)),dyvv(u(t),v(t)),dzvv(u(t),v(t))))*dv(t)
## 		+array((dxv(u(t),v(t)),dyv(u(t),v(t)),dzv(u(t),v(t))))*dvv(t))
#xnew,ynew,znew representieren die x,y,z Koordinaten der Kurve
## myobj.xnew, myobj.ynew, myobj.znew = K(myobj.t,myobj.tckp)
#TODO: ueberpruefen ob das von noeten ist.
## xyz = sqrt(xnew**2+ynew**2+znew**2)
## xnew_n, ynew_n, znew_n = xnew/xyz, ynew/xyz, znew/xyz
#a,b,c sind die Koeffizienten fuer die Tangentenvektoren
## a, b, c = dKt(myobj.t,myobj.tckp)
## myobj.a_n, myobj.b_n, myobj.c_n = normalisiere(a,b,c)
#Zeichnet die Kurve nach den Punkten.
## myobj.kurve = mlab.plot3d(myobj.xnew, myobj.ynew, myobj.znew, tube_radius=0.005, color=(1,1,1))
#damit dann ich sichtbar und unsichtbar machen.

#Das ist der Vektor der zweiten Ableitung der Splinekurve.
#Dieser Vektor liegt ebenfalls in der Tangentialebene.
## d,e,f = dKtt(myobj.t,myobj.tckp)
## deff = sqrt(d**2+e**2+f**2)
## d_n, e_n, f_n = d/deff, e/deff, f/deff
## myobj.d_n, myobj.e_n, myobj.f_n = normalisiere(d,e,f)

#Das ist der Binormalenvektor(blau).
## g,h,i = kreuzprodukt(a,b,c,d,e,f)
## g,h,i = kreuzprodukt(myobj.a_n,myobj.b_n,myobj.c_n,myobj.d_n,myobj.e_n,myobj.f_n)
## ghi = sqrt(g**2+h**2+i**2)
## g_n,h_n,i_n = g/ghi, h/ghi, i/ghi
## myobj.g_n,myobj.h_n,myobj.i_n = normalisiere(g,h,i)
## g,h,i = kreuzprodukt(d,e,f,a,b,c)
##     mlab.quiver3d(xnew, ynew, znew, d, e, f, scale_factor='0.001')
##     mlab.quiver3d(xnew, ynew, znew, g, h, i, scale_factor='0.001')
#Das ist der Hauptnormalenvektor(gruen).
## j,k,l = kreuzprodukt(a,b,c,g,h,i)
## j,k,l = kreuzprodukt(g,h,i,a,b,c)
## j,k,l = kreuzprodukt(myobj.g_n,myobj.h_n,myobj.i_n,myobj.a_n,myobj.b_n,myobj.c_n)
## j,k,l = kreuzprodukt(a_n,b_n,c_n,g_n,h_n,i_n)
## jkl = sqrt(j**2+k**2+l**2)
## j_n,k_n,l_n = j/jkl, k/jkl, l/jkl
## myobj.j_n,myobj.k_n,myobj.l_n = normalisiere(j, k, l)
## #
## #t: h+b,h-b,-h-b,-h+b,h+b
## #
## scale_factor=1,scale_mode='scalar',
## #Zeichnet die Tangenten(rot) an die Kurve.
## myobj.tangente = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.a_n[0], myobj.b_n[0], myobj.c_n[0], color=(1,0,0))
## myobj.ableitung2 = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.d_n[0], myobj.e_n[0], myobj.f_n[0], color=(1,1,0))
## myobj.hauptnormale = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.j_n[0], myobj.k_n[0], myobj.l_n[0], color=(0,1,0))
## myobj.binormale = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.g_n[0], myobj.h_n[0], myobj.i_n[0], color=(0,0,1))
## def dreibein(ii):
##     tangente.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=a_n[ii], v=b_n[ii], w=c_n[ii])
##     ableitung2.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=d_n[ii], v=e_n[ii], w=f_n[ii])
##     hauptnormale.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=j_n[ii], v=k_n[ii], w=l_n[ii])
##     binormale.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=g_n[ii], v=h_n[ii], w=i_n[ii])
##     tangente_fu.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=u1_n[ii], v=u2_n[ii], w=u3_n[ii])
##     tangente_fv.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=v1_n[ii], v=v2_n[ii], w=v3_n[ii])
##     normale_f.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=uv1_n[ii], v=uv2_n[ii], w=uv3_n[ii])

#erhalte ich die daten zur tangente
## tangente.mlab_source.get()
#setze die tangentendaten neu
## tangente.mlab_source.set(x=xnew[99], y=ynew[99],z=znew[99],u=a[99], v=b[99], w=c[99])
#


## myobj.normalebene = ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.j_n,myobj.k_n,myobj.l_n,myobj.g_n,myobj.h_n,myobj.i_n,(1,0,0),0)
## myobj.schmiegebene = ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.a_n,myobj.b_n,myobj.c_n,myobj.j_n,myobj.k_n,myobj.l_n,(0,0,1),0)
## myobj.rektifizierendeebene = ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.a_n,myobj.b_n,myobj.c_n,myobj.g_n,myobj.h_n,myobj.i_n,(0,1,0),0)
#eckpunkte der normalebene
## px1n,py1n,pz1n = [j_n+g_n+xnew,xnew],[k_n+h_n+ynew,ynew],[l_n+i_n+znew,znew]
## px2n,py2n,pz2n = [j_n-g_n+xnew,xnew],[k_n-h_n+ynew,ynew],[l_n-i_n+znew,znew]
## px3n,py3n,pz3n = [-j_n-g_n+xnew,xnew],[-k_n-h_n+ynew,ynew],[-l_n-i_n+znew,znew]
## px4n,py4n,pz4n = [-j_n+g_n+xnew,xnew],[-k_n+h_n+ynew,ynew],[-l_n+i_n+znew,znew]
## obj.epxn = array([px1n,px2n,px3n,px4n,px1n])
## obj.epyn = array([py1n,py2n,py3n,py4n,py1n])
## obj.epzn = array([pz1n,pz2n,pz3n,pz4n,pz1n])
## myobj.epxn,myobj.epyn,myobj.epzn = eckpunkte_ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.j_n,myobj.k_n,myobj.l_n,myobj.g_n,myobj.h_n,myobj.i_n)
#eckpunkte der schmiegebene
## px1s,py1s,pz1s = [a_n+j_n+xnew,xnew],[b_n+k_n+ynew,ynew],[c_n+l_n+znew,znew]
## px2s,py2s,pz2s = [a_n-j_n+xnew,xnew],[b_n-k_n+ynew,ynew],[c_n-l_n+znew,znew]
## px3s,py3s,pz3s = [-a_n-j_n+xnew,xnew],[-b_n-k_n+ynew,ynew],[-c_n-l_n+znew,znew]
## px4s,py4s,pz4s = [-a_n+j_n+xnew,xnew],[-b_n+k_n+ynew,ynew],[-c_n+l_n+znew,znew]
## obj.epxs = array([px1s,px2s,px3s,px4s,px1s])
## obj.epys = array([py1s,py2s,py3s,py4s,py1s])
## obj.epzs = array([pz1s,pz2s,pz3s,pz4s,pz1s])
## myobj.epxs,myobj.epys,myobj.epzs = eckpunkte_ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.a_n,myobj.b_n,myobj.c_n,myobj.j_n,myobj.k_n,myobj.l_n)
#eckpunkte der rektifizierendeebene
## px1r,py1r,pz1r = [a_n+g_n+xnew,xnew],[b_n+h_n+ynew,ynew],[c_n+i_n+znew,znew]
## px2r,py2r,pz2r = [a_n-g_n+xnew,xnew],[b_n-h_n+ynew,ynew],[c_n-i_n+znew,znew]
## px3r,py3r,pz3r = [-a_n-g_n+xnew,xnew],[-b_n-h_n+ynew,ynew],[-c_n-i_n+znew,znew]
## px4r,py4r,pz4r = [-a_n+g_n+xnew,xnew],[-b_n+h_n+ynew,ynew],[-c_n+i_n+znew,znew]
## obj.epxr = array([px1r,px2r,px3r,px4r,px1r])
## obj.epyr = array([py1r,py2r,py3r,py4r,py1r])
## obj.epzr = array([pz1r,pz2r,pz3r,pz4r,pz1r])
## myobj.epxr,myobj.epyr,myobj.epzr = eckpunkte_ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.a_n,myobj.b_n,myobj.c_n,myobj.g_n,myobj.h_n,myobj.i_n)
#fuer jeden einzelnen kurvenpunkt im vorraus berechnet, dann wie beim dreibein gemacht.
## def ebene_bewegen(ii):
##     #pxn[...,0] = pxn[:,:,0] = pxn.T[0].T
##     normalebene.mlab_source.set(x=pxn[...,ii],y=pyn[...,ii],z=pzn[...,ii])
##     schmiegebene.mlab_source.set(x=pxs[...,ii],y=pys[...,ii],z=pzs[...,ii])
##     rektifizierendeebene.mlab_source.set(x=pxr[...,ii],y=pyr[...,ii],z=pzr[...,ii])
##     tangentialebene_f.mlab_source.set(x=pxt[...,ii],y=pyt[...,ii],z=pzt[...,ii])
#

#Tangente an die Isoparameterlinier in Abhaengigkeit von dem Flaechenparameter u
## myobj.u1,myobj.u2,myobj.u3 = dKu(myobj.t,myobj.tckp)
## u123 = sqrt(u1**2+u2**2+u3**2)
## myobj.u1_n,myobj.u2_n,myobj.u3_n = u1/u123, u2/u123, u3/u123
## myobj.u1_n,myobj.u2_n,myobj.u3_n = normalisiere(myobj.u1,myobj.u2,myobj.u3)
#Tangente an die Isoparameterlinier in Abhaengigkeit von dem Flaechenparameter v
## myobj.v1,myobj.v2,myobj.v3 = dKv(myobj.t,myobj.tckp)
## v123 = sqrt(v1**2+v2**2+v3**2)
## v1_n,v2_n,v3_n = v1/v123, v2/v123, v3/v123
## myobj.v1_n,myobj.v2_n,myobj.v3_n = normalisiere(myobj.v1,myobj.v2,myobj.v3)
#Normalenvektor zur Flaeche.
## myobj.uv1,myobj.uv2,myobj.uv3 = kreuzprodukt(myobj.u1,myobj.u2,myobj.u3,myobj.v1,myobj.v2,myobj.v3)
## uv123 = sqrt(uv1**2+uv2**2+uv3**2)
#Normaleneinheitsvektor zur Flaeche.
#Damit der Normaleneinheitsvektor immer von der Flaeche weg zeigt, muss ich wohl den Absulut Wert von den Tangentenvektoren u,v nehmen.
## uv1_n,uv2_n,uv3_n = uv1/uv123, uv2/uv123, uv3/uv123
## myobj.uv1_n,myobj.uv2_n,myobj.uv3_n = normalisiere(myobj.uv1,myobj.uv2,myobj.uv3)
## myobj.tangente_fu = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.u1_n[0], myobj.u2_n[0], myobj.u3_n[0], color=(1,0,1))
## myobj.tangente_fv = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.v1_n[0], myobj.v2_n[0], myobj.v3_n[0], color=(1,0,1))
## myobj.normale_f = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.uv1_n[0], myobj.uv2_n[0], myobj.uv3_n[0], color=(0.5,0.5,0.5))
#Berechnung der Eckpunkte der Tangentialebene der Flaeche.
## px1t,py1t,pz1t = [u1_n+v1_n+xnew,xnew],[u2_n+v2_n+ynew,ynew],[u3_n+v3_n+znew,znew]
## px2t,py2t,pz2t = [u1_n-v1_n+xnew,xnew],[u2_n-v2_n+ynew,ynew],[u3_n-v3_n+znew,znew]
## px3t,py3t,pz3t = [-u1_n-v1_n+xnew,xnew],[-u2_n-v2_n+ynew,ynew],[-u3_n-v3_n+znew,znew]
## px4t,py4t,pz4t = [-u1_n+v1_n+xnew,xnew],[-u2_n+v2_n+ynew,ynew],[-u3_n+v3_n+znew,znew]
## obj.epxt = array([px1t,px2t,px3t,px4t,px1t])
## obj.epyt = array([py1t,py2t,py3t,py4t,py1t])
## obj.epzt = array([pz1t,pz2t,pz3t,pz4t,pz1t])
## myobj.epxt,myobj.epyt,myobj.epzt = eckpunkte_ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.u1_n,myobj.u2_n,myobj.u3_n,myobj.v1_n,myobj.v2_n,myobj.v3_n)
## myobj.tangentialebene_f = ebene(myobj.xnew,myobj.ynew,myobj.znew,myobj.u1_n,myobj.u2_n,myobj.u3_n,myobj.v1_n,myobj.v2_n,myobj.v3_n,(1,1,1),0)
#--------neu
#Fundamentalgroessen der zweiten Fundamentalform
## myobj.n = array([myobj.uv1_n,myobj.uv2_n,myobj.uv3_n])

## myobj.A = A_n(myobj.t,myobj.tckp) * myobj.n
## myobj.B1 = B1_n(myobj.t,myobj.tckp) * myobj.n
## myobj.B2 = B2_n(myobj.t,myobj.tckp) * myobj.n
## myobj.C = C_n(myobj.t,myobj.tckp) * myobj.n

## Gf = lambda t: array((dxu(u(t),v(t)),dyu(u(t),v(t)),dzu(u(t),v(t))))
## Hf1 = lambda t: array((dxu(u(t),v(t)),dyu(u(t),v(t)),dzu(u(t),v(t))))
## Hf2 = lambda t: array((dxv(u(t),v(t)),dyv(u(t),v(t)),dzv(u(t),v(t))))
## If = lambda t: array((dxv(u(t),v(t)),dyv(u(t),v(t)),dzv(u(t),v(t))))
#Betrag der Fundamentalgroessen
## A_B = sqrt(A[0]**2+A[1]**2+A[2]**2)
## B1_B = sqrt(B1[0]**2+B1[1]**2+B1[2]**2)
## B2_B = sqrt(B2[0]**2+B2[1]**2+B2[2]**2)
## C_B = sqrt(C[0]**2+C[1]**2+C[2]**2)
## myobj.G = Gf(myobj.t,myobj.tckp)
## myobj.H = Hf(myobj.t,myobj.tckp)
## myobj.I = If(myobj.t,myobj.tckp)
## G_werte = Gf(t)
## H1_werte = Hf1(t)
## H2_werte = Hf2(t)
## I_werte = If(t)
## G_B = sqrt(G_werte[0]**2+G_werte[1]**2+G_werte[2]**2)
## H_B = sqrt(H_werte[0]**2+H_werte[1]**2+H_werte[2]**2)
## I_B = sqrt(I_werte[0]**2+I_werte[1]**2+I_werte[2]**2)
## G_B = (sqrt(G_werte[0]**2+G_werte[1]**2+G_werte[2]**2))**2
## H1_B = (sqrt(H1_werte[0]**2+H1_werte[1]**2+H1_werte[2]**2))**2
## H2_B = (sqrt(H2_werte[0]**2+H2_werte[1]**2+H2_werte[2]**2))**2
## I_B = (sqrt(I_werte[0]**2+I_werte[1]**2+I_werte[2]**2))**2
#Normalkruemmung
## myobj.du_werte = du(myobj.t,myobj.tckp)
## myobj.dv_werte = dv(myobj.t,myobj.tckp)
## myobj.du_2 = myobj.du_werte**2
## myobj.dv_2 = myobj.dv_werte**2
## myobj.du_2 = du(t,tckp)**2
## myobj.dv_2 = dv(t,tckp)**2
## k_n = (A_B*du_2+(B1_B+B2_B)*du*dv+C_B*dv_2)/(G_B*du_2+2*H_B*du*dv+I_B*dv_2)
## k_n = (A_B*du_2+(B1_B+B2_B)*du*dv+C_B*dv_2)/(G_B*du_2+(H1_B+H2_B)*du*dv+I_B*dv_2)
## k_n = (A*du_2+(B1+B2)*du*dv+C*dv_2)/(G*du_2+2*H*du*dv+I*dv_2)
## myobj.k_nf = ((myobj.A[0]+myobj.A[1]+myobj.A[2])*myobj.du_2+((myobj.B1[0]+myobj.B1[1]+myobj.B1[2])+(myobj.B2[0]+myobj.B2[1]+myobj.B2[2]))*myobj.du_werte*myobj.dv_werte+(myobj.C[0]+myobj.C[1]+myobj.C[2])*myobj.dv_2)/((myobj.G[0]+myobj.G[1]+myobj.G[2])*myobj.du_2+2*(myobj.H[0]+myobj.H[1]+myobj.H[2])*myobj.du_werte*myobj.dv_werte+(myobj.I[0]+myobj.I[1]+myobj.I[2])*myobj.dv_2)
## k_nf = ((A[0]+A[1]+A[2])*du(t)**2+((B1[0]+B1[1]+B1[2])+(B2[0]+B2[1]+B2[2]))*du(t)*dv(t)+(C[0]+C[1]+C[2])*dv(t)**2)/((G[0]+G[1]+G[2])*du(t)**2+2*(H[0]+H[1]+H[2])*du(t)*dv(t)+(I[0]+I[1]+I[2])*dv(t)**2)
#TODO: kn_n ist noch nicht richtig, bei einer kugel muesste sie immer die gleiche laenge haben.
#sieht schon besser aus, aber immernoch nicht die gleiche laenge, ob das wohl mit den rundungfehler zu tun hat?
#also ob ich du(t),dv(t) in k_nf aufrufe oder vorher gibt kein unterschied an den zahlen.
#bleibt nur noch bei der berechnung der A,B,C,G,H,I zu untersuchen.
## kn_n = negative(k_n*n)
## myobj.kn_nf = abs(myobj.k_nf)*myobj.n
## kn1_n = kn_n[0]
## kn2_n = kn_n[1]
## kn3_n = kn_n[2]
## myobj.normalkruemmung = mlab.quiver3d(myobj.xnew[0], myobj.ynew[0], myobj.znew[0], myobj.kn_nf[0][0],myobj.kn_nf[1][0], myobj.kn_nf[2][0],scale_factor=myobj.k_nf[0], color=(0,0,0))
## normalkruemmung = mlab.quiver3d(xnew[0], ynew[0], znew[0], kn_n[0][0],kn_n[1][0], kn_n[2][0],scale_factor=k_n[0][0], color=(0,0,0))
## normalkruemmung = mlab.quiver3d(xnew[0], ynew[0], znew[0], kn_n[0][0],kn_n[1][0], kn_n[2][0],scale_mode='vector', color=(0,0,0))
## normalkruemmung = mlab.quiver3d(xnew[0], ynew[0], znew[0], kn1_n[0],kn2_n[0], kn3_n[0], color=(0,0,0))
## normalkruemmung.glyph.glyph.set(scale_factor=k_n[0])

## def dreibein2(ii):
##     tangente_fu.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=u1_n[ii], v=u2_n[ii], w=u3_n[ii])
##     tangente_fv.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=v1_n[ii], v=v2_n[ii], w=v3_n[ii])
##     normale_f.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=uv1_n[ii], v=uv2_n[ii], w=uv3_n[ii])
##     normalkruemmung.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=kn_nf[0][ii], v=kn_nf[1][ii], w=kn_nf[2][ii],scale_factor=k_nf[ii])

#--------neu ende
#TODO: geodaetische Kruemmung berechnen und dann die Summe der beiden Krummungen berechnen.
#ob ich die geodaetische Kruemmung nach dem spatprodukt rechnen kann? siehe seite 169
#TODO: Kruemmung der Flaeche berechnen.


#spaeter, wenn es erwuenscht ist
## myobj = Kugel(1,1,1)
## myobj.flaeche_berechnen()
# Connect our dialog to the filter
extent_dialog = ExtentDialog(myobj=myobj)
## extent_dialog = ExtentDialog(mesh=mesh, tangente=tangente, ableitung2=ableitung2, hauptnormale=hauptnormale, binormale=binormale, tangente_fu=tangente_fu,tangente_fv=tangente_fv,normale_f=normale_f,normalkruemmung=normalkruemmung,normalebene=normalebene,schmiegebene=schmiegebene,rektifizierendeebene=rektifizierendeebene,tangentialebene_f=tangentialebene_f)
# We need to use 'edit_traits' and not 'configure_traits()' as we do
# not want to start the GUI event loop (the call to mlab.show())
# at the end of the script will do it.
extent_dialog.edit_traits()

## myobj.mesh._hideshow()
## myobj.tangente_fu._hideshow()
## myobj.tangente_fv._hideshow()
## myobj.normale_f._hideshow()
## myobj.normalkruemmung._hideshow()
## myobj.normalebene._hideshow()
## myobj.schmiegebene._hideshow()
## myobj.rektifizierendeebene._hideshow()
## myobj.tangentialebene_f._hideshow()

# Some logic to select 'mesh' and the data index when picking.

## def picker_callback(self, picker_obj):
##     picked = picker_obj.actors
##     if self.mesh.actor.actor._vtk_obj in [o._vtk_obj for o in picked]:
## 	    # m.mlab_source.points is the points array underlying the vtk
## 	    # dataset. GetPointId return the index in this array.
## 	    x_, y_ = np.lib.index_tricks.unravel_index(picker_obj.point_id,u_f.shape)
## 	    print "Data indices: %i, %i" % (x_, y_)
## 	    self.cursor3d.mlab_source.set(x=myobj.x_f_werte[x_, y_],y=myobj.y_f_werte[x_, y_],z=myobj.z_f_werte[x_, y_])
## 	    print cursor3d.mlab_source.get('points')
## 	    myobj.index_u[myobj.global_i] = x_
## 	    myobj.index_v[myobj.global_i] = y_
## 	    myobj.x_p[myobj.global_i] = cursor3d.mlab_source.x
## 	    myobj.y_p[myobj.global_i] = cursor3d.mlab_source.y
## 	    myobj.z_p[myobj.global_i] = cursor3d.mlab_source.z
## 	    myobj.global_i = mod(myobj.global_i+1,4)



## myobj.fig.on_mouse_pick(picker_callback)
## mlab.show()

## mlab.show()

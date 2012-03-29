from scipy.interpolate import splev, splprep
from scipy.integrate import quad
from numpy import sin,cos,zeros_like,ones_like,array,sqrt,cross,abs

#############################################################################
#alle funktionen fuer die flaeche
## x_f = lambda u_f,v_f: cos(u_f)*sin(v_f)
## y_f = lambda u_f,v_f: sin(u_f)*sin(v_f)
## z_f = lambda u_f,v_f: cos(v_f)

#############################################################################
#alle funktionen fuer die kurve und die dazugehoerigen funktionen
u = lambda t,tckp : splev(t,tckp,0)[0]
v = lambda t,tckp : splev(t,tckp,0)[1]
#du,dv sind die ersten Ableitungen der Flaechenparameter.
du = lambda t,tckp : splev(t,tckp,1)[0]
dv = lambda t,tckp : splev(t,tckp,1)[1]
#x,y,z sind die Koordinaten im dreidimensionalem euklidischen Raum
#### x = lambda u,v: cos(u)*sin(v)
#### y = lambda u,v: sin(u)*sin(v)
#### z = lambda u,v: cos(v)
#ones_like = einfach die arraywerte in 1 umschreiben.
#dxu,dxv sind die Werte der ersten Patielenableitung
#### dxu = lambda u,v: -sin(u)*sin(v)
#zeros_like = einfach die arraywerte in 0 umschreiben.
#### dxv = lambda u,v: cos(u)*cos(v)
#### dyu = lambda u,v: cos(u)*sin(v)
#### dyv = lambda u,v: sin(u)*cos(v)
#### dzu = lambda u,v: zeros_like(u)
#### dzv = lambda u,v: -sin(v)
## #K ist die Kurvenfunktion
## K = lambda t,tckp: (x(u(t,tckp),v(t,tckp)), y(u(t,tckp),v(t,tckp)), z(u(t,tckp),v(t,tckp)))
## #dKt ist die erste Ableitung der Kurvenfunktion.
## dKt = lambda t: array((dxu(u(t)),dyu(u(t)),dzu(u(t))))*du(t) + array((dxv(v(t)),dyv(v(t)),dzv(v(t))))*dv(t)
## dKt = lambda t,tckp: array((dxu(u(t,tckp),v(t,tckp)),dyu(u(t,tckp),v(t,tckp)),dzu(u(t,tckp),v(t,tckp))))*du(t,tckp) + array((dxv(u(t,tckp),v(t,tckp)),dyv(u(t,tckp),v(t,tckp)),dzv(u(t,tckp),v(t,tckp))))*dv(t,tckp)
#------------------neu
## dxuu = lambda u,v: -cos(u)*sin(v)
## dxvu = lambda u,v: cos(u)*(-sin(v))
## dxuv = lambda u,v: -sin(u)*cos(v)
## dxvv = lambda u,v: cos(u)*(-sin(v))

## dyuu = lambda u,v: -sin(u)*sin(v)
## dyvu = lambda u,v: cos(u)*cos(v)
## dyuv = lambda u,v: cos(u)*cos(v)
## dyvv = lambda u,v: sin(u)*(-sin(v))
## dzuu = lambda u,v: zeros_like(u)
## dzvu = lambda u,v: zeros_like(u)
## dzuv = lambda u,v: zeros_like(v)
## dzvv = lambda u,v: -cos(v)

duu = lambda t,tckp : splev(t,tckp,2)[0]
duv = lambda t,tckp : zeros_like(duu(t,tckp))
dvu = lambda t,tckp : zeros_like(dvv(t,tckp))
dvv = lambda t,tckp : splev(t,tckp,2)[1]
## #Das muesste die richtige zweite Ableitung sein fuer die Kurve.
## dKtt = lambda t,tckp: array((dxuu(u(t,tckp),v(t,tckp)),dyuu(u(t,tckp),v(t,tckp)),dzuu(u(t,tckp),v(t,tckp))))*du(t,tckp)+array((dxu(u(t,tckp),v(t,tckp)),dyu(u(t,tckp),v(t,tckp)),dzu(u(t,tckp),v(t,tckp))))*duu(t,tckp) + array((dxvv(u(t,tckp),v(t,tckp)),dyvv(u(t,tckp),v(t,tckp)),dzvv(u(t,tckp),v(t,tckp))))*dv(t,tckp)+array((dxv(u(t,tckp),v(t,tckp)),dyv(u(t,tckp),v(t,tckp)),dzv(u(t,tckp),v(t,tckp))))*dvv(t,tckp)

## #dKu ist die erste Ableitung der Kurvenfunktion nach dem Parameter u.
#### dKt = lambda t: array((dxu(u(t)),dyu(u(t)),dzu(u(t))))*du(t) + array((dxv(v(t)),dyv(v(t)),dzv(v(t))))*dv(t)
## dKu = lambda t,tckp: array((dxu(u(t,tckp),v(t,tckp)),dyu(u(t,tckp),v(t,tckp)),dzu(u(t,tckp),v(t,tckp))))*du(t,tckp)
## #dKv ist die erste Ableitung der Kurvenfunktion nach dem Parameter v.
## dKv = lambda t,tckp: array((dxv(u(t,tckp),v(t,tckp)),dyv(u(t,tckp),v(t,tckp)),dzv(u(t,tckp),v(t,tckp))))*dv(t,tckp)

## A_n = lambda t,tckp: array((dxuu(u(t,tckp),v(t,tckp)),dyuu(u(t,tckp),v(t,tckp)),dzuu(u(t,tckp),v(t,tckp))))
## B1_n = lambda t,tckp: array((dxuv(u(t,tckp),v(t,tckp)),dyuv(u(t,tckp),v(t,tckp)),dzuv(u(t,tckp),v(t,tckp))))
## B2_n = lambda t,tckp: array((dxvu(u(t,tckp),v(t,tckp)),dyvu(u(t,tckp),v(t,tckp)),dzvu(u(t,tckp),v(t,tckp))))
## C_n = lambda t,tckp: array((dxvv(u(t,tckp),v(t,tckp)),dyvv(u(t,tckp),v(t,tckp)),dzvv(u(t,tckp),v(t,tckp))))
## #Fundamentalgroessen der ersten Fundamentalform
## Gf = lambda t,tckp: array((dxu(u(t,tckp),v(t,tckp)),dyu(u(t,tckp),v(t,tckp)),dzu(u(t,tckp),v(t,tckp))))**2
## Hf = lambda t,tckp: array((dxu(u(t,tckp),v(t,tckp)),dyu(u(t,tckp),v(t,tckp)),dzu(u(t,tckp),v(t,tckp)))) * array((dxv(u(t,tckp),v(t,tckp)),dyv(u(t,tckp),v(t,tckp)),dzv(u(t,tckp),v(t,tckp))))
## If = lambda t,tckp: array((dxv(u(t,tckp),v(t,tckp)),dyv(u(t,tckp),v(t,tckp)),dzv(u(t,tckp),v(t,tckp))))**2

################## neu
#Laenge eines Vektors
def vektorlaenge(x,y,z):
    laenge = sqrt(x**2+y**2+z**2)
    return laenge
    
def vektorausrichtung(x,y,z):
    richtung = x+y+z
    return richtung
    
def positivevektorausrichtung(x,y,z):
    matrix1 = abs(vektorausrichtung(x,y,z))/vektorausrichtung(x,y,z)
    x,y,z = array([x,y,z])*matrix1
    return x,y,z
################## neu ende
################## neu
## index_t = r_[0:101:1]
def func(index_t, G, H, I, du, dv, du2, dv2):
    return sqrt((G[0][index_t]+G[1][index_t]+G[2][index_t])*du2[index_t] + 2*(H[0][index_t]+H[1][index_t]+H[2][index_t])*du[index_t]*dv[index_t] + (I[0][index_t]+I[1][index_t]+I[2][index_t])*dv2[index_t])
def sf(t,index_t, G, H, I, du, dv, du2, dv2):
##     return quad(func,0,t[index_t],args=(t[index_t]))
    return quad(func,0,t[index_t], args=(G, H, I, du, dv, du2, dv2))[0]
## def mys(t,index_t):
##     mys_werte = zeros_like(t)
##     for ii in index_t:
##         mys_werte[ii] = sf(t,index_t[ii])
##     return mys_werte
def bogenlaenge(t,index_t, G, H, I, du, dv, du2, dv2):
    bogenlaenge_werte = zeros_like(t)
##     for ii in r_[0:101:1]:
    for ii in index_t:
        bogenlaenge_werte[ii] = sf(t,index_t[ii], G, H, I, du, dv, du2, dv2)
    return bogenlaenge_werte
################## neu ende

################## neu2
## index_t = r_[0:101:1]
def func2(index_t, G, H, I, du, dv, du2, dv2):
    return sqrt((G[0][index_t]+G[1][index_t]+G[2][index_t])*du2[index_t] + 2*(H[0][index_t]+H[1][index_t]+H[2][index_t])*du[index_t]*dv[index_t] + (I[0][index_t]+I[1][index_t]+I[2][index_t])*dv2[index_t])
def sf2(t,index_t, G, H, I, du, dv, du2, dv2):
    if index_t > 0:
        index_tt = index_t - 1
    else:
        index_tt = 0
    return quad(func2,t[index_tt],t[index_t], args=(G, H, I, du, dv, du2, dv2))[0]
## def mys(t,index_t):
##     mys_werte = zeros_like(t)
##     for ii in index_t:
##         mys_werte[ii] = sf(t,index_t[ii])
##     return mys_werte
def bogenlaenge2(t,index_t, G, H, I, du, dv, du2, dv2):
    bogenlaenge_werte = zeros_like(t)
##     for ii in r_[0:101:1]:
    for ii in index_t:
        bogenlaenge_werte[ii] = sf2(t,index_t[ii], G, H, I, du, dv, du2, dv2)
    return bogenlaenge_werte
################## neu2 ende

#Normalisierung eines Vektors
def normalisiere(a,b,c):
	abc = sqrt(a**2+b**2+c**2)
	a_n, b_n, c_n = a/abc, b/abc, c/abc
	return a_n, b_n, c_n
#Kreuzprodukt von zwei Vektoren
def kreuzprodukt(t1,t2,t3,h1,h2,h3):
    return cross(array([t1, t2, t3]).T, array([h1, h2, h3]).T).T

def spatprodukt(v1,v2,v3,v11,v12,v13,v21,v22,v23):
    return kreuzprodukt(v1,v2,v3,v11,v12,v13) * array([v21,v22,v23])
#Eckpunkte einer Ebene
def eckpunkte_ebene(x,y,z,u1,v1,w1,u2,v2,w2):
    px1,py1,pz1 = [u1+u2+x,x],[v1+v2+y,y],[w1+w2+z,z]
    px2,py2,pz2 = [u1-u2+x,x],[v1-v2+y,y],[w1-w2+z,z]
    px3,py3,pz3 = [-u1-u2+x,x],[-v1-v2+y,y],[-w1-w2+z,z]
    px4,py4,pz4 = [-u1+u2+x,x],[-v1+v2+y,y],[-w1+w2+z,z]
    epx = array([px1,px2,px3,px4,px1])
    epy = array([py1,py2,py3,py4,py1])
    epz = array([pz1,pz2,pz3,pz4,pz1])
    return epx, epy, epz

#von kurve_berechnen in tckp_berechnen umbenannt.
def tckp_berechnen(u_werte, v_werte, grad, glaettung):
## 	print 'test'
	tckp, nix = splprep([u_werte,v_werte],k=grad, s=glaettung, nest=-1)
## 	print 'Kurve wurde berechnet'
	return tckp
from numpy import mod, lib, r_, zeros
from enthought.mayavi import mlab
## from calculation import tckp_berechnen
from calculation import * #bogenlaenge,vektorlaenge,normalisiere,kreuzprodukt...
from myutil import ebene

class myobject(object):
    fig = None
    #fuer die flaeche
    mesh = None
####     u_f = None
####     v_f = None
####     x_f_werte = None #x_f(u_f,v_f)
####     y_f_werte = None #y_f(u_f,v_f)
####     z_f_werte = None #z_f(u_f,v_f)
##     u_f = zeros((180,180))
    u_f = None
    v_f = None
    x_werte = None #x_f(u_f,v_f)
    y_werte = None #y_f(u_f,v_f)
    z_werte = None #z_f(u_f,v_f)
    #die zu anzuzeigende kurve
    kurve = None
    t = None
    #################### neu
    t_index = None
    s = None
    #################### neu ende
    tckp = None
    #fuer die 4 kurvenpunkte, aus den ich die kurve berechne
    kurvenpunkte_4 = None
    #damit ich tckp richtig berechnen kann
    u_f4 = None
    v_f4 = None
####     nix = None
    #alle anzuzeigende vektoren
    tangente = None
    ableitung2 = None
    hauptnormale = None
    binormale = None
    tangente_fu = None
    tangente_fv = None
    normale_f = None
    normalkruemmung = None
    ######################## neu
    kruemmung = None
    geodaetischekruemmung = None
    ######################## neu ende
    #alle anzuzeigenden ebenen
    normalebene = None
    schmiegebene = None
    rektifizierendeebene = None
    tangentialebene_f = None
    #alle kurvenpunkte
    xnew = None
    ynew = None
    znew = None
    
    #alle koeffizienten fuer die vektorenausrichtung
    #TODO: soll ich auch die zwischenwerte(vor der normalisierung) hier mit ausnehmen?
    a = None
    b = None
    c = None
    d = None
    e = None
    f = None
    g = None
    h = None
    i = None
    j = None
    k = None
    l = None
    a_n = None
    b_n = None
    c_n = None
    d_n = None
    e_n = None
    f_n = None
    g_n = None
    h_n = None
    i_n = None
    j_n = None
    k_n = None
    l_n = None
    #alle variablen fuer den picker benoetigt werden
    index_u = array([0,0,0,0]) #None #array([0,0,0,0])
    index_v = array([0,0,0,0]) #None #array([0,0,0,0])
    x_p = array([0.,0.,0.,0.]) #None #array([0,0,0,0])
    y_p = array([0.,0.,0.,0.]) #None #array([0,0,0,0])
    z_p = array([0.,0.,0.,0.]) #None #array([0,0,0,0])
    global_i = 0 #None #0
    #alle variablen zur skalierung der flaeche
    skalierung_x = None
    skalierung_y = None
    skalierung_z = None
    #alle eckpunke fuer die ebenen
    epxn = None #normalebene
    epyn = None
    epzn = None
    epxs = None #schmiegebene
    epys = None
    epzs = None
    epxr = None #rektifizierende ebene
    epyr = None
    epzr = None
    epxt = None #tangentialebene der flaeche
    epyt = None
    epzt = None
    #alle variablen fuer die differentialgeometrischen eigenschaften der flaeche
    u1 = None
    u2 = None
    u3 = None
    v1 = None
    v2 = None
    v3 = None
    uv1 = None
    uv2 = None
    uv3 = None
    #alle variablen fuer die fundamentalgroessen
    n = None
    A = None
    B1 = None
    B2 = None
    C = None
    G = None
    H = None
    I = None
    du_2 = None
    dv_2 = None
    k_nf = None #Normalkruemmung
    kn_nf = None #Normalenvektor*Normalkruemmung
    ####################### neu
    kg = None #geodaetische Kruemmungsvektor = dKtt(t)-kn_nf
    kg_laenge = None #laenge des geodaetische Kruemmungsvektors
    dKtt_laenge = None #laenge des Kruemmungsvektors
    dKs_werte = None
    dKss_werte = None
    ####################### neu ende
          
    #K ist die Kurvenfunktion
    K = lambda self,t,tckp: array([self.x(u(t,tckp),v(t,tckp)), self.y(u(t,tckp),v(t,tckp)), self.z(u(t,tckp),v(t,tckp))])
    #dKt ist die erste Ableitung der Kurvenfunktion.
    dKt = lambda self,t,tckp: array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))])*du(t,tckp) + array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])*dv(t,tckp)
    #Das muesste die richtige zweite Ableitung sein fuer die Kurve.
##     dKtt = lambda self,t,tckp: array([self.dxuu(u(t,tckp),v(t,tckp)),self.dyuu(u(t,tckp),v(t,tckp)),self.dzuu(u(t,tckp),v(t,tckp))])*du(t,tckp) + array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))])*duu(t,tckp) + array([self.dxvv(u(t,tckp),v(t,tckp)),self.dyvv(u(t,tckp),v(t,tckp)),self.dzvv(u(t,tckp),v(t,tckp))])*dv(t,tckp) + array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])*dvv(t,tckp)
    dKtt = lambda self,t,tckp: array([self.dxuu(u(t,tckp),v(t,tckp)),self.dyuu(u(t,tckp),v(t,tckp)),self.dzuu(u(t,tckp),v(t,tckp))])*du(t,tckp) + 2*(array([self.dxuv(u(t,tckp),v(t,tckp)),self.dyuv(u(t,tckp),v(t,tckp)),self.dzuv(u(t,tckp),v(t,tckp))]))*du(t,tckp)*dv(t,tckp) + array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))])*duu(t,tckp) + array([self.dxvv(u(t,tckp),v(t,tckp)),self.dyvv(u(t,tckp),v(t,tckp)),self.dzvv(u(t,tckp),v(t,tckp))])*dv(t,tckp) + array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])*dvv(t,tckp)
    
    
    #Ks ist die Kurvenfunktion
    Ks = lambda self,t,tckp: array([self.x(u(t,tckp),v(t,tckp)), self.y(u(t,tckp),v(t,tckp)), self.z(u(t,tckp),v(t,tckp))])
    #dKs ist die erste Ableitung der Kurvenfunktion.
    dKs = lambda self,t,tckp: array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))])*du(t,tckp) + array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])*dv(t,tckp)
    #Das muesste die richtige zweite Ableitung sein fuer die Kurve.
    #hier hab ich den 2*(Kuv * us*vs) hizugefuegt,
    #aber wie bekomm ich Kuv?
    dKss = lambda self,t,tckp: array([self.dxuu(u(t,tckp),v(t,tckp)),self.dyuu(u(t,tckp),v(t,tckp)),self.dzuu(u(t,tckp),v(t,tckp))])*(du(t,tckp))**2 + 2*(array([self.dxuv(u(t,tckp),v(t,tckp)),self.dyuv(u(t,tckp),v(t,tckp)),self.dzuv(u(t,tckp),v(t,tckp))]))*du(t,tckp)*dv(t,tckp) + array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))])*duu(t,tckp) + array([self.dxvv(u(t,tckp),v(t,tckp)),self.dyvv(u(t,tckp),v(t,tckp)),self.dzvv(u(t,tckp),v(t,tckp))])*(dv(t,tckp)**2) + array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])*dvv(t,tckp)
    
    #dKu ist die erste Ableitung der Kurvenfunktion nach dem Parameter u.
    dKu = lambda self,t,tckp: array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))])*du(t,tckp)
    #dKv ist die erste Ableitung der Kurvenfunktion nach dem Parameter v.
    dKv = lambda self,t,tckp: array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])*dv(t,tckp)

    A_n = lambda self,t,tckp: array([self.dxuu(u(t,tckp),v(t,tckp)),self.dyuu(u(t,tckp),v(t,tckp)),self.dzuu(u(t,tckp),v(t,tckp))])
    B1_n = lambda self,t,tckp: array([self.dxuv(u(t,tckp),v(t,tckp)),self.dyuv(u(t,tckp),v(t,tckp)),self.dzuv(u(t,tckp),v(t,tckp))])
    B2_n = lambda self,t,tckp: array([self.dxvu(u(t,tckp),v(t,tckp)),self.dyvu(u(t,tckp),v(t,tckp)),self.dzvu(u(t,tckp),v(t,tckp))])
    C_n = lambda self,t,tckp: array([self.dxvv(u(t,tckp),v(t,tckp)),self.dyvv(u(t,tckp),v(t,tckp)),self.dzvv(u(t,tckp),v(t,tckp))])
    #Fundamentalgroessen der ersten Fundamentalform
    Gf = lambda self,t,tckp: array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))])**2
    Hf = lambda self,t,tckp: array([self.dxu(u(t,tckp),v(t,tckp)),self.dyu(u(t,tckp),v(t,tckp)),self.dzu(u(t,tckp),v(t,tckp))]) * array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])
    If = lambda self,t,tckp: array([self.dxv(u(t,tckp),v(t,tckp)),self.dyv(u(t,tckp),v(t,tckp)),self.dzv(u(t,tckp),v(t,tckp))])**2

    def __init__(self):
        self.fig = mlab.figure(1,bgcolor=(1,1,1))
##         self.cursor3d = mlab.points3d(0., 0., 0., mode='sphere',
##                                 color=(0, 0, 0),
##                                 scale_factor=0.03)
    
            
    def flaeche_berechnen(self):
        self.x_werte = self.x(self.u_f,self.v_f)
        self.y_werte = self.y(self.u_f,self.v_f)
        self.z_werte = self.z(self.u_f,self.v_f)
        self.mesh = mlab.mesh(self.x_werte,self.y_werte,self.z_werte,color=(0.6,0.6,0.6))
##         print self.u_f.shape , self.v_f.shape
##         print self.u_f
        ############ von __init__ hier runter geholt
        self.cursor3d = mlab.points3d(0., 0., 0., mode='sphere',
                                color=(0, 0, 0),
                                scale_factor=0.03)
        ############################################
        #TODO: sah kein unterschied zwischen den beiden zeilen hier drunter.
        self.fig.on_mouse_pick(lambda picker_obj: self.picker_callback(picker_obj))
##         self.fig.on_mouse_pick(self.picker_callback)
##         mlab.show()
    
    def kurve_berechnen(self):
        self.kurvenpunkte_4 = mlab.points3d(self.x_p, self.y_p, self.z_p, mode='sphere',color=(0, 0, 0),scale_factor=0.02)
        #TODO: ich muss tckp_berechnen die richtigen werte uebergeben
        #also nicht index_u sondern u_f4
        #wobei u_f4 = [u_f[index_u[0]][index_v[0]], u_f[index_u[1]][index_v[1]], u_f[index_u[2]][index_v[2]], u_f[index_u[3]][index_v[3]]
##         self.tckp = tckp_berechnen(self.index_u, self.index_v, 3, 3.0)
        self.u_f4 = [self.u_f[self.index_u[0]][self.index_v[0]], self.u_f[self.index_u[1]][self.index_v[1]], self.u_f[self.index_u[2]][self.index_v[2]], self.u_f[self.index_u[3]][self.index_v[3]]]
        self.v_f4 = [self.v_f[self.index_u[0]][self.index_v[0]], self.v_f[self.index_u[1]][self.index_v[1]], self.v_f[self.index_u[2]][self.index_v[2]], self.v_f[self.index_u[3]][self.index_v[3]]]
        self.tckp = tckp_berechnen(self.u_f4, self.v_f4, 3, 3.0)
##         print self.index_u, self.index_v
        #t ist der parameter der kurve
        self.t = r_[0:1:101j]
        ###################### neu
        self.t_index = r_[0:101:1]
        ###################### neu ende
        #xnew,ynew,znew representieren die x,y,z Koordinaten der Kurve
        self.xnew, self.ynew, self.znew = self.K(self.t, self.tckp)
##         print 'xnew,ynew,znew'
##         print self.xnew, self.ynew, self.znew
        #Zeichnet die Kurve nach den Punkten.
        self.kurve = mlab.plot3d(self.xnew, self.ynew, self.znew, tube_radius=0.005, color=(1,1,1), name='Kurve')
        #a,b,c sind die Koeffizienten fuer die Tangentenvektoren
        self.a, self.b, self.c = self.dKt(self.t, self.tckp)
        self.a_n, self.b_n, self.c_n = normalisiere(self.a,self.b,self.c)
##         self.a_n, self.b_n, self.c_n = a,b,c
        #Das ist der Vektor der zweiten Ableitung der Splinekurve.
        #Dieser Vektor liegt ebenfalls in der Tangentialebene.
        self.d,self.e,self.f = self.dKtt(self.t, self.tckp)
        self.d_n, self.e_n, self.f_n = normalisiere(self.d,self.e,self.f)
##         self.d_n, self.e_n, self.f_n = d,e,f
        #Das ist der Binormalenvektor(blau).
##         self.g,self.h,self.i = kreuzprodukt(self.a_n, self.b_n, self.c_n, self.d_n, self.e_n, self.f_n)
        self.g,self.h,self.i = kreuzprodukt(self.a, self.b, self.c, self.d, self.e, self.f)
        self.g_n, self.h_n, self.i_n = normalisiere(self.g,self.h,self.i)
##         self.g_n, self.h_n, self.i_n = g,h,i
        #Das ist der Hauptnormalenvektor(gruen).
##         j,k,l = kreuzprodukt(self.g_n, self.h_n, self.i_n, self.a_n, self.b_n, self.c_n)
        self.j,self.k,self.l = kreuzprodukt(self.g, self.h, self.i, self.a, self.b, self.c)
        self.j_n, self.k_n, self.l_n = normalisiere(self.j, self.k, self.l)
##         self.j_n, self.k_n, self.l_n = j, k, l
        #
        #t: h+b,h-b,-h-b,-h+b,h+b
        #
        #Zeichnet die Tangenten(rot) an die Kurve.
##         self.tangente = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.a_n[0], self.b_n[0], self.c_n[0], color=(1,0,0), name='Tangente')
##         self.ableitung2 = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.d_n[0], self.e_n[0], self.f_n[0], color=(0.6,0.6,0.6), name='2 Ableitung')
##         self.hauptnormale = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.j_n[0], self.k_n[0], self.l_n[0], color=(0,1,0), name='Hauptnormale')
##         self.binormale = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.g_n[0], self.h_n[0], self.i_n[0], color=(0,0,1), name='Binormale')
        self.tangente = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.a[0], self.b[0], self.c[0], color=(1,0,0), name='Tangente')
        self.ableitung2 = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.d[0], self.e[0], self.f[0], color=(1,0.65,0), name='2 Ableitung')
        self.hauptnormale = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.j[0], self.k[0], self.l[0], color=(0,1,0), name='Hauptnormale')
        self.binormale = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.g[0], self.h[0], self.i[0], color=(0,0,1), name='Binormale')
        self.normalebene = ebene(self.xnew,self.ynew,self.znew,self.j_n,self.k_n,self.l_n,self.g_n,self.h_n,self.i_n,(1,0,0),0, 'Normalebene')
        self.schmiegebene = ebene(self.xnew,self.ynew,self.znew,self.a_n,self.b_n,self.c_n,self.j_n,self.k_n,self.l_n,(0,0,1),0, 'Schmiegebene')
        self.rektifizierendeebene = ebene(self.xnew,self.ynew,self.znew,self.a_n,self.b_n,self.c_n,self.g_n,self.h_n,self.i_n,(0,1,0),0, 'Rektifizierende Ebene')
        #eckpunkte der normalebene, schmiegebene, rektifizierendeebene
        self.epxn, self.epyn, self.epzn = eckpunkte_ebene(self.xnew,self.ynew,self.znew,self.j_n,self.k_n,self.l_n,self.g_n,self.h_n,self.i_n)
        self.epxs, self.epys, self.epzs = eckpunkte_ebene(self.xnew,self.ynew,self.znew,self.a_n,self.b_n,self.c_n,self.j_n,self.k_n,self.l_n)
        self.epxr, self.epyr, self.epzr = eckpunkte_ebene(self.xnew,self.ynew,self.znew,self.a_n,self.b_n,self.c_n,self.g_n,self.h_n,self.i_n)
        #Tangente an die Isoparameterlinier in Abhaengigkeit von dem Flaechenparameter u
        self.u1,self.u2,self.u3 = self.dKu(self.t,self.tckp)
        self.u1_n,self.u2_n,self.u3_n = normalisiere(self.u1,self.u2,self.u3)
        #Tangente an die Isoparameterlinier in Abhaengigkeit von dem Flaechenparameter v
        self.v1,self.v2,self.v3 = self.dKv(self.t,self.tckp)
        self.v1_n,self.v2_n,self.v3_n = normalisiere(self.v1,self.v2,self.v3)
        
        # neu
##         matrix1 = positivevektorausrichtung(self.u1_n,self.u2_n,self.u3_n)
##         self.u1_n,self.u2_n,self.u3_n = positivevektorausrichtung(self.u1_n,self.u2_n,self.u3_n)
##         print 'umatrix'
##         print matrix1
##         self.u1_n,self.u2_n,self.u3_n = array([self.u1_n,self.u2_n,self.u3_n])*matrix1
##         print 'u'
##         print vektorausrichtung(self.u1_n,self.u2_n,self.u3_n)
##         self.v1_n,self.v2_n,self.v3_n = positivevektorausrichtung(self.v1_n,self.v2_n,self.v3_n)
##         matrix1 = positivevektorausrichtung(self.v1_n,self.v2_n,self.v3_n)
##         self.v1_n,self.v2_n,self.v3_n = array([self.v1_n,self.v2_n,self.v3_n])*matrix1
##         print 'vmatrix'
##         print matrix1
##         print 'v'
##         print vektorausrichtung(self.v1_n,self.v2_n,self.v3_n)
        # neu ende
##         self.u1_n,self.u2_n,self.u3_n = positivevektorausrichtung(self.u1_n,self.u2_n,self.u3_n)
##         self.v1_n,self.v2_n,self.v3_n = positivevektorausrichtung(self.v1_n,self.v2_n,self.v3_n)
        
        #Normalenvektor zur Flaeche.
        self.uv1,self.uv2,self.uv3 = kreuzprodukt(self.u1,self.u2,self.u3,self.v1,self.v2,self.v3)
##         self.uv1,self.uv2,self.uv3 = kreuzprodukt(self.u1_n,self.u2_n,self.u3_n,self.v1_n,self.v2_n,self.v3_n)
        #Normaleneinheitsvektor zur Flaeche.
        #Damit der Normaleneinheitsvektor immer von der Flaeche weg zeigt, muss ich wohl den Absulut Wert von den Tangentenvektoren u,v nehmen.
        self.uv1_n,self.uv2_n,self.uv3_n = normalisiere(self.uv1,self.uv2,self.uv3)
##         self.tangente_fu = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.u1_n[0], self.u2_n[0], self.u3_n[0], color=(1,0,1), name='Tangente u')
##         self.tangente_fv = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.v1_n[0], self.v2_n[0], self.v3_n[0], color=(1,0,1), name='Tangente v')
##         self.normale_f = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.uv1_n[0], self.uv2_n[0], self.uv3_n[0], color=(1,1,0), name='Flaechennormale')
        self.tangente_fu = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.u1[0], self.u2[0], self.u3[0], color=(1,0.65,0), name='Tangente u')
        self.tangente_fv = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.v1[0], self.v2[0], self.v3[0], color=(1,0.65,0), name='Tangente v')
        self.normale_f = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.uv1[0], self.uv2[0], self.uv3[0], color=(1,1,0), name='Flaechennormale')
        #Berechnung der Eckpunkte der Tangentialebene der Flaeche.
        self.epxt,self.epyt,self.epzt = eckpunkte_ebene(self.xnew,self.ynew,self.znew,self.u1_n,self.u2_n,self.u3_n,self.v1_n,self.v2_n,self.v3_n)
        self.tangentialebene_f = ebene(self.xnew,self.ynew,self.znew,self.u1_n,self.u2_n,self.u3_n,self.v1_n,self.v2_n,self.v3_n,(1,1,0),0,'Tangentialebene der Flaeche')
        #Fundamentalgroessen der zweiten Fundamentalform
        self.n = array([self.uv1_n,self.uv2_n,self.uv3_n])
##         self.n = array([self.uv1,self.uv2,self.uv3])
        ### neu
##         print 'u1-u3'
##         print self.u1
##         print 
##         print self.u2
##         print 
##         print self.u3
##         print 'v1-v3'
##         print self.v1
##         print 
##         print self.v2
##         print 
##         print self.v3
##         print 'vektorlaenge u v'
##         print vektorausrichtung(self.u1,self.u2,self.u3)
##         print 
##         print vektorausrichtung(self.v1,self.v2,self.v3)
##         print 'vektorlaenge ende'

        # hier sollte ich lieber anstelle von n gleich u und v vektor 
        # in positive ausrichtung bringen
##         print 'richtung n'
##         print vektorausrichtung(self.n[0],self.n[1],self.n[2])
##         matrix1 = abs(vektorausrichtung(self.n[0],self.n[1],self.n[2]))/vektorausrichtung(self.n[0],self.n[1],self.n[2])
##         print 'matrix1'
##         print matrix1
##         self.n = self.n*matrix1
##         print 'neue n'
##         print self.n
##         self.uv1_n = self.n[0]
##         self.uv2_n = self.n[1]
##         self.uv3_n = self.n[2]
##         self.normale_f = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.uv1_n[0], self.uv2_n[0], self.uv3_n[0], color=(1,1,0), name='Flaechennormale')
        
##         self.n = abs(self.n)
        ### neu ende
        
        self.A = self.A_n(self.t,self.tckp) * self.n
        self.B1 = self.B1_n(self.t,self.tckp) * self.n
        self.B2 = self.B2_n(self.t,self.tckp) * self.n
        self.C = self.C_n(self.t,self.tckp) * self.n
        self.G = self.Gf(self.t,self.tckp)
        self.H = self.Hf(self.t,self.tckp)
        self.I = self.If(self.t,self.tckp)
        #Normalkruemmung
        self.du_werte = du(self.t,self.tckp)
        self.dv_werte = dv(self.t,self.tckp)
        self.du_2 = self.du_werte**2
        self.dv_2 = self.dv_werte**2
        self.k_nf = ((self.A[0]+self.A[1]+self.A[2])*self.du_2+((self.B1[0]+self.B1[1]+self.B1[2])+(self.B2[0]+self.B2[1]+self.B2[2]))*self.du_werte*self.dv_werte+(self.C[0]+self.C[1]+self.C[2])*self.dv_2)/((self.G[0]+self.G[1]+self.G[2])*self.du_2+2*(self.H[0]+self.H[1]+self.H[2])*self.du_werte*self.dv_werte+(self.I[0]+self.I[1]+self.I[2])*self.dv_2)
        
##         self.kn_nf = abs(self.k_nf)*self.n*(-1)
##         self.k_nf = abs(self.k_nf)
        self.kn_nf = self.k_nf*self.n
##         self.k_nf = abs(self.k_nf)
##         self.kn_nf = self.k_nf*self.n
##         self.kn_nf = abs(self.k_nf)*self.n
        self.normalkruemmung = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.kn_nf[0][0],self.kn_nf[1][0], self.kn_nf[2][0],scale_factor=self.k_nf[0], color=(0,0,0), name='Normalkruemmung')
        ################################# neu
##         self.dKtt_laenge = vektorlaenge(d,e,f)
####         self.kruemmung = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.d_n[0], self.e_n[0], self.f_n[0], scale_factor=self.dKtt_laenge[0], color=(0.6,0.6,0.6), name='Flaechenkruemmung')
##         self.kruemmung = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.d_n[0], self.e_n[0], self.f_n[0], color=(0.6,0.6,0.6), name='Flaechenkruemmung')
##         self.kg_laenge = self.dKtt_laenge - self.k_nf
##         self.kg = array([d - self.kn_nf[0], e - self.kn_nf[1], f - self.kn_nf[2]])
####         self.geodaetischekruemmung = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.kg[0][0], self.kg[1][0], self.kg[2][0], scale_factor=self.kg_laenge[0], color=(0.6,0.6,0.6), name='geodaetische Kruemmung')
##         self.geodaetischekruemmung = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.kg[0][0], self.kg[1][0], self.kg[2][0], color=(0.6,0.6,0.6), name='geodaetische Kruemmung')
        ####### test
##         n_nicht = vektorlaenge(self.uv1,self.uv2,self.uv3)
##         test_laenge = self.dKtt_laenge - n_nicht
##         print ''
##         print 'test_laenge'
##         print test_laenge
##         print 'n_nicht'
##         print n_nicht
        ####### test ende
        ################################# neu ende
        ############################################# neu 
        self.s = bogenlaenge(self.t,self.t_index, self.G, self.H, self.I, self.du_werte, self.dv_werte, self.du_2, self.dv_2)
        self.dKs_werte = self.dKt(self.s, self.tckp)
        self.dKss_werte = self.dKtt(self.s, self.tckp)
####         self.G = self.Gf(self.s,self.tckp)
####         self.H = self.Hf(self.s,self.tckp)
####         self.I = self.If(self.s,self.tckp)
##         spatprodukt_werte = spatprodukt(self.n[0],self.n[1],self.n[2], self.dKs_werte[0],self.dKs_werte[1],self.dKs_werte[2], self.dKss_werte[0],self.dKss_werte[1],self.dKss_werte[2])
##         self.kg = vektorlaenge(spatprodukt_werte[0],spatprodukt_werte[1],spatprodukt_werte[2])
##         print 'kg'
##         print self.kg
##         print 's'
##         print self.s
##         print 'dKss_werte'
##         print self.dKss_werte
##         print 'dKss_werte laenge'
##         print vektorlaenge(self.dKss_werte[0],self.dKss_werte[1],self.dKss_werte[2])
##         print 'dKss_werte_normalisiert'
##         print normalisiere(self.dKss_werte[0],self.dKss_werte[1],self.dKss_werte[2])
        ############## test
##         self.du_werte = du(self.s,self.tckp)
##         self.dv_werte = dv(self.s,self.tckp)
##         self.du_2 = self.du_werte**2
##         self.dv_2 = self.dv_werte**2
##         self.A = self.A_n(self.s,self.tckp) * self.n
##         self.B1 = self.B1_n(self.s,self.tckp) * self.n
##         self.B2 = self.B2_n(self.s,self.tckp) * self.n
##         self.C = self.C_n(self.s,self.tckp) * self.n
##         my_k_nf = (self.A[0]+self.A[1]+self.A[2])*self.du_2+((self.B1[0]+self.B1[1]+self.B1[2])+(self.B2[0]+self.B2[1]+self.B2[2]))*self.du_werte*self.dv_werte+(self.C[0]+self.C[1]+self.C[2])*self.dv_2
##         print 'my_k_nf'
##         print my_k_nf
##         self.xnew, self.ynew, self.znew = self.K(self.s, self.tckp)
##         #Zeichnet die Kurve nach den Punkten.
##         mlab.plot3d(self.xnew, self.ynew, self.znew, tube_radius=0.005, color=(0,0,0), name='Kurve2')
        ############## test ende
        ############################################# neu ende
        ##### neu vektor der geodaetischen ist richtig durch kg = n x t, aber die laenge stimmt nicht
        self.kg = kreuzprodukt(self.n[0],self.n[1],self.n[2],self.a_n,self.b_n,self.c_n)
##         self.kg[0],self.kg[1],self.kg[2] = positivevektorausrichtung(self.kg[0], self.kg[1], self.kg[2])
        self.geodaetischekruemmung = mlab.quiver3d(self.xnew[0], self.ynew[0], self.znew[0], self.kg[0][0], self.kg[1][0], self.kg[2][0], color=(1,0,1), name='geodaetische Kruemmung')
##         print 
##         print 'ausrichtung kg'
##         print positivevektorausrichtung(self.kg[0], self.kg[1], self.kg[2])
        ##### neu ende
        ### neu print
##         print 'flaechennormale n'
##         print self.n
##         print 'flaechennormale n absolut'
##         print abs(self.n)
        
##         print 'd,e,f'
##         print self.d, self.e, self.f
##         print 'vektorlaenge'
##         print vektorlaenge(self.d, self.e, self.f)
        ### neu print ende
        
        
        #TODO: geodaetische Kruemmung berechnen und dann die Summe der beiden Krummungen berechnen.
        #ob ich die geodaetische Kruemmung nach dem spatprodukt rechnen kann? siehe seite 169
        #TODO: Kruemmung der Flaeche berechnen.
        self.tangente._hideshow()
        self.ableitung2._hideshow()
        self.hauptnormale._hideshow()
        self.binormale._hideshow()
        self.tangente_fu._hideshow()
        self.tangente_fv._hideshow()
        self.normale_f._hideshow()
        self.normalkruemmung._hideshow()
        self.normalebene._hideshow()
        self.schmiegebene._hideshow()
        self.rektifizierendeebene._hideshow()
        self.tangentialebene_f._hideshow()
        ###################################### neu
        self.geodaetischekruemmung._hideshow()
##         self.kruemmung._hideshow()
##         print 'k_nf:'
##         print self.k_nf
##         print 'dKtt_laenge:'
##         print self.dKtt_laenge
##         print
##         print 'kg_laenge:'
##         print self.kg_laenge
        ###################################### neu ende
    
    def picker_callback(self, picker_obj):
        #das sollte ausreichen
####         global self.global_i
####         global global_i
        #die da unten brauch ich garnicht
####         global self.index_u
####         global self.index_v
####         global self.x_p
####         global self.y_p
####         global self.z_p
        picked = picker_obj.actors
        if self.mesh.actor.actor._vtk_obj in [o._vtk_obj for o in picked]:
	    # m.mlab_source.points is the points array underlying the vtk
	    # dataset. GetPointId return the index in this array.
	    x_, y_ = lib.index_tricks.unravel_index(picker_obj.point_id,self.u_f.shape)
	    print "Data indices: %i, %i" % (x_, y_)
	    self.cursor3d.mlab_source.set(x=self.x_werte[x_, y_],y=self.y_werte[x_, y_],z=self.z_werte[x_, y_])
	    print self.cursor3d.mlab_source.get('points')
####             self.index_u[global_i] = x_
#### 	    self.index_v[global_i] = y_
#### 	    self.x_p[global_i] = self.cursor3d.mlab_source.x
#### 	    self.y_p[global_i] = self.cursor3d.mlab_source.y
#### 	    self.z_p[global_i] = self.cursor3d.mlab_source.z
#### 	    global_i = mod(global_i+1,4)
	    self.index_u[self.global_i] = x_
	    self.index_v[self.global_i] = y_
            #TODO: das interessante ist, dass er intern anscheinen global_i benutz
            #und global nicht. index_u und index_v werden auch befuellt
            #nur x_p, y_p, z_p werden nicht befuellt, warum auch immer.
##             print 'self.global_i,self.index_u,self.index_v:'
##             print self.global_i, self.index_u, self.index_v
##             self.x_p[self.global_i] = self.x_werte[x_,y_]
## 	    self.y_p[self.global_i] = self.y_werte[x_,y_]
## 	    self.z_p[self.global_i] = self.z_werte[x_,y_]
	    self.x_p[self.global_i] = self.cursor3d.mlab_source.x
	    self.y_p[self.global_i] = self.cursor3d.mlab_source.y
	    self.z_p[self.global_i] = self.cursor3d.mlab_source.z
## 	    print 'self.x_p, self.y_p, self.z_p:'
##             print self.x_p, self.y_p, self.z_p
            print 'punkt:'
            print self.global_i
            self.global_i = mod(self.global_i+1,4)
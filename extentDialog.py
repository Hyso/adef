################################################################################
# A dialog to edit a range interactively and propagate it to the filter
## from traits.api import HasTraits, Range, Button, ToolbarButton, Float, Int, Instance, \
from traits.api import HasTraits, Range, Button, Bool, Enum, Array, Float, Int, Instance, \
    on_trait_change
from traitsui.api import View, Item
from myutil import punkt
from calculation import tckp_berechnen#, flaeche_berechnen,x_f,y_f,z_f
from numpy import array
from enthought.mayavi import mlab
from parabolischer_Zylinder import parabolischer_Zylinder
from elliptischer_Zylinder import elliptischer_Zylinder
from hyperbolischer_Zylinder import hyperbolischer_Zylinder
from elliptisches_Paraboloid import elliptisches_Paraboloid
from hyperbolisches_Paraboloid import hyperbolisches_Paraboloid
from elliptischer_Kegel import elliptischer_Kegel
from Ellipsoid import Ellipsoid
from einschaliges_Hyperboloid import einschaliges_Hyperboloid
from zweischaliges_Hyperboloid import zweischaliges_Hyperboloid
from Torus import Torus
## from myobject import flaeche_berechnen, kurve_berechnen

class ExtentDialog(HasTraits):
    """ A dialog to graphical adjust the extents of a filter.
    """
    Flaechen = Enum('parabolischer Zylinder',
			'elliptischer Zylinder',
                        'hyperbolischer Zylinder',
			'elliptisches Paraboloid',
			'hyperbolisches Paraboloid',
                        'elliptischer Kegel',
                        'Ellipsoid',
                        'einschaliges Hyperboloid',
                        'zweischaliges Hyperboloid',
                        'Torus',)

    Skalierung = Array(float,(1,3),array([[1,1,1]]))
    Flaeche = Button('berechnen')
    # Data extents
    Kurvenpunkt = Range(0, 100, 0)
    #Kurve berechnen
    Kurve = Button('berechnen')
    #Buttons sollen einen style='button', 'radio', 'checkbox'
    Flaeche_anzeigen = Bool()
    Dreibein = Bool()
    Tangente = Bool()
    zweite_Ableitung = Bool()
    Hauptnormale = Bool()
    Binormale = Bool()
    Flaechen_Tangente_u = Bool()
    Flaechen_Tangente_v = Bool()
    Flaechen_Normale = Bool()
    Normalkruemmung = Bool()
    ################################# neu
    Kruemmung = Bool()
    geodaetische_Kruemmung = Bool()
    ################################# neu ende
    Ebenen = Bool()
    Normalebene = Bool()
    Schmiegebene = Bool()
    rektifizierende_Ebene = Bool()
    Tangentialebene = Bool()
    #funktioniert nicht
##     Flaeche2 = ButtonEditor(style='checkbox')
##     Flaeche2 = ToolbarButton('sichtbar/unsichtbar',style='checkbox')
##     Normalebene = Button('sichtbar/unsichtbar', style='radio')
##     def __init__(self, mesh, tangente,ableitung2,hauptnormale,binormale,tangente_fu,tangente_fv,normale_f,normalkruemmung,normalebene,schmiegebene,rektifizierendeebene,tangentialebene_f):
## 	self.mesh = mesh
## 	self.tangente = tangente
## 	self.hauptnormale = hauptnormale
## 	self.binormale = binormale
## 	self.ableitung2 = ableitung2
## 	self.tangente_fu = tangente_fu
## 	self.tangente_fv = tangente_fv
## 	self.normale_f = normale_f
## 	self.normalkruemmung = normalkruemmung
## 	self.normalebene = normalebene
## 	self.schmiegebene = schmiegebene
## 	self.rektifizierendeebene = rektifizierendeebene
## 	self.tangentialebene_f = tangentialebene_f
## 	HasTraits.__init__(self)




    def __init__(self, myobj):
	self.myobj = myobj
	HasTraits.__init__(self)

##     @on_trait_change('Skalierung')
##     def update_skalierung(self):
##         pass
##         self.myobj.skalierung_x = self.Skalierung[0][0]
##         self.myobj.skalierung_y = self.Skalierung[0][1]
##         self.myobj.skalierung_z = self.Skalierung[0][2]
    
    @on_trait_change('Kurve')
    def update_kurve(self):
##         pass
	#eigentlich sollte ich hier wahrscheinlich die 100 kurvenpunkte berechnen lassen
        #und die dazugehoerigen daten, wie tangente, ...
##         self.myobj.tckp = tckp_berechnen(self.myobj.index_u, self.myobj.index_v, 3, 3)
##         self.myobj.kurve = mlab.plot3d(self.myobj.xnew, self.myobj.ynew, self.myobj.znew, tube_radius=0.005, color=(1,1,1))
##         if self.myobj.
        self.myobj.fig.children[2:] = []
        self.myobj.kurve_berechnen()

    @on_trait_change('Flaeche')
    def update_flaeche(self):
##         pass
##         mlab.clf()
##         self.myobj.fig.childeren[0:len(self.myobj.fig.childeren)] = []
        #diese if abfrage brauch ich spaeter um du differenzieren welche
        #flaeche angezeigt werden soll.
        self.myobj.fig.children[0:] = []
        ###########################################
        if self.Flaechen == 'parabolischer Zylinder':
            self.myobj = parabolischer_Zylinder(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'elliptischer Zylinder':
            self.myobj = elliptischer_Zylinder(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'hyperbolischer Zylinder':
            self.myobj = hyperbolischer_Zylinder(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'elliptisches Paraboloid':
            self.myobj = elliptisches_Paraboloid(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'hyperbolisches Paraboloid':
            self.myobj = hyperbolisches_Paraboloid(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'elliptischer Kegel':
            self.myobj = elliptischer_Kegel(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'Ellipsoid':
            self.myobj = Ellipsoid(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'einschaliges Hyperboloid':
            self.myobj = einschaliges_Hyperboloid(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'zweischaliges Hyperboloid':
            self.myobj = zweischaliges_Hyperboloid(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        elif self.Flaechen == 'Torus':
            self.myobj = Torus(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
        ###########################################
        self.myobj.flaeche_berechnen()
        self.Flaeche_anzeigen = bool('true')
        self.Kurvenpunkt = 0

####         if kugel:
####             self.myobj = Kugel(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
####         elif box:
####             self.myobj = Box(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
##         self.myobj.fig.children[0:] = []
##         self.myobj = Ellipsoid(self.Skalierung[0][0],self.Skalierung[0][1],self.Skalierung[0][2])
##         self.myobj.flaeche_berechnen()
####         self.myobj.fig.children[0:1] = []
####         self.myobj.fig.children[1:] = []
####         self.myobj.fig.on_mouse_pick(picker_callback)
##         #das alles wird jetzt in myobj berechnet und ist in der methode
##         #flaeche_berechnen
####         self.myobj.x_f_werte = self.myobj.x_f(self.myobj.u_f,self.myobj.v_f)
####        self.myobj.y_f_werte = self.myobj.y_f(self.myobj.u_f,self.myobj.v_f)
####         self.myobj.z_f_werte = self.myobj.z_f(self.myobj.u_f,self.myobj.v_f)
####         self.myobj.mesh = mlab.mesh(self.myobj.x_f_werte,self.myobj.y_f_werte,self.myobj.z_f_werte,color=(0.6,0.6,0.6))
##         self.Flaeche_anzeigen = bool('true')
#### 	flaeche_berechnen(self.myobj.index_u, self.myobj.index_v, 3, 3)
    
    @on_trait_change('Flaeche_anzeigen')
    def update_flaeche_anzeigen(self):
	self.myobj.mesh.set(visible=self.Flaeche_anzeigen)

    @on_trait_change('Dreibein')
    def update_dreibein(self):
        self.myobj.tangente.set(visible=self.Dreibein)
	self.myobj.hauptnormale.set(visible=self.Dreibein)
	self.myobj.binormale.set(visible=self.Dreibein)

    
    @on_trait_change('Tangente')
    def update_tangente(self):
        self.myobj.tangente.set(visible=self.Tangente)
    
    @on_trait_change('zweite_Ableitung')
    def update_ableitung2(self):
        self.myobj.ableitung2.set(visible=self.zweite_Ableitung)
    
    @on_trait_change('Hauptnormale')
    def update_hauptnormale(self):
        self.myobj.hauptnormale.set(visible=self.Hauptnormale)
    
    @on_trait_change('Binormale')
    def update_binormale(self):
        self.myobj.binormale.set(visible=self.Binormale)
    
    @on_trait_change('Flaechen_Tangente_u')
    def update_tangente_fu(self):
        self.myobj.tangente_fu.set(visible=self.Flaechen_Tangente_u)

    @on_trait_change('Flaechen_Tangente_v')
    def update_tangente_fv(self):
        self.myobj.tangente_fv.set(visible=self.Flaechen_Tangente_v)
    
    @on_trait_change('Flaechen_Normale')
    def update_normale_f(self):
        self.myobj.normale_f.set(visible=self.Flaechen_Normale)
    
    @on_trait_change('Normalkruemmung')
    def update_normalkruemmung(self):
        self.myobj.normalkruemmung.set(visible=self.Normalkruemmung)
    
    ############################### neu
    @on_trait_change('Kruemmung')
    def update_kruemmung(self):
        self.myobj.kruemmung.set(visible=self.Kruemmung)
    
    @on_trait_change('geodaetische_Kruemmung')
    def update_geodaetischekruemmung(self):
        self.myobj.geodaetischekruemmung.set(visible=self.geodaetische_Kruemmung)
    ############################### neu ende
    
    @on_trait_change('Ebenen')
    def update_ebenen(self):
        self.myobj.normalebene.set(visible=self.Ebenen)
        self.myobj.schmiegebene.set(visible=self.Ebenen)
        self.myobj.rektifizierendeebene.set(visible=self.Ebenen)
        self.myobj.tangentialebene_f.set(visible=self.Ebenen)
    
##     @on_trait_change('Flaeche2')
##     def update_flaeche2(self):
##         self.myobj.mesh.set(visible=self.Flaeche2)
    
    @on_trait_change('Schmiegebene')
    def update_schmiegebene(self):
        self.myobj.schmiegebene.set(visible=self.Schmiegebene)
    
    @on_trait_change('Normalebene')
    def update_normalebene(self):
        self.myobj.normalebene.set(visible=self.Normalebene)
    
    @on_trait_change('rektifizierende_Ebene')
    def update_rektifizierende(self):
        self.myobj.rektifizierendeebene.set(visible=self.rektifizierende_Ebene)
    
    @on_trait_change('Tangentialebene')
    def update_tangentialebene(self):
        self.myobj.tangentialebene_f.set(visible=self.Tangentialebene)
    
    @on_trait_change('Kurvenpunkt')
    def update_kurvenpunkt(self):
##         self.vektor.mlab_source.set(x=xnew[vektor.punkte], y=ynew[vektor.punkte],z=znew[vektor.punkte],u=a_n[vektor.punkte], v=b_n[vektor.punkte], w=c_n[vektor.punkte])
##         punkt(self.tangente,self.ableitung2,self.hauptnormale,self.binormale,self.tangente_fu,self.tangente_fv,self.normale_f,self.normalkruemmung,self.normalebene,self.schmiegebene,self.rektifizierendeebene,self.tangentialebene_f,self.Kurvenpunkt)
	punkt(self.myobj, self.Kurvenpunkt)

    #die bezeichnung der extra gui.
    #die x_min, ... muessen anscheinend auch die variablennamen sein.
    view = View(Item(name='Flaechen', label = 'Flaechen'),
                Item(name='Skalierung', label='Skalierung x,y,z'),
                Item(name='Flaeche', label='Flaeche'),
                Item(name='Flaeche_anzeigen', label='Flaeche anzeigen'),
                '_',
                Item(name='Kurve'),
                Item(name='Dreibein'),
                Item(name='Tangente'),
                Item(name='zweite_Ableitung', label='zweite Ableitung'),
                Item(name='Hauptnormale'),
                Item(name='Binormale'),
                Item(name='Flaechen_Tangente_u', label='Flaechentangente u'),
                Item(name='Flaechen_Tangente_v', label='Flaechentangente v'),
                Item(name='Flaechen_Normale', label='Flaechennormale'),
                ######################## neu
                Item(name='Kruemmung', label='Flaechenkruemmung'),
                ######################## neu ende
                Item(name='Normalkruemmung'),
                ######################## neu
                Item(name='geodaetische_Kruemmung', label='geodaetische Kruemmung'),
                ######################## neu ende
                '_',
                Item(name='Ebenen'),
                Item(name='Schmiegebene'),
                Item(name='Normalebene'),
                Item(name='rektifizierende_Ebene', label='rektifizierende Ebene'),
                Item(name='Tangentialebene', label='Tangentialebene der Flaeche'),
                '_',
                'Kurvenpunkt', title='My GUI', resizable=True)
    #show_label
##     view = View(Item('Kurve', show_label=False), 'Flaeche', 'Dreibein', 'Tangente', 'zweite_Ableitung', 'Hauptnormale', 'Binormale', 'Flaechen_Tangente_u', 'Flaechen_Tangente_v', 'Flaechen_Normale', 'Normalkruemmung', 'Ebenen', 'Schmiegebene', 'Normalebene', 'rektifizierende_Ebene', 'Tangentialebene', 'Kurvenpunkt', title='My GUI', resizable=True)
##     view = View('Kurvenpunkt', 'Flaeche', 'Dreibein', 'Ebenen', title='My GUI', resizable=True)


################################################################################
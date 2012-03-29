from enthought.mayavi import mlab
from numpy import array

def ebene(x,y,z,u1,v1,w1,u2,v2,w2,rgb,ii,myname):
    px1,py1,pz1 = [u1[ii]+u2[ii]+x[ii],x[ii]],[v1[ii]+v2[ii]+y[ii],y[ii]],[w1[ii]+w2[ii]+z[ii],z[ii]]
    px2,py2,pz2 = [u1[ii]-u2[ii]+x[ii],x[ii]],[v1[ii]-v2[ii]+y[ii],y[ii]],[w1[ii]-w2[ii]+z[ii],z[ii]]
    px3,py3,pz3 = [-u1[ii]-u2[ii]+x[ii],x[ii]],[-v1[ii]-v2[ii]+y[ii],y[ii]],[-w1[ii]-w2[ii]+z[ii],z[ii]]
    px4,py4,pz4 = [-u1[ii]+u2[ii]+x[ii],x[ii]],[-v1[ii]+v2[ii]+y[ii],y[ii]],[-w1[ii]+w2[ii]+z[ii],z[ii]]
    px = array([px1,px2,px3,px4,px1])
    py = array([py1,py2,py3,py4,py1])
    pz = array([pz1,pz2,pz3,pz4,pz1])
    return mlab.mesh(px,py,pz,color=rgb,opacity=0.5,name=myname)

def punkt(myobj,ii):
    #Alle Vektoren
    myobj.tangente.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.a_n[ii], v=myobj.b_n[ii], w=myobj.c_n[ii])
    myobj.ableitung2.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.d_n[ii], v=myobj.e_n[ii], w=myobj.f_n[ii])
    myobj.hauptnormale.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.j_n[ii], v=myobj.k_n[ii], w=myobj.l_n[ii])
    myobj.binormale.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.g_n[ii], v=myobj.h_n[ii], w=myobj.i_n[ii])
    myobj.tangente_fu.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.u1_n[ii], v=myobj.u2_n[ii], w=myobj.u3_n[ii])
    myobj.tangente_fv.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.v1_n[ii], v=myobj.v2_n[ii], w=myobj.v3_n[ii])
    myobj.normale_f.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.uv1_n[ii], v=myobj.uv2_n[ii], w=myobj.uv3_n[ii])
    myobj.normalkruemmung.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.kn_nf[0][ii], v=myobj.kn_nf[1][ii], w=myobj.kn_nf[2][ii],scale_factor=myobj.k_nf[ii])
    ############################# neu
##     myobj.kruemmung.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.d_n[ii], v=myobj.e_n[ii], w=myobj.f_n[ii])
##     myobj.geodaetischekruemmung.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.kg[0][ii], v=myobj.kg[1][ii], w=myobj.kg[2][ii],scale_factor=myobj.kg_laenge[ii])
    myobj.geodaetischekruemmung.mlab_source.set(x=myobj.xnew[ii], y=myobj.ynew[ii],z=myobj.znew[ii],u=myobj.kg[0][ii], v=myobj.kg[1][ii], w=myobj.kg[2][ii])
    ############################# neu ende
    #Alle Ebenen
    #pxn[...,0] = pxn[:,:,0] = pxn.T[0].T
    myobj.normalebene.mlab_source.set(x=myobj.epxn[...,ii],y=myobj.epyn[...,ii],z=myobj.epzn[...,ii])
    myobj.schmiegebene.mlab_source.set(x=myobj.epxs[...,ii],y=myobj.epys[...,ii],z=myobj.epzs[...,ii])
    myobj.rektifizierendeebene.mlab_source.set(x=myobj.epxr[...,ii],y=myobj.epyr[...,ii],z=myobj.epzr[...,ii])
    myobj.tangentialebene_f.mlab_source.set(x=myobj.epxt[...,ii],y=myobj.epyt[...,ii],z=myobj.epzt[...,ii])

## def punkt(tangente,ableitung2,hauptnormale,binormale,tangente_fu,tangente_fv,normale_f,normalkruemmung,normalebene,schmiegebene,rektifizierendeebene,tangentialebene_f,ii):
##     #Alle Vektoren
##     tangente.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=a_n[ii], v=b_n[ii], w=c_n[ii])
##     ableitung2.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=d_n[ii], v=e_n[ii], w=f_n[ii])
##     hauptnormale.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=j_n[ii], v=k_n[ii], w=l_n[ii])
##     binormale.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=g_n[ii], v=h_n[ii], w=i_n[ii])
##     tangente_fu.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=u1_n[ii], v=u2_n[ii], w=u3_n[ii])
##     tangente_fv.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=v1_n[ii], v=v2_n[ii], w=v3_n[ii])
##     normale_f.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=uv1_n[ii], v=uv2_n[ii], w=uv3_n[ii])
##     normalkruemmung.mlab_source.set(x=xnew[ii], y=ynew[ii],z=znew[ii],u=kn_nf[0][ii], v=kn_nf[1][ii], w=kn_nf[2][ii],scale_factor=k_nf[ii])
##     #Alle Ebenen
##     #pxn[...,0] = pxn[:,:,0] = pxn.T[0].T
##     normalebene.mlab_source.set(x=pxn[...,ii],y=pyn[...,ii],z=pzn[...,ii])
##     schmiegebene.mlab_source.set(x=pxs[...,ii],y=pys[...,ii],z=pzs[...,ii])
##     rektifizierendeebene.mlab_source.set(x=pxr[...,ii],y=pyr[...,ii],z=pzr[...,ii])
##     tangentialebene_f.mlab_source.set(x=pxt[...,ii],y=pyt[...,ii],z=pzt[...,ii])
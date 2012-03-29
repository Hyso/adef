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

extent_dialog = ExtentDialog(myobj=myobj)
# We need to use 'edit_traits' and not 'configure_traits()' as we do
# not want to start the GUI event loop (the call to mlab.show())
# at the end of the script will do it.
extent_dialog.edit_traits()

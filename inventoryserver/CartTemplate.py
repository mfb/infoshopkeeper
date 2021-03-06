#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Skeleton import Skeleton

##################################################
## MODULE CONSTANTS
try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.0.1'
__CHEETAH_versionTuple__ = (2, 0, 1, 'final', 0)
__CHEETAH_genTime__ = 1309384747.4918439
__CHEETAH_genTimestamp__ = 'Wed Jun 29 17:59:07 2011'
__CHEETAH_src__ = 'CartTemplate.html'
__CHEETAH_srcLastModified__ = 'Sun Apr 18 18:16:51 2010'
__CHEETAH_docstring__ = 'Autogenerated by CHEETAH: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class CartTemplate(Skeleton):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        Skeleton.__init__(self, *args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def pagetitle(self, **KWS):



        ## CHEETAH: generated from #def pagetitle at line 4, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''Your current cart:
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def body(self, **KWS):



        ## CHEETAH: generated from #def body at line 8, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''<h1>Your cart currently contains:</h1>
<a class="close" href="javascript:window.close()">X</a>
<form action="/addtocart">
<table>
''')
        for q in VFFSL(SL,"quantities",True): # generated from line 13, col 1
            write('''<tr><td><input type="text" width="3" name="select_x_like_''')
            _v = VFN(VFFSL(SL,"q",True)[0],"id",True) # '${q[0].id}' on line 14, col 58
            if _v is not None: write(_filter(_v, rawExpr='${q[0].id}')) # from line 14, col 58.
            write('''" value="''')
            _v = VFFSL(SL,"q",True)[1] # '${q[1]}' on line 14, col 77
            if _v is not None: write(_filter(_v, rawExpr='${q[1]}')) # from line 14, col 77.
            write('''" /></td><td>''')
            _v = VFN(VFFSL(SL,"q",True)[0],"title.booktitle",True) # '${q[0].title.booktitle}' on line 14, col 97
            if _v is not None: write(_filter(_v, rawExpr='${q[0].title.booktitle}')) # from line 14, col 97.
            write('''</td></tr>
''')
        write('''</table>
<input type="hidden" name="reset_quantities" value="true" />
<input class="submit-inline" type="submit" name="update" value="update quantities"/>
<input class="submit-inline" type="submit" name="checkout" value="checkout" />
</form>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''

''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_CartTemplate= 'writeBody'

## END CLASS DEFINITION

if not hasattr(CartTemplate, '_initCheetahAttributes'):
    templateAPIClass = getattr(CartTemplate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(CartTemplate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=CartTemplate()).run()



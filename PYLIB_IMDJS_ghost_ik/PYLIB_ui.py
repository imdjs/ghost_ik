
import bpy
from bpy.props import *
# from ctypes import c_int,c_void_p;
# import PYLIB.LG as LG;
# from .PYLIB_object import SetMode;
# from .PYLIB_find import mod罒;

def 仌厶0(self, context):
	if(self.bp0):
		self.icon0="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon0='DISCLOSURE_TRI_DOWN';
def 仌厶1(self, context):
	if(self.bp1):
		self.icon1="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon1='DISCLOSURE_TRI_DOWN';
def 仌厶2(self, context):
	if(self.bp2):
		self.icon2="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon2='DISCLOSURE_TRI_DOWN';
def 仌厶3(self, context):
	if(self.bp3):
		self.icon3="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon3='DISCLOSURE_TRI_DOWN';
def 仌厶4(self, context):
	if(self.bp4):
		self.icon4="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon4='DISCLOSURE_TRI_DOWN';
		
def 仌厶5(self, context):
	if(self.bp5):
		self.icon5="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon5='DISCLOSURE_TRI_DOWN';
def 仌厶6(self, context):
	if(self.bp6):
		self.icon6="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon6='DISCLOSURE_TRI_DOWN';
def 仌厶7(self, context):
	if(self.bp7):
		self.icon7="DISCLOSURE_TRI_RIGHT";
	else:
		self.icon7='DISCLOSURE_TRI_DOWN';
# def 仌厶8(self, context):
	# if(self.bp8):
		# self.icon8="DISCLOSURE_TRI_RIGHT";
	# else:
		# self.icon8='DISCLOSURE_TRI_DOWN';
# def 仌厶9(self, context):
	# if(self.bp9):
		# self.icon9="DISCLOSURE_TRI_RIGHT";
	# else:
		# self.icon9='DISCLOSURE_TRI_DOWN';
# def 仌厶10(self, context):
	# if(self.bp10):
		# self.icon10="DISCLOSURE_TRI_RIGHT";
	# else:
		# self.icon10='DISCLOSURE_TRI_DOWN';
#====界面厶,pp厶==========================================
class 厶PropertyGroup(bpy.types.PropertyGroup):
	bp0:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶0);
	icon0:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	bp1:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶1);
	icon1:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');	
	bp2:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶2);
	icon2:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	bp3:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶3);
	icon3:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');	
	bp4:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶4);
	icon4:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	bp5:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶5);
	icon5:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	bp6:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶6);
	icon6:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	bp7:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶7);
	icon7:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	# bp8:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶8);
	# icon8:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	# bp9:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶9);
	# icon9:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
	# bp10:BoolProperty(name="",description="",default=False,subtype='NONE',update=仌厶10);
	# icon10:StringProperty(name='',description='',default='DISCLOSURE_TRI_DOWN');
bpy.utils.register_class(厶PropertyGroup) ;

	

	
	
    
    

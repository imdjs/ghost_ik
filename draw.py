import bpy,sys
from bpy.props import BoolProperty,StringProperty;
from ctypes import c_int,c_void_p


if("IMDJS_ghost_ik.G" in sys.modules):
	Gik = sys.modules["IMDJS_ghost_ik.G"];
else:
	import IMDJS_ghost_ik.G as Gik;
	
try:
	from PYLIB.PYLIB_draw import 灬gl乚,灬gl数据,灬gl乚2d,灬gl数据2d,py_叵画,卐画3dlib卐Operator,LG,画3d;
except:
	from .PYLIB_IMDJS_ghost_ik.PYLIB_draw import 灬gl乚,灬gl数据,灬gl乚2d,灬gl数据2d,py_叵画,卐画3dlib卐Operator,LG,画3d;


#==================================================
class 卐画3dik卐Operator(卐画3dlib卐Operator):
	bl_idname = "op.draw_3d_ik"
	bl_label = "draw_3d_ik"
	bl_description = "draw_3d_ik"
	
	def invoke(self, context, event):
		if(self.bp显示 and Gik.卍dll.dll==None):
			# self.report({"ERROR"},"Gik.卍dll.dll==None,%p"%id(Gik));#"INFO" "ERROR" "DEBUG" "WARNING"
			self.report({"ERROR"},"Gik.卍dll.dll==None");
			return {"FINISHED"};
		self.十十乚(context,event,Gik);
		return {"FINISHED"}; 
bpy.utils.register_class(卐画3dik卐Operator);


#========================================
def 画3dOP(bp显示,bp画面=True,bp画丷=False,bp画弓=False,bp画m=True,ip画字=1,bp灬=True):
	bpy.ops.op.draw_3d_ik("INVOKE_DEFAULT",bp显示=bp显示,bp画弓=bp画弓,bp画面=bp画面,bp画丷=bp画丷,bp画m=bp画m,ip画字=ip画字);
	
	
	
	
	
	
	
	

from ctypes import *

def 凷cvp(LG_,context):
	LG_.cvpC=c_void_p(context.as_pointer());LG_.oA=context.active_object;LG_.cvpA=c_void_p(LG_.oA.as_pointer());LG_.cvpSC= c_void_p(context.scene.as_pointer());LG_.pbA=context.active_pose_bone;
	print("凷cvp ==",id(LG_),LG_.cvpC);


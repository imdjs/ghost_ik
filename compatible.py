

# from .G import 语,LG;
# from .func import*
# from .__init__ import bl_info
# from .func import 十十fcurve1o
from ctypes import c_float;

#==================================================
def Δ仌2022物理骨(o,context):
	# scene=context.scene;
	from .__init__ import bl_info;# ● 必须在里面
	# print("o.ppO.ivp3版本!=bl_info[version]==",o.name,o.ppO.ivp3版本!=bl_info["version"]);
	# wm=context.window_manager;
	if(o.type=="ARMATURE"):# and 卩二二版本(o,bl_info)==False
		Cpb=o.pose.bones;#print("Cpb==",Cpb.__len__());
		for pb in Cpb:
			# print("keys()==",pb.name,pb["PoseBone"].keys(),"PoseBone" in pb);
			if("PoseBone" in pb):
				print("head==","head" in pb["PoseBone"],pb["PoseBone"].keys());
				if("head" in pb["PoseBone"]):
					pb["PoseBone"]["head"]=(c_float*3)(*pb["PoseBone"]["head"]);
				if("tail" in pb["PoseBone"]):
					pb["PoseBone"]["tail"]=(c_float*3)(*pb["PoseBone"]["tail"]);	print("tail==",pb.name,*pb["PoseBone"]["tail"]);			
				if("p" in pb["PoseBone"]):
					pb["PoseBone"]["p"]=(c_float*3)(*pb["PoseBone"]["p"]);
				if("e" in pb["PoseBone"]):
					pb["PoseBone"]["e"]=(c_float*3)(*pb["PoseBone"]["e"]);
				if("q" in pb["PoseBone"]):
					pb["PoseBone"]["q"]=(c_float*4)(*pb["PoseBone"]["q"]);					
				if("s" in pb["PoseBone"]):
					pb["PoseBone"]["s"]=(c_float*3)(*pb["PoseBone"]["s"]);					
				if("f16mι" in pb["PoseBone"]):
					pb["PoseBone"]["f16mι"]=(c_float*16)(*pb["PoseBone"]["f16mι"]);	
				if("脚跟ι" in pb["PoseBone"]):
					pb["PoseBone"]["脚跟ι"]=(c_float*3)(*pb["PoseBone"]["脚跟ι"]);	
				if("z地" in pb["PoseBone"]):
					pb["PoseBone"]["z地"]=(c_float*3)(*pb["PoseBone"]["脚跟ι"]);						
		# 二版本(o,bl_info);#print("bl_info==",卩二二版本(o,bl_info));
# ////END////END////END////END////END////END////END////END////


	


	
	

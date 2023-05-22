import bpy
import copy
import os,sys;
from ctypes import c_float,c_int,c_void_p;


dllpathIK64 = os.path.abspath("%s/ghost_ik64.dll" % os.path.dirname(__file__));#● 必须用英文名,否则bl安装变乱码
dllpathIK64B ="B:/ghost_ik64.dll" 
# dllpathIK64B ="B:/ghost_ik64 - 副本.dll" 

# print("os.path.exists文件夹此ghost+",os.path.exists(os.path.dirname(__file__)+"\\LANG.py"),os.path.dirname(__file__)+"\\LANG.py");
if (os.path.exists(os.path.dirname(__file__)+"\\LANG.py")):  # 如果文件存在
    os.remove(os.path.dirname(__file__)+"\\LANG.py") ;
	#os.unlink(path);这个也可以

文件夹此ghost=os.path.basename(os.path.dirname(__file__));	
if(文件夹此ghost+".LANG.LANG" in sys.modules):
	语=sys.modules[文件夹此ghost+".LANG.LANG"];
else:
	exec("import "+文件夹此ghost+".LANG.LANG as 语");#√

# wm=bpy.context.window_manager;
# wm["s物理骨dll路径B"]="B:/PHYSIC64.dll".encode('UTF-8');
# wm["s物理骨dll路径B"]="B:/PHYSIC64.dll";#√
# wm["s物理骨dll路径B"]= c_wchar_p("B:/PHYSIC64.dll");#Χ
# wm["s物理骨dll路径"]=(os.path.dirname(__file__)+"/PHYSIC64.dll")#.encode('UTF-8');

# wm["s修正骨dll路径B"]="B:/CORRECT64.dll";#√
# wm["s修正骨dll路径"]=(os.path.dirname(__file__)+"/CORRECT64.dll")#.encode('UTF-8');
#------------------------------
try:
	from PYLIB.LG import*;
except:
	from .PYLIB_IMDJS_ghost_ik.LG import*;

from .func import bg罒骨组,col紫;
#------------------------------
Limdjs驱动=["2Y_Shoulder_L","2Y_Shoulder1_L","2Y_Shoulder2_L"
		,"2T_Farm_L","2T_Farm_R","2Y_Shoulder_R","2Y_Shoulder1_R","2Y_Shoulder2_R","2R_Arm_L","2R_Arm_R","2T_Arm_L","2T_Arm_R"
		,"2Y_ArmF_L","2Y_ArmF1_L","2Y_ArmF2_L","2Y_ArmF_R","2Y_ArmF1_R","2Y_ArmF2_R","2Y_ArmB_L","2Y_ArmB1_L","2Y_ArmB2_L","2Y_ArmB_R","2Y_ArmB1_R","2Y_ArmB2_R"
		,"2Y_ArmO_L","2Y_ArmO1_L","2Y_ArmO2_L","2Y_ArmO_R","2Y_ArmO1_R","2Y_ArmO2_R"
		,"2Y_ArmOO_L","2Y_ArmOO1_L","2Y_ArmOO2_L","2Y_ArmOO_R","2Y_ArmOO1_R","2Y_ArmOO2_R"
		,"2Y_Farm_L","2Y_Farm1_L","2Y_Farm_R","2Y_Farm1_R","2R_Hand_L","2R_Hand_R"
		,"3R_Hip_L","3R_Hip_R","3T_Thigh_L","3T_Thigh_R"
		,"3Y_ThighFF_L","3Y_ThighFF1_L","3Y_ThighFF2_L","3Y_ThighFF_R","3Y_ThighFF1_R","3Y_ThighFF2_R"
		,"3Y_ThighF_L","3Y_ThighF1_L","3Y_ThighF2_L","3Y_ThighF_R","3Y_ThighF1_R","3Y_ThighF2_R","3Y_ThighI_L","3Y_ThighI1_L","3Y_ThighI2_L","3Y_ThighI_R","3Y_ThighI1_R","3Y_ThighI2_R","3Y_ThighB_L","3Y_ThighB1_L","3Y_ThighB2_L","3Y_ThighB_R","3Y_ThighB1_R","3Y_ThighB2_R"
		,"3Y_ThighIB_L","3Y_ThighIB1_L","3Y_ThighIB2_L","3Y_ThighIB_R","3Y_ThighIB1_R","3Y_ThighIB2_R"
		,"3T_Shin_L","3T_Shin_R"
		,"3R_Foot_L","3R_Foot_R"
		,"Sarm_L","Sarm_R","2Y_Breast_L","2Y_Breast_R"
		,"0R_Head","0R_Neck","1R_Chest","1R_Waist"
		];
		
L=["2Shoulder_L","2Arm_L","2Shoulder_R","2Arm_R","2Forearm_L","2Hand_L","2Forearm_R","2Hand_R","3Thigh_L","1Hip","3Foot_L","3Shin_L","3Foot_R","3Shin_R"
		,"IK_Forearm_L","IK_Forearm_R",];

# L宇驱动=("lCollar","lShldrBend","rCollar","rShldrBend"
	# ,"lForearmBend","lHand","rForearmBend","rHand"
	# ,"lThighBend","pelvis","rThighBend","pelvis"
	# ,"lMetatarsals","lShin","rMetatarsals","rShin"
	# );
#------------------------------
L卐骷物理=[];b烘焙G=False;b首尾插值=False;i多少帧=0;b初次G=False;
卍dll=卐DLL();
卐o骷=None;L卐o修正骷=[];

bModalG=False;
# 乚3d=None;乚2d=None;
MpbPRS={};Ms申={};Ms向={};
sp警告G="";
#====IK==========================
MoLpbIKG={};
def Δ仌约束(b,oA,dll,MoLpbIKG):
	print("Δ仌约束==",b,oA);
	if(oA):
		if(oA not in MoLpbIKG):
			MoLpbIKG[oA]=[];
		LpbIK=MoLpbIKG[oA];
		if(LpbIK==[]):
			for pb in oA.pose.bones:
				if(0<pb.constraints.__len__()):
					if(pb.constraints[0].type in["IK","COPY_ROTATION","TRACK_TO"] ):
						LpbIK.append(pb);print("++pb==",pb.name);
		#------------------------------					
		if(b==False):
			for pb in LpbIK:
				pb.constraints[0].enabled=False;
				if(1<pb.constraints.__len__()):
					pb.constraints[1].enabled=False;

		else:
			dll.凸仌约束(c_void_p(oA.as_pointer()));#IMDJS_pose_collector\Global_var.h
			for pb in LpbIK:
				pb.constraints[0].enabled=True;
			if(1<pb.constraints.__len__()):
				pb.constraints[1].enabled=True;

ci丌播放G=c_int();



#========================================
class 卐O:
	o=None;ψ=None;
	def __init__(self,o_):
		self.o=o_;self.ψ=c_void_p(o_.as_pointer());
	
	def __del__(self):
		if(self.o):
			self.o=None;self.ψ=None;

	

def 凷键(键,o,属性=None):
	if(键 not in o):
		if(属性):
			o[键]=属性;
		else:
			o[键]={};
			


	
	
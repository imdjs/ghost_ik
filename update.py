
import	bpy,sys,os
from ctypes import*
from bpy.app.handlers import persistent

文件夹此IK=os.path.basename(os.path.dirname(__file__));#IMDJS_green_land
if(文件夹此IK+".G" in sys.modules):
	Gik=sys.modules[文件夹此IK+".G"];
else:
	exec("import "+文件夹此IK+".G as Gik");#√
	
dllpathIK64 = os.path.abspath("%s/ghost_ik64.dll" % os.path.dirname(__file__));
dllpathIK64B ="B:/ghost_ik64.dll" 

print("dllpathIK64==",dllpathIK64);
# from PYLIB.PYLIB_animation import 丨巜帧;	
try:
	from PYLIB.PYLIB_draw import *;
	from PYLIB.PYLIB_module import dll载入dll;	
	from PYLIB.PYLIB_animation import 丨巜帧;	
except:	   
	exec("from	"+".PYLIB_"+Gik.文件夹此ghost+".PYLIB_"+Gik.文件夹此ghost+"	 import*");
	exec("from "+文件夹此IK+".PYLIB_"+文件夹此IK+".PYLIB_draw"+"  import*");
	exec("from "+文件夹此IK+".PYLIB_"+文件夹此IK+".PYLIB_animation"+"  import 丨巜帧");
	
from .func import Δ重填Lo物理骨,Δ十IK组,bg罒骨组,col红,col灰蓝,col绿,col浅绿,col黄,iΔ叵Cpb,Δ叵scene,Δ一一无效列表物,Δ乙卍dll,丌播放,Δ一一ik;
from IMDJS_ghost_ik.G import  TYPE_无,TYPE_SPLINE,TYPE_TWO孙子,TYPE_TWO孙,TYPE_TWO子,TYPE_TWO父,TYPE_TWO爷,TYPE_物理,TYPE_布料,dllpathIK64B,dllpathIK64;
from .draw import 画3dOP;
from .bake import Δ0乛烘焙物理骨;


# def Δ同步pb参数(f参数,)

def Δ仌勾选本键(self, context): 
	Lkc=[None,None,None];
	Lkc[0]= bpy.context.window_manager.keyconfigs.addon;
	Lkc[1]= bpy.context.window_manager.keyconfigs.user;
	Lkc[2]= bpy.context.window_manager.keyconfigs.default;
	for kc in Lkc:
		if(kc):
			for LsKC in LLsKC类别:
				km = kc.keymaps.find(LsKC[0]);#Pose模式按键
				if(km):
					Ckmi全部=km.keymap_items;#全部键丅
					Lkeys=Ckmi全部.keys();
					for kmi全部 in Ckmi全部:
						for i项 in LsKC[3]:#[0,1,2,3,4,5,6,7]
							Ms类别id与按键 = LMs类别id与按键[i项];#{"idname":"ghost_ik.pin","type":"D","value":"PRESS",  "any":False,	"shift":False,"ctrl":False, "alt":True, "oskey":False,"head":False,"properties":{}}
							if(Ms类别id与按键["idname"] in Lkeys):
								if (kmi全部.type ==Ms类别id与按键["type"]):
									if(context.scene.ghost_ik.bp用ghost_ik==False ):	 
										kmi全部.active=False;
									else:
										kmi全部.active=True;
	#print("bpy.app.handlers.frame_change_post==",bpy.app.handlers.frame_change_post,Δ刷新动力骨Post in bpy.app.handlers.frame_change_post);self==True and 
	if(Δ刷新动力骨Post  not in bpy.app.handlers.frame_change_post):
		bpy.app.handlers.frame_change_post.append(Δ刷新动力骨Post);
		print("++ add frame_change_post==",);
		
def Δ仌itype(self, context): 
	oA=context.pose_object;
	if(oA.ppO.init==0):
		Δ叵Cpb(context);
	Δ十一IKgroupp(self,context);
	bpy.ops.op.set_bone_type("INVOKE_DEFAULT",spType=self.epIkType);#●●INVOKE_DEFAULT 是可以弹出菜单
	#print("Δ仌itype==",);

def Δ仌重力因子(self, context): 
	# return;
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		#print("update ==",Gik.pbA);
		Gik.pbA=context.active_pose_bone;
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(Gik.pbA);
		for pb in CpbS:
			if(pb==Gik.pbA):continue;
			pb.ghost_ik.fp重力fac=self.fp重力fac;
		Gik.pbA=None;
		LG.b丌仌=False;	
		
def Δ仌丨小(self, context): 
	# return;
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		#print("update ==",Gik.pbA);
		if(Gik.pbA == None):
			Gik.pbA=context.active_pose_bone;
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(Gik.pbA);
		for pb in CpbS:
			if(pb==Gik.pbA):continue;
			pb.ghost_ik.fvp丨小=self.fvp丨小;
		Gik.pbA=None;
		LG.b丌仌=False;		
		
def Δ仌刚性(self, context): 
	# return;
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		#print("update ==",Gik.pbA);
		if(Gik.pbA == None):
			Gik.pbA=context.active_pose_bone;
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(Gik.pbA);
		for pb in CpbS:
			if(pb==Gik.pbA):continue;
			pb.ghost_ik.fp刚性=self.fp刚性;
		Gik.pbA=None;
		LG.b丌仌=False;
		
def Δ仌弹性(self, context): 
	# return;
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		#print("update ==",Gik.pbA);
		Gik.pbA=context.active_pose_bone;
		# if(Gik.pbA.ghost_ik.fp弹性==self.fp弹性):
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(Gik.pbA);
		for pb in CpbS:
			if(pb==Gik.pbA):continue;
			pb.ghost_ik.fp弹性=self.fp弹性;
		Gik.pbA=None;	
		LG.b丌仌=False;
		
def Δ仌恢复(self, context): 
	# return;
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		#print("update ==",Gik.pbA);
		Gik.pbA=context.active_pose_bone;
		# if(Gik.pbA.ghost_ik.fp恢复==self.fp恢复):
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(Gik.pbA);
		for pb in CpbS:
			if(pb==Gik.pbA):continue;
			pb.ghost_ik.fp恢复=self.fp恢复;
		Gik.pbA=None;	
		LG.b丌仌=False;
"""
def Δ仌弹性类型(self, context): 
	if(LG.b丌仌==False):
		#print("update benditype==",Gik.pbA);
		if(Gik.pbA == None):
			Gik.pbA=context.active_pose_bone;
			if(Gik.pbA.ghost_ik.ip弹性类型==self.ip弹性类型):
				CpbS=context.selected_pose_bones_from_active_object;
				
				if(1<Gik.pbA and CpbS.__len__()):
					for pb in CpbS:
						if(pb==Gik.pbA):continue;
						pb.ghost_ik.ip弹性类型=self.ip弹性类型;
			Gik.pbA=None;
"""

def Δ仌扭性(self, context): 
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		Gik.pbA=context.active_pose_bone;
		# if(Gik.pbA	and Gik.pbA.ghost_ik.fp扭性==self.fp扭性):
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(Gik.pbA);
		for pb in CpbS:
			if(pb==Gik.pbA):continue;
			pb.ghost_ik.fp扭性=self.fp扭性;
		Gik.pbA=None;
		LG.b丌仌=False;
		
# ㄥ89=1.562f;
#ㄥ179    3.13286f

#----pin--------------------------
def Δ十钉组(context,pbA):
	pose=context.object.pose;Cbg=pose.bone_groups;print("Δ十钉组==",pbA.ghost_ik.type)
	bg钉=bg罒骨组(context,Cbg,"spline-IK-pin",col红);
	if(pbA.ghost_ik.type in[TYPE_TWO子,TYPE_SPLINE,TYPE_物理,TYPE_布料]):
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(pbA);
		for pb in CpbS:
			if(pb.ghost_ik.type in[TYPE_TWO子,TYPE_SPLINE,TYPE_物理,TYPE_布料]):
				pb.bone_group=bg钉;
				if(pb.ghost_ik.type ==TYPE_TWO子 and "d16m钉子"not in pb):
					pb["d16m钉子"]=[-999.0]*16;#为了 节点的ik钉子
					
def Δ一钉组(context,pbA):
	pose=context.object.pose;Cbg=pose.bone_groups;print("Δ一钉组==",pbA.name);
	bg原来=None;
	# if(pbA.ghost_ik.type==TYPE_TWO孙):
		# bg原来=bg罒骨组(context,Cbg,"two-IK-grandson",col浅绿);
	if(pbA.ghost_ik.type==TYPE_TWO子):
		bg原来=bg罒骨组(context,Cbg,"two-IK-child",col绿);
	elif(pbA.ghost_ik.type==TYPE_SPLINE):
		bg原来=bg罒骨组(context,Cbg,"spline-IK",col灰蓝);
	elif(pbA.ghost_ik.type==TYPE_物理):
		bg原来=bg罒骨组(context,Cbg,"physical-IK",col黄);	
	elif(pbA.ghost_ik.type==TYPE_布料):
		bg原来=bg罒骨组(context,Cbg,"cloth-IK",col黄);
	#----变回原来颜色--------------------------
	if(pbA.ghost_ik.type in[TYPE_TWO子,TYPE_SPLINE,TYPE_物理,TYPE_布料]):
		CpbS=context.selected_pose_bones_from_active_object;
		if(CpbS==[]):CpbS.append(pbA);
		for pb in CpbS:
			if(pb.ghost_ik.type in[TYPE_TWO子,TYPE_SPLINE,TYPE_物理,TYPE_布料]):
				pb.bone_group=bg原来;
				
#========================================
def Δ仌钉头(self, context): 
	print("Δ仌钉头==",LG.b丌仌);
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		Δ乙卍dll();
		Gik.pbA=context.active_pose_bone;
		# if(Gik.pbA.ghost_ik.type==TYPE_TWO子):
			# Gik.卍dll.dll.凸十十钉子(c_void_p(Gik.pbA.as_pointer()));
		CpbS=context.selected_pose_bones_from_active_object;#print("Gik.pbA==",Gik.pbA);
		if(CpbS==[]):CpbS.append(Gik.pbA);
		for pb in CpbS:
			pb["PoseBone"]["b钉"]=pb.ghost_ik.bp钉=self.bp钉;	
			if(pb.ghost_ik.type==TYPE_TWO子):		
				# Gik.卍dll.dll.凸十十钉子(c_void_p(pb.as_pointer()));
				Gik.卍dll.dll.凸乙申(c_void_p(context.as_pointer()),False);
			
		#Δ十一IKgroupp(self,context);
		if(self.bp钉==False):
			Δ一钉组(context,Gik.pbA);
		else:
			Δ十钉组(context,Gik.pbA);
		Gik.pbA=None;

		LG.b丌仌=False;
		
def Δ仌传递(self, context): 
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		#print("update INHERIT==",self.name);
		Δ乙卍dll();
		Gik.卍dll.dll.Inherit(c_void_p(context.as_pointer()));
		LG.b丌仌=False;
		
# def 凸仌最小弧度(self, context): 
	# if(LG.b丌仌==False):
		# LG.b丌仌=True;
		# Δ乙卍dll();
			
		# Gik.卍dll.dll.凸仌最小弧度(c_void_p(context.as_pointer()));	 
		# LG.b丌仌=False;
		
def Δ仌改名(self, context): 
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		if(self.name!=""):
			Co=context.scene.objects ;
			if(self.name in Co):
				o=Co[self.name];print("pose_object==", o,context.pose_object);
				oA=context.pose_object;
				if(oA):
					self.name="";
					print("this select armature is itself!!!",);
			else:
				self.name="";
		LG.b丌仌=False;
	   
def Δ仌模式(self, context): 
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		print("self==",self);oA=context.active_object;
		# for arm in bpy.data.armatures :
		b找到=False;
		for o in context.scene.objects :
			if(o.type=="ARMATURE"):
				for i,pg in enumerate(oA.ppO.cp骨找):
					if(o.name==pg.name):
						b找到=True;
						break;
					if(b找到):
						break;
		#------------------------------
		if(b找到==False):
			pg=oA.ppO.cp骨找.add();pg.name=o.name;pg.idx=oA.ppO.cp骨找.__len__()-1;
		
		LG.b丌仌=False;

#====self=>pb.ghost_ik==========================
col黄='THEME09';col浅黑='THEME10';
def Δ仌禁用(self, context): 
	# print("self==",self);
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		if(self.ghost_ik.type in[TYPE_物理,TYPE_布料]):
			print("self IN==",self);
			Gik.pbA=context.active_pose_bone;
			CpbS=context.selected_pose_bones_from_active_object;
			if(CpbS==[]):CpbS.append(Gik.pbA);
			for pb in CpbS:
				if(pb==self):continue;
				if(self.ghost_ik.type==TYPE_物理):
					Δ十IK组(context,"6",pb,"physical-IK",col黄);
				elif(self.ghost_ik.type==TYPE_布料):
					Δ十IK组(context,"7",pb,"cloth-IK",col棕);
		LG.b丌仌=False;
		

#====bp画画====================================
def Δ仌画IK(self, context): 
	# print("Δ仌画IK Gik==",Gik);
	if(LG.b丌仌==False):
		print("Δ仌画IK ==",Gik.卍dll.dll ,id(Gik),self.bp画画);
		LG.b丌仌=True;
		if(Gik.卍dll.dll == None or Gik.cvpC==None):#●有可能G.dll 卸载,指向不未知地址引起崩溃.
			if(Gik.卍dll.b乙(dllpathIK64B,dllpathIK64)):
				Gik.卍dll.dll.凸载入scene亖IK(c_void_p(context.as_pointer()));
			else:
				print("★Δ仌画IK return;Gik.卍dll.b乙 失败==",);return;
				
			Gik.cvpC=c_void_p(context.as_pointer());#Gik.cvpGraph=c_void_p(bpy.context.view_layer.depsgraph.as_pointer());
			Δ重填Lo物理骨(Gik,context.scene);
			
		if(self.bp画画):
			if(Gik.CL条序L点序f2画G==None or Gik.卍dll.dll.卩凸画〇(True,True,True)):
				ci2骨数__=(c_int*2)(0,0);Gik.卍dll.dll.ii凸骨(c_void_p(context.scene.as_pointer()),ci2骨数__);
				#----叵--------------------------
				if(0 < ci2骨数__[1]):
					画3dOP(bp显示=False);
					py_叵画(Gik,context.scene,b画面=True,b画丷=True,b画Λ=True,b画字=True,b画弓=False,b画m=True,b画2d=False \
												,L2条数丶iSize点=(3,ci2骨数__[1]*10),L2条数丶iSize线=(3,ci2骨数__[1]*3),L2条数丶iSize乛=(3,ci2骨数__[1]*3)\
												,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=400	 );
			画3dOP(bp显示=True,bp画面=True,ip画字=True,bp灬=False);				
		else:
			画3dOP(bp显示=False,bp画面=False,ip画字=False,bp灬=False);
			
		LG.b丌仌=False;
		
	
#========================================
def Δ钉自动变红(context):
	if(context.object):
		pose=context.object.pose;
		if(pose==None):return;
		Cbg=pose.bone_groups;print("--pin group==");
		bg原来=None;
		bg原来spline=bg罒骨组(context,Cbg,"spline-IK",col灰蓝);
		bg原来physical=bg罒骨组(context,Cbg,"physical-IK",col黄);	
		bg原来cloth=bg罒骨组(context,Cbg,"cloth-IK",col黄);
		
		bg钉=bg罒骨组(context,Cbg,"spline-IK-pin",col红);
		LG.b丌仌=True;
		for O in Gik.L卐骷物理:
			if(O.o.ppO.bp物理o):
				if(O.o.ppO.init<1):
					Δ一一ik(O.o.ppO.o,False);
					continue;
				Cpb=O.o.pose.bones;
				for pb in Cpb:
					if(pb.ghost_ik.type in[TYPE_SPLINE,TYPE_物理,TYPE_布料]):
						if(pb.ghost_ik.bp钉):
							if(pb.bone_group!=bg钉):
								pb.bone_group=bg钉;
						else:
							if(pb.bone_group==bg钉):
								if(pb.ghost_ik.type==TYPE_SPLINE):
									bg原来=bg原来spline;
								elif(pb.ghost_ik.type==TYPE_物理):
									bg原来=bg原来physical;
								elif(pb.ghost_ik.type==TYPE_布料):
									bg原来=bg原来cloth;
								pb.bone_group=bg原来;
		LG.b丌仌=False;


#====动力====================================
I=0;
@persistent
def Δ刷新动力骨Post(scene):
	if(scene.ghost_ik.bp禁用sc):return;
	#----初始帧-----------------------------------------
	if(scene.frame_current==scene.frame_start):
		if(scene.ghost_ik.bp物理sc==False):return;
		if(Gik.C!=bpy.context):
			Gik.C=bpy.context;
		# if(Gik.C.active_object and Gik.C.active_object.type=="ARMATURE"):
			# SetMode(Gik.C.active_object,mode='POSE');
		if(scene.ghost_ik.init==0):
			Δ叵scene(scene.ghost_ik);
		
		Δ钉自动变红(Gik.C);
		
	# if(Gik.卍dll.dll):
		# Gik.卍dll.dll.b凸IK钉子骨();
	
	if(scene.ghost_ik.bp物理sc==False):return;
		
	# print("REFLASH==",Gik,Gik.卍dll.dll , Gik.cvpC,Gik.b烘焙G );
	# bΔ凷cvp卩(bpy.Gik.C);
	# if(Gik.ci丌播放G.value==True):
		# 丌播放(bpy.Gik.C);
	#------------------------------
	if(Gik.卍dll.dll == None or Gik.cvpC==None or Gik.C==None \
		or scene.ghost_ik.bp画画 and Gik.CL条序L点序f2画G==None):
		t版本=bpy.app.version;
		if(t版本[0]!=3 and t版本[1]!=1):#(3, 1, 2)
			print("★★ blender.version!=3.1",bpy.app.version);
			return;
		if(Gik.C!=bpy.context):
			Gik.C=bpy.context;			
		if(Gik.卍dll.dll==None):
			if(Gik.卍dll.b乙(dllpathIK64B,dllpathIK64)):
				Gik.卍dll.dll.凸载入scene亖IK(c_void_p(Gik.C.as_pointer()));
			else:
				print("★ return;Gik.卍dll.b乙 失败==",);return;

		Gik.cvpC=c_void_p(Gik.C.as_pointer());#print("Gik.卍dll.dll==",Gik.卍dll.dll,Gik.dllDJS,Gik.cvpC);
		丨巜帧(Gik.C);
		Δ重填Lo物理骨(Gik,scene,True);#★★ 引起 crash
		# if(Gik.卍dll.dll.b凸物理骨有动画(Gik.cvpC)):
			# bpy.ops.op.delete_phy_keyframes();    
		
	#----画-------------------------------------------------
	if(scene.ghost_ik.bp画画):
		if(Gik.CL条序L点序f2画G==None or Gik.卍dll.dll.卩凸画〇(True,True,True)):#
			ci2骨数__=(c_int*2)(0,0);Gik.卍dll.dll.ii凸骨(c_void_p(scene.as_pointer()),ci2骨数__);print("ci2骨数__==",*ci2骨数__);
			if(0 < ci2骨数__[1]):
				画3dOP(bp显示=False);
				py_叵画(Gik,scene,b画面=True,b画丷=True,b画Λ=True,b画字=True,b画弓=False,b画m=True,b画2d=False \
												,L2条数丶iSize点=(3,ci2骨数__[1]*3),L2条数丶iSize线=(3,ci2骨数__[1]*3),L2条数丶iSize乛=(3,ci2骨数__[1]*3) \
												,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=400 );
		#------------------------------
		if(Gik.卍dll.乚3d==None):
			画3dOP(bp显示=True,bp画面=True,ip画字=True,bp灬=False);
	else:
		if(Gik.卍dll.乚3d==True):
			# 画3dOP(False,True);
			Gik.卍dll.dll.凸画3d(False);
	# print("Gik.CL条序L点序f2画G==",Gik.CL条序L点序f2画G);
	#-----------------------------------------------------
	I=Gik.卍dll.dll.i凸物理骨all(Gik.cvpC,byref(Gik.ci丌播放G));#Gik.cvpGraph,
	if(I<1):
		if(I==-1):
			print("I stop==",I);
			Δ重填Lo物理骨(Gik,scene);丌播放(Gik.C);
		elif(I==-2):
			iΔ叵Cpb(Gik.oA,True);Δ叵scene(scene.ghost_ik);
		print("I return ",I);
		return;

	print("I,Gik.L卐骷物理==",I,Gik.L卐骷物理,scene.ghost_ik.bp有待删除);
	for O in Gik.L卐骷物理:
		# pb=o.pose.bones[0];#print("head==",pb.matrix,pb.head); # print("o==",o,o.ppO.bp物理o);
		if(O.o.ppO.bp物理o):
			# print("O.ψ==",O.o,O.ψ);
			if(Gik.卍dll.dll.b凸无效o(O.ψ)):continue;
			if(O.o["i仌"]==2):
				O.o.update_tag(refresh={'DATA'});#刷新 'OBJECT', 'DATA', 'TIME'
				O.o["i仌"]=0;
				# o.location=o.location;#刷新
				# print("FRASH o==",o);
			
	if(scene.ghost_ik.bp有待删除):
		Δ一一无效列表物(scene);
	#----烘焙-------------------------------------------------
	print("b烘焙G==",Gik.b烘焙G,scene.frame_current, scene.frame_end);
	if(Gik.b烘焙G and scene.frame_current== scene.frame_end):#
		丌播放(Gik.C);
		Δ0乛烘焙物理骨(Gik.oA,Gik.C);
		Gik.b烘焙G=False;
		return;#不画

#====关闭前====================================
@persistent#可以不断有效
def Δ重载scenePre(scene):
	print("Δ重载scenePre==",scene);
	if(scene==None):
		scene=bpy.context.scene;
	bpy.ops.op.delete_ghost_ik();
	# bΔ凷cvp卩(bpy.context);
	# bpy.context.scene.frame_current= bpy.context.scene.frame_start;
	
#----打开场景后-------------------------------------------------
@persistent#可以不断有效
def Δ重载scenePost(scene):
	print("RE LOAD SCENE post==",scene);
	# return;
	if(scene==None):
		scene=bpy.context.scene;
	# if(Gik.sp警告G!=""):
		# scene.ghost_ik.sp警告=Gik.sp警告G;
	# else:
		# scene.ghost_ik.sp警告="";
	if(scene.ghost_ik.bp禁用sc):return;		
	bpy.ops.op.delete_ghost_ik();

	# if("REFRESH" not in scene):
		# scene["REFRESH"]=True;
	Δ叵scene(scene.ghost_ik,False);
	for o in scene.objects:
		if(o.type=="ARMATURE" and 0<o.ppO.init):
			# Δ叵o(o);
			o.ppO.bp用申o=o.ppO.bp用申o;
	# bpy.ops.op.delete_ghost_ik();
	# if(Gik.卍dll.dll == None):
		# Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);
		
	
#////end////end////end////end////end////end////end////end////


import os 
from ctypes import*
from ctypes import wintypes

from .fill import*
from .draw import 画3dOP
from .compatible import Δ仌2022物理骨
# print("dllpathIK64==",dllpathIK64);
文件夹此IK=os.path.basename(os.path.dirname(__file__));
# if(文件夹此IK+".Gik" in sys.modules):
	# Gik=sys.modules[文件夹此IK+".Gik"];
# else:
exec("import "+文件夹此IK+".G as Gik");#√
exec("from "+ 文件夹此IK+".G import *");


try:
	from PYLIB.PYLIB_main import*;
	# from PYLIB.PYLIB_animation import 十十fcurve1o;
except:	   
	exec("from	"+".PYLIB_"+Gik.文件夹此ghost+".PYLIB_"+Gik.文件夹此ghost+"	 import*");#PYLIB_IMDJS_ghost_ik.py
	exec("from	"+".PYLIB_"+Gik.文件夹此ghost+".PYLIB_draw	import*");	
	exec("from	"+".PYLIB_"+Gik.文件夹此ghost+".PYLIB_animation	import*");	
	exec("from	"+".PYLIB_"+Gik.文件夹此ghost+".PYLIB_armature	import*");		
	exec("from	"+".PYLIB_"+Gik.文件夹此ghost+".PYLIB_ui	import*");	

col红='THEME01';#钉
col橙='THEME02';#布料
col绿='THEME03';#two-IK-脚
col蓝='THEME04';#

col酒红='THEME05';
col深紫='THEME06';
col灰蓝='THEME08';#spline ik
col黄='THEME09';#物理

col黑='THEME10';#禁用物理
col紫='THEME11';#修正骨
col浅绿='THEME12';#two-IK-grandson
col灰='THEME13';
col棕='THEME14';
col深绿='THEME15';#two-IK-parent
# from .__init__ import	 卐GHOST_IK卐Operator;#Χ
#//////////////////////////////////////
def Δ删除属性(self,Cpb,s信息):
	for pb in Cpb:
		pb.bone_group=None;
		if("PoseBone"in pb):
			del pb["PoseBone"];
		pb.ghost_ik.type=-1;
	self.report({"ERROR"},s信息);#"INFO" "ERROR" "DEBUG" "WARNING"

#====●为了 在其它插件读取属性==========================
def Δ仌属性(self,oA):
	Cpb=oA.pose.bones;print("Δ仌属性==",Δ仌属性);
	if("PoseBone" not in oA):
		oA["PoseBone"]={};
	oA["PoseBone"]["b有属性"]=oA.ppO.bp缺属性;
	for pb in Cpb:
		if("PoseBone" not in pb):
			pb["PoseBone"]={};

	
def Δ卌prsm(pb):
	if("b根" not in pb["PoseBone"] or "q" not in pb["PoseBone"]):
		pb["PoseBone"]["p"]=(c_float*3)(0.0,0.0,0.0);pb["PoseBone"]["e"]=(c_float*3)(0.0,0.0,0.0);pb["PoseBone"]["q"]=(c_float*4)(1.0,0.0,0.0,0.0);pb["PoseBone"]["s"]=(c_float*3)(1.0,1.0,1.0);pb["PoseBone"]["q"]=(c_float*4)(1.0,0.0,0.0,0.0);pb["PoseBone"]["f16mι"]=(c_float*16)(1.0,0.0,0.0,0.0,	   0.0,1.0,0.0,0.0,	   0.0,0.0,1.0,0.0,	   0.0,0.0,0.0,1.0);
		pb["PoseBone"]["b根"]=False;
	if(pb.rotation_mode!="QUATERNION"):
		pb.rotation_mode="QUATERNION";
		
def Δ叵2ik(pb,o,s类型,i孙子父=-1,b强制=True):
	print("Δ叵2ik==",pb.name,i孙子父);
	凷键("PoseBone",o);	
	if(pb.name not in o["PoseBone"]):
		o["PoseBone"][pb.name]={};
		
	pb["PoseBone"]["type"]=pb.ghost_ik.type=s类型;
	#----2ik--------------------------
	pb["PoseBone"]["bLR"]=0;#pb.ghost_ik.bpZX=pb.ghost_ik.bpZX;
	# if("b脚" not in pb["PoseBone"]):
		# pb["PoseBone"]["b脚"]=False;
	#----保存在 object 随时变--------------------------
	if((i孙子父==0 or  i孙子父==1)and "脚跟ι" not in o["PoseBone"][pb.name] or "申Φ" not in o["PoseBone"][pb.name]):#子
		o["PoseBone"][pb.name]["申Φ"]=(c_float*6)(0.0,0.0,0.0  , 0.0,0.0,0.0 );
		pb["PoseBone"]["脚跟ι"]=(c_float*3)(-999.0,-999.0,-999.0);
	if(i孙子父==0 or  i孙子父==1):
		if("z地" not in pb["PoseBone"] or b强制):
			pb["PoseBone"]["z地"]=(c_float*3)(-999.0,-999.0,-999.0);
		
		
	if("b冖a" not in pb["PoseBone"]):
		pb["PoseBone"]["b冖a"]=0.0;pb["PoseBone"]["b冖a099"]=0.0;#pb["PoseBone"][""]=0.0;
		# pb["PoseBone"]["b脚"]=False;
	if("Λx" not in pb["PoseBone"]):#子父 -1<i孙子父 and 
		pb["PoseBone"]["Λx"]=0.0;#骨x轴与IK平面轴的夹角
		
	# if(-1<i孙子父 and "b反向" not in pb["PoseBone"]):
		# pb["PoseBone"]["b反向"]=False;#状态
		
	#------------------------------
	pb.ghost_ik.fp反向fac=pb.ghost_ik.fp反向fac;
	pb.ghost_ik.fvp父旋=pb.ghost_ik.fvp父旋;pb.ghost_ik.bp用申=pb.ghost_ik.bp用申;
	
	#pb.ghost_ik.fp冖3xy=pb.ghost_ik.fp冖3xy;pb.ghost_ik.fp冖3xy099=pb.ghost_ik.fp冖3xy099;
	Δ卌prsm(pb);


def Δ叵物理ik(pb):
	print("Δ叵物理ik==",pb.name);	
	pb.ghost_ik.fp大=pb.ghost_ik.fp大;pb.ghost_ik.bp十一=pb.ghost_ik.bp十一;#物理风向
	Δ卌prsm(pb);
	pb["PoseBone"]["head"]=(c_float*3)(*pb.head);pb["PoseBone"]["tail"]=(c_float*3)(*pb.tail);#用于计算弹簧长度.
#========================================
def Δ叵1pb(pb,b强制=False):
	if(pb.ghost_ik.type<1 \
		or  b强制 and (pb.bone.select or 0<pb.ghost_ik.type) \
		or "PoseBone" not in pb):
		#----for imdjs_nodes ik--------------------------
		凷键("PoseBone",pb);
		print("pb==",pb.name,pb["PoseBone"],type(pb["PoseBone"]));
		# 凷键("flag",pb["PoseBone"],-1);
		#----spline--------------------------
		pb["PoseBone"]["ξ"]=pb.ghost_ik.ξ=pb.ghost_ik.ξ;pb["PoseBone"]["ξik"]=pb.ghost_ik.ξik=pb.ghost_ik.ξik;
		pb.ghost_ik.bp移=pb.ghost_ik.bp移;
		pb.ghost_ik.bp钉=pb.ghost_ik.bp钉;pb.ghost_ik.ip影响=pb.ghost_ik.ip影响;
		#----all ● 为在其它插件找到类型--------------------------
		if(pb.ghost_ik.type<0 or "type" not in pb["PoseBone"]):
			pb.ghost_ik.type=0;pb["PoseBone"]["type"]=0;
		else:
			pb["PoseBone"]["type"]=pb.ghost_ik.type;
		pb["PoseBone"]["b动画"]=False;
		pb["PoseBone"]["b驱动"]=False;pb["PoseBone"]["b禁用"]=False;#for ImdjsNodes
		pb.ghost_ik.init=pb.ghost_ik.init;
		pb.ghost_ik.bp扭父=pb.ghost_ik.bp扭父;
		pb.ghost_ik.bp要插关键帧=pb.ghost_ik.bp要插关键帧;
		pb.ghost_ik.fvp丨小=pb.ghost_ik.fvp丨小;
		#----物理--------------------------
		pb.ghost_ik.bp物理=pb.ghost_ik.bp物理;
		pb.ghost_ik.fp弹性=pb.ghost_ik.fp弹性;pb.ghost_ik.fp刚性=pb.ghost_ik.fp刚性;pb.ghost_ik.fp恢复=pb.ghost_ik.fp恢复;
		pb.ghost_ik.fp力=pb.ghost_ik.fp力;pb.ghost_ik.fp重力fac=pb.ghost_ik.fp重力fac;pb.ghost_ik.fp质量=pb.ghost_ik.fp质量;pb.ghost_ik.fp风力fac=pb.ghost_ik.fp风力fac;
		# pb.ghost_ik.fp消除横力=pb.ghost_ik.fp消除横力;
		pb.ghost_ik.bp碰撞=pb.ghost_ik.bp碰撞;
		# pb.ghost_ik.sp骨色=pb.ghost_ik.sp骨色;
		pb.ghost_ik.ip头尾=pb.ghost_ik.ip头尾;
		#------------------------------
		pb.bp物理=pb.bp物理;#pb.ghost_ik.ip弹性类型=pb.ghost_ik.ip弹性类型;	
	
#====所有 pb====================================
def iΔ叵Cpb(oA,b强制=False):
	print("iΔ叵Cpb==",b强制);
	#----叵--------------------------
	if(oA and oA.type=="ARMATURE"):
		Cpb=oA.pose.bones;LG.b丌仌=True;
		for pb in Cpb:
			# print("pb init==",'PoseBone'in pb,b强制,pb.bone.select);
			Δ叵1pb(pb,b强制);
		#----更新--------------------------
		"""m
		if(oA.ppO.version<Gik.version):
			for pb in Cpb:
				pass;
			oA.ppO.version=Gik.version;
		"""
		oA.ppO.ip骨数=Cpb.__len__();
		# Δ叵o(oA,b强制);
		if(oA.ppO.bp缺属性== True):oA.ppO.bp缺属性=False;
		LG.b丌仌=False;
		return Cpb.__len__();
	return 0;
	
#========================================
def Δ叵碰撞体(o,ii面3):
	print("ii面3==",o,ii面3);
	LG.b丌仌=True;
	o.ppO.type=2;
	o.ppO.fp摩擦力=o.ppO.fp摩擦力;o.ppO.fp反弹力=o.ppO.fp反弹力;o.ppO.冖检测距离=o.ppO.冖检测距离;o.ppO.fp亍=o.ppO.fp亍;o.ppO.ip开始帧=o.ppO.ip开始帧;o.ppO.ip结束帧=o.ppO.ip结束帧;
	o.ppO.bp要删除=o.ppO.bp要删除;o.ppO.bp有关联点=o.ppO.bp有关联点;o.ppO.bp物理o=o.ppO.bp物理o;
	if("COLLIDER" not in o):o["COLLIDER"]={};
	# ii点=o.data.vertices.__len__();#print("ii点==",ii点);
	# o["COLLIDER"]["L冖点"]=(c_float*ii点)(*[0.0]*ii点);
	o["COLLIDER"]["L冖面"]=(c_float*ii面3)(*[0.0]*ii面3);
	o["COLLIDER"]["b冄冖"]=False;
	LG.b丌仌=False;
	
def Δ叵o(oA,b强制=False):
	print("Δ叵o  oA==",oA.name,oA.ppO.init,b强制);
	LG.b丌仌=True;
	#------------------------------
	if("PoseBone" not in oA):
		oA["PoseBone"]={};#● 必须要有为了 Lo类型G=Lo巜type(OB_ARMATURE,C,"PoseBone",true);
	oA["PoseBone"]["b有属性"]=True;
	if("b有修正骨" not in oA["PoseBone"]):
		oA["PoseBone"]["b有修正骨"]=False;oA["PoseBone"]["bIMDJS"]=True;
	if("bIMDJS" not in oA["PoseBone"]):
		oA["PoseBone"]["bIMDJS"]=-1;

	if(oA.ppO.fp反向ik==0):
		oA.ppO.fp反向ik=0.05;
	oA.ppO.fp最大缩=oA.ppO.fp最大缩;oA.ppO.fp肌肉延长=oA.ppO.fp肌肉延长;oA.ppO.fp缩o=oA.ppO.fp缩o;
	oA.ppO.ip骨数=oA.ppO.ip骨数;
	oA.ppO.fp扭范围=oA.ppO.fp扭范围;oA.ppO.fp范围o=oA.ppO.fp范围o;
	if(oA.ppO.init< 1 or b强制==True):
		oA.ppO.ivp3版本=oA.ppO.ivp3版本;
		oA["i仌"]=0;oA.ppO.bp禁用o=oA.ppO.bp禁用o;oA.ppO.fp反向ik=oA.ppO.fp反向ik;
		# oA.ppO.ip开始帧=oA.ppO.ip开始帧;oA.ppO.ip结束帧=oA.ppO.ip结束帧;
		oA.ppO.bp用ghost_ik=oA.ppO.init=1;oA.ppO.bp只选=oA.ppO.bp只选;oA.ppO.bp播放了动画=oA.ppO.bp播放了动画;oA.ppO.bp地面丨o=oA.ppO.bp地面丨o;oA.ppO.fp地面丨亍=oA.ppO.fp地面丨亍;oA.ppO.bp缺属性=oA.ppO.bp缺属性;
		if(oA.ppO.cp骨同步.__len__()==0):
			oA.ppO.cp骨同步.add();oA.ppO.cp骨同步.clear();
			oA.ppO.cp骨找.add();oA.ppO.cp骨找.clear();
			
		oA.ppO.fp摩擦力=oA.ppO.fp摩擦力;oA.ppO.fp反弹力=oA.ppO.fp反弹力;oA.ppO.fp消除横力=oA.ppO.fp消除横力;oA.ppO.fp渐变带动=oA.ppO.fp渐变带动;oA.ppO.fp收缩值=oA.ppO.fp收缩值;
		oA.ppO.冖检测距离=oA.ppO.冖检测距离;
		oA.ppO.fp亍=oA.ppO.fp亍;oA.ppO.冖Ж=oA.ppO.冖Ж;oA.ppO.bp碰撞o=oA.ppO.bp碰撞o;oA.ppO.bp封闭=oA.ppO.bp封闭;oA.ppO.bp中点=oA.ppO.bp中点;
		if(oA.ppO.cp排除碰撞体.__len__()==0):
			oA.ppO.cp排除碰撞体.add();oA.ppO.cp排除碰撞体.clear();
		oA.ppO.ip碰撞体ξ=oA.ppO.ip碰撞体ξ;
		oA.ppO.bp有烘焙=oA.ppO.bp有烘焙;
		#------------------------------
		oA.ppO.bp用风=oA.ppO.bp用风;oA.ppO.fvp风向=oA.ppO.fvp风向;oA.ppO.fp十=oA.ppO.fp十;oA.ppO.fp随机=oA.ppO.fp随机;oA.ppO.fp风倍=oA.ppO.fp风倍;
		oA.ppO.bp要删除=oA.ppO.bp要删除;
		
		oA.ppO.bp用钉o=oA.ppO.bp用钉o;oA.ppO.bp限制o=oA.ppO.bp限制o;oA.ppO.bp用申o=oA.ppO.bp用申o;#oA.ppO.bp不动父=oA.ppO.bp不动父;
		
	oA.ppO.bp物理o=oA.ppO.bp物理o;

	LG.b丌仌=False;
#========================================
def Δ叵scene(sceneGHIK,b强制=False):
	print("Δ叵scene==",sceneGHIK.ip碰撞体ξ,sceneGHIK.init);
	LG.b丌仌=True;
	if(sceneGHIK.init<1 or b强制):
		#----DEBUG--------------------------
		
		sceneGHIK.version=sceneGHIK.version;sceneGHIK.bp画画=sceneGHIK.bp画画;
		sceneGHIK.ip跟踪点=sceneGHIK.ip跟踪点;sceneGHIK.bp恢复=sceneGHIK.bp恢复;sceneGHIK.bp修正力=sceneGHIK.bp修正力;sceneGHIK.bp阻力=sceneGHIK.bp阻力;sceneGHIK.bp弹力=sceneGHIK.bp弹力;sceneGHIK.bp拉力=sceneGHIK.bp拉力;sceneGHIK.bp弹簧=sceneGHIK.bp弹簧;sceneGHIK.bp弹簧隔=sceneGHIK.bp弹簧隔;sceneGHIK.bp弹簧布=sceneGHIK.bp弹簧布;sceneGHIK.bp乛丨=sceneGHIK.bp乛丨;sceneGHIK.bpΣ=sceneGHIK.bpΣ;sceneGHIK.bp关联点=sceneGHIK.bp关联点;sceneGHIK.bp物理sc=sceneGHIK.bp物理sc;
		if(sceneGHIK.ip碰撞体ξ==-1 or b强制):
			sceneGHIK.ip碰撞体ξ=0;sceneGHIK.cp碰撞体.add();sceneGHIK.cp碰撞体.remove(sceneGHIK.cp碰撞体.__len__()-1);
		
		sceneGHIK.bp有待删除=sceneGHIK.bp有待删除;sceneGHIK.冖检测距离=sceneGHIK.冖检测距离;sceneGHIK.ip结束帧=sceneGHIK.ip结束帧;
		#------------------------------
		sceneGHIK.bp预模拟=sceneGHIK.bp预模拟;sceneGHIK.ip预模拟帧=sceneGHIK.ip预模拟帧;
		sceneGHIK.ip开始帧=sceneGHIK.ip开始帧;sceneGHIK.ip结束帧=sceneGHIK.ip结束帧;
		print("==INIT",sceneGHIK.ip碰撞体ξ);
		sceneGHIK.init=1;
	sceneGHIK.bp碰撞sc=sceneGHIK.bp碰撞sc;
	# print("Δ叵scene== >>",LG.b丌仌)
	LG.b丌仌=False;
	
#====Gik.L卐骷物理 ■====================================
def Δ重填Lo物理骨(Gik,scene,b灬=False):
	print("Δ重填Lo物理骨 ==",Gik,Gik.cvpC);#Gik.卍dll.dll.凸ASSERT("Δ重填Lo物理骨",True);
	if(Gik.卍dll.dll == None):
		Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);
	if(b灬):
		Gik.卍dll.dll.凸灬骨();
	Gik.L卐骷物理.clear();
	LG.b丌仌=True;
	for o in scene.objects:
		if(o.type =="ARMATURE" ):
			print("o.ppO.init==",o.ppO.init);
			Δ仌2022物理骨(o,bpy.context);
			if(o.ppO.init==1):
				Gik.L卐骷物理.append(Gik.卐O(o));print("十十 o物理骨",o.name);
				#----◆ 临时,为了兼容之前版本属性--------------------------
				""" #★★ 引起 回到第1帧按F crash
				Cpb=o.pose.bones;
				for pb in Cpb:
					pb["PoseBone"]["ξ"]=pb.ghost_ik.ξ=pb.ghost_ik.ξ;
					pb.ghost_ik.fp弹性=pb.ghost_ik.fp弹性;pb.ghost_ik.fp刚性=pb.ghost_ik.fp刚性;pb.ghost_ik.fp恢复=pb.ghost_ik.fp恢复;pb.ghost_ik.fp扭性=pb.ghost_ik.fp扭性;pb.ghost_ik.fp重力fac=pb.ghost_ik.fp重力fac;pb.ghost_ik.bp碰撞=pb.ghost_ik.bp碰撞;
					pb.bp物理=pb.bp物理;
				"""
	Gik.卍dll.dll.b凸凷L骷G(None,Gik.cvpC);#L骨架G ■#Ms骨：pbik,骨架.L条序L物理ψpbik ■ ●因为Gik.L卐骷物理.append(Gik.卐O(o)); 所以这个一定要执行
	#---------------------------------------------
	Gik.卍dll.dll.b凸凷物理dll(Gik.cvpC);
	Gik.卍dll.dll.凸凷碰撞体(Gik.cvpC,c_void_p(scene.as_pointer()));#L碰撞体G ■

	LG.b丌仌=False;
	# scene.frame_current= scene.frame_start;

def Δ乙卍dll():
	if(Gik.卍dll.dll == None):
		Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);
		print("Gik.卍dll.dll==",Gik.卍dll.dll);
		
def bΔNone凷物理(context):
	if(Gik.卍dll.dll == None or Gik.cvpC==None or Gik.卍dll.dll.卩凸画〇(True,True,True)):
		Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);	
		凷cvp(Gik,context);
		Δ重填Lo物理骨(Gik,context.scene);ci2骨数__=(c_int*2)(0,0);Gik.卍dll.dll.ii凸骨(c_void_p(context.scene.as_pointer()),ci2骨数__);print("ci2骨数__==",*ci2骨数__);
		# if(scene.ghost_ik.bp画画):
		if(0 < ci2骨数__[1]):
			画3dOP(bp显示=False);
			py_叵画(Gik,context.scene,b画面=True,b画丷=True,b画Λ=True,b画字=True,b画弓=False,b画m=True,b画2d=False \
											,L2条数丶iSize点=(3,ci2骨数__[1]*3),L2条数丶iSize线=(3,ci2骨数__[1]*3),L2条数丶iSize乛=(3,ci2骨数__[1]*3) \
											,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=400 );	
		return True;
	else:
		return False;
		
#========================================
def pb罒4(i,j,k,l,CpbS):
	if(CpbS[i].parent):
		print("ijkl==",CpbS[i].name,CpbS[j].name,CpbS[k].name,CpbS[l].name);
		pb父=CpbS[i].parent;# i
		if(pb父==CpbS[j]):
			if(CpbS[j].parent==CpbS[k]):
				if(CpbS[k].parent==CpbS[l]):# l→k→j→i
					return pb父;#子		
			elif(CpbS[j].parent==CpbS[l]):
				if(CpbS[l].parent==CpbS[k]):# k→l→j→i
					return pb父;
					
		elif(pb父==CpbS[k]):
			if(CpbS[k].parent==CpbS[j]):
				if(CpbS[j].parent==CpbS[l]):# l→j→k→i
					return CpbS[i];	
			elif(CpbS[k].parent==CpbS[l]):
				if(CpbS[l].parent==CpbS[j]):#j →l→k→i
					return pb父;
					
		elif(pb父==CpbS[l]):
			if(CpbS[l].parent==CpbS[k]):
				if(CpbS[k].parent==CpbS[j]):# j→k→l→i
					return pb父;
			elif(pb父==CpbS[l]):
				if(CpbS[l].parent==CpbS[j]):
					if(CpbS[j].parent==CpbS[k]):# k→j→l→i
						return pb父;					
	return None;
	
#==============================
def pbΔ罒子(CpbS):
	pb子=None;len=CpbS.__len__();print("len==",len);
	if(len==2):
		if(CpbS[1].parent and CpbS[1].parent==CpbS[0]):
			pb子=CpbS[1];#子	
		else:
			pb子=CpbS[0];
	#------------------------------
	elif(len==3):
		if(CpbS[2].parent):
			if(CpbS[2].parent==CpbS[1] and CpbS[1].parent==CpbS[0]):#0→1→2
				pb子=CpbS[1];#子	
		elif(CpbS[1].parent):
			if(CpbS[1].parent==CpbS[2] and CpbS[2].parent==CpbS[0]):#1→2→0
				pb子=CpbS[2];
		elif(CpbS[2].parent):
			if(CpbS[2].parent==CpbS[0] and CpbS[0].parent==CpbS[1]):#2→0→1
				pb子=CpbS[0];
	#------------------------------
	elif(len==4):
		pb子=pb罒4(0,1,2,3,CpbS);
		if(pb子==None):
			pb子=pb罒4(1,0,2,3,CpbS);
			if(pb子==None):
				pb子=pb罒4(2,0,1,3,CpbS);		
				if(pb子==None):
					pb子=pb罒4(3,0,1,2,CpbS);
		# if(b脚 and pb子 and pb子.parent):
			# return pb子.parent;#腿→小腿→脚 →脚趾
	return pb子;
	
#==============================
""""""
def bg罒骨组(context,Cbg,sIk,col):
	ξ组 = Cbg.find(sIk);
	if( ξ组 < 0):#找不到
		bpy.ops.pose.group_add();
		ξ组 = Cbg.active_index;print("ξ组==",Cbg,ξ组); #激活的当前组ξ
		bg=Cbg[ξ组];bg.name=sIk;bg.color_set=col;
	else:
		bg = Cbg[ξ组];
	return bg;

	
#------------------------------
def Δ十IK组(self,context,CpbS,epIkType):
	print("Δ十IK组==",);#pbA.name,pbA.ghost_ik.type,epIkType
	pose=context.object.pose;Cbg=pose.bone_groups;
	bgSelf=bg罒骨组(context,Cbg,self.sIk,self.col);#pbA.ghost_ik.sp骨色=bgSelf.color_set;
	CpbS=context.selected_pose_bones_from_active_object;
	if(CpbS==[]):
		print("★ CpbS==[]",CpbS);
		return;
	#----spline--------------------------
	if(epIkType =="1"):
		for pb in CpbS:
			if(pb.ghost_ik.type ==TYPE_SPLINE):
				if(pb.ghost_ik.bp钉):
					bg钉=bg罒骨组(context,Cbg,"spline-IK-pin",col红);
					pb.bone_group=bg钉;
				else:
					pb.bone_group=bgSelf;#pb.ghost_ik.sp骨色=bgSelf.color_set;
				
	elif(epIkType in["7","8"]):#8 mix ik
		for pb in CpbS:
			# print("pb.ghost_ik.type==",pb,pb.ghost_ik.type,TYPE_物理);
			if(pb.ghost_ik.type in[TYPE_物理,TYPE_布料]):# and pb.bone.use_connect
				pb.bone_group=bgSelf;#pb.ghost_ik.sp骨色=bgSelf.color_set;
	#----2 ik--------------------------
	else:
		# pb子=None;
		# if(pbA.ghost_ik.type in[TYPE_TWO孙,TYPE_TWO子,TYPE_TWO父,TYPE_TWO爷]):
		pb子=pbΔ罒子(CpbS);print("pb子==",pb子,pb子["PoseBone"]["b脚"],bgSelf);
		if(pb子):
			bg深绿=bg罒骨组(context,Cbg,"two-IK-parent",col深绿);
			bg绿=bg罒骨组(context,Cbg,"two-IK-child",col绿);
			bg浅绿=bg罒骨组(context,Cbg,"two-IK-grandson",col浅绿);
			bg钉=bg罒骨组(context,Cbg,"spline-IK-pin",col红);
			pb子.bone_group=bg钉;#子默认就是pin
			if(pb子.parent):
				pb父=pb子.parent;
				pb父.bone_group=bg深绿;	#pb父.ghost_ik.sp骨色=bg深绿.color_set;
				if(pb父.parent and pb父.parent.ghost_ik.type ==TYPE_TWO爷):
					pb父.parent.bone_group=bg深绿;#pb父.parent.ghost_ik.sp骨色=bg深绿.color_set;
					
			for pb孙 in pb子.children:
				if(pb孙.ghost_ik.type==TYPE_TWO孙):
					if(pb子["PoseBone"]["b脚"]):
						pb孙.bone_group=bgSelf;#col绿
					else:
						pb孙.bone_group=bg浅绿;
					break;
					#pb孙.ghost_ik.sp骨色=bg浅绿.color_set;
		# elif(pbA.ghost_ik.type ==TYPE_TWO目标):
			# for pb in CpbS:
				# pb.bone_group=bg罒骨组(context,Cbg,"two-IK-target",col酒红);
				
#========================================
def Δ一IK组(context):		   
	# pose=context.object.pose;Cbg=pose.bone_groups;
	# ξ组 = Cbg.find(pbA.bone_group.name);print("--group==",ξ组,pbA,Cbg.keys(),pbA.bone_group);
	# if( ξ组 > -1):#找到
	#Cbg.active_index=ξ组; #激活的当前组ξ
	# if(self.epIkType in["1","8"]):
	CpbS=context.selected_pose_bones_from_active_object;
	if(CpbS==[]):CpbS.append(pbA);
	for pb in CpbS:
		pb.bone_group=None;


def Δ十一IKgroup(self,context,epIkType):
	CpbS=context.selected_pose_bones_from_active_object;#if(CpbS==[]):CpbS.append(pbA);
	# pbA = context.active_pose_bone;
	print("卐十一IKgroup卐Operator epIkType==",epIkType );
	if(CpbS):
		#----remove ik------------------------------------
		if(epIkType=="0"):
			self.sIk="";self.col="DEFAULT";
			Δ一IK组(context);	  print("pb remove==");
			return {"FINISHED"};
		#----spline ik--------------------------
		elif(epIkType=="1"):
			self.sIk="spline-IK";self.col=col灰蓝;
		#----2 ik--------------------------
		elif(epIkType=="2"):
			self.sIk="two-IK-child";self.col=col绿;#子骨
			
		#----物理ik--------------------------
		elif(epIkType=="7"):
			self.sIk="physical-IK";self.col=col黄;	
		#----布料ik--------------------------
		elif(epIkType=="8"):
			self.sIk="cloth-IK";self.col=col棕;
		#------------------------------
		Δ十IK组(self,context,CpbS,epIkType);
		# print("pb add==",self.epIkType,self.sIk,self.col);
	else:
		self.report({"ERROR"},"!!no selected bones");#"INFO" "ERROR" "DEBUG" "WARNING"
	return {"FINISHED"};
	
#//////////////////////////////////////
def 灬cvpIK():
	Gik.cvpC=Gik.C=None;Gik.cvpA=Gik.oA=None;Gik.cvpSC=Gik.pbA=None;
	Gik.L卐骷物理.clear();Gik.b烘焙G=False;Gik.b初次G=False;
	bModalG=False;LG.b丌仌=False;
	#------------------------------
	Gik.L卐o修正骷.clear();
	print("灬cvpIK==",Gik.卍dll.dll);
	

def Δ一一无效列表物(scene):
	print("- - - DEL GROUP objects==",);
	if(scene.ghost_ik.bp有待删除):
		i=0;
		for pg in scene.ghost_ik.cp碰撞体:
			if(pg.bp要删除):
				scene.ghost_ik.cp碰撞体.remove(i);print("----Scene del pg==",pg.name);
				continue;
			i+=1;
		scene.ghost_ik.bp有待删除=False;
		
	for O in Gik.L卐骷物理:
		if(O.o.ppO.bp要删除):
			i=0;
			for i,pg in enumerate(O.o.cp排除碰撞体):
				print("pg.bp要删除==",pg.bp要删除);
				if(pg.bp要删除):
					O.o.cp排除碰撞体.remove(i);print("----o del pg==",pg.name);
					continue;
				i+=1;
			O.o.ppO.bp要删除=False;  
#==============================================
def Δ一一ik(骷,bΘ=True):
	if(骷.type=="ARMATURE"):
		Cpb=骷.pose.bones;
		for pb in Cpb:
			if(bΘ and pb.bone.select or bΘ==False):
				pb.bone_group=None;

				if("PoseBone"in pb):
					del pb["PoseBone"];
				pb.ghost_ik.init=False;pb.ghost_ik.type=-1;pb.ghost_ik.bp物理=False;
				if(-1<pb.ghost_ik.ip头尾):pb.ghost_ik.ip头尾=-1;
				# print("dir==",dir(pb.ghost_ik),pb.ghost_ik.__dict__);
				# if(hasattr(pb, 'ghost_ik')):
					# delattr(pb, 'ghost_ik');print("delattr==",pb.name);
					# bpy.ops.wm.properties_remove(data_path="active_pose_bone",property_name= 'ghost_ik');	

		# 骷.ppO.init=0;
		骷.ppO.ivp3版本[2]=0;
		if(Gik.卍dll.dll):
			Gik.卍dll.dll.凸灬骷(c_void_p(骷.as_pointer()));


# ////END////END////END////END////END////END////END////END////
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			
						
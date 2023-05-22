
import	bpy,sys
from bpy.props import *


from .update import*
from .G import 语,卐O,Limdjs驱动,TYPE_修正骨;
from .func import bg罒骨组,col紫;
pi=3.14159267;

# try:
	# exec("from	"+".PYLIB_"+Gik.文件夹此ghost+".PYLIB_"+Gik.文件夹此ghost+"	 import oPropertyGroup");

# except:	   
	# from PYLIB.PYLIB_attribute import oPropertyGroup

from .func import col灰,dllpathIK64,dllpathIK64B;
	
def Δ仌开始帧(self, context): 
	if(LG.b丌仌==False):
		if(self.ip开始帧>=self.ip结束帧):
			self.ip开始帧=self.ip结束帧-1;
			
def Δ仌结束帧(self, context): 
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		if(self.ip结束帧<=self.ip开始帧):
			self.ip结束帧=self.ip开始帧+1; 
		LG.b丌仌=False;
		
def Δ仌改名(self, context): 
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		if(self.name!=""):
			Co=context.scene.objects ;
			if(self.name in Co):
				o=Co[self.name];print("==", o,context.pose_object);
				oA=context.pose_object;
				if(oA.type=="POSE" and arm==oA.data):
					self.name="";
					print("this select armature is itself!!!",);
			else:
				self.name="";
		LG.b丌仌=False;

def Δ仌约束(self, context): 
	# print("Δ仌画IK Gik==",Gik);
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		if(Gik.卍dll.dll==None):
			Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);
		oA=context.pose_object;
		Gik.Δ仌约束(self.bpIK约束,oA,Gik.卍dll.dll,Gik.MoLpbIKG);
		#------------------------------
		LG.b丌仌=False;
		
def Δ仌关联点(self, context): 
	print("Δ仌关联点 ==",LG.b丌仌);
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		bpy.ops.op.set_related_points(bp灬=self.sp关联点=="");
		#------------------------------
		LG.b丌仌=False;
				
#====ghost_ik==============================
class namePropertyGroup(bpy.types.PropertyGroup): #单个乙 cpSK模式id
	name : StringProperty(name="", default="",update=None);
	bp要删除:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
bpy.utils.register_class(namePropertyGroup);

class idxPropertyGroup(bpy.types.PropertyGroup):#单个预置 cpSK预置id
	name:StringProperty(name="Name", default="",update=Δ仌改名);
	idx:IntProperty(name='',description='',default=-1,min=0,max=1000,step=1);
	name原:StringProperty(name="原名", default="");
	sp条目类型:StringProperty(name="", default="NONE");
bpy.utils.register_class(idxPropertyGroup);


#====pb.ghost_ik====================================
class 卐pb属性卐PropertyGroup(bpy.types.PropertyGroup):
	ξ:IntProperty(name='index',description=' bone index',default=-1);
	ξik:IntProperty(name='index',description='ik bone index',default=-1);
	#----属性--------------------------
	type:IntProperty(name=语.Lik[0][0],description=语.Lik[1][1],default=-1,options={'HIDDEN'},update=None);#-1 未初始 , 0无,1spline,2,3,4,5,6;7 物理,8 布料	 ==.ghost_ik.type
	init:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);#如果为True,设置骨时不改变原来参数
	bp物理:BoolProperty(name=语.L物理[0],description=语.L物理[1],default=False,subtype='NONE',update=None);	
	bp要插关键帧:BoolProperty(name="",description="",default=False,subtype='NONE',update=None);	
	
	bp钉:BoolProperty(name=语.L自动选或钉[1],description=语.L自动选或钉[4],default=False,subtype='NONE',options={'ANIMATABLE'},update=Δ仌钉头);#二 pb["b钉"]
	bp移:BoolProperty(name=语.L自动选或钉[7],description=语.L自动选或钉[8],default=False,subtype='NONE',update=None);
	bp用申:BoolProperty(name=语.L用申[0],description=语.L用申[1],default=True,subtype='NONE',update=None);
	ip头尾:IntProperty(name=语.L头尾[0],description=语.L头尾[1],default=-1,update=None);# 根据骨距离定义分离骨,-1:未初始,0:连,1:头,2:尾

	# sp骨色:StringProperty(name='color',description='bone color',default=col灰);
	#----操作--------------------------
	fp刚性:FloatProperty(name=语.L刚性[0],description=语.L刚性[1],default=0.30,min=0.01,max=1.0,step=3,precision=2,update=Δ仌刚性);
	fp弹性:FloatProperty(name=语.L弹性[0],description=语.L弹性[1],default=0.20,min=0.01,max=1.0,step=3,precision=2,update=Δ仌弹性);#反弹
	fp恢复:FloatProperty(name=语.L恢复[0],description=语.L恢复[1],default=0.30,min=0.0,max=1.0,step=3,precision=2,update=Δ仌恢复);
	# ip弹性类型:IntProperty(name=语.L弹性类型[0],description=语.L弹性类型[1],default=0,min=0,max=1,step=1,subtype='NONE',update=Δ仌弹性类型);
	#'GRARY_EDITABLE','PROPORTIONAL',"TEXTEDIT_仌",,subtype='NONE',unit='NONE',update=Δ仌刚性, options={"ANIMATABLE",'GRARY_EDITABLE','PROPORTIONAL',"TEXTEDIT_仌"}
	#--------------------------------------------------
	fp反向fac:FloatProperty(name=语.Lpp属性o[0], description="(the factor of ik reverse bending)ik反向弯曲的比例", default=1.0, min=-0.5, max=2.0, precision=3, subtype="NONE", unit="NONE", update=None);
	"""
	fp最大弧度丨:FloatProperty(default=pi/2,min=0.01,max=pi/2);#用于限制最大角度
	fp最小弧度丨:FloatProperty(default=0,min=0.00,max=pi/2);
	#fp最大弧度:FloatProperty(name='max angle',description="max angle limitation",default=pi/2,min=0.01,max=pi/2,update=凸仌最小弧度);#限制最小角度
	fp最小弧度伸:FloatProperty(name=语.L弧度伸d[0],description=语.L弧度伸d[1],default=0.0,min=0.0,max=pi/2,update=凸仌最小弧度);#限制最小角度
	fp最大弧度缩:FloatProperty(name=语.L弧度缩[0],description=语.L弧度缩[1],default=0.0,min=0.0,max=pi/2,update=凸仌最小弧度);
	fp绑定弧度:FloatProperty(default=0.0,min=0.0,max=pi/2);
	fp绑定IK长:FloatProperty(default=0.0,min=0.0,max=10000);
	fp最大IK长:FloatProperty(default=0.0,min=0.0,max=10000);#算上fp最小弧度 后的最长IK限制
	fp最小IK长:FloatProperty(default=0.001,min=0.001,max=10000);
	"""
	ip影响:IntProperty(name=语.L样条ik[0],description=语.L样条ik[1],default=0,min=0,max=100);#在一一ik 里
	
	#----ik(●只保存在子)--------------------------
	bp扭父:BoolProperty(name=语.L扭父[0],description=语.L扭父[1],default=True,subtype='NONE',update=None);	

	# fp冖3xy:FloatProperty(default=0.0,min=0.0);
	# fp冖3xy099:FloatProperty(default=0.0,min=0.0);
	
	# bp限制:BoolProperty(name=语.L限制[0],description=语.L限制[1],default=True,subtype='NONE',update=None);
	bLR:BoolProperty(default=True);#计算子骨 旋转限制方向
	# bpZX:BoolProperty(default=True);#2ik子以自身什么轴转动.
	fvp丨小:FloatVectorProperty(name="",description="min angle",size=2,min=0,max=3,default=(2.0, 1.5),update=Δ仌丨小);#关节旋转限制小 角度,第二个是两骨Y轴夹角限制
	# fvp丨大:FloatVectorProperty(name="",description="max angle",size=3,min=-3.13,max=3.13,default=(1,0.8,1),update=None);#ㄥ179==3.13286f
	# fvp申:FloatVectorProperty(size=3,default=( 0.0, 0.0,0.0));#这个是相对物的ι
	fvp父旋:FloatVectorProperty(size=3,default=( 0.0, 0.0,0.0));#虚拟ik平面 父头.相对父m的ι
	#----修正骨--------------------------
	fp修正量pb:FloatProperty(name=语.L修正骨[0],description=语.L修正骨[1],default=1.0,min=0.0,max=1.0,step=3,precision=2);
	fp缩pb:FloatProperty(name=语.L修正骨[2],description=语.L修正骨[3],default=1.0,min=0.1,max=3.0,step=3,precision=2);
	fp扭Y:FloatProperty(name=语.L修正骨[4],description=语.L修正骨[5],default=0.5,min=0.1,max=1.0,step=3,precision=2,subtype='NONE',unit='NONE',update=None);
	#----L物理[0]--------------------------
	fp力:FloatProperty(name=语.L重力[4][0],description=语.L重力[4][1],default=1.0,min=0.01,max=1,update=None);
	fp重力fac:FloatProperty(name=语.L重力[1][0],description=语.L重力[1][1],default=1.0,min=-100,max=100,update=Δ仌重力因子);
	fp质量:FloatProperty(name=语.L重力[2][0],description=语.L重力[2][1],default=1.0,min=0,max=100);
	fp风力fac:FloatProperty(name=语.L重力[5][0],description=语.L重力[5][1],default=1.0,min=0,max=100,update=Δ仌重力因子);
	# fp冖:FloatProperty(default=0.0,min=0.0,max=10000);
	
	# fp冖冖:FloatProperty(default=0.0,min=0.0,max=10000);#隔骨长
	# fp冖冖x:FloatProperty(default=0.0,min=0.0,max=10000);
	# fp冖冖z:FloatProperty(default=0.0,min=0.0,max=10000);

	bp碰撞:BoolProperty(name=语.L碰撞[3],description='using collision for the selected pose bones',default=True,subtype='NONE',update=None);
	#----风>>>>--------------------------
	fp大:FloatProperty(name="1", description="",default=0,min=0,max=1);#当前增加的风量
	bp十一:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);#当前是增加还是减少风量
	pass;
	
bpy.utils.register_class(卐pb属性卐PropertyGroup);

#==== o.ppO==========================
class oIKPropertyGroup(bpy.types.PropertyGroup):#单个预置 cpSK预置id
	ivp3版本:IntVectorProperty(name='version',description='this blend file version',default=(0,0,0));
	type:IntProperty(name='',description='',default=0,min=0,max=2);#0无,2碰撞体
	init:IntProperty(name='',description='',default=0,min=0,max=2);#0未乙 1ik 丶 物理
	bp禁用o:BoolProperty(name=语.Lpp属性o物理[0]+语.L全局[1],description="disable of this armature",default=False);

	fp反向ik:FloatProperty(name=语.Lpp属性o[0]+语.L全局[1], description="(the value of ik reverse bending)ik反向弯曲的值", default=0.0, min=0.000, max=0.5, precision=3, subtype="NONE", unit="NONE", update=None);
	
	bp缺属性:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	#----缓存--------------------------------------------
	iip长度当前缓存:IntProperty(default=0);#1,2,3,4
	# cp缓存PRS:CollectionProperty(type=卐PRS记录卐PropertyGroup);#每个物每帧1个缓存
	# cp布料缓存 :bpy.props.CollectionProperty(type=卐缓存cloth卐PropertyGroup,name='',description='',);
	#pp物动力学o = bpy.props.PointerProperty(type=卐动力学卐PropertyGroup);
	#cpSPRING = bpy.props.CollectionProperty(type=卐布料spring卐PropertyGroup,name='',description='',);
	#ip碰撞迭代次数=bpy.props.IntProperty(name='iteration',description='iteration of cloth simulation',default=3,min=1, max=10, step=1,);
	#----属性--------------------------
	bp更新了骨:BoolProperty(default=False);
	#0显,1隐,-1无
	bp开始了:BoolProperty(name=语.Lpp属性o[2],description='',default=False,subtype='NONE',update=None);
	bp隐藏动画 :BoolProperty(name=语.Lpp属性o[3],description="hide animation",default=False,subtype='NONE',update=None);
	# ip时刻成为父子:IntProperty(default=-1);
	bp只选:BoolProperty(name=语.Lpp属性o[4],description=语.Lpp属性o[5],default=False);
	bp播放了动画:BoolProperty(default=False);#防止 播放了动画后,再 刷新窗口 可能引起crash
	bp地面丨o:BoolProperty(name=语.Lpp属性o[6],description=语.Lpp属性o[7],default=False);
	fp地面丨亍:FloatProperty(name=语.Lpp属性o[8], description=语.Lpp属性o[9], default=0.0, min=-10.000, max=10.0, precision=3, subtype="NONE", unit="NONE", update=None);
	bpIK约束:BoolProperty(name=语.Lpp属性o[10],description=语.Lpp属性o[11],default=False,update=Δ仌约束);
	#====骨==========================
	ip骨数 :IntProperty(name=语.Lpp属性o[12],description="",default=0);
	bp要增加关键帧:BoolProperty(name='',description='',default=False);
	
	# fp扭性 :FloatProperty(name=语.L扭性[0],description=语.L扭性[1],default=0.5,min=0.1,max=1.0,step=3,precision=2,subtype='NONE',unit='NONE',update=Δ仌扭性);
	fp扭范围 :FloatProperty(name=语.L扭性[2],description=语.L扭性[3],default=0.1,min=0.1,max=0.5,step=3,precision=2,subtype='NONE',unit='NONE');
	
	fp范围o:FloatProperty(name=语.L样条ik[0],description=语.L样条ik[1],default=0.1,min=0.01,max=0.5,step=3,precision=2);
	#----修正骨--------------------------
	# bp用修正:BoolProperty(name="correction",description="use code correction(使用骨修正)",default=False,subtype='NONE',update=Δ仌修正骨);
	fp最大缩:FloatProperty(name=语.L修正骨[6]+语.L全局[1], description=语.L修正骨[7]+语.L全局[1], default=2.0, min=1.000, max=5.0, precision=3, subtype="NONE", unit="NONE", update=None);#扭的最大缩
	fp缩o:FloatProperty(name=语.L修正骨[2]+语.L全局[1],description=语.L修正骨[3]+语.L全局[1],default=1.0,min=0.1,max=3.0,step=3,precision=2);
	fp肌肉延长:FloatProperty(name=语.L修正骨[8]+语.L全局[1], description=语.L修正骨[9]+语.L全局[1], default=1.0, min=0.000, max=1.0, precision=3, subtype="NONE", unit="NONE", update=None);#扭的最大缩
	# bpIMDJS:BoolProperty(name='IMDJS',description='使用IMDJS修正骨',default=True,subtype='NONE',update=Δ仌IMDJS);
	#----关键帧--------------------------
	ip缺多少帧视:IntProperty(name='',description='',default=0,min=0,max=10000,step=1);
	ip缺多少帧渲:IntProperty(name='',description='',default=0,min=0,max=10000,step=1);
	# ip骨数pre :IntProperty(name="num",description="",default=0,min=0,max=1000);
	""" iterations :IntProperty(name="迭代",description="---",default=50,min=1,max=1000);#不能改名 """
	bp用钉o:BoolProperty(name=语.L自动选或钉[2]+语.L全局[1],description=语.L自动选或钉[3],default=True,subtype='NONE',update=None);#ik模式 ,物体全局钉
	# bp不动父:BoolProperty(name=语.L自动选或钉[5],description=语.L自动选或钉[6],default=True,subtype='NONE',update=None);
	bp限制o:BoolProperty(name=语.L限制[0]+语.L全局[1],description=语.L限制[1],default=False,subtype='NONE',update=None);
	bp用申o:BoolProperty(name=语.L用申[0]+语.L全局[1],description=语.L用申[1],default=False,subtype='NONE',update=None);	
	#----物理--------------------------
	bp物理o:BoolProperty(name=语.Lpp属性o物理[1]+语.L全局[1],description=语.Lpp属性o物理[2],default=True,update= None);
	bp碰撞o:BoolProperty(name=语.Lpp属性o物理[4]+语.L全局[1],description="colision(global)",default=True,subtype='NONE',update=None);
	bp封闭:BoolProperty(name='closed',description=' looped closed cloth',default=True,subtype='NONE',update=None);	
	bp中点:BoolProperty(name=语.Lpp属性o物理1[0]+语.L全局[1],description=语.Lpp属性o物理1[1],default=True,subtype='NONE',update=None);
	bp自碰撞:BoolProperty(name="self-collide", default=False );
	# fp弹力:FloatProperty(name=语.Lpp属性o物理[10]+语.L全局[1], description="spring",default=0.5,min=0.0,max=1, precision=3);	
	fp消除横力:FloatProperty(name=语.L重力[3][0]+语.L全局[1],description=语.L重力[3][1],default=0.4,min=0,max=1);
	fp渐变带动:FloatProperty(name=语.L渐变带动[0]+语.L全局[1],description=语.L渐变带动[1],default=0.6,min=0,max=1);
	fp收缩值:FloatProperty(name='srink',description='spring shrinkage value',default=0.2,min=0.0,max=0.9,step=3,precision=2);
		
	ip开始帧 :IntProperty(name=语.Lpp属性o物理[5],description="start frame",default=0,min=0,max=10000,update= Δ仌开始帧);
	ip结束帧:IntProperty(name=语.Lpp属性o物理[6],description="end frame",default=1000,min=1,max=10000,update= Δ仌结束帧);
	#---------------------------------------------
	fp亍:FloatProperty(name=语.Lpp属性o物理[7], description="collide offset", default=0.01, min=0.001, max=1, precision=3, subtype="NONE", unit="NONE", update=None);#根据整体平均长度  定义长度
	冖Ж:FloatProperty(name="", description="collide size", default=0.1, min=0.001, max=1, precision=3, subtype="NONE", unit="NONE", update=None);#根据整体 计算平均长度,用于 计算 o.ppO.fp亍,1.0为整体长度 
	fp摩擦力:FloatProperty(name=语.Lpp属性o物理[8], description="friction",default=0.5,min=0.05,max=1, precision=3);#每帧减少量.
	fp反弹力:FloatProperty(name=语.Lpp属性o物理[9], description="bounce",default=0.2,min=0.00,max=1, precision=3);#每帧减少量.
	冖检测距离:FloatProperty(name=语.Lpp属性o物理[11], description="distance of collider detection",default=1,min=0.05,max=100, precision=3);#检测碰撞距离
	
	
	cp排除碰撞体:CollectionProperty(type=namePropertyGroup,name='',description='');
	ip碰撞体ξ:IntProperty(default=-1,min=-1,max=100,step=1);
	bp有烘焙:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	bp要删除:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	#----风--------------------------
	bp用风:BoolProperty(name=语.Lpp属性o物理[12]+语.L全局[1],description=语.Lpp属性o物理[15],default=False,subtype='NONE',update=None);
	fp十:FloatProperty(name=语.Lpp属性o物理[13], description="",default=0.02,min=0.0002,max=0.3, precision=4);#频率
	
	fp风倍:FloatProperty(name=语.Lpp属性o物理[14], description="",default=0.01,min=0.001,max=10, precision=3);
	fvp风向:FloatVectorProperty(name='',min=-1,max=1,description=语.Lpp属性o物理[15],size=3,default=(0.0, 1.0,0.0));
	fp随机:FloatProperty(name=语.Lpp属性o物理[16], description="random",default=0.02,min=0.0,max=1, precision=3);	
	#------------------------------
	sp关联点:StringProperty(name="related points",description= 语.L设置[3]	,default='',update=Δ仌关联点);
	bp有关联点:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	#----烘焙--------------------------
	ip间隔帧数:IntProperty(name=语.L烘培[11],description=语.L烘培[12],default=0,min=0,max=100,step=1);
	#----骨同步--------------------------
	cp骨同步: CollectionProperty(type=idxPropertyGroup);
	cp骨找:CollectionProperty(type=idxPropertyGroup);
bpy.utils.register_class(oIKPropertyGroup);

#====Scene.ghost_ik==========================
def Δ仌物理(self, context):
	print("Δ仌物理==",LG.b丌仌);
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		# if(self.bp应用品==False):
		if(Gik.卍dll.dll==None):
			Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);
		Gik.卍dll.dll.b凸凷物理dll(c_void_p(context.as_pointer()));
		LG.b丌仌=False;
		
def Δ仌碰撞(self, context):
	print("Δ仌碰撞==",LG.b丌仌);
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		# if(self.bp应用品==False):
		if(Gik.卍dll.dll==None):
			Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);
		if(Gik.卍dll.dll):
			Gik.卍dll.dll.b凸仌碰撞(c_void_p(context.as_pointer()));
		LG.b丌仌=False;
		
def Δ仌修正骨(self, context):
	print("Δ仌修正骨==",LG.b丌仌,Gik.L卐o修正骷.__len__(),context.scene.ghost_ik.bp用修正);
	if(LG.b丌仌==False):
		LG.b丌仌=True;
		# if(self.bp应用品==False):
		if(Gik.卍dll.dll==None):
			Gik.卍dll.b乙(dllpathIK64B,dllpathIK64);
		oA=context.active_object;
		if(oA and context.scene.ghost_ik.bp用修正):
			if(Gik.卍dll.dll.b凸凷修正骨dll(c_void_p(context.as_pointer()))==False):
				context.scene.ghost_ik.bp用修正=False;print("!!! 无法载入修正骨dll== return;");
				return;
			if(Gik.L卐o修正骷==[]):
				if(bΔ凷1修正骷(context.object,context,False)==False):#L卐o修正骷 ■
					context.scene.ghost_ik.bp用修正=False
				else:
					if("B_noik" in oA.data.name or "Sharon"in oA.data.name):
						if(oA["PoseBone"]["b有修正骨"]==False):
							oA["PoseBone"]["b有修正骨"]=True;		
						if("B_noik"in oA.data.name):
							oA["PoseBone"]["bIMDJS"]=True;		
							# elif("Sharon"in oA.data.name):
						else:
							oA["PoseBone"]["bIMDJS"]=False;
					else:
						if(oA["PoseBone"]["b有修正骨"]==True):
							oA["PoseBone"]["b有修正骨"]=False;
			print("b有修正骨==",oA.name,oA["PoseBone"]["b有修正骨"]);
			# if(oA["PoseBone"]["b有修正骨"]):
				
		LG.b丌仌=False;
		
#------------------------------
def 卩罒o(o,L卐o骷):
	for o_ in L卐o骷:
		if(o==o_.o):
			return True;
	return False;
# ==============================
def Δ卌驱动属性(pb,bg紫):
	# print("Δ卌驱动属性==",pb.name,pb.ghost_ik.type);
	if("PoseBone" not in pb):
		pb["PoseBone"]={};
	if("driver" not in pb["PoseBone"] or pb.ghost_ik.type!=TYPE_修正骨):
		pb["PoseBone"]["driver"]=True;
		pb.ghost_ik.type=pb.ghost_ik.type=TYPE_修正骨;
		pb["PoseBone"]["b禁用"]=True;
		
		print("Δ卌驱动属性 1==",pb.name,pb.ghost_ik.type);
		pb.ghost_ik.fp修正量pb=pb.ghost_ik.fp修正量pb;
		pb.ghost_ik.fp缩pb=pb.ghost_ik.fp缩pb;pb.ghost_ik.fp扭Y=pb.ghost_ik.fp扭Y;
		if(pb.bone_group!=bg紫):
			pb.bone_group=bg紫;
			
def bΔ凷1修正骷(o,context,b强制=False):
	print("bΔ凷1修正骷==",o,context.scene.ghost_ik.bp用修正);
	if(context.scene.ghost_ik.bp用修正):
		if(o.type=="ARMATURE"):#
			# print("o==",o.name);
			if(卩罒o(o,Gik.L卐o修正骷)==False and "PoseBone" in o):
				# 凷键("PoseBone",o);
				if("b有修正骨" not in o["PoseBone"]):
					o["PoseBone"]["b有修正骨"]=False;o["PoseBone"]["bIMDJS"]=True;
				if("B_noik" in o.data.name or "Sharon"in o.data.name):
					if(o["PoseBone"]["b有修正骨"]==False):
						o["PoseBone"]["b有修正骨"]=True;		
					if("B_noik"in o.data.name):
						if(o["PoseBone"]["bIMDJS"]==False):
							o["PoseBone"]["bIMDJS"]=True;		
					else:
						if(o["PoseBone"]["bIMDJS"]==True):
							o["PoseBone"]["bIMDJS"]=False;
				else:
					if(o["PoseBone"]["b有修正骨"]==True):
						o["PoseBone"]["b有修正骨"]=False;
				#------------------------------
				Cbg=o.pose.bone_groups;print("Cbg==",Cbg);
				if(Cbg.__len__()==0):
					return False;
				bg紫=bg罒骨组(context,Cbg,"driver",col紫);
				Gik.L卐o修正骷.append(卐O(o));print("十十卐o ==",o.name);
				# b罒=False;
				Limdjs驱动吅=Limdjs驱动.copy();
				for pb in o.pose.bones:
					# b罒=False;
					for i,name in enumerate(Limdjs驱动吅):
						# print("pb.name==",pb.name,name);
						if(pb.name==name):
							Δ卌驱动属性(pb,bg紫);Limdjs驱动吅.pop(i);#b罒=True;
							break;

				# try:
				# print("oC==",o,context,Gik.卍dll.dll1);#Gik.卍dll.dll1.凸test修正();
				if(Gik.卍dll.dll.b凸凵修正骨()):
					Δ仌修正骨(None,context);
				if(Gik.卍dll.dll.b凸凷1修正骷(c_void_p(o.as_pointer()),c_void_p(context.as_pointer()),False)==False):#Mo卍骷驱动G ■
					return False;
				# except:
					# o.ppO.bp用修正=False;
		return True;
	return False;	
	

def bΔ凷L卐o骷G(context,bp用修正,b强制=False):
	print("bΔ凷L卐o骷G==");
	scene=context.scene;
	if(bp用修正):
		for o in scene.objects:
			if(bΔ凷1修正骷(o,context,b强制)==False):
				return False;
		return True;
	return False;
		
#----scene.ghost_ik --------------------------
class 卐scene工具乙ik卐PropertyGroup(bpy.types.PropertyGroup):
	init:IntProperty(name='',description='',default=0,min=0,max=2);# 0未乙
	bp禁用sc:BoolProperty(name=语.Lpp属性o物理[0]+语.L全局[0],description="disable the addon",default=False);
	bp物理sc:BoolProperty(name=语.Lpp属性o物理[1]+语.L全局[0],description=语.Lpp属性o物理[3],default=True,update= Δ仌物理);
	version:IntProperty(name='',description='',default=0,min=0,max=10000,step=1);
	bp画画:BoolProperty(name=语.L画画[0],description=语.L画画[1],default=False,update= Δ仌画IK);
	bp自动选:BoolProperty(name=语.L自动选或钉[0],description=语.L自动选或钉[0],default=False);
	bp用ghost_ik:BoolProperty(name=语.L激活[0]+语.L全局[0],description=语.L激活[1],default=False,update= Δ仌勾选本键);#无用
	bp用修正:BoolProperty(name=语.L修正[0]+语.L全局[0],description=语.L修正[1]+语.L全局[0],default=False,subtype='NONE',update=Δ仌修正骨);

	ip骨数A:IntProperty(name="num",description="",default=0,min=0,max=1000);
	sp骨名A:StringProperty(name='',description='',default='',maxlen=0,subtype='NONE',update=None);
	
	# bpIK模式:BoolProperty(name=语.LIK模式[0],description=语.LIK模式[1],default=True,subtype='NONE',update=Δ仌模式0);
	# bp动力学模式:BoolProperty(name=语.L物理模式[0],description=语.L物理模式[1],default=False,subtype='NONE',update=Δ仌模式1);
	ep模式:EnumProperty(name='',description='---',items=[('ik',语.LIK模式[0],语.LIK模式[1],'CON_SPLINEIK',0),('phy',语.L物理模式[0],语.L物理模式[1],'PHYSICS',1)],default='ik',update=None);
	epik·同步模式:EnumProperty( name="mode", description="mode",items=	[("0",语.L同步模式[0],"phyical ik mode","BONE_DATA",0),("1",语.L同步模式[1],"wind","FORCE_WIND",1),("2",语.L同步模式[2],"bake mode","KEY_HLT",2)],default="0",update=Δ仌模式);
	epik·修正模式:EnumProperty( name="mode", description="mode",items=	[("0",语.L同步模式[3],"IK","NONE",3),("1",语.L同步模式[4],"correction mode","MODIFIER_ON",4)],default="0",update=None);
	#----碰撞--------------------------
	sp物理骨dll路径:StringProperty(name='',description='',default='NONE');
	bp碰撞sc:BoolProperty(name=语.L碰撞[2],description=语.L碰撞[3],default=True,subtype='NONE',update=Δ仌碰撞);
	cp碰撞体:CollectionProperty(type=namePropertyGroup,name='',description='');
	ip碰撞体ξ:IntProperty(default=-1,min=-1,max=100,step=1);
	冖检测距离:FloatProperty(name=语.L碰撞[6],description=语.L碰撞[7],default=1.0,min=1.0,max=100.0,step=3,precision=2);
	bp有待删除:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	fp重力:FloatProperty(name=语.L重力[0][0]+语.L全局[0],description=语.L重力[0][1],default=0.98,min=-10.0,max=10.0,step=3,precision=3,subtype='NONE',unit='NONE',update=None);
	#----DEBUGik--------------------------
	ip跟踪点:IntProperty(name='',description='',default=-1,min=-1,max=1000000);
	# bp力滑:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	bp恢复:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	bp修正力:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	bp阻力:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);	
	bp弹力:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	bp拉力:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	bp弹簧:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);	
	bp弹簧隔:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);	
	bp弹簧布:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	bp乛丨:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	bp骨在线段:BoolProperty(name='',description='',default=True,subtype='NONE',update=None);
	bpΣ:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	bp关联点:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	#----烘焙--------------------------
	bp预模拟:BoolProperty(name=语.L模拟帧[0][0]+语.L全局[0],description=语.L模拟帧[0][1]+语.L全局[0],default=False,subtype='NONE',update=None);	
	ip预模拟帧:IntProperty(name=语.L模拟帧[1][0],description=语.L模拟帧[1][1],default=20,min=0,max=200);	
	# bp惯性:BoolProperty(name=语.L模拟帧[2][0],description=语.L模拟帧[2][1],default=True,subtype='NONE',update=None);
		
	# ip开始帧:IntProperty(name=语.L烘培[13],description='bake frame',default=0,min=0,max=10000,step=1);
	# ip结束帧:IntProperty(name=语.L烘培[14],description='bake frame',default=100,min=1,max=10000,step=1);
	# sp烘焙参考arm:StringProperty(name=语.L烘培[4],description=语.L烘培[6],default='');
	# sp烘焙参考骨:StringProperty(name=语.L烘培[5],description=语.L烘培[6],default='');
	# bp只烘焙激活o:BoolProperty(name=语.L烘培[7],description=语.L烘培[8],default=True,subtype='NONE',update=None);	
	# bp参考关键帧:BoolProperty(name=语.L烘培[9],description=语.L烘培[10],default=False,subtype='NONE',update=None);		
	
bpy.utils.register_class(卐scene工具乙ik卐PropertyGroup);

#/////////////////////////////////////////
class UL_UL_GlobalColliderUIList(bpy.types.UIList):
	def draw_item(self,context, layout, data, item, icon, active_data, active_property, index=0, flt_flag=0):
		if self.layout_type in {'DEFAULT', 'COMPACT'}:
			#layout.label(text=item.name, translate=False, icon_value=icon)
			row = layout.row().split(factor=0.7, align=False);
			row.prop(item, "name", text="", icon="MOD_PHYSICS", emboss=False);
			# if(index!=0 ):
				# row.prop(item, "fp影响", text="", emboss=True,slider=True);
bpy.utils.register_class(UL_UL_GlobalColliderUIList) ;
		
#----scene.DEBUGik --------------------------
class 卐sceneDEBGEik卐PropertyGroup(bpy.types.PropertyGroup):
	init:IntProperty(name='',description='',default=0,min=0,max=2);# 0未乙
	亖叵:BoolProperty(name="叵",description="",default=False);
	亖IK:BoolProperty(name="IK",description="",default=False);
	亖扭:BoolProperty(name="扭",description="",default=False);
	亖凷:BoolProperty(name="凷",description="",default=False);
	
	亖数ik:BoolProperty(name="数ik",description="",default=False);
	亖一一:BoolProperty(name="一一",description="",default=False);	
	亖节点:BoolProperty(name="节点",description="",default=False);
	亖烘:BoolProperty(name="烘",description="",default=False);
	
	亖骨在线:BoolProperty(name="在线",description="",default=True);	
	亖乛丨ik:BoolProperty(name="乛丨ik",description="",default=True);	
	#----修正骨-----------------------------------------
	亖驱:BoolProperty(name="驱",description="",default=True);	
	亖驱数:BoolProperty(name="驱数",description="",default=True);	
	亖驱扭:BoolProperty(name="驱扭",description="",default=True);	
	亖挤:BoolProperty(name="挤",description="",default=True);	
	亖旋:BoolProperty(name="旋",description="",default=True);	
	
	
bpy.utils.register_class(卐sceneDEBGEik卐PropertyGroup);
#==================================================
class 卐INITik卐Operator(bpy.types.Operator): 
	bl_idname = "op.init_scene_debug_ik"
	bl_label = "init_scene_debug_ik "
	bl_description = "---"

	def execute(self,context):
		if(context.scene.DEBUGik.init==0):
			context.scene.DEBUGik.亖叵=context.scene.DEBUGik.亖叵;context.scene.DEBUGik.亖IK=context.scene.DEBUGik.亖IK;
			context.scene.DEBUGik.亖扭=context.scene.DEBUGik.亖扭;context.scene.DEBUGik.亖凷=context.scene.DEBUGik.亖凷;
			context.scene.DEBUGik.亖节点=context.scene.DEBUGik.亖节点;context.scene.DEBUGik.亖烘=context.scene.DEBUGik.亖烘;context.scene.DEBUGik.亖数ik=context.scene.DEBUGik.亖数ik;context.scene.DEBUGik.亖一一=context.scene.DEBUGik.亖一一;
			context.scene.DEBUGik.亖骨在线=context.scene.DEBUGik.亖骨在线;context.scene.DEBUGik.亖乛丨ik=context.scene.DEBUGik.亖乛丨ik;
			
			context.scene.DEBUGik.亖驱=context.scene.DEBUGik.亖驱;context.scene.DEBUGik.亖驱数=context.scene.DEBUGik.亖驱数;context.scene.DEBUGik.亖驱扭=context.scene.DEBUGik.亖驱扭;context.scene.DEBUGik.亖挤=context.scene.DEBUGik.亖挤;context.scene.DEBUGik.亖旋=context.scene.DEBUGik.亖旋;
			context.scene.DEBUGik.init=1;
		return {"FINISHED"};
bpy.utils.register_class(卐INITik卐Operator);
			
"""
class UL_UL_卐骨同步卐UIList(bpy.types.UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
		if (self.layout_type in {'DEFAULT', 'COMPACT'}):   
			layout.prop(item, "name", text="", emboss=False,icon_value=ICONV);# icon=ICON,
"""

#////end////end////end////end////end////end////end////end////

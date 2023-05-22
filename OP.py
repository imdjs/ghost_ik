


from .G import 语;
from .PG import bΔ凷L卐o骷G;
from .func import *;
from .func import wintypes;

from .bake import *;
from .draw import 画3dOP;
	
CON_无=	-1
CON_F	= 0
CON_AF= 1
CON_CF= 2
CON_SHIFT	=  3
CON_SAF	=4
#----扭--------------------------
CON_X= 5
CON_AX= 6
CON_CX= 7
CON_SX= 8 #扭脚尖
#------------------------------
CON_传递	= 9
CON_应用=10
#==== 2 IK ==========================
class 卐GHOST_IK卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik";
	bl_label = "GHOST_ik";
	# bl_options = {'UNDO'};# ★ 这个如果有dll.函数会出错
	
	ip控:IntProperty(name='ip控',description='',default=0,min=0,max=10,subtype='NONE',update=None);#0 只按F,1:ctrl+F ,2:alt+F ,3:shift+F ,4:CON_传递,5:CON_节点,6:CON_扭
	b结束=False;

	def invoke(self, context, event):  
		print("invoke 2IK==",);scene=context.scene;
		if(scene.ghost_ik.bp禁用sc):return {"CANCELLED"};
		
		if(context.mode != 'POSE' or context.mode == 'PAINT_WEIGHT'):
			return {"CANCELLED"};  
		if(scene.ghost_ik.bp自动选):
			bpy.ops.view3d.select('INVOKE_DEFAULT');#print("active bone==",context.active_pose_bone);
		if (context.area.type == 'VIEW_3D'):
			#----debug-------------------------------------------------
			bpy.ops.op.load_ghost_ik();凷cvp(Gik,context);print("Gik.cvpSC)==",id(Gik),Gik.卍dll.dll,Gik.cvpSC);#Gik.cvpC ,Gik.oA,Gik.cvpA,Gik.pbA ■
			if(scene.ghost_ik.bp禁用sc or  Gik.oA and Gik.oA.ppO.bp禁用o):
				return {"CANCELLED"};
			if(Gik.pbA == None):
				self.report({"ERROR"},语.L出错[0]);#"INFO" "ERROR" "DEBUG" "WARNING"
				return {"CANCELLED"};
			if(Gik.pbA.ghost_ik.type<TYPE_SPLINE or TYPE_布料<Gik.pbA.ghost_ik.type):
				self.report({"ERROR"},语.L出错[1]);#"INFO" "ERROR" "DEBUG" "WARNING"
				return {"CANCELLED"};
			if(Gik.oA.ppO.init<1):#在物理骨检测到低版本
				# Θall(Gik.oA);
				Δ一一ik(Gik.oA,False);
				self.report({"ERROR"},"you need to reset the ik bones");#"INFO" "ERROR" "DEBUG" "WARNING"
				return {"CANCELLED"};
			# return {"CANCELLED"};
			""""""
			Gik.卍dll.dll.b凸凷rv3d(Gik.cvpC,True);
			print("Gik.pbA.ghost_ik.type==",Gik.pbA.ghost_ik.type,Gik.cvpSC);
			if(Gik.CL条序L点序f2画G==None or Gik.卍dll.dll.卩凸画〇(True,True,True)):
				ci2骨数__=(c_int*2)(0,0);Gik.卍dll.dll.ii凸骨(Gik.cvpSC,ci2骨数__);
				画3dOP(bp显示=False);
				py_叵画(Gik,context.scene,b画面=True,b画丷=True,b画Λ=True,b画字=True,b画弓=False,b画m=True,b画2d=False \
													,L2条数丶iSize点=(3,ci2骨数__[1]*3),L2条数丶iSize线=(3,ci2骨数__[1]*3),L2条数丶iSize乛=(3,ci2骨数__[1]*3) \
													,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=400 );
			
			#////■■■■■■////////////////////////////////									
			# bΔNone凷物理(context);
			#----要升级版本-------------------------------
			Cpb=context.pose_object.pose.bones;#Δ仌属性(self,Gik.oA);
			# if(卩二二版本(Gik.oA)==False):
				# Δ删除属性(self,Cpb,"this is the old version of setting need to reset bone ik!!");
				# Δ仌属性(self,Gik.oA);
				# return {"CANCELLED"};
			#-----------------------------------------------------
			# else:
			len=Cpb.__len__();b=False;
			if(scene.ghost_ik.ip骨数A!=len or scene.ghost_ik.sp骨名A!=Gik.oA.name):
				scene.ghost_ik.ip骨数A=len;scene.ghost_ik.sp骨名A=Gik.oA.name;
				if(Gik.卍dll.dll.b凸凷1骷1次(Gik.cvpA ,Gik.cvpC,True,True)):
					b=True;
				
			#----添加乚-------------------------------
			if(b==True or Gik.卍dll.dll.b凸凷1骷1次(Gik.cvpA,Gik.cvpC,True,False)):
				#丅鼠preG ■,ψpare子G ■f
				# pass
				if(Gik.卍dll.dll.b凸initIK1o每次A丅(Gik.cvpA,Gik.cvpC,self.ip控)):# ★★ 只能返回int 如果返回bool 会出错
					if(Gik.卍dll.dll.b凸IK骨(Gik.cvpA,Gik.cvpC,context.scene.ghost_ik.bp用修正,self.ip控)):
						if(context.scene.ghost_ik.bp画画 and Gik.卍dll.乚3d==None):
							画3dOP(True,bp画丷=True);
						# Gik.bModalG = True;
						#----修正骨--------------------------
						if(scene.ghost_ik.bp用修正):
							if(Gik.L卐o修正骷==[]):
								# Gik.卍dll.dll1.凸灬G();#Gik.L卐o修正骷.clear();#●全局变量如果不清除,重载场景会出错
								bΔ凷L卐o骷G(context,scene.ghost_ik.bp用修正,False);#L卐o修正骷 ■
								# Gik.卍dll.dll1.凸凷修正骷(c_void_p(context.as_pointer()),False);#Mo卍骷驱动G ■	
							if(Gik.L卐o修正骷==[]):
								# print("!!! 没有 s修正骨dll路径B==",Gik.卍dll.dll1);
								self.report({"ERROR"},"!!! 没有 s修正骨dll路径B");
								context.scene.ghost_ik.bp用修正=False;
								# self.Δ丌modal();
								return {"FINISHED"};#★ 不能返回 FINISHED 会crash
							print("Gik.L卐o修正骷==",Gik.L卐o修正骷);
							for 卐o骷 in Gik.L卐o修正骷:
								if(Gik.卐o骷==None or 卐o骷.o==Gik.oA and 卐o骷.o!=Gik.卐o骷.o):
									Gik.卐o骷=卐o骷;
									break;
							if(Gik.卐o骷==None):
								self.report({"ERROR"},"Gik.卐o骷==None");#"INFO" "ERROR" "DEBUG" "WARNING"
								context.scene.ghost_ik.bp用修正=False;
								# self.Δ丌modal();
								return {"FINISHED"};#★ 不能返回 FINISHED 会crash
						context.window_manager.modal_handler_add(self); # ●● 必须 在最后才添加,不然可能会crash
						return {'RUNNING_MODAL'};
					else:
						return {"FINISHED"};
			else:
				iΔ叵Cpb(Gik.oA,True);
			# Δ删除属性(self,Cpb,"bones miss some attibutes ,need to reset bone ik!!");
			# Gik.bModalG=False;
			return {"CANCELLED"};#● 如果有modal_handler_add  就必须要 先 进入modal 再退出
		else:
			return {"CANCELLED"};
	#============================================================
	def modal(self, context, event): #event	   Window Manager Event	   
		# if(Gik.bModalG):
		if (event.type == 'MOUSEMOVE'):
			B=Gik.卍dll.dll.b凸IK骨(Gik.cvpA,Gik.cvpC,context.scene.ghost_ik.bp用修正,self.ip控);#print("B==",B);
			if(B<1):
				self.report({"ERROR"},"b凸IK骨 ==B<1");#"INFO" "ERROR" "DEBUG" "WARNING"
				return {"FINISHED"};
			Gik.oA.update_tag();#print("▍oA.update_tag==",);
			# if(Gik.oA.ppO.bp播放了动画):Gik.oA.ppO.bp播放了动画=False;
			# else:
				# print("★ Gik.area3dG==",Gik.area3dG);
				
		# elif (event.type == 'E' and event.value == 'PRESS' ):#按下E键
			# self.ip按键 = Gik.iG键;
			# self.invoke(context, event);
		#----确认-------------------------------------------------
		elif (event.type == 'LEFTMOUSE'and event.value == 'PRESS'):#丌
			self.Δ丌modal();
			return {"FINISHED"};
		#----取消-------------------------------------------------
		elif (event.type == 'MIDDLEMOUSE'and event.value == 'PRESS'):#如果按下右键
			self.Δ丌modal();#bpy.ops.op.delete_ghost_ik();
			return {"FINISHED"};	
		elif (event.type == 'RIGHTMOUSE'and event.value == 'PRESS'):#如果按下右键
			self.Δ丌modal();
			return {"FINISHED"};

		
		return {'RUNNING_MODAL'};
		#-----------------------------------------------------
		# else:
			# return {"FINISHED"};
			
	#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
	def Δ丌modal(self):
		print ("Δ丌modal");
		Gik.卍dll.dll.凸丌(c_void_p(Gik.oA.as_pointer()),Gik.cvpC);
		# Gik.卍dll.dll.凸〇画(True);
		# Gik.bModalG = False;
		# bpy.context.region.tag_redraw();#相当于 Δ刷新窗口LIB();

			
class 卐GHOST_IK_F卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_no";
	bl_label = "GHOST_ik_f";
	
	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_F);
		return {"FINISHED"};
#----还原扭曲--------------------------
class 卐GHOST_IK_ALT卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_alt";
	bl_label = "GHOST_ik_alt";

	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_AF);
		return {"FINISHED"};
		
class 卐GHOST_IK_CTRL卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_ctrl";
	bl_label = "GHOST_ik_ctrl";

	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_CF);
		return {"FINISHED"};
		
class 卐GHOST_IK_SHIFT卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_shift";#刚性拉
	bl_label = "GHOST_ik_shift";

	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_SHIFT);
		return {"FINISHED"};
		
class 卐GHOST_IK_SHIFTALT卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_shiftaltf";
	bl_label = "GHOST_ik_shiftaltf";

	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_SAF);
		return {"FINISHED"};
#----扭--------------------------
class 卐GHOST_IK_扭卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_twist";
	bl_label = "GHOST_ik_x";
	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_X);
		return {"FINISHED"};
		
class 卐GHOST_IK_扭alt卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_twist1bone";
	bl_label = "GHOST_ik_alt_x";
	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_AX);
		return {"FINISHED"};
#----连带子动--------------------------
class 卐GHOST_IK_扭ctrl卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_twist2";
	bl_label = "GHOST_ik_ctrl_x";
	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_CX);
		return {"FINISHED"};
		
class 卐GHOST_IK_扭shift卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_ik_twist3";
	bl_label = "GHOST_ik_shift_x";
	def invoke(self, context, event):  
		bpy.ops.op.ghost_ik("INVOKE_DEFAULT",ip控=CON_SX);
		return {"FINISHED"};		
#========================================
class 卐IK1次卐Operator(bpy.types.Operator):
	bl_idname = "op.exe_ik_onece"
	# bl_label =语.L设置[2]
	bl_label ="exe ik"
	bl_description="excute ik once"
	#------------------------------------------------------------
	def execute(self, context):
		if(context.mode != 'POSE' or context.mode == 'PAINT_WEIGHT'):
			return {"CANCELLED"}; 
		if (context.area.type == 'VIEW_3D'):
			bpy.ops.op.load_ghost_ik();凷cvp(Gik,context);scene=context.scene;
			Gik.卍dll.dll.b凸凷rv3d(Gik.cvpC,True);#Δ凷area3d(Gik,context);
			print("Gik.pbA.ghost_ik.type==",Gik.pbA.ghost_ik.type,Gik.cvpSC);
			if(Gik.CL条序L点序f2画G==None or Gik.卍dll.dll.卩凸画〇(True,True,True)):
				ci2骨数__=(c_int*2)(0,0);Gik.卍dll.dll.ii凸骨(Gik.cvpSC,ci2骨数__);
				画3dOP(bp显示=False);
				py_叵画(Gik,context.scene,b画面=True,b画丷=True,b画Λ=True,b画字=True,b画弓=False,b画m=True,b画2d=False \
													,L2条数丶iSize点=(3,ci2骨数__[1]*3),L2条数丶iSize线=(3,ci2骨数__[1]*3),L2条数丶iSize乛=(3,ci2骨数__[1]*3) \
													,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=400 );
			#------------------------------
			Cpb=context.pose_object.pose.bones;#Δ仌属性(self,Gik.oA);
			len=Cpb.__len__();b=False;
			if(scene.ghost_ik.ip骨数A!=len or scene.ghost_ik.sp骨名A!=Gik.oA.name):
				scene.ghost_ik.ip骨数A=len;scene.ghost_ik.sp骨名A=Gik.oA.name;
				Gik.卍dll.dll.b凸凷1骷1次(Gik.cvpA ,Gik.cvpC,True,True);b=True;
			#----添加乚-------------------------------
			if(b==True or Gik.卍dll.dll.b凸凷1骷1次(Gik.cvpA,Gik.cvpC,True,False)):
				if(Gik.卍dll.dll.b凸initIK1o每次A丅(Gik.cvpA,Gik.cvpC,-1)):# ★★ 只能返回int 如果返回bool 会出错
					B=Gik.卍dll.dll.b凸IK骨(Gik.cvpA,Gik.cvpC,scene.ghost_ik.bp用修正,CON_应用);print("B==",B);
					if(0<B):			
						Gik.卍dll.dll.凸丌(c_void_p(Gik.oA.as_pointer()),Gik.cvpC);
						Gik.oA.update_tag(refresh={ 'DATA'});
						Gik.卍dll.dll.凸刷新窗口(Gik.cvpC);
		return {"FINISHED"};

#========================================
class 卐乙关联点卐Operator(bpy.types.Operator):
	bl_idname = "op.set_related_points"
	# bl_label =语.L设置[2]
	bl_label =""
	bl_description=语.L设置[3]
	# sp:StringProperty(name="note", description="", default="are you sure remove ik setting卩");
	
	bp灬:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	#------------------------------------------------------------
	def execute(self, context):
		# bΔNone凷物理(context);
		bpy.ops.op.load_ghost_ik();
		oA=context.active_object;oA["COLLIDER"]={};oA["COLLIDER"]["RELATED"]=[];
		if(self.bp灬==False):
			Gik.cvpA=c_void_p(oA.as_pointer());CL块点数_=(c_int*10)(*[-1]*10);
			ii块=Gik.卍dll.dll.i凸关联数0(Gik.cvpA,CL块点数_);L=[(-1)];
			if(0< ii块):
				# oA["COLLIDER"]["RELATED"]=CLLi巜(CL块点数_[0],CL块点数_[1]);print("==",oA["COLLIDER"]["RELATED"]);
				for i in range(ii块):
					if(0<CL块点数_[0]):
						L.append((-1)*CL块点数_[0]);#[(-1,-1,..),(-1,-1,..),]
				
				oA["COLLIDER"]["RELATED"]=L;print("L==",L);
				Gik.卍dll.dll.凸卌入关联点1(Gik.cvpA);
			# oA.update_tag();#★这个crash
			oA.ppO.bp有关联点=True;
		else:
			oA.ppO.bp有关联点=False;
		# Gik.卍dll.dll.凸丌(Gik.cvpC);
		self.report({"WARNING"},str(self.bp灬));#"INFO" "ERROR" "DEBUG" "WARNING"
		return {"FINISHED"};

class 卐画碰撞体卐Operator(bpy.types.Operator):
	bl_idname = "op.draw_collider"
	# bl_label =语.L设置[2]
	bl_label ="画碰撞体"
	# sp:StringProperty(name="note", description="", default="are you sure remove ik setting卩");
	#------------------------------------------------------------
	def execute(self, context):
		# bΔNone凷物理(context);
		bpy.ops.op.load_ghost_ik();
		if(Gik.卍dll.dll.b凸凷物理dll(c_void_p(context.as_pointer()))==False):
			return {"FINISHED"};
				
		oA=context.active_object;
		i点数=oA.data.vertices.__len__()*2;print("i点数==",i点数);
		画3dOP(bp显示=False);
		py_叵画(Gik,context.scene,b画面=True,b画丷=False,b画字=True,b画弓=False,b画m=True,b画2d=False \
										,L2条数丶iSize点=(2,i点数),L2条数丶iSize线=(2,i点数),L2条数丶iSize乛=(2,i点数) \
										,iSize字=i点数*4);
										
		if(Gik.卍dll.乚3d==None):
			画3dOP(bp显示=True,bp画弓=False,bp画面=False,ip画字=1);
			
		Gik.cvpA=c_void_p(oA.as_pointer());CL块点数_=(c_int*2)(-1,-1);
		Gik.卍dll.dll.凸画碰撞体(Gik.cvpA,c_void_p(context.as_pointer()));

		return {"FINISHED"};
		
#==================================================
class 卐一一IK骨卐Operator(bpy.types.Operator):
	bl_idname = "op.remove_ik__bones"
	bl_label =语.Lik[2][0]
	bl_description=语.Lik[2][1]
	# bl_options = {"REGISTER", "UNDO"}
	sp:StringProperty(name="note", description="", default="are you sure remove ik setting卩");
	#------------------------------------------------------------
	def draw(self, context):	self.layout.prop(self, "sp");

	def invoke(self, context, event):
		bpy.ops.op.load_ghost_ik();
		return context.window_manager.invoke_props_dialog(self,width=400);#运行的第1步
		
	def execute(self, context):
		Gik.oA=context.pose_object;
		if(Gik.oA):
			Δ一一ik(Gik.oA);
			bpy.ops.op.delete_ghost_ik();
			self.report({"INFO"},语.L出错[2]);#"INFO" "ERROR" "DEBUG" "WARNING"
		return {"FINISHED"};
	
#==================================================
class 卐乙IK骨卐Operator(bpy.types.Operator):
	bl_idname = "op.set_bones_attri"
	bl_label = 语.Lik[1][0]
	bl_description=语.Lik[1][1]

	epIkType:EnumProperty(name=语.Lik[0][0], description=语.Lik[0][1],items=	 [("1","spline-ik","---","OUTLINER_DATA_CURVE",0),("2", "two-ik","---","BONE_DATA",1)],default="1" );
	epDynType:EnumProperty(name=语.L物理[2], description=语.L物理[3],items=  [("7","phy-ik","physical ik bones","CONSTRAINT_DATA",0) ,("8","phy-cloth","cloth ik bones","MATCLOTH",1)],default="7");
	
	ep轴向:EnumProperty(name="axis", description="--",items=[("Z","Left","---","EVENT_Z",0) ,("-Z","Right","Right side","NONE",1),("X","x","Right side","EVENT_Z",2) ,("-X","-x","---","NONE",3)],default="Z");
	# bp目标:BoolProperty(name=语.Lik[4],description=语.Lik[4],default=False,subtype='NONE',update=None);
	bp旋父:BoolProperty(name=语.Lik[5][0],description=语.Lik[5][1],default=True,subtype='NONE',update=None);
	ip链:IntProperty(name='links',description='number of ik links',default=2,min=2,max=3,step=1,subtype='NONE',update=None);
	fp乙扭性:FloatProperty(name=语.L扭性[0],description=语.L扭性[1],default=0.5,min=0.01,max=1.0,step=3,precision=2);	
	fp乙刚性:FloatProperty(name=语.L刚性[0],description=语.L刚性[1],default=0.5,min=0.01,max=1.0,step=3,precision=2);
	fp乙弹性:FloatProperty(name=语.L弹性[0],description=语.L弹性[1],default=0.3,min=0.01,max=1.0,step=3,precision=2);
	fp乙恢复:FloatProperty(name=语.L恢复[0],description=语.L恢复[1],default=0.0,min=0.00,max=1.0,step=3,precision=2);
	bp渐变:BoolProperty(name='gradient',description='',default=False,subtype='NONE',update=None);
	bp碰撞:BoolProperty(name='collision',description='',default=True,subtype='NONE',update=None);	
	bp封闭:BoolProperty(name='closed',description=' looped closed cloth',default=True,subtype='NONE',update=None);		
	bp布料:BoolProperty(name='cloth',description='is cloth physical bones',default=False,subtype='NONE',update=None);
	bp简单:BoolProperty(name='simple(简单)',description='only set two bones as 2IK(只设置两根骨作为2ik)',default=False,subtype='NONE',update=None);
	#sp:StringProperty(name="note", description="", default="align bones axis?", );
	col="";sIk="";
	#----------------------------------------
	@classmethod
	def poll(cls, context):#决定是否激活
		return (context.object.type=="ARMATURE");

	def draw(self, context):
		uil行=self.layout.row(align=True);
		if(context.scene.ghost_ik.ep模式=="ik"):
			uil行.prop_enum(self,'epIkType',value="1",);#spline
			uil行.prop_enum(self,'epIkType',value="2",);#two ik 子
			if(self.epIkType=="2"):
				# self.layout.prop(self,	 "bp目标",translate=True,icon="EMPTY_SINGLE_ARROW");
				# if(self.bp目标==False):
				# uil行2=self.layout.row(align=True);
				# uil行2.prop_enum(self,'ep轴向',value="Z",);
				# uil行2.prop_enum(self,'ep轴向',value="-Z",);

				
				uil行2=self.layout.row(align=False);
				uil行2.prop(self,"bp简单",translate=True,icon="NONE");
				# uil行2.prop(self,	 "bp旋父",translate=True,icon="EMPTY_ARROWS");#● 必须 对齐父,作为整个的Φ
	
		else:
			uil行.label(text=语.Lik类型[3],text_ctxt='',translate=True,icon='NONE',icon_value=0);
			uil行.prop_enum(self,'epDynType',value="7",);#phy ik
			uil行.prop_enum(self,'epDynType',value="8",);#phy cloth
			#------------------------------
			uil行=self.layout.row(align=False);
			uil行.prop(self,	 "fp乙扭性",translate=True,icon="NONE");
			uil行.prop(self,	 "fp乙刚性",translate=True,icon="NONE");
			uil行.prop(self,	 "fp乙弹性",translate=True,icon="NONE");	
			uil行.prop(self,	 "fp乙恢复",translate=True,icon="NONE");				
			
			uil行=self.layout.row(align=False);		
			uil行.prop(self,	 "bp渐变",translate=True,icon="NONE");			
			uil行.prop(self,	 "bp碰撞",translate=True,icon="NONE");		
			if(self.epDynType=="8"):
				uil行.prop(self,	 "bp封闭",translate=True,icon="NONE");					
			# uil行.prop(self,	 "bp布料",translate=True,icon="NONE");	
			#uil行.prop(self,  "ip链",icon="NONE");	
			#uil行.prop(self,  "bp乙IK",icon="CONSTRAINT_BONE");
			
	def invoke(self, context, event):
		print("self.epIkType==",type(self.epIkType),self.epIkType);
		bpy.ops.op.load_ghost_ik();凷cvp(Gik,context);#Gik.cvpC ,Gik.oA,Gik.cvpA,Gik.pbA ,Gik.cvpSC ■		
		if(context.scene.ghost_ik.ep模式=="phy"):
			if(self.epIkType=="7"):
				self.bp布料=True;

		#----画画--------------------------
		print("Gik.CL条序L点序f2画G==",Gik.CL条序L点序f2画G,Gik.卍dll.乚3d,Gik.cvpSC);
		ci2骨数__=(c_int*2)(0,0);Gik.卍dll.dll.ii凸骨(Gik.cvpSC,ci2骨数__);print("ci2骨数__==",*ci2骨数__);
		if(Gik.CL条序L点序f2画G==None or Gik.CL条序L点序f2画G[0].__len__()<ci2骨数__[1] or Gik.卍dll.dll.卩凸画〇(True,True,True) ):
			画3dOP(bp显示=False);
			py_叵画(Gik,context.scene,b画面=True,b画丷=True,b画Λ=True,b画字=False,b画弓=False,b画m=True,b画2d=False \
										,L2条数丶iSize点=(3,ci2骨数__[1]*3),L2条数丶iSize线=(3,ci2骨数__[1]*3),L2条数丶iSize乛=(3,ci2骨数__[1]*3)\
										,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=ci2骨数__[1]*3);
		if(Gik.卍dll.乚3d==None):
			画3dOP(bp显示=True,bp画面=True,ip画字=True,bp灬=False);
		if(context.scene.ghost_ik.bp画画==False):
			Gik.卍dll.dll.凸画3d(False);
		
		return context.window_manager.invoke_props_dialog(self);#运行的第1步
	#----------------------------------------
	def execute(self, context):#运行的第三步
		sceneGHIK=context.scene.ghost_ik;
		cModePre=Gik.oA.mode;
		if(Gik.oA.mode!="POSE"):bpy.ops.object.mode_set(mode="POSE");
		iΔ叵Cpb(Gik.oA,True);print(" Gik.oA==",c_void_p(Gik.oA.as_pointer()),sceneGHIK.ep模式);
		Δ叵o(Gik.oA,True);
		Δ叵scene(sceneGHIK,False);
		
		LG.b丌仌=True;print("self.epIkType==",self.epIkType);
		#------------------------------------------
		# Llay=Gik.oA.data.layers;
		Cpb=Gik.oA.pose.bones;
		CpbS=context.selected_pose_bones_from_active_object;#print("CpbS==",CpbS);
		iiS=CpbS.__len__();
		for pb in CpbS:
			pb["PoseBone"]["type"]=pb.ghost_ik.type=TYPE_无;
			pb.rotation_mode="QUATERNION";pb.rotation_mode="XYZ";#● 可能是bl的bug,有时要切换模式才能正常.
		#------------------------------
		if(sceneGHIK.ep模式=="ik"):
			if(self.epIkType=="2"):
				pbA = context.active_pose_bone;pb爷=None;pb父=None;pb子=None;pb孙=None;pb孙子=None;cvpPb孙=None;cvpPb孙子=None;cvpPb子=None;cvpPb爷=None;

				if(iiS==0):CpbS.append(pbA);
				# if(iiS<2 or 4<iiS):
				if(iiS<2 or 2<iiS):
					self.report({"ERROR"},语.L出错[3]);#"INFO" "ERROR" "DEBUG" "WARNING"
					return {"FINISHED"};
					
				pb子=pbΔ罒子(CpbS);
				
				if(pb子):
					cvpPb子=c_void_p(pb子.as_pointer());print("▼pb子 ==",pb子.name);
					#pb子.ghost_ik.bp要更新=pb子.ghost_ik.bp要更新;
					Δ叵2ik(pb子,Gik.oA,TYPE_TWO子,1);
					# if(self.bp简单):
						# pb子["PoseBone"]["b脚"]=True;
					# else:
						# pb子["PoseBone"]["b脚"]=False;
						
					# if(self.ep轴向=="Z"):
						# pb子["PoseBone"]["bLR"]=0;
					# else:
						# pb子["PoseBone"]["bLR"]=1;
					# print("bLR==",pb子,pb子["PoseBone"]["bLR"]);
					#----状态--------------------------
					if(pb子.parent and pb子.parent.bone.select):
						pb父=pb子.parent;print("pb父==",pb父,pb父.parent);
						Δ叵2ik(pb父,Gik.oA,TYPE_TWO父,2);#Δ叵pb编ι(pb父);
						if(pb父.parent and pb父.parent.ghost_ik.type==TYPE_无 and \
							(pb父.bone.use_connect or pb父.bone.use_connect==False and 卩二二v(pb父.bone.head_local,pb父.parent .bone.tail_local))):#肩,爷 
							pb子["PoseBone"]["b脚"]=False;#手
							pb爷=pb父.parent;Δ叵2ik(pb爷,Gik.oA,TYPE_TWO爷);#Δ叵pb编ι(pb爷);
							cvpPb爷=c_void_p(pb爷.as_pointer());#print("pb爷==",pb爷.name);
						else:
							pb子["PoseBone"]["b脚"]=True;print("b脚==True",pb子.name);
						if(self.bp简单==False):
							for pb孙_ in pb子.children:
								if(pb孙_.bone.use_connect or pb孙_.bone.use_connect==False and 卩二二v(pb孙_.bone.head_local,pb子.bone.tail_local)):#pb孙_.ghost_ik.type==TYPE_无 and 
									Δ叵2ik(pb孙_,Gik.oA,TYPE_TWO孙,0);#Δ叵pb编ι(pb孙_);
									pb孙=pb孙_;cvpPb孙=c_void_p(pb孙.as_pointer());
									#print("pb孙==",pb孙.name);
									for pb孙子_ in pb孙_.children:
										if(pb孙子_.bone.use_connect or pb孙子_.bone.use_connect==False and 卩二二v(pb孙子_.bone.head_local,pb孙_.bone.tail_local)):
											pb孙_["PoseBone"]["b脚"]=pb孙子_["PoseBone"]["b脚"]=pb子["PoseBone"]["b脚"];
											Δ叵2ik(pb孙子_,Gik.oA,TYPE_TWO孙子,0);
											pb孙子=pb孙子_;cvpPb孙子=c_void_p(pb孙子.as_pointer());
											break;

									break;
				

					else:
						self.report({"ERROR"},语.L出错[4]);#"INFO" "ERROR" "DEBUG" "WARNING"
						return {"FINISHED"};
				else:#没有pcA
					self.report({"ERROR"},语.L出错[5]);#"INFO" "ERROR" "DEBUG" "WARNING"
					return {"FINISHED"};
				#----2ik--------------------------
				if(Gik.卍dll.dll.b凸SetType(cvpPb孙子,cvpPb孙,cvpPb子,cvpPb爷,Gik.cvpC,2,True)==False):#,self.bp目标
					# Δ删除属性(self,Cpb,"some bone may missing some attributes!! need to reset bone attributes");
					return {"FINISHED"};
				# print("4 type==",pb爷.ghost_ik.type,pb父.ghost_ik.type,pb子.ghost_ik.type,pb孙.ghost_ik.type);
				#------------------------------
				if(Gik.oA.mode!="EDIT"):bpy.ops.object.mode_set(mode="EDIT");#只有进入 EDIT 模式 才有 ebone数据,●● 这个会让原来 的arm_mat 指针失效
				Ceb=Gik.oA.data.edit_bones;print("self.ep轴向==",self.ep轴向,pb父.name,pb子.name);
				Gik.卍dll.dll.凸2eb骨roll(c_void_p(Ceb[pb父.name].as_pointer()),c_void_p(Ceb[pb子.name].as_pointer()),self.ep轴向.encode('UTF-8'),self.bp旋父);#默认对齐子轴
				bpy.ops.object.mode_set(mode="POSE");
				
				#------------------------------
				print("5▲==",pb爷,pb父,pb子,pb孙,pb孙子);#,pb子.ghost_ik.type
				I=Gik.卍dll.dll.i凸记录pc角(cvpPb孙子,cvpPb孙,cvpPb子,cvpPb爷,c_void_p(context.as_pointer()));
				if(I<0):return {"FINISHED"};
			#----spline ik--------------------------
			elif(self.epIkType=="1"):
				for pb in CpbS:
					Δ叵物理ik(pb);#["f16mι"] ■
					pb["PoseBone"]["type"]=pb.ghost_ik.type=TYPE_SPLINE;
				if(Gik.卍dll.dll.b凸SetType(None,None,None,None,Gik.cvpC,1,True)==False):#,False
					# Δ删除属性(self,Cpb,"some bone may missing some attributes!! need to reset bone attributes");
					return {"FINISHED"};
			#------------------------------
			print("self.epIkType==",self.epIkType);
			Δ十一IKgroup(self,context,self.epIkType);
		#----L物理[0]--------------------------
		else:
			def Δ选尾骨_(pb):
				if(pb.bone.select and pb.children):
					for pb子 in pb.children:
						if(pb子.bone.select==False and (pb子.bone.use_connect or pb子.bone.use_connect==False and 卩二二v(pb子.bone.head_local,pb.bone.tail_local))):
							pb子.bone.hide=False;pb子.bone.hide_select=False;pb子.bone.select=True;
							Δ选尾骨_(pb子);
			for pb子 in CpbS:
				Δ选尾骨_(pb子);
			#----叵scene--------------------------
			if(Gik.卍dll.dll.b凸凷物理dll(Gik.cvpC)==False):
				return {"FINISHED"};
			CpbS=context.selected_pose_bones_from_active_object;
			
			i物理丨布料=int(self.epDynType);print("sceneGHIK==",sceneGHIK.ip碰撞体ξ,i物理丨布料);
			for pb子 in CpbS:
				pb子.ghost_ik.bp物理=True;
				Δ叵物理ik(pb子);
				if(i物理丨布料==TYPE_物理):
					pb子["PoseBone"]["type"]=pb子.ghost_ik.type=TYPE_物理;
				elif(i物理丨布料==TYPE_布料):
					pb子["PoseBone"]["type"]=pb子.ghost_ik.type=TYPE_布料;
			Gik.oA.ppO.bp封闭=self.bp封闭;Gik.oA.ppO.bp物理o=True;
			if(Gik.卍dll.dll.b凸SetType(None,None,None,None,Gik.cvpC,i物理丨布料,False)==False):#,False
				# Δ删除属性(self,Cpb,"some bone may missing some attributes!! need to reset bone attributes");
				return {"FINISHED"};
			Gik.卍dll.dll.凸卌物理IK1次(c_float(self.fp乙扭性),c_float(self.fp乙刚性),c_float(self.fp乙弹性),self.bp渐变,self.bp碰撞,self.bp布料,Gik.cvpC);
			Δ十一IKgroup(self,context,self.epDynType);
			#------------------------------
			b=False;
			for O in Gik.L卐骷物理:
				if(O.o ==Gik.oA):
					b=True;break;
			if(b==False):
				Gik.L卐骷物理.append(Gik.卐O(Gik.oA));
				
		#----版本-----------------------------------------
		# if(Gik.oA.ppO.ivp3版本[2]==0):
		if(Gik.oA.ppO.ivp3版本[0]!=bpy.app.version[0] or Gik.oA.ppO.ivp3版本[1]!=bpy.app.version[1] or Gik.oA.ppO.ivp3版本[2]!=bpy.app.version[2] ):
			Gik.oA.ppO.ivp3版本=bpy.app.version;
		# Gik.卍dll.dll.凸blend版本_(b"ppO","ivp3版本".encode('UTF-8'),Gik.cvpC,c_void_p(Gik.oA.as_pointer()));
		print("Gik.oA.ppO.ivp3版本==",*Gik.oA.ppO.ivp3版本,bpy.app.version);
		# Gik.oA.ppO.ivp3版本[2]=Gik.oA.ppO.ivp3版本[0];
		#------------------------------
		LG.b丌仌=False;
		bpy.ops.object.mode_set(mode=cModePre);
		# bpy.ops.op.delete_ghost_ik();
		return {"FINISHED"};
		
# ////////////////////////////////////////////
class 卐十十全局碰撞卐Operator(bpy.types.Operator): 
	bl_idname = "op.add_ghostik_collider"
	bl_label = 语.L碰撞[0]
	bl_description = 语.L列表[1]
	
	def invoke(self, context, event):
		bΔNone凷物理(context);
		return self.execute(context);
		
	def execute(self,context):
		# return {"FINISHED"};
		CoS=bpy.context.selected_objects;sceneGHIK=context.scene.ghost_ik;ii点艹=0;
		for oS in CoS:	 
			if(oS.type=="MESH"):
				ii点=oS.data.vertices.__len__();
				if(oS.data.vertices.__len__()<10):
					self.report({"ERROR"},语.L出错[6]);#"INFO" "ERROR" "DEBUG" "WARNING"
					return {"FINISHED"};
				sceneGHIK.bp有待删除=sceneGHIK.bp有待删除;
				if(oS.name not in sceneGHIK.cp碰撞体.keys()):
					pg=sceneGHIK.cp碰撞体.add();sceneGHIK.ip碰撞体ξ=sceneGHIK.cp碰撞体.__len__()-1;
					pg.name=oS.name;pg.bp要删除=pg.bp要删除;cvpOS=c_void_p(oS.as_pointer());
					#------------------------------
					Δ叵碰撞体(oS,Gik.卍dll.dll.ii凸面3(cvpOS));
					# Δ凷1o属性col(self,context,oS,Gik.卍dll.dll);
					oS.color=Gik.浅蓝;Gik.卍dll.dll.凸十十1碰撞体(cvpOS);
					#---------------------------------------------
					if(ii点艹<ii点):
						ii点艹=ii点;
		#----画画--------------------------
		print("Gik.CL条序L点序f2画G==",Gik.CL条序L点序f2画G,Gik.卍dll.乚3d,Gik.cvpSC,ii点艹);
		if(Gik.CL条序L点序f2画G==None or Gik.CL条序L点序f2画G[0].__len__() <ii点艹 or Gik.卍dll.dll.卩凸画〇(True,True,True)):
			#----叵--------------------------
			画3dOP(bp显示=False);
			py_叵画(Gik,context.scene,b画面=True,b画丷=True,b画Λ=True,b画字=False,b画弓=False,b画m=True,b画2d=False \
										,L2条数丶iSize点=(3,ii点艹*2),L2条数丶iSize线=(3,ii点艹*2),L2条数丶iSize乛=(3,ii点艹*2)\
										,iSize丷=ii点艹+20,iSizeΛ=ii点艹*3,iSize厶=40,iSize字=ii点艹*2);
		if(Gik.卍dll.乚3d==None):
			画3dOP(bp显示=True,bp画面=True,ip画字=True,bp灬=False);
		if(context.scene.ghost_ik.bp画画==False):
			Gik.卍dll.dll.凸画3d(False);
		return {"FINISHED"};
		   
#========================================
class 卐一一全局碰撞卐Operator(bpy.types.Operator): 
	bl_idname = "op.remove_ghostik_collider"
	bl_label =语.L碰撞[1]
	bl_description = 语.L列表[2]		
	
	def invoke(self, context, event):
		try:
			bΔNone凷物理(context);
		except:pass;	
			
		return self.execute(context);	
	def execute(self,context):
		sceneGHIK=context.scene.ghost_ik;sA=sceneGHIK.cp碰撞体[sceneGHIK.ip碰撞体ξ].name;
		Co场=context.scene.objects;
		if(sA in Co场):
			oA=Co场[sA];
			if("COLLIDER" in oA):
				del oA["COLLIDER"];
			oA.ppO.type=0;oA.ppO.init=0;print("del COLLIDER");
			oA.color=Gik.白;
		sceneGHIK.cp碰撞体.remove(sceneGHIK.ip碰撞体ξ);Gik.卍dll.dll.凸一一1碰撞体(c_void_p(oA.as_pointer()));
		if (sceneGHIK.cp碰撞体.__len__()-1<sceneGHIK.ip碰撞体ξ):
			setattr(sceneGHIK,"ip碰撞体ξ", sceneGHIK.cp碰撞体.__len__()-1);#激活最后1个
		#---------------------------------------------
		bpy.ops.op.set_related_points(bp灬=True);
		return {"FINISHED"};
	
# ////本地////////////////////////////////////////
class 卐十十排除碰撞卐Operator(bpy.types.Operator): 
	bl_idname = "op.add_ghostik_collider_exclude"
	bl_label =  语.L列表2[1]	
	bl_description = 语.L列表2[1]		

	def execute(self,context):
		oA=context.pose_object;#骨架
		if(oA):
			pg=oA.ppO.cp排除碰撞体.add();
			pg.name=pg.name;pg.bp要删除=pg.bp要删除;
			# Δ凷1o属性col(self,context,oS,Gik.卍dll.dll);
		return {"FINISHED"};   
		   
#========================================
class 卐一一排除碰撞卐Operator(bpy.types.Operator): 
	bl_idname = "op.remove_ghostik_collider_exclude"
	bl_label = 语.L列表2[2]
	bl_description = 语.L列表2[2]		
	
	ξ:IntProperty(name='',description='',default=-1,min=-1,max=1000);
	def execute(self,context):
		if(Gik.oA==None):
			Gik.oA=context.pose_object;#骨架
		if(Gik.oA):
			Gik.oA.ppO.cp排除碰撞体.remove(self.ξ);
		return {"FINISHED"};
		
#========================================
class 卐乙绑定pose卐Operator(bpy.types.Operator): 
	bl_idname = "op.set_bind_pose"
	bl_label = 语.L设置[0]
	bl_description = 语.L设置[1]		
	
	def invoke(self, context, event):
		bΔNone凷物理(context);
		# return self.execute(context);
		return context.window_manager.invoke_props_dialog(self);
		
	def execute(self,context):
		Gik.卍dll.dll.凸乙绑定pose(c_void_p(context.as_pointer()));
		return {"FINISHED"};
		
#========================================
class 卐乙当前申卐Operator(bpy.types.Operator): 
	bl_idname = "op.set_anchor_pose"
	bl_label = 语.L设置[10]
	bl_description = 语.L设置[11]		
	
	def invoke(self, context, event):
		bΔNone凷物理(context);
		# return self.execute(context);
		return context.window_manager.invoke_props_dialog(self);
		
	def execute(self,context):
		Gik.卍dll.dll.凸乙申(c_void_p(context.as_pointer()),False);
		return {"FINISHED"};
		
#========================================
class 卐仌属性ik卐Operator(bpy.types.Operator): 
	bl_idname = "op.update_attribute_ik"
	bl_label = 语.L设置[6];
	bl_description = 语.L设置[7];
	
	def invoke(self, context, event):
		bpy.ops.op.load_ghost_ik();凷cvp(Gik,context);
		return context.window_manager.invoke_props_dialog(self);
	def execute(self,context):
		sceneGHIK=context.scene.ghost_ik;Co=context.scene.objects;
		for o in Co:
			print("o.name==",o.name,o.ppO.init);
			if(o.type=="ARMATURE" and 0<o.ppO.init):
				# self.report({"ERROR"},"select object is not an armature!!");#"INFO" "ERROR" "DEBUG" "WARNING"
				# return {"FINISHED"};
				iΔ叵Cpb(o,True);
				Δ叵o(o,True);
				# CpbS=context.selected_pose_bones_from_active_object;
				Cpb=o.pose.bones;
				for pb in Cpb:
					if(pb.ghost_ik.type in[TYPE_TWO孙子,TYPE_TWO孙,TYPE_TWO子,TYPE_TWO父,TYPE_TWO爷]):
						Δ叵2ik(pb,o,0);#全部当成子仌
					elif(pb.ghost_ik.type in[TYPE_物理,TYPE_布料]):
						Δ叵物理ik(pb);
				o.ppO.ivp3版本=bpy.app.version;
		#------------------------------
		if(0<sceneGHIK.cp碰撞体.__len__()):
			for pg碰撞体 in sceneGHIK.cp碰撞体:
				if(pg碰撞体.name in Co):
					o碰撞体=Co[pg碰撞体.name];
					Δ叵碰撞体(o碰撞体,Gik.卍dll.dll.ii凸面3(c_void_p(o碰撞体.as_pointer())));
					
		Δ叵scene(sceneGHIK,True);

		#------------------------------
		bpy.ops.op.load_ghost_ik();凷cvp(Gik,context);
		# Gik.卍dll.dll.凸重属性骷(Gik.cvpC);
		bpy.ops.op.update_bind_ik();
		return {"FINISHED"};
#========================================
class 卐仌ik绑定卐Operator(bpy.types.Operator): 
	bl_idname = "op.update_bind_ik"
	bl_label = 语.L设置[8];
	bl_description = 语.L设置[9];
	
	def invoke(self, context, event):
		bpy.ops.op.load_ghost_ik();凷cvp(Gik,context);
		return context.window_manager.invoke_props_dialog(self);
	def execute(self,context):
		
		Gik.oA=context.pose_object;
		if(Gik.oA):
			if(Gik.oA.mode!="EDIT"):bpy.ops.object.mode_set(mode="EDIT");#只有进入 EDIT 模式 才有 
			# Gik.卍dll.dll.凸仌ik绑定(c_void_p(context.as_pointer()));
			Cpb=Gik.oA.pose.bones;Ceb=Gik.oA.data.edit_bones;
			for pb in Cpb:
				if("b禁用" not in pb["PoseBone"]):#for ImdjsNodes
					pb["PoseBone"]["b禁用"]=False;
				if("driver"in pb["PoseBone"] and  pb.ghost_ik.type==TYPE_修正骨):
					pb["PoseBone"]["b禁用"]=True;
					
				if(pb.ghost_ik.type==TYPE_TWO子):
					Δ叵2ik(pb,Gik.oA,0);
					cvpPb孙子=None;cvpPb孙=None;cvpPb子=c_void_p(pb.as_pointer());cvpPb爷=None;
					if(pb.parent and pb.parent.ghost_ik.type==TYPE_TWO父):
						if(pb.parent.parent and pb.parent.parent.ghost_ik.type==TYPE_TWO爷):
							cvpPb爷=c_void_p(pb.parent.parent .as_pointer());
						if(pb.children and pb.children[0].ghost_ik.type==TYPE_TWO孙 and pb.children[0].bone.use_connect):
							cvpPb孙=c_void_p(pb.children[0].as_pointer());
							if(pb.children[0].children and pb.children[0].children[0].ghost_ik.type==TYPE_TWO孙子 and pb.children[0].children[0].bone.use_connect):
								Δ叵2ik(pb.children[0].children[0],Gik.oA,0);
								cvpPb孙=c_void_p(pb.children[0].children[0].as_pointer());				
					Gik.卍dll.dll.凸2eb骨roll(c_void_p(Ceb[pb.parent.name].as_pointer()),c_void_p(Ceb[pb.name].as_pointer()),"Z".encode('UTF-8'),True);#默认对齐子轴
					Gik.卍dll.dll.i凸记录pc角(cvpPb孙子,cvpPb孙,cvpPb子,cvpPb爷,c_void_p(context.as_pointer()));
			bpy.ops.object.mode_set(mode="POSE");
			bpy.ops.op.delete_ghost_ik();
		return {"FINISHED"};
#========================================
_L="_L";
_R="_R";
L_=".L";
R_=".R";
l_="l";
r_="r";

class 卍PRS:
	p=None;s=None;r=None;q=None;申=None;
	def __init__(self,pb,o):
		self.p=copy.deepcopy(pb.location);self.r=copy.deepcopy(pb.rotation_euler);self.s=copy.deepcopy(pb.scale);self.q=copy.deepcopy(pb.rotation_quaternion);print("==",self.p);
		if(pb.ghost_ik.type==TYPE_TWO子):
			self.申=tuple(o["PoseBone"][pb.name]["申Φ"]);

		pass;
#========================================
class 卐对称pose卐Operator(bpy.types.Operator): 
	bl_idname = "op.sym_pose"
	bl_label = 语.L对称[0]
	bl_description = 语.L对称[1]		
	
	ip:IntProperty(name='',description='',default=0,min=0,max=2,step=1);#0 复制,1粘贴,2对称粘贴
	def invoke(self, context, event):
		if(self.ip==0):#吅
			Gik.MpbPRS.clear();
		Gik.oA=context.pose_object;
		if(Gik.oA):
			return self.execute(context);
		return {"CANCELED"};
	
	def Δ对称pbLR(self,pb入,o,PRS,b反):
		print("Δ对称pbLR==",pb入.name,PRS,b反,Gik.oA.ppO.bp只选);
		# if(Gik.oA.ppO.bp只选 and pb入.bone.select or Gik.oA.ppO.bp只选==False):
		if(b反):
			pb入.rotation_euler.x=PRS.r.x;pb入.rotation_euler.y=-PRS.r.y;pb入.rotation_euler.z=-PRS.r.z;
			pb入.rotation_quaternion.w=PRS.q.w;pb入.rotation_quaternion.x=PRS.q.x;pb入.rotation_quaternion.y=-PRS.q.y;pb入.rotation_quaternion.z=-PRS.q.z;
			if(PRS.p.x!=0 or PRS.p.y!=0 or PRS.p.z!=0):
				pb入.location.x=-PRS.p.x;pb入.location.y=PRS.p.y;pb入.location.z=PRS.p.z;
			if(pb入.ghost_ik.type==TYPE_TWO子):
				o["PoseBone"][pb入.name]["申Φ"]=(c_float*6)(-PRS.申[0],PRS.申[1],PRS.申[2],PRS.申[3],PRS.申[4],PRS.申[5]);
		
		else:
			pb入.rotation_euler.x=PRS.r.x;pb入.rotation_euler.y=PRS.r.y;pb入.rotation_euler.z=PRS.r.z;
			pb入.rotation_quaternion.w=PRS.q.w;pb入.rotation_quaternion.x=PRS.q.x;pb入.rotation_quaternion.y=PRS.q.y;pb入.rotation_quaternion.z=PRS.q.z;
			if(PRS.p.x!=0 or PRS.p.y!=0 or PRS.p.z!=0):
				pb入.location.x=PRS.p.x;pb入.location.y=PRS.p.y;pb入.location.z=PRS.p.z;			
			if(pb入.ghost_ik.type==TYPE_TWO子):
				o["PoseBone"][pb入.name]["申Φ"]=(c_float*6)(*PRS.申);

		pb入.scale=PRS.s;	
		
	def bΔL_R后(self,sL,sR,pb入,Cpb,o,PRS):
		if(pb入.name[-2:]==sL):
			nameL=pb入.name[:-2];
			if(Cpb):
				for pbR in Cpb:
					if(pbR==pb入):continue;
					if(pbR.name[-2:]==sR and nameL==pbR.name[:-2]):
						self.Δ对称pbLR(pbR,o,PRS,True);
						return True;
		elif(pb入.name[-2:]==sR):
			nameR=pb入.name[:-2];
			if(Cpb):
				for pbL in Cpb:
					if(pbL==pb入):continue;
					if(pbL.name[-2:]==sL and nameR==pbL.name[:-2]):
						self.Δ对称pbLR(pbL,o,PRS,True);
						return True;						
		return False;
	#----Left_bone,Right_bone--------------------------
	def bΔL_R前5(self,sL,sR,pb入,Cpb,o,PRS):
		if(pb入.name[:5]==sL):
			nameL=pb入.name[5:];
			if(Cpb):
				for pbR in Cpb:
					if(pbR==pb入):continue;
					if(pbR.name[:5]==sR and nameL==pbR.name[5:]):
						self.Δ对称pbLR(pbR,o,PRS,True);
						return True;
		elif(pb入.name[:5]==sR):
			nameR=pb入.name[5:];
			if(Cpb):
				for pbL in Cpb:
					if(pbL==pb入):continue;
					if(pbL.name[:5]==sL and nameR==pbL.name[5:]):
						self.Δ对称pbLR(pbL,o,PRS,True);
						return True;						
		return False;
	#----lBone,rBone--------------------------
	def bΔL_R前1(self,sL,sR,pb入,Cpb,o,PRS):
		if(pb入.name[:1]==sL):#l
			nameL=pb入.name[1:];#Bone
			if(Cpb):
				for pbR in Cpb:
					if(pbR==pb入):continue;
					if(pbR.name[:1]==sR and nameL==pbR.name[1:]):
						self.Δ对称pbLR(pbR,o,PRS,True);
						return True;
		elif(pb入.name[:1]==sR):
			nameR=pb入.name[1:];
			if(Cpb):
				for pbL in Cpb:
					if(pbL==pb入):continue;
					if(pbL.name[:1]==sL and nameR==pbL.name[1:]):
						self.Δ对称pbLR(pbL,o,PRS,True);
						return True;						
		return False;
	#========================================
	def execute(self,context):
		Cpb=Gik.oA.pose.bones;
		if(Gik.oA.ppO.bp只选):
			CpbS=context.selected_pose_bones;#print("CpbS==",CpbS);
		else:
			CpbS=Cpb;
		#----吅--------------------------
		if(self.ip==0):
			if(CpbS):
				for pb in CpbS:
					Gik.MpbPRS[pb]=卍PRS(pb,Gik.oA);print("Gik.MpbPRS[pb]==",Gik.MpbPRS[pb].r);
			self.report({"INFO"},"have copy poses:%d"%CpbS.__len__());#"INFO" "ERROR" "DEBUG" "WARNING"
		#----粘贴--------------------------
		else:
			print("self.ip==",self.ip);
			#----1粘贴 --------------------------
			if(self.ip==1):
				for pb入,PRS in Gik.MpbPRS.items():
					self.Δ对称pbLR(pb入,Gik.oA,PRS,False);
			#----2 反粘贴--------------------------
			elif(self.ip==2):
				for pb入,PRS in Gik.MpbPRS.items():
					print("PRS==",pb入.name,PRS.p,PRS.r);
					if(self.bΔL_R后(_L,_R,pb入,Cpb,Gik.oA,PRS)==False):
						if(self.bΔL_R后(L_,R_,pb入,Cpb,Gik.oA,PRS)==False):
							if(self.bΔL_R前1(l_,r_,pb入,Cpb,Gik.oA,PRS)==False):
								print("!! 找不到 bΔL_R前1==",pb入.name);
								if(pb入.name[-2:] not in [_L,_R,L_,R_] \
									or pb入.name[:5] !=l_ or pb入.name[:6] !=r_):#自己
									self.Δ对称pbLR(pb入,Gik.oA,PRS,True);
								
							
		return {"FINISHED"};
		
#========================================
class 卐吅申卐Operator(bpy.types.Operator): 
	bl_idname = "op.copy_anchor"
	bl_label = 语.L对称[5]
	bl_description = 语.L对称[5]		
	
	ip:IntProperty(name='',description='',default=0,min=0,max=2,step=1);#0 复制,1粘贴
	# bp选中:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	def invoke(self, context, event):
		print("self.ip 0==",self.ip);
		bpy.ops.op.load_ghost_ik();#凷cvp(Gik,context);
		Gik.oA=context.pose_object;
		if(Gik.oA):
			return self.execute(context);
		return {"CANCELED"};
		
	def execute(self,context):
		Cpb=Gik.oA.pose.bones;
		if(Gik.oA.ppO.bp只选):
			CpbS=context.selected_pose_bones;#print("CpbS==",CpbS);
		else:
			CpbS=Cpb;
		#----吅--------------------------
		if(self.ip==0):
			Gik.卍dll.dll.凸吅申(c_void_p(context.as_pointer()),False);
		#----粘贴--------------------------
		else:
			print("self.ip 粘贴==",self.ip);
			#----1粘贴 --------------------------
			if(self.ip==1):
				Gik.卍dll.dll.凸吅申(c_void_p(context.as_pointer()),True)
				Gik.oA.update_tag(refresh={'DATA'});
		return {"FINISHED"};
		
# ========================================
# class 卐执行ik卐Operator(bpy.types.Operator): 
	# bl_idname = "op.excute_ik"
	# bl_label ="执行ik"
	# bl_description = 语.L对称[5]		
	
#========================================
class 卐插入关键帧pose卐Operator(bpy.types.Operator): 
	bl_idname = "op.insert_keyframe_pose"
	bl_label = 语.L设置[4]
	bl_description = 语.L设置[5]		
	
	#----------------------------------------
	@classmethod
	def poll(cls, context):#决定是否激活
		return (context.object.type=="ARMATURE");

	def draw(self, context):
		uil行=self.layout.row(align=False);
		uil行.prop(context.object.ppO,"bp只选",translate=True,icon="NONE");
		
	def invoke(self, context, event):
		bpy.ops.op.load_ghost_ik();凷cvp(Gik,context);
		if(Gik.oA==None):
			Gik.oA=context.pose_object;#骨架
		return context.window_manager.invoke_props_dialog(self);
		
	def execute(self,context):
		B=Gik.卍dll.dll.b凸插入关键帧pose(c_void_p(Gik.oA.as_pointer()),c_void_p(context.as_pointer()),Gik.oA.ppO.bp只选);
		if(B==False):
			iΔ叵Cpb(Gik.oA,True);
			
			Gik.卍dll.dll.b凸凷L骷G(None,Gik.cvpC);
			self.report({"WARNING"},"iΔ叵Cpb");#"INFO" "ERROR" "DEBUG" "WARNING"
			return {"FINISHED"};
		CpbA=Gik.oA.pose.bones;pbA=context.active_pose_bone;艹=0;
		# if(pbA==None):pbA=Gik.oA.data.bones.active=CpbA[0];
		S骨(False);
		for pb in CpbA:
			print("bp要插关键帧==",pb.name,pb.ghost_ik.bp要插关键帧,pb["PoseBone"]["b动画"]);
			if(pb.ghost_ik.bp要插关键帧):
				# LpbS[艹]=pb;
				if(pb["PoseBone"]["b动画"]):
					# 艹+=1;
					pb.bone.select=True;pb.ghost_ik.bp要插关键帧=False;#print("插入关键帧pose pbS==",pb.name);
		bpy.ops.anim.keyframe_insert_menu(type='Available', always_prompt=False);
		S骨(False);
		Gik.oA.data.bones.active=pbA.bone;
		return {"FINISHED"};
		
		
#//////////////////////////////////////
class 卐激活物名给sp卐Operator(bpy.types.Operator):
	bl_idname = "op.ghost_active_name_sp";
	bl_label = "active_name_sp";
	bl_context='object';
	bl_description="pick the active object"

	sp:StringProperty(name="注意", description="", default="are you sure init group ?");
	def invoke(self, context, event):
		Gik.oA=context.active_object;
		if(Gik.oA.type!="ARMATURE"):
			self.report({"ERROR"},语.L出错[7]);#"INFO" "ERROR" "DEBUG" "WARNING"
			return {"FINISHED"};
		return self.execute(context);
	#------------------------------------------------------------
	def execute(self, context):
		if(Gik.oA):
			self.nThis.sp计算距离物体=Gik.oA.name;
			print("pick up object: %s"%oA.name);
		else:
			self.report({"ERROR"},"!!! can't find node");#"INFO" "ERROR" "DEBUG" "WARNING"
		return {"FINISHED"};
			
class 卐十十1个arm卐Operator(bpy.types.Operator):#按+ 号
	bl_idname = 'op.add_one_armature'
	bl_label = 语.增加骨架
	bl_description = "add an armature to be synchronization"

	def execute(self, context):
		oA=context.pose_object;
		if(oA):
			oA.ppO.cp骨同步.add();
		return {"FINISHED"};
  
class 卐一一1个arm卐Operator(bpy.types.Operator):#按-号
	bl_idname = 'op.dele_one_armature'
	bl_label = 语.移除骨架
	bl_description = "delete this item"
	sp:StringProperty(name='',description='',default='remove this armature?');

	ip第几个:IntProperty(name='',description='',default=0,min=0,max=10000,step=1);
	#------------------------------------------------------------
	def draw(self, context):	
		self.layout.props_enum(self, "sp");
		
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self,width=400);#召唤

	def execute(self, context):
		oA=context.pose_object;
		if(oA):
			oA.ppO.cp骨同步.remove(self.ip第几个);
		return {"FINISHED"};
#========================================
class 卐十十约束给arm的卐Operator(bpy.types.Operator):#按+ 号
	bl_idname = 'op.add_selected_armature_cons'
	bl_label = 语.增加骨架约束con
	bl_description = "add constraints to  selected armature	 from active armature to be synchronization"
	sp:StringProperty(name='',description='',default='add constraints to the selected armature?');
	
	#------------------------------------------------------------
	def draw(self, context):	
		self.layout.label(text=self.sp,text_ctxt='',translate=True,icon='NONE',icon_value=0);
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self,width=400);#召唤
	def execute(self, context):
		oA=context.active_object;
		if(oA):
			CoS=bpy.context.selected_objects;
			if(CoS.__len__()<2):
				self.report({"ERROR"},"must select at least two armatures!!");#"INFO" "ERROR" "DEBUG" "WARNING"
				return {"FINISHED"};
			s2 = bpy.context.scene;CpbA=oA.pose.bones;
			for o选 in CoS:
				if(o选==oA):continue;
				if(o选.type =="ARMATURE"):
					# Ms骨boneS=o选.data.bones;
					CpbS=o选.pose.bones;#所有pb骨
					for sA,pbA in CpbA.items():
					# for sS,pbS in CpbS.items():
						if(sA in CpbS):#同名骨
							pbS=CpbS[sA];b链接=pbS.bone.use_connect;
							CconsS=pbS.constraints;b有否旋转约束=None;b找到=False;b找到2=False;
							for cons in CconsS:
								i判断=None;
								if(cons.type=="COPY_ROTATION"):
									if(cons.name[:5] =="SYNC-"):
										b找到=True;
										if(b链接):
											break;
											
								if(b链接==False):
									if(cons.type=="COPY_LOCATION"):
										if(cons.name[:5] =="SYNC-"):
											b找到2=True;break;
							if(b找到==False):
								cons=CconsS.new("COPY_ROTATION");cons.name="SYNC-R_"+pbS.name;
								cons.target=oA;cons.subtarget=pbA.name;cons.owner_space=cons.target_space="LOCAL";
							if(b链接==False and b找到2==False):
								cons=CconsS.new("COPY_LOCATION");cons.name="SYNC-L_"+pbS.name;
								cons.target=oA;cons.subtarget=pbA.name;cons.owner_space=cons.target_space="LOCAL";
								
		return {"FINISHED"};
		
		
class 卐切换约束arm卐Operator(bpy.types.Operator):#
	bl_idname = 'op.toggle_selected_armature_cons'
	bl_label = 语.切换骨架约束con开关
	bl_description = "toggle selected constraints on/off"
	bp开关:BoolProperty(name='',description='',default=False,subtype='NONE',update=None);
	def execute(self, context):
		CoS=bpy.context.selected_objects;self.bp开关=not self.bp开关;i约束数=0;
		for o选 in CoS:
			if(o选.type =="ARMATURE"):
				# Ms骨boneS=o选.data.bones;
				# CpbS=o选.pose.bones;#所有pb骨
				for pbS in o选.pose.bones:
					b链接=pbS.bone.use_connect;
					CconsS=pbS.constraints;i处理完两个=0;
					for cons in CconsS:
						if(cons.type=="COPY_ROTATION"):
							if(cons.name[:5] =="SYNC-"):
								cons.mute=self.bp开关;
								i约束数+=1;
								break;
								
					if(b链接==False):	   
						for cons in CconsS:
							if(cons.type=="COPY_LOCATION"):
								if(cons.name[:5] =="SYNC-"):
									cons.mute=self.bp开关;
									i约束数+=1;
									break;
						 
			 
		self.report({"ERROR"},"on/off=%d,num=%d"%(not self.bp开关,i约束数));#"INFO" "ERROR" "DEBUG" "WARNING"
		return {"FINISHED"};
		
#========================================
class 卐关于Ghost_ik卐Operator(卐关于我卐Operator):
	bl_idname = 'op.about_me_ghost_ik'
	bl_label = ''
	bl_description = 'about me'
	bp查看更新:BoolProperty(name="check update?",description = 'some of my other addons',default=True);
	bp查看其它插件:BoolProperty(name='check my other addons?',description='check my other addons?',default=True,subtype='NONE',update=None);

	url链接="https://blenderartists.org/t/ghost-ik-virtual-inverse-kinematics-bone-physic-bone-ik-c/1101771";
	url其它插件="https://blenderartists.org/u/imdjs/activity/topics";
	#url捐助="https://inspirepay.com/pay/imdjs";
	#url捐助="https://imdjs.blogspot.com/2017/09/original-addons-for-blender.html";
	#---------------------------------------------
	@classmethod 
	def poll(self,context):
		return True;
	
	def draw(self, context):
		for s in 语.Ls介绍:
			self.layout.label(text=s, text_ctxt="", translate=True, icon='NONE', icon_value=0);
		uil行=self.layout.row(align=False);
		uil行.prop(self, "bp查看更新");
		self.layout.prop(self, "bp查看其它插件");	 
		
	def invoke(self, context, event):#运行的第1步
		return context.window_manager.invoke_props_dialog(self,width=600);
	""""""
	def execute(self, context):
		if(self.bp查看更新):
			webbrowser.open(self.url链接, new=0, autoraise=True);
		if(self.bp查看其它插件):
			webbrowser.open(self.url其它插件, new=2, autoraise=True);
		return {"FINISHED"};
		
		
		
		
		
		

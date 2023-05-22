
from .G import 语;
import platform;
bl_info = {
	"name": "IMDJS_ghost_ik",
	"author": "imdjs",
	#"version": Gik.version,
	"version": (1,1,0),
	"blender": (3,6, 0),
	# "description": 语.description,
	"description": "virtual IK that use the defromed bone as controler/physical bone simulator",
	"wiki_url": "https://blenderartists.org/u/imdjs/activity/topics",
	"tracker_url": "https://blenderartists.org/u/imdjs/activity/topics",
	"warning": "--",
	"category": "Animation"}
#—————————————————————————————————————————————————————————
import mathutils
# from IMDJS_nodes.OP_cloth import Δ凷1o属性col;#卐碰撞物init卐Operator
from .OP import *
# from ctypes import wintypes
# from .OP import wintypes
windll.kernel32.FreeLibrary.argtypes = [wintypes.HMODULE];
from .draw import 画3dOP;

from .func import Δ乙卍dll;
from .PG import*
from .bake import*

from IMDJS_ghost_ik.PG import 卐pb属性卐PropertyGroup;
from IMDJS_ghost_ik.G import  TYPE_无,TYPE_SPLINE,TYPE_TWO孙子,TYPE_TWO孙,TYPE_TWO子,TYPE_TWO父,TYPE_TWO爷,TYPE_物理,TYPE_布料;



class 卐ghost_ik卐AddonPreferences(bpy.types.AddonPreferences):
	bl_idname =__name__ #●●必须用__name__ 
	
	def 仌(self, context):
		if(self.ep语言!="None"):
			file=os.path.join(os.path.dirname(__file__),"LANG\\lang.txt");
			with open(file, 'w',encoding='gbk') as 文件:
				文件.write(self.ep语言);
				文件.close();
				print("仌==",self.ep语言);	
	
	ep语言:EnumProperty( name=语.L语言[0], description=语.L语言[1], items=[("None","None(无)","--",0),("english","english(英文)","--",1),("chinese","chinese(中文)","--",2)],default="None",update=仌);
	def draw(self, context):
		uil界 = self.layout;
		uil界.label(text='language (语言,重启blender生效) avilable after restarting Blender',text_ctxt='',translate=True,icon='NONE',icon_value=0);
		uil行=uil界.row();
		# uil栋=uil行.column();
		uil行.prop_enum(self,"ep语言",value="None");
		uil行.prop_enum(self,"ep语言",value="english");#单行切换按钮
		uil行.prop_enum(self,"ep语言",value="chinese");
bpy.utils.register_class(卐ghost_ik卐AddonPreferences);

class 卐XDLL卐Operator(bpy.types.Operator):
	bl_idname = 'op.delete_ghost_ik';
	bl_label = 'del_dll';

	def execute(self, context):
		if(Gik.卍dll.dll):
			bpy.ops.screen.animation_cancel(restore_frame=False);
			
			画3dOP(bp显示=False,bp灬=True);
			# windll.kernel32.FreeLibrary.argtypes = [wintypes.HMODULE];#定义参数的类型
			灬cvpIK();	
			try:
				Gik.卍dll.dll.凸灬dllik();#●有可能 在imdjs_nodes 删除了dll
				Gik.卍dll.dll.凸灬dlldjs();Gik.卍dll.dll.凸灬dllbl();Gik.卍dll.dll.凸灬dll物理();
				print("Gik.卍dll.i凸引用数()==",Gik.卍dll.dll.i凸引用数());
				if(Gik.卍dll.dll.i凸引用数()==0):
					Gik.卍dll.灬();
			except:
				Gik.卍dll.灬();
			
			print ("已经删除DLLЖ////////////////////////////////Ж////////////////////////////////Ж////////////////////////////////");
			
		# LG.b丌仌=True;context.scene.ghost_ik.bp画画=False;LG.b丌仌=False;
		#print ("fp=",context.scene.fp参数s2)
		return {"FINISHED"};
		
class 卐载入DLL卐Operator(bpy.types.Operator):
	bl_idname = 'op.load_ghost_ik';
	bl_label = '载入dll';
	
	def execute(self, context):
		#D=卐DLL类型();
		# print("Gik.卍dll.dll==",Gik.卍dll.dll);

		if(Gik.卍dll.b乙(dllpathIK64B,dllpathIK64)):
			Gik.卍dll.dll.凸载入scene亖IK(c_void_p(context.as_pointer()));
			
			print("Gik.卍dll.b乙==",dllpathIK64B);
			if(context.scene.ghost_ik.bp用修正):
				if(Gik.L卐o修正骷==[]):
					# Gik.卍dll.dll1.凸灬G();Gik.L卐o修正骷.clear();#●全局变量如果不清除,重载场景会出错
					bΔ凷L卐o骷G(context,context.scene.ghost_ik.bp用修正,False);#L卐o修正骷 ■
					# Gik.卍dll.dll1.凸凷修正骷(c_void_p(context.as_pointer()),False);#Mo卍骷驱动G ■
			"""
			凷cvp(Gik,context);
			Gik.卍dll.dll.凸画3d(False); 
			Gik.Ms申.clear();Gik.Ms向.clear();
			"""
			bpy.ops.op.init_scene_debug_ik();
		else:
			print("★载入dll失败==",dllpathIK64B,dllpathIK64);
			# self.report({"ERROR"},"★载入dll失败 %s ,%s"%(dllpathIK64B,dllpathIK64));#"INFO" "ERROR" "DEBUG" "WARNING"
		try:
			print("LOAD dll==",Gik.cvpC,Gik.卍dll.dll);
		except:pass;	
		return {"FINISHED"};
				
#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－		 
class 卐正常化骨四元卐Operator(bpy.types.Operator): 
	bl_idname = "o2.norm"
	bl_label = " "
	bl_description = "---"		
	@classmethod 
	def poll(self,context):
		return context.active_pose_bone ;
	def execute(self,context):
		pbA=context.active_pose_bone ;
		pbA.rotation_quaternion.normalize();
		return {"FINISHED"};
		
class 卐选骨不用gIK卐Operator(bpy.types.Operator): 
	bl_idname = "o2.g_ik_off"
	bl_label = " "
	bl_description = "---"		
	@classmethod 
	def poll(self,context):
		return context.active_pose_bone ;
	def execute(self,context):
		LpbA=bpy.context.selected_pose_bones_from_active_object;
		#for pbA in LpbA:	 
			#pbA.ghost_ik.ep选类型 = Gik.DEFAULT;
		return {"FINISHED"};   
		
class 卐SetType卐Operator(bpy.types.Operator): 
	bl_idname = "op.set_bone_type"
	bl_label = " "
	bl_description = "---"		
	sp:StringProperty(name='',description='',default='are you want to change bone type from spline IK to normal IK?',maxlen=0,subtype='NONE',update=None);
	spType:StringProperty(name='',description='',default='',maxlen=0,subtype='NONE',update=None);

	def draw(self, context):
		uil行=self.layout.row(align=True);
		uil行.prop(self,	 "sp",icon="NONE");
		
	def invoke(self, context, event):
		print("invoke==",);
		pbA = context.active_pose_bone;#print("spType==",pbA.ghost_ik.type,self.spType);
		Δ乙卍dll();	
		"""
		if(pbA.ghost_ik.type==0 and self.spType!="0"):
			return context.window_manager.invoke_props_dialog(self);#运行的第1步
		else:
			return self.execute(context);
		"""
		return self.execute(context);
		
	def execute(self,context):
		print("execute==",);

		Gik.卍dll.dll.b凸SetType(None,None,None,None,c_void_p(context.as_pointer()),int(self.spType),True);
			
		return {"FINISHED"}; 

# ////////////////////////////////////////////
class 卐画碰撞卐Operator(bpy.types.Operator): 
	bl_idname = "op.draw_ghostik_collider"
	bl_label = "画碰撞"
	bl_description = "画碰撞顶点"		

	def execute(self,context):
		scene=context.scene;cp碰撞体=scene.ghost_ik.cp碰撞体;Co=scene.objects;
		Δ乙卍dll();		
		Gik.卍dll.dll.凸画亍丅(c_void_p(context.as_pointer()));
		for pg in cp碰撞体:
			if(pg.name in Co):
				o=Co[pg.name];
				if(Gik.CL条序L点序f2画G==None or Gik.卍dll.dll.卩凸画〇(True,True,True)):
					冖=o.data.vertices.__len__()+5;
					画3dOP(bp显示=False);
					py_叵画(Gik,context.scene,Gik,b画面=True,b画丷=True,b画Λ=True,b画字=True,b画弓=False,b画m=True,b画2d=False \
											,L2条数丶iSize点=(5,冖),L2条数丶iSize线=(5,冖),L2条数丶iSize乛=(5,冖*3) \
											,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=400 );
		if(Gik.卍dll.乚3d==None):
			画3dOP(bp显示=True,bp画面=True,bp画弓=False);
		return {"FINISHED"};

# ////////////////////////////////////////////
class 卐试碰撞卐Operator(bpy.types.Operator): 
	bl_idname = "op.try_ghostik_collider"
	bl_label = "试碰撞"
	bl_description = "试碰撞"		

	def invoke(self, context, event):
		print("invoke==",Gik.卍dll.dll);
		pbA = context.active_pose_bone;#print("spType==",pbA.ghost_ik.type,self.spType);
		Δ乙卍dll();	
		return self.execute(context);
		
	def execute(self,context):
		scene=context.scene;cp碰撞体=scene.ghost_ik.cp碰撞体;Co=scene.objects;

		for pg in cp碰撞体:
			if(pg.name in Co):
				o=Co[pg.name];
				if(Gik.CL条序L点序f2画G==None or Gik.卍dll.dll.卩凸画〇(True,True,True)):
					冖=o.data.vertices.__len__()+5;
					画3dOP(bp显示=False);
					py_叵画(Gik,context.scene,Gik,b画面=True,b画丷=True,b画Λ=True,b画字=True,b画弓=False,b画m=True,b画2d=False \
												,L2条数丶iSize点=(5,冖),L2条数丶iSize线=(5,冖),L2条数丶iSize乛=(5,冖*3) \
											,iSize丷=ci2骨数__[1]+20,iSizeΛ=ci2骨数__[1]*3,iSize厶=40,iSize字=400);
		#-----------------------------------
		Gik.cvpC=c_void_p(context.as_pointer());
		Δ重填Lo物理骨(Gik,scene);
		Gik.卍dll.dll.凸试碰撞(c_void_p(context.as_pointer()));

		if(Gik.卍dll.乚3d==None):
			画3dOP(bp显示=True,bp画面=True,bp画丷=True,bp画弓=False);
		return {"FINISHED"};
		
# ////////////////////////////////////////////
class  PT_PT_IK_Tools(bpy.types.Panel):
	bl_space_type = "VIEW_3D";
	bl_region_type = "UI";#UI,TOOLS
	bl_label = "ghost_ik 2023-5-1";
	bl_description = "virtual IK  and physical bone(blender 3.41)."	   
	# bl_context = "posemode"
	bl_category="DJS"
	# sp骨架:StringProperty(name='',description='',default='');
	sceneGHIK=None;ppO=None;iArm=-1;# 0 mesh,1 骨
	def draw(self, context):
		#uil界.prop(context.scene.ghost_ik,'bp用硬子');
		uil界=self.layout;
		if(Gik.sp警告G!=""):
			# if(context.window_manager.sp警告==""):
				# context.window_manager.sp警告=Gik.sp警告G;
			uil界.label(text="ERROR ★",icon="ERROR");
			uil界.label(text=Gik.sp警告G);
			uil界.label(text="now your BL version is: ");
			uil界.label(text=str(bpy.app.version));
			return ;
		Gik.oA=context.active_object;pbA=context.active_pose_bone;
		self.sceneGHIK=context.scene.ghost_ik;
		uil行禁用= uil界.row(align=True);
		uil行禁用.operator(卐XDLL卐Operator.bl_idname, text="X dll",icon="COLORSET_01_VEC");	
		uil行禁用.prop(self.sceneGHIK,'bp禁用sc', toggle=False,translate=True,);
		if(self.sceneGHIK.bp禁用sc):
			return;
		label = uil界.row(align=True);
		label1 = uil界.row(align=True);		
		
		uil行 = uil界.row(align=True);
		uil行.prop_enum(self.sceneGHIK,"ep模式", value="ik", text_ctxt="", translate=True, );#IK模式
		uil行.prop_enum(self.sceneGHIK,"ep模式", value="phy", text_ctxt="", translate=True, );#物理模式
		uil行.scale_y=1.5; 
		uil行模式1 = uil界.row(align=True);
		
		if(Gik.oA):
			if(Gik.oA.type=="ARMATURE"):
				self.iArm=1;
			else:
				self.iArm=0;#mesh
			self.ppO=Gik.oA.ppO;
			uil行禁用.prop(self.ppO,'bp禁用o',toggle=True, translate=True,);
			uil行 = uil界.row(align=True);uil行.enabled=False;
			uil行.prop(self.ppO,'ivp3版本',translate=True,icon='NONE',slider=False,toggle=False);
			if(pbA):
				uil行=uil界.split(factor=0.2, align=True );
				uil行.label(text='type:',translate=True,icon='NONE',icon_value=0);#print("pbA.ghost_ik.type==",pbA.ghost_ik.type);
				if(pbA.ghost_ik.type<1):
					uil行.label(text='',translate=True,icon='NONE',icon_value=0);
				elif(pbA.ghost_ik.type==TYPE_SPLINE):
					uil行.label(text='spline IK',translate=True,icon='OUTLINER_DATA_CURVE',icon_value=0);
				elif(pbA.ghost_ik.type==TYPE_TWO孙子):
					uil行.label(text='two IK great-grandson',translate=True,icon='BONE_DATA',icon_value=0);	
				elif(pbA.ghost_ik.type==TYPE_TWO孙):
					uil行.label(text='two IK grandson',translate=True,icon='BONE_DATA',icon_value=0);	
				elif(pbA.ghost_ik.type==TYPE_TWO子):
					uil行.label(text='two IK child',translate=True,icon='BONE_DATA',icon_value=0);	 
				elif(pbA.ghost_ik.type==TYPE_TWO父):
					uil行.label(text='two IK parent',translate=True,icon='BONE_DATA',icon_value=0);	
				elif(pbA.ghost_ik.type==TYPE_TWO爷):
					uil行.label(text='two IK root',translate=True,icon='CONSTRAINT_BONE',icon_value=0);						
				elif(pbA.ghost_ik.type==TYPE_物理):
					uil行.label(text='physical IK',translate=True,icon='FORCE_CURVE',icon_value=0);		
				elif(pbA.ghost_ik.type==TYPE_布料):
					uil行.label(text='cloth IK',translate=True,icon='MOD_CLOTH',icon_value=0);		
				elif(pbA.ghost_ik.type==TYPE_修正骨):
					uil行.label(text='driver',translate=True,icon='DRIVER',icon_value=0);						
			#----用物理-------------------------------
			uil行物理=uil界.row(align=True);
			uil行物理.prop(self.sceneGHIK,'bp物理sc',translate=True,toggle=False,icon="NONE");
			#----IK 模式-------------------------------
			if(self.sceneGHIK.ep模式=="ik"):
				uil行ik=uil界.row(align=True);
				uil行ik.prop(self.ppO,'bp用钉o',translate=True,toggle=False);uil行ik.prop(self.ppO,'bp用申o',translate=False,toggle=False);
				uil行ik=uil界.row(align=True);	
				uil行ik.prop(self.ppO,'bp地面丨o',translate=True,toggle=False);		
				if(self.ppO.bp地面丨o):
					uil行ik.prop(self.ppO,'fp地面丨亍',translate=True,toggle=False);	
				uil行ik=uil界.row(align=True);
				uil行ik.prop(self.ppO,'fp反向ik',translate=True,slider=True,icon="INDIRECT_ONLY_OFF");		
				if(pbA and pbA.ghost_ik.type==TYPE_TWO子):
					uil行ik.prop(pbA.ghost_ik,'fp反向fac',translate=True,slider=True,icon="INDIRECT_ONLY_OFF");			
				uil行ik=uil界.row(align=True);
				uil行ik.prop(self.ppO,'bpIK约束',translate=True,slider=True,icon="CON_SPLINEIK");	
			
				label.label(text=语.L样条ik[2],text_ctxt='',translate=True,icon='QUESTION',icon_value=0);
				label1.label(text=语.L样条ik[3],text_ctxt='',translate=True,icon='QUESTION',icon_value=0);
				#------------------------------
				uil行模式1.prop_enum(self.sceneGHIK,"epik·修正模式", value="0", translate=True, );
				uil行模式1.prop_enum(self.sceneGHIK,"epik·修正模式", value="1", translate=True, );
				#----修正骨--------------------------
				if(self.sceneGHIK.epik·修正模式=="1"):
					uil行ik= uil界.row(align=True);uil行ik.prop(context.scene.pp厶ik,'bp0',icon=context.scene.pp厶ik.icon0);uil行ik.label(text='----correction (修正骨)----------------------------------------------',text_ctxt='',icon='NONE',icon_value=0);uil行ik.scale_y=0.4;uil行ik.active=False;
					if(context.scene.pp厶ik.bp0==False):
						uil行ik=uil界.row(align=True);	
						uil行ik.prop(self.sceneGHIK,'bp用修正',translate=True,toggle=False);	
						
						# if("b有修正骨" in Gik.oA["PoseBone"] and Gik.oA["PoseBone"]["b有修正骨"]):
						uil行ik=uil界.row(align=False);	
						try:
							uil行ik.prop(self.ppO,'fp最大缩',translate=True,slider=False,);
							uil行ik.prop(self.ppO,'fp缩o',translate=True,slider=False,);
							uil行ik.prop(self.ppO,'fp肌肉延长',translate=True,slider=False,);
						except:pass;	
						if(pbA and pbA.ghost_ik.type==TYPE_修正骨):# or pbA.ghost_ik.type==TYPE_TWO孙
							uil行ik=uil界.row(align=True);
							uil行ik.prop(pbA.ghost_ik,'fp修正量pb',translate=True,slider=True,);		
							uil行ik.prop(pbA.ghost_ik,'fp缩pb',translate=True,slider=True,);
							# uil行ik.prop(pbA.ghost_ik,'fp扭Y',translate=True,slider=True,);
						
				# uil行ik=uil界.split(align=False );
				# uil行ik.prop(self.sceneGHIK,'bp用ghost_ik');
				uil行ik= uil界.row(align=True);uil行ik.prop(context.scene.pp厶ik,'bp1',icon=context.scene.pp厶ik.icon1);uil行ik.label(text='----pose bone----------------------------------------------',text_ctxt='',icon='NONE',icon_value=0);uil行ik.scale_y=0.4;uil行ik.active=False;
				if(context.scene.pp厶ik.bp1==False):
					if(pbA):
						if(pbA.ghost_ik.type==TYPE_SPLINE):
							uil行ik=uil界.row(align=True).split(factor=0.4,align=True);
							uil行ik.prop(pbA.ghost_ik,'bp钉',translate=True,toggle=False,);
							uil行ik.prop(pbA.ghost_ik,'bp移',translate=True,toggle=False,);
							uil行ik.prop(pbA.ghost_ik,'bp扭父',translate=True,toggle=False,);
							uil行ik=uil界.row(align=True);
							uil行ik.prop(self.ppO,'fp范围o',translate=True,slider=True);
							uil行ik.prop(self.ppO,'fp扭范围',translate=True,slider=True);

							uil行1=uil行ik.row(align=True);uil行1.enabled=False;
							uil行1.prop(pbA.ghost_ik,'ip头尾',translate=True,toggle=True,);
							#
						elif(pbA.ghost_ik.type==TYPE_TWO子):# or pbA.ghost_ik.type==TYPE_TWO孙
							uil行ik=uil界.row(align=True).split(factor=0.6,align=False);
							uil行ik.prop(pbA.ghost_ik,'bp钉',translate=True,toggle=False,);
							uil行ik.prop(pbA.ghost_ik,'bp用申',translate=True,toggle=False,);
							# uil行ik.prop(pbA["PoseBone"],'bLR',translate=True,);
							uil行ik.prop(self.sceneGHIK,'bp自动选',toggle=False);	#	,icon="RESTRICT_SELECT_OFF"
							
			#====物理==========================
			else:
				uil行模式1.prop_enum(self.sceneGHIK,"epik·同步模式", value="0", translate=True, );
				uil行模式1.prop_enum(self.sceneGHIK,"epik·同步模式", value="1", translate=True, );
				uil行模式1.prop_enum(self.sceneGHIK,"epik·同步模式", value="2", translate=True, );
				
				uil行物理.prop(self.ppO,'bp物理o',translate=True,toggle=False,icon="NONE");
				uil行物理1=uil界.row(align=False);
				uil行物理1.prop(self.ppO,'bp中点',translate=True,icon="NONE");
				#----预模拟-------------------------------------------------
				uil行=uil界.row(align=True).split(factor=0.3,align=True);
				uil行.prop(self.sceneGHIK,'bp预模拟',translate=True,toggle=True);
				if(self.sceneGHIK.bp预模拟):
					uil行.prop(self.sceneGHIK,'ip预模拟帧',translate=True,toggle=False);
					# uil行.prop(self.sceneGHIK,'bp惯性',translate=True,toggle=True);
				# uil行=uil界.row(align=False);
				# uil行.operator(卐试碰撞卐Operator.bl_idname,translate=True,icon="MOD_PHYSICS");				
				# uil行.operator(卐画碰撞卐Operator.bl_idname,translate=True,icon="GREASEPENCIL");
				
				if(self.sceneGHIK.bp物理sc):
					if(uil行模式1.enabled==False):uil行模式1.enabled=True;
					#----o--------------------------
					# uil行2=uil界.row(align=False);
					# uil行2.prop(self.ppO,'ip开始帧',translate=True,icon="NONE");
					# uil行2.prop(self.ppO,'ip结束帧',translate=True,icon="NONE");
					if(self.iArm==1):
						#----风--------------------------
						if(self.sceneGHIK.epik·同步模式=="1"):
							uil界.prop(Gik.oA.ppO,'bp用风',translate=True,icon='FORCE_WIND',slider=False,toggle=False);
							if(Gik.oA.ppO.bp用风):
								uil行=uil界.row(align=True);
								uil行.prop(Gik.oA.ppO,'fvp风向',translate=True,icon='NONE',slider=True,toggle=False);
								uil行=uil界.row(align=True);
								uil行.prop(Gik.oA.ppO,'fp十',translate=True,slider=True,icon='NONE');
								uil行.prop(Gik.oA.ppO,'fp随机',translate=True,slider=True,icon='NONE');
								uil行.prop(Gik.oA.ppO,'fp风倍',translate=True,slider=True,icon='NONE');								
						#----烘焙-------------------------------
						elif(self.sceneGHIK.epik·同步模式=="2"):
							"""
							uil行=uil界.row(align=True);	
							uil行.prop_search(self.sceneGHIK,'sp烘焙参考arm', bpy.data, "armatures",icon='NONE');#translate=True,
							uil行=uil界.row(align=False);
							uil行bp=uil界.row(align=False);
							if(self.sceneGHIK.sp烘焙参考arm!=""):
								try:
									Arm= bpy.data.armatures[self.sceneGHIK.sp烘焙参考arm];
									uil行.prop_search(self.sceneGHIK,'sp烘焙参考骨',Arm,"bones",translate=True,icon='NONE');
								except:pass;
								if(self.sceneGHIK.sp烘焙参考骨!=""):
									uil行bp.prop(self.sceneGHIK,'bp参考关键帧',translate=True,icon='NONE',slider=False,toggle=False);	
							uil行bp.prop(self.sceneGHIK,'bp只烘焙激活o',translate=True,icon='NONE',slider=False,toggle=False);
							"""
							uil行=uil界.row(align=False);
							uil行.prop(Gik.oA.ppO,'ip间隔帧数',translate=True,icon='NONE',slider=False);
							# if(self.sceneGHIK.bp只烘焙激活o or self.sceneGHIK.bp只烘焙激活o==False):
							uil行=uil界.row(align=False);	
							uil行1=uil行.row(align=False);
							uil行1.operator(卐ik烘培关键帧卐Operator0.bl_idname,translate=True,icon="KEY_HLT");
							uil行2=uil行.row(align=False);
							uil行2.operator(卐一一烘焙卐Operator.bl_idname,translate=True,icon="KEY_DEHLT");
							
							# uil行=uil界.row(align=False);	
							# uil行2.operator(卐首尾关键帧插值卐Operator0.bl_idname,translate=True,icon="NODE_INSERT_OFF");
							
							"""
							uil行.prop(self.ppO,'bp有烘焙',translate=True,icon='NONE',slider=False,toggle=False);
							if(self.ppO.bp有烘焙):
								uil行1.enabled=False;uil行2.enabled=True;
							else:
								uil行1.enabled=True;uil行2.enabled=False;
							"""
				else:
					if(uil行模式1.enabled==True):uil行模式1.enabled=False;
		#----没有激活物--------------------------
		else:
			self.iArm=-1;
		# print("self.iArm==",self.iArm);
		#----物理,列表-------------------------------------------------
		uil栋=uil界.column(align=True);
		if(self.sceneGHIK.bp物理sc):
			uil栋.enabled=True;
		else:
			uil栋.enabled=False;
		
		if(self.sceneGHIK.ep模式=="phy" and self.sceneGHIK.epik·同步模式=="0"):	
			#-----------------------------------------------------
			uil栋1=uil栋.column(align=True);
			uil栋1.prop(self.sceneGHIK,'bp碰撞sc',translate=True,icon='NONE',slider=False,toggle=False);	
			
			uil栋1=uil栋.column(align=True);
			if(self.sceneGHIK.bp碰撞sc):
				uil栋1.enabled=True;
			else:
				uil栋1.enabled=False;

			uil行= uil栋1.row(align=True);uil行.prop(context.scene.pp厶ik,'bp3',icon=context.scene.pp厶ik.icon3);uil行.label(text=语.L列表[0],text_ctxt='',translate=True,icon='NONE',icon_value=0);uil行.scale_y=0.4;uil行.active=False;
			if(context.scene.pp厶ik.bp3==False):
				if(-1<self.iArm):
					# if(Gik.oA.ppO.type==1):#骨架
					
					if(self.iArm==1):
						uil栋1.label(text=语.L列表2[0],text_ctxt='',translate=True,icon='NONE',icon_value=0);
						for i,pg in enumerate(self.ppO.cp排除碰撞体):
							uil行=uil栋1.row(align=True);
							uil行.prop_search(pg,"name", self.sceneGHIK, "cp碰撞体", icon = "NONE");
							# uil行.prop(pg,name'',translate=True,icon='NONE',slider=False,toggle=False);
							uil行.operator(卐一一排除碰撞卐Operator.bl_idname, text='',icon="REMOVE").ξ=i;

						uil行=uil栋1.split(factor=0.5,align=False);
						uil行.operator(卐十十排除碰撞卐Operator.bl_idname,translate=True,icon="ADD");
					#----碰撞体属性--------------------------------------------
					elif(self.iArm==0):#mesh
						uil行=uil栋1.row(align=True);
						uil行.prop(self.ppO,'fp亍',translate=True,icon='NONE',slider=False,toggle=False);	
						uil行.prop(self.ppO,'冖检测距离',translate=True,icon='NONE',slider=False,toggle=False);
						uil行=uil栋1.row(align=False);	
						uil行.prop(self.ppO,'fp摩擦力',translate=True,slider=False,icon="NONE");
						uil行.prop(self.ppO,'fp反弹力',translate=True,slider=False,icon="NONE");
						#----关联点-------------------------------------------------
						uil行=uil栋1.row(align=True);	
						uil行.prop_search(self.ppO,'sp关联点', Gik.oA, "vertex_groups",icon='NONE');
						# if(self.ppO.sp关联点!=""):
							# uil行.operator(卐乙关联点卐Operator.bl_idname,translate=True,text_ctxt='set',icon="TOOL_SETTINGS");
						uil行=uil栋1.split(factor=0.5,align=False);
						uil行.operator(卐十十全局碰撞卐Operator.bl_idname,translate=True,icon="ADD");
						uil行.operator(卐一一全局碰撞卐Operator.bl_idname,translate=True,icon="REMOVE");
						#------------------------------
				if(0<self.sceneGHIK.cp碰撞体.__len__()):
					uil界.template_list('UL_UL_GlobalColliderUIList', '－－－', self.sceneGHIK, 'cp碰撞体', self.sceneGHIK, 'ip碰撞体ξ', rows=2,maxrows=20,);

			#------------------------------
			if(Gik.oA):
				uil行=uil界.row(align=True);
				uil行.prop(Gik.oA.ppO,'fp消除横力',translate=True,icon='NONE',slider=True,toggle=True);	
				uil行.prop(Gik.oA.ppO,'fp渐变带动',translate=True,icon='NONE',slider=True,toggle=True);
				uil行.prop(Gik.oA.ppO,'fp收缩值',translate=True,icon='NONE',slider=True,toggle=True);				
			#----碰撞-------------------------------------------------
			uil行=uil界.row(align=True);	
			uil行.prop(self.sceneGHIK,'fp重力',translate=True,icon='NONE',slider=False,toggle=True);	
			if(0<self.iArm and pbA):
				uil行.prop(pbA.ghost_ik,'fp重力fac',translate=True,slider=False);
				uil行.prop(pbA.ghost_ik,'fp风力fac',translate=True,slider=False);
		#====共同====================================
		if(pbA):
			# if(Gik.oA.type=="ARMATURE"):
			if(self.sceneGHIK.ep模式=="phy"):#物理 and self.sceneGHIK.epik·同步模式=="0"
				uil行= uil界.row(align=True);uil行.prop(context.scene.pp厶ik,'bp4',icon=context.scene.pp厶ik.icon4);uil行.label(text='----bend----------------------------------------------',text_ctxt='',icon='NONE',icon_value=0);uil行.scale_y=0.4;uil行.active=False;
				if(context.scene.pp厶ik.bp4==False):
					if(pbA.ghost_ik.type in(TYPE_物理,TYPE_布料)):
						box = uil界.box();
						uil行=box.row(align=True);	 
						uil行.prop(pbA.ghost_ik,'fp刚性',translate=True,slider=True);
						uil行.prop(pbA.ghost_ik,'fp弹性',translate=True,slider=True);	
						uil行=box.row(align=True);					
						uil行.prop(pbA.ghost_ik,'fp力',translate=True,slider=True);
						# uil行=box.row(align=True);					
						# uil行.prop(pbA.ghost_ik,'fp扭性',translate=True,slider=True);
						# uil行.prop(pbA.ghost_ik,'fp恢复',translate=True,slider=True);	
						
						uil行=box.row(align=True);
						uil行.prop(pbA.ghost_ik,'bp钉',translate=True,toggle=False,);	
						uil行1=uil行.row(align=True);uil行1.enabled=False;
						uil行1.prop(pbA.ghost_ik,'ip头尾',translate=True,toggle=True,);
						
						uil行=box.row(align=True);
						uil行.prop(pbA,'bp物理',translate=True,toggle=False);
						uil行.prop(pbA.ghost_ik,'bp碰撞',translate=True,toggle=False);				
						# uil行.prop(pbA.ghost_ik,'bp布料',translate=True,toggle=True);
			#---------------------------------------------
			if(pbA.ghost_ik.type in[TYPE_SPLINE,TYPE_TWO爷,TYPE_TWO父,TYPE_物理,TYPE_布料]):
				# uil界.prop(pbA.ghost_ik,'Λx',translate=True,icon='NONE',);
				uil行ik= uil界.row(align=True);uil行ik.prop(context.scene.pp厶ik,'bp2',icon=context.scene.pp厶ik.icon2);uil行ik.label(text='----LIMIT----------------------------------------------',text_ctxt='',icon='NONE',icon_value=0);uil行ik.scale_y=0.4;uil行ik.active=False;
				if(context.scene.pp厶ik.bp2==False):	
					uil行ik=uil界.row(align=False);
					uil行ik.prop(self.ppO,'bp限制o',translate=False,toggle=False);
					if(self.ppO.bp限制o):
						# uil行ik.prop(pbA.ghost_ik,'bp限制',translate=True,icon='CON_ROTLIMIT',slider=False,toggle=False);
						# if(pbA.ghost_ik.bp限制):
						uil行ik.prop(pbA.ghost_ik,'fvp丨小',translate=True,icon='NONE',);
						# uil界.prop(pbA.ghost_ik,'fvp丨大',translate=True,icon='NONE',);	
		#-----------------------------------------------------
		if(Gik.oA):
			uil行= uil界.row(align=True);uil行.prop(context.scene.pp厶ik,'bp5',icon=context.scene.pp厶ik.icon5);uil行.label(text='----setting----------------------------------------------',text_ctxt='',icon='NONE',icon_value=0);
			uil行.scale_y=0.4;uil行.active=False;
			if(context.scene.pp厶ik.bp5==False):
				box = uil界.box();
				uil行=box.split(factor=0.6,align=False);		
				uil行.operator(卐乙IK骨卐Operator.bl_idname,translate=True,icon="TOOL_SETTINGS");
				uil行.operator(卐一一IK骨卐Operator.bl_idname,translate=True,icon="REMOVE");
				uil行.scale_y=1.3;
				
				uil行=box.row(align=False);
				uil行.operator(卐乙绑定pose卐Operator.bl_idname,translate=True,icon="ARMATURE_DATA");	
				uil行.operator(卐乙当前申卐Operator.bl_idname,translate=True,icon="ORIENTATION_GLOBAL");
				uil行=box.row(align=False);
				uil行.operator(卐插入关键帧pose卐Operator.bl_idname,translate=True,icon="KEY_HLT");
				#------------------------------
				uil行=box.row(align=True);
				uil行.prop(self.ppO,'bp只选',translate=True,toggle=False);#,icon='RESTRICT_SELECT_OFF'
				uil行=box.row(align=True);
				uil行.operator(卐对称pose卐Operator.bl_idname,text=语.L对称[2],translate=True,icon="COPYDOWN").ip=0;#复制
				uil行.operator(卐对称pose卐Operator.bl_idname,text=语.L对称[3],translate=True,icon="PASTEDOWN").ip=1;#粘贴
				uil行.operator(卐对称pose卐Operator.bl_idname,text=语.L对称[4],translate=True,icon="PASTEFLIPDOWN").ip=2;#对称粘贴
				#----吅 申--------------------------
				uil行=box.row(align=True);
				uil行.operator(卐吅申卐Operator.bl_idname,text=语.L对称[5],translate=True,icon="COPYDOWN").ip=0;#复制
				uil行.operator(卐吅申卐Operator.bl_idname,text=语.L对称[6],translate=True,icon="PASTEDOWN").ip=1;#粘贴
				uil行.operator(卐IK1次卐Operator.bl_idname,translate=True,icon="HAND");
								
				
		#------------------------------
		uil行=uil界.row(align=False);
		uil行.operator(卐仌属性ik卐Operator.bl_idname,translate=True, icon = "RECOVER_LAST");
		uil行.operator(卐仌ik绑定卐Operator.bl_idname,translate=True, icon = "RECOVER_LAST");		
		uil行.operator(卐关于Ghost_ik卐Operator.bl_idname,translate=True, icon = "QUESTION");
		
					
		# if(self.ppO):

			#----骨架-------------------------------------------------
			# uil界.label(text='----debug----------------------------------------------',text_ctxt='',icon='NONE',icon_value=0);

		#----DEBUG--------------------------------------------------	
		uil行= uil界.row(align=True);uil行.prop(context.scene.pp厶ik,'bp6',icon=context.scene.pp厶ik.icon6);uil行.label(text='----DEBUG----------------------------------------------',text_ctxt='',icon='NONE',icon_value=0);uil行.scale_y=0.4;uil行.active=False;

		if(context.scene.pp厶ik.bp6==False):
			uil界.operator(卐INITik卐Operator.bl_idname,translate=True, icon = "NONE");
			if(context.scene.DEBUGik.init):
				uil行=uil界.row(align=True);
				uil行.prop(context.scene.DEBUGik, "亖叵",toggle=True,translate=True);	 uil行.prop(context.scene.DEBUGik, "亖IK",toggle=True,translate=True);	  uil行.prop(context.scene.DEBUGik, "亖扭",toggle=True,translate=True);	 uil行.prop(context.scene.DEBUGik, "亖凷",toggle=True,translate=True);	
				uil行=uil界.row(align=True);
				uil行.prop(context.scene.DEBUGik, "亖数ik",toggle=True,translate=True);uil行.prop(context.scene.DEBUGik, "亖一一",toggle=True,translate=True);uil行.prop(context.scene.DEBUGik, "亖节点",toggle=True,translate=True);uil行.prop(context.scene.DEBUGik, "亖烘",toggle=True,translate=True);
				uil行=uil界.row(align=True);
				uil行.prop(context.scene.DEBUGik, "亖骨在线",toggle=True,translate=True);	uil行.prop(context.scene.DEBUGik, "亖乛丨ik",toggle=True,translate=True);
				if(self.sceneGHIK.epik·修正模式=="1"):
					uil行=uil界.row(align=True);
					uil行.prop(context.scene.DEBUGik, "亖驱",toggle=True,translate=True);	uil行.prop(context.scene.DEBUGik, "亖驱数",toggle=True,translate=True);	uil行.prop(context.scene.DEBUGik, "亖驱扭",toggle=True,translate=True);	uil行.prop(context.scene.DEBUGik, "亖挤",toggle=True,translate=True);	uil行.prop(context.scene.DEBUGik, "亖旋",toggle=True,translate=True);	
				
			#---------------------------------------------
			uil行=uil界.row().split(factor=0.2,align=True);
			uil行.prop(self.sceneGHIK,'bp画画', text=语.L画画[0],toggle=False,icon='GREASEPENCIL');
			# uil行.operator(卐载入DLL卐Operator.bl_idname, text="载入",icon="CHECKMARK");		
			uil行=uil行.row().split(factor=0.3,align=True);
			uil行.operator(卐画碰撞体卐Operator.bl_idname, text="画碰撞体",icon="NONE");
			uil行.operator(卐XDLL卐Operator.bl_idname, text="X dll",icon="COLORSET_01_VEC");
			
			uil行=uil界.row(align=True);		
			uil行1=uil行.row(align=False);uil行1.prop(self.sceneGHIK,'init', text="init",toggle=False,icon='NONE');uil行1.enabled=False;
			if(Gik.oA):
				uil行1=uil行.row(align=False);uil行1.prop(Gik.oA.ppO,'init', text="init(o)",toggle=False,icon='NONE');uil行1.enabled=False;
			if(self.sceneGHIK.ep模式=="phy"):#物理
				uil行跟踪=uil界.row(align=True);
				uil行跟踪.prop(self.sceneGHIK,'ip跟踪点', text="跟踪点",toggle=False,icon='NONE');
				if(pbA):
					# 
					uil行1.prop(pbA.ghost_ik,'init',translate=True,slider=False);
					uil行跟踪1=uil行跟踪.row(align=False);
					uil行跟踪1.prop(pbA.ghost_ik,'ξik',translate=True,slider=False);
					uil行跟踪1.enabled=False;
					
				uil行=uil界.row(align=True);	
				# uil行.prop(self.sceneGHIK,'bp力滑', text="bp力滑",toggle=False,icon='NONE');
				uil行.prop(self.sceneGHIK,'bp恢复', text="恢复",toggle=False,icon='NONE');
				uil行.prop(self.sceneGHIK,'bp弹力', text="弹力",toggle=False,icon='NONE');	
				# uil行.prop(self.sceneGHIK,'bp修正力', text="修正力",toggle=False,icon='NONE');
				# uil行.prop(self.sceneGHIK,'bp拉力', text="bp拉力",toggle=False,icon='NONE');		
				# uil行=uil界.row(align=True);			
				# uil行.prop(self.sceneGHIK,'bp阻力', text="阻力",toggle=False,icon='NONE');		
				uil行=uil界.row(align=True);
				uil行.prop(self.sceneGHIK,'bp弹簧', text="弹簧",toggle=False,icon='NONE');	
				uil行.prop(self.sceneGHIK,'bp弹簧隔', text="弹簧隔",toggle=False,icon='NONE');	
				uil行=uil界.row(align=True);
				uil行.prop(self.sceneGHIK,'bp弹簧布', text="弹簧布",toggle=False,icon='NONE');			
				uil行.prop(self.sceneGHIK,'bp骨在线段', text="骨缩线",toggle=False,icon='NONE');	
				uil行=uil界.row(align=True);
				uil行.prop(self.sceneGHIK,'bp乛丨', text="乛丨",toggle=False,icon='NONE');
				# uil行=uil界.row(align=True);			
				# uil行.prop(self.sceneGHIK,'bp渐变带动', text="渐变带动",toggle=False,icon='NONE');				
				uil行=uil界.row(align=True);			
				uil行.prop(self.sceneGHIK,'bpΣ', text="Σ",toggle=False,icon='NONE');			
				uil行.prop(self.sceneGHIK,'bp关联点', text="关联点",toggle=False,icon='NONE');	
				
		
#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
"""
class Panel_PT_卐属性面板卐Panel(bpy.types.Panel):
	bl_space_type = 'PROPERTIES';
	bl_region_type = 'WINDOW';
	bl_context = "bone";
	bl_label = "ghost_ik";

	@classmethod
	def poll(cls, context):
		return context.active_pose_bone;
	def draw(self, context):
		uil界 = uil界;
		pbA = context.active_pose_bone;
		uil界.label(text=pbA.name);
		uil界.prop(pbA.ghost_ik,'ep选类型');
		if (pbA.ghost_ik.ep选类型 == Gik.BONE):
			uil界.prop(pbA.ghost_ik,'soft_pin');
			if (pbA.parent):
				uilBox = uil界#.box();
				uilBox.prop(pbA,'bpIK');
				uilBox.prop(pbA,'gIK_softness');
				uilBox.prop(pbA,'gIK_error_correction');
"""
#/////键////////////////////////////////////////
LLsKC类别=[("Pose","VIEW_3D","WINDOW",[0,1,2,3,4,5,6,7,8])];#[]决定要LMs类别id与按键注册的条项

LMs类别id与按键= \
	[
	{"idname":卐GHOST_IK_F卐Operator.bl_idname,"type":"F","value":"PRESS",	"any":False,  "shift":False,"ctrl":False, "alt":False, "oskey":False,"head":False,"properties":{} },#0
	{"idname":卐GHOST_IK_ALT卐Operator.bl_idname,"type":"F","value":"PRESS",	"any":False,  "shift":False,"ctrl":False, "alt":True, "oskey":False,"head":False,"properties":{}},#1
	{"idname":卐GHOST_IK_CTRL卐Operator.bl_idname,"type":"F","value":"PRESS",	"any":False,  "shift":False,"ctrl":True, "alt":False, "oskey":False,"head":False,"properties":{}},#2
	{"idname":卐GHOST_IK_SHIFT卐Operator.bl_idname,"type":"F","value":"PRESS",	"any":False,  "shift":True,"ctrl":False, "alt":False, "oskey":False,"head":False,"properties":{}},#3	
	{"idname":卐GHOST_IK_SHIFTALT卐Operator.bl_idname,"type":"F","value":"PRESS",	"any":False,  "shift":True,"ctrl":False, "alt":True, "oskey":False,"head":False,"properties":{}},#4
	
	{"idname":卐GHOST_IK_扭卐Operator.bl_idname,"type":"X","value":"PRESS",  "any":False,	 "shift":False,"ctrl":False, "alt":False, "oskey":False,"head":False,"properties":{} },#5			
	{"idname":卐GHOST_IK_扭alt卐Operator.bl_idname,"type":"X","value":"PRESS",  "any":False,	 "shift":False,"ctrl":False, "alt":True, "oskey":False,"head":False,"properties":{} },#6	
	{"idname":卐GHOST_IK_扭ctrl卐Operator.bl_idname,"type":"X","value":"PRESS",  "any":False,	 "shift":False,"ctrl":True, "alt":False, "oskey":False,"head":False,"properties":{} },#7		
	{"idname":卐GHOST_IK_扭shift卐Operator.bl_idname,"type":"X","value":"PRESS",  "any":False,	 "shift":True,"ctrl":False, "alt":False, "oskey":False,"head":False,"properties":{} },#8
	]


class 卐重载Ghost_IK卐Operator(bpy.types.Operator):
	bl_idname = "op.reload_ghost_ik";
	bl_label =语.L重载[0];
	bl_description = 语.L重载[1] ;
	def execute(self, context):
		Δ重载addonG(Gik.文件夹此ghost,True);
		return {"FINISHED"};
		
class 卐moteTest卐Operator(bpy.types.Operator):
	bl_idname = "op.move_test";
	bl_label ="moveTest";
	bl_description = "--";
	
	
#—————————————————————————————————————————————————————————
L注册ghostik=[(卐ik烘培关键帧卐Operator0,卐一一烘焙卐Operator,卐一一IK骨卐Operator,卐乙IK骨卐Operator,卐乙绑定pose卐Operator,卐乙当前申卐Operator,卐仌属性ik卐Operator,卐仌ik绑定卐Operator,卐对称pose卐Operator,卐吅申卐Operator,卐插入关键帧pose卐Operator,卐激活物名给sp卐Operator,卐十十1个arm卐Operator,卐一一1个arm卐Operator,卐十十约束给arm的卐Operator,卐切换约束arm卐Operator,卐关于Ghost_ik卐Operator,卐GHOST_IK_扭卐Operator,卐GHOST_IK_扭alt卐Operator,卐GHOST_IK_扭ctrl卐Operator,卐GHOST_IK_扭shift卐Operator,卐IK1次卐Operator,卐GHOST_IK卐Operator,卐GHOST_IK_F卐Operator,卐GHOST_IK_ALT卐Operator,卐GHOST_IK_CTRL卐Operator,卐GHOST_IK_SHIFT卐Operator,卐GHOST_IK_SHIFTALT卐Operator,卐载入DLL卐Operator,卐XDLL卐Operator,卐正常化骨四元卐Operator,卐选骨不用gIK卐Operator,卐乙关联点卐Operator,卐画碰撞体卐Operator,卐SetType卐Operator,卐十十全局碰撞卐Operator,卐一一全局碰撞卐Operator,卐十十排除碰撞卐Operator,卐一一排除碰撞卐Operator,卐画碰撞卐Operator,卐试碰撞卐Operator,PT_PT_IK_Tools,卐重载Ghost_IK卐Operator,),(卐moteTest卐Operator,)]

#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－		 
def ΔΔ建Property():
	bpy.types.PoseBone.ghost_ik = PointerProperty(type=卐pb属性卐PropertyGroup);
	# if(hasattr(bpy.types.Object,'ppO')==False):
	bpy.types.Object.ppO = PointerProperty(type= oIKPropertyGroup);
	# if(hasattr(bpy.types.Object,'ip仌')==False):
	# bpy.types.Object["i仌"] = IntProperty(default=-1);
	bpy.types.Object.ψ=IntProperty(default=0);	
	bpy.types.Scene.ghost_ik = PointerProperty(type=卐scene工具乙ik卐PropertyGroup);
	# bpy.types.PoseBone.bp叵 = BoolProperty(name="叵 ",description="---",default=False,);
	bpy.types.PoseBone.bp物理=BoolProperty(name=语.L碰撞[8],description='enable ik for the selected pose bone only',default=True,subtype='NONE',update=Δ仌禁用);
	bpy.types.Scene.pp厶ik=PointerProperty(type=厶PropertyGroup);
	bpy.types.Scene.DEBUGik=PointerProperty(type=卐sceneDEBGEik卐PropertyGroup);
	# bpy.types.Object.test=PointerProperty(type= oIKPropertyGroup); 
	# bpy.types.WindowManager.sp物理骨dll路径=StringProperty(name='',description='',default='');
	# bpy.types.WindowManager.sp修正骨dll路径=StringProperty(name='',description='',default='');

	# wm=bpy.context.window_manager;
	# wm.sp物理骨dll路径=(os.path.dirname(__file__)+"/PHYSIC64.dll");#.encode('UTF-8')
	# wm.sp修正骨dll路径=(os.path.dirname(__file__)+"/CORRECT64.dll"); 
def ΔΔ删除属性():
	del bpy.types.PoseBone.ghost_ik;
	del bpy.types.Object.ppO;
	del bpy.types.PoseBone.bp物理;	
	# del bpy.types.WindowManager.sp物理骨dll路径;	del bpy.types.WindowManager.sp修正骨dll路径;
	del bpy.types.Scene.ghost_ik;
	del bpy.types.Scene.DEBUGik;
	# del bpy.types.PoseBone.bp叵;
	
@persistent#可以不断有效
def ΔUndoPost(scene):		
	bpy.ops.op.delete_ghost_ik();
	
def register():
	注册类(L注册ghostik,True);
		
	ΔΔ建Property();wm = bpy.context.window_manager;kc = wm.keyconfigs.addon;#Key configuration that can be extended by addons, and is added to the active configuration when handling events
														#Type : KeyConfig, (readonly)
	注册按键(LLsKC类别,LMs类别id与按键);
	# Δ乙卍dll();	

	# bpy.app.handlers.render_complete.append(renderCompleted)
	# bpy.app.handlers.render_init.append(render叵ialized)
	# bpy.app.handlers.render_cancel.append(renderCancelled)
	# bpy.app.handlers.render_pre.append(renderPre)
	
	# bpy.app.handlers.frame_change_pre.append(Δ刷新动力骨Post);#●●可以准确同步骨与网格,第一帧pose_mat 不正确
	bpy.app.handlers.frame_change_post.append(Δ刷新动力骨Post);#●●可以在第一帧pose_mat 就正确,优先于关键帧
	# bpy.app.handlers.load_pre.append(Δ重载scenePre);#换场景
	bpy.app.handlers.load_post.append(Δ重载scenePost);#换场景
	bpy.app.handlers.undo_pre.append(ΔUndoPost);#
	#------------------------------
	t版本=bpy.app.version;print("t版本==",t版本);#t版本== (3, 1, 2)
	# if(t版本[0]!=3 or t版本[1]!=5 or t版本[1]!=6):
	if(t版本[0]!=3 or t版本[1]<5 or 6<t版本[1]):
		Gik.sp警告G="this version of ghost ik only support blender 3.5 !!★"
		print("ERROR ★ghost ik only support  blender 3.5 !!★==",t版本);
		# return;
	elif(platform.system()!="Windows"):
		Gik.sp警告G="this 's not Windows OS, only  support Winodows10 x64 !!★";	
	else:
		Gik.sp警告G="";
		

#==============================================================
def unregister():
	bpy.ops.screen.animation_cancel(restore_frame=False);
	ΔΔ删除属性();
	#bpy.app.handlers.frame_change_post.remove(frame_change);
	# bpy.utils.unregister_module(__name__);
	注销类(L注册ghostik);
	wm = bpy.context.window_manager;
	try:
		# bpy.app.handlers.frame_change_pre.remove(Δ刷新动力骨Post);
		bpy.app.handlers.frame_change_post.remove(Δ刷新动力骨Post);		 
		# bpy.app.handlers.load_pre.remove(Δ重载scenePre);
		bpy.app.handlers.load_post.remove(Δ重载scenePost);
	except:pass;
	try:
		bpy.app.handlers.undo_pre.remove(ΔUndoPost);
	except:pass;
	画3dOP(False,True);LG.b丌仌=False;
	
	# if(Gik.卍dll.dll):
		# Gik.卍dll.dll.凸win不();
	Gik.卍dll.灬();	  
	FOLDER=Gik.文件夹此ghost+".PYLIB_"+Gik.文件夹此ghost;print("FOLDER==",FOLDER);#IMDJS_ghost_ik.PYLIB_IMDJS_ghost_ik
	删除模块(Ls模块名=[Gik.文件夹此ghost+'.LANG.LANG',Gik.文件夹此ghost+'.G',Gik.文件夹此ghost+'.PG',Gik.文件夹此ghost+'.bake',Gik.文件夹此ghost+'.compatible',Gik.文件夹此ghost+'.func',Gik.文件夹此ghost+'.draw',Gik.文件夹此ghost+'.fill',Gik.文件夹此ghost+'.OP',Gik.文件夹此ghost+'.OPtwist',Gik.文件夹此ghost+'.update',"IMDJS_nodes.OP_cloth" 
	,FOLDER+".LG",FOLDER+".PYLIB_"+Gik.文件夹此ghost,FOLDER
	,Gik.文件夹此ghost]+Gik.Ls模块selfG+LG.Ls模块LIB,b打印=True);
	# print("sys.modules==",sys.modules.keys());
	注销按键(LLsKC类别,LMs类别id与按键);
	#不勾按键(LLsKC类别=LLsKC类别,LMs类别id与按键=LMs类别id与按键,b注册还是反注册=False);
	# print("==",sys.modules.keys());
#==============================================================
if (__name__ == "__main__"):
	register();
  


	  
	  
	  

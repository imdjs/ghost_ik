
from mathutils import Quaternion
from .G import 语,LG;
from .func import*
# from .func import 十十fcurve1o
#//////////////////////////////////////
#==================================================
"""
def Δ集物理骨(self,scene,o,Cfc物体全部弓,Ms骨名MfcLf4丅值当前帧__,Mkf帧f4丅值当前帧All__,Mkf帧f4丅值当前帧Bone__,i当前帧,b选中骨):
		if(b选中骨):
			Cpb = [pb for pb in bpy.context.selected_pose_bones_from_active_object];
			#print("COLLECTE ",Cpb);#√
		else:
			Cpb = o.pose.bones;
		
		for pb in Cpb:
			for fc in Cfc物体全部弓:#1个fc  表示1个通道一条弓
				#print("BONE NAME==",fc.data_path);
				if (fc.data_path[:5] == "pose."):
					if (fc.data_path.split('"')[1] == pb.name):#骨名称
						#print("POSE BONE", pb.name);#√
						#print("Ds KEY==",Ms骨名MfcLf4丅值当前帧__.keys());
						if(pb.name not in Ms骨名MfcLf4丅值当前帧__.keys()):
							Ms骨名MfcLf4丅值当前帧__[pb.name]={};
						if(fc not in Ms骨名MfcLf4丅值当前帧__[pb.name].keys()):
							Ms骨名MfcLf4丅值当前帧__[pb.name][fc]=[];
						for kf帧 in fc.keyframe_points:
							#----全部帧--------------------------------------------
							if (not scene.bp只当前帧s2 or self.bp整体偏移  or self.bp整体缩):
								#if (kf帧.co.x >= i开始帧 and kf帧.co.x <= i结束帧):#在所有帧范围内
								Ms骨名MfcLf4丅值当前帧__[pb.name][fc].append( [kf帧.co.x, kf帧.handle_left.x - kf帧.co.x,	 kf帧.handle_right.x - kf帧.co.x,kf帧.co.y]  );
								Mkf帧f4丅值当前帧All__.setdefault(kf帧,[kf帧.co.x, kf帧.handle_left.x - kf帧.co.x,  kf帧.handle_right.x - kf帧.co.x,kf帧.co.y]);
								Mkf帧f4丅值当前帧Bone__.setdefault(kf帧,[kf帧.co.x, kf帧.handle_left.x - kf帧.co.x,  kf帧.handle_right.x - kf帧.co.x,kf帧.co.y]);
							#----当前帧------------------------------------------------
							elif (scene.bp只当前帧s2):
								if (kf帧.co.x == i当前帧):#检测是在当前帧	co.x表示时间 co.y表示值
									Ms骨名MfcLf4丅值当前帧__[pb.name][fc].append(	[kf帧.co.x, kf帧.handle_left.x - kf帧.co.x,  kf帧.handle_right.x - kf帧.co.x,kf帧.co.y]  );
									#print("APPEND F4",pb.name);print("add bone kf",pb.name,kf帧);#√
									Mkf帧f4丅值当前帧All__.setdefault(kf帧,[kf帧.co.x, kf帧.handle_left.x - kf帧.co.x,  kf帧.handle_right.x - kf帧.co.x,kf帧.co.y]);#记录了kf帧.handle_left.x 相对kf帧.co.x 位移
									Mkf帧f4丅值当前帧Bone__.setdefault(kf帧,[kf帧.co.x, kf帧.handle_left.x - kf帧.co.x,  kf帧.handle_right.x - kf帧.co.x,kf帧.co.y]);#记录了kf帧.handle_left.x 相对kf帧.co.x 位移
		#print("SELECT	",Ms骨名MfcLf4丅值当前帧__);
"""

			
#==================================================
def Δ0乛烘焙物理骨(o,context):
	# i物理骨数=Gik.卍dll.dll.i凸物理骨数();
	Gik.b烘焙G=True;scene=context.scene;#oA=context.active_object;
	wm=context.window_manager;ii帧=scene.frame_end-scene.frame_start+1;
	L=[(c_float*10)(-1.0,-1.0,-1.0,  -1.0,-1.0,-1.0,-1.0,  -1.0,-1.0,-1.0)]*ii帧;#[p,p,p , q,q,q,q , s,s,s]  #float
	# L=[(-1.0,-1.0,-1.0,  -1.0,-1.0,-1.0,-1.0,  -1.0,-1.0,-1.0)]*ii帧;
	if(LG.MpbL10kc.__len__()<1):
		print("LG.MpbL10kc.__len__()<1  return;",LG.MpbL10kc.__len__());
		return;
	
	if(Gik.b首尾插值):
		Gik.卍dll.dll.凸首尾插值(c_void_p(o.as_pointer()),Gik.cvpC,Gik.i多少帧);
	#---------------------------------------------
	wm["Ms骨L帧"]={};#M={};
	print("MpbL10kc==",LG.MpbL10kc)	
	for pb in LG.MpbL10kc:
		wm["Ms骨L帧"][pb.name]=L;#M[pb.name]=L;
		print("Ms骨L帧==",*wm["Ms骨L帧"][pb.name][2]);
	o.ppO.bp有烘焙=True;#print("BAKE o PHY==",o,o.ppO.bp有烘焙,ii帧);

	Gik.卍dll.dll.凸1o乛烘焙物理骨(Gik.cvpC);# wm["Ms骨L帧"] ■
	Gik.卍dll.dll.凸烘焙物理骨end(Gik.cvpC);
	

	# Gik.卍dll.dll.ΔPTwm属性("Ms骨L帧",c_void_p(wm.as_pointer()));
	# PTmapkey亖亖(wm["Ms骨L帧"]);
	for s,L帧Lf10 in wm["Ms骨L帧"].items():
		# for s in wm["Ms骨L帧"]:
		# L帧Lf10= wm["Ms骨L帧"][s];
		# print("s==",s,L帧Lf10.__len__());
		for ξ帧,Lf10 in enumerate(L帧Lf10):
			# print("Lf10==",ξ帧,"__",*Lf10,type(Lf10[1]),float(Lf10[1]));#●如果是零会打印无效,但数据有效
			pass;
	# Gik.卍dll.dll.凸PTMsLLid("Ms骨L帧",c_void_p(wm.as_pointer()));
	# return;
	#----卌入py--------------------------
	# for O in Gik.L卐骷物理:
		# if(o==O.o):
	屮key1o(o,scene,o.ppO.ip间隔帧数);
	o.update_tag(refresh={'DATA'});
	Gik.卍dll.dll.凸刷新窗口action(c_void_p(context.as_pointer()));
	Gik.卍dll.dll.凸刷新窗口graph(c_void_p(context.as_pointer()));
	Gik.卍dll.dll.凸刷新窗口node0(c_void_p(context.as_pointer()));
	
	o.ppO.bp物理o=False;
	# break;
			
#====1次只烘焙1个====================================
class 卐ik烘培关键帧卐Operator0(bpy.types.Operator):
	bl_idname = "op.ik_bake_keyframe0"
	bl_label =语.L烘培[0]
	bl_description=语.L烘培[1]

	sp:StringProperty(name="note", description="", default="are you sure卩");
	bp插值:BoolProperty(name=语.L关键帧[0][0],description=语.L关键帧[0][1],default=False,subtype='NONE',update=None);
	ip:IntProperty(name=语.L关键帧[1][0],description=语.L关键帧[1][1],default=3,min=1,max=10000,step=1);
	#------------------------------------------------------------
	def invoke(self, context, event):#运行的第1步
		return context.window_manager.invoke_props_dialog(self,width=300);
	#------------------------------------------------------------
	def draw(self, context):
		self.layout.prop(self, "sp");
		uil行=self.layout.row(align=False);
		uil行.prop(self, "bp插值");
		if(self.bp插值):
			uil行.prop(self, "ip");
		
	def execute(self, context):
		scene=context.scene;
		bΔNone凷物理(context);
		oA=context.pose_object;print("BAKE FRAME==",oA);
		#----先插入关键帧,再播放,结束后再烘焙 --------------------------
		for O in Gik.L卐骷物理:
			# if(scene.ghost_ik.bp只烘焙激活o and oA==O.o or scene.ghost_ik.bp只烘焙激活o==False):
			if(oA==O.o):
				LG.MpbL10kc.clear();
				Cpb = O.o.pose.bones;
				for pb in Cpb:
					if(pb.ghost_ik.type in[TYPE_物理,TYPE_布料]):
						print("pb bp物理==",pb,pb.bp物理);
						if(pb.bp物理):
							LG.MpbL10kc[pb]={};
				print("LG.MpbL10kc ==",LG.MpbL10kc);
				if(LG.MpbL10kc.__len__()<0):
					print("LG.MpbL10kc.__len__()<1  return;",LG.MpbL10kc.__len__());
					self.report({"ERROR"},"LG.MpbL10kc.__len__()<1");#"INFO" "ERROR" "DEBUG" "WARNING"
					return {"FINISHED"};
				十十fcurve1o(O.o);
				break;
		scene.frame_current=scene.frame_start;
		Gik.卍dll.dll.凸烘焙物理骨start(Gik.cvpC);
		Gik.b烘焙G =True;Gik.b首尾插值 =self.bp插值;Gik.i多少帧 =self.ip;
		
		bpy.ops.screen.animation_play();#=>Δ0乛烘焙物理骨
		

		return {"FINISHED"};	
		
#==================================================
class 卐一一烘焙卐Operator(bpy.types.Operator):
	bl_idname = 'op.delete_phy_keyframes0'
	bl_label = 语.L烘培[2]
	bl_description=语.L烘培[3]
	
	def execute(self, context):
		bΔNone凷物理(context);
		
		oA=context.pose_object;
		for O in Gik.L卐骷物理:
			if(O.o.type=="ARMATURE" and oA==O.o):#and o.ppO.type==1
				一一bake1o(self,O.o,0);
				
		LG.MpbL10kc.clear();
		oA.ppO.bp物理o=True;
		return {"FINISHED"};
		

		
# ////END////END////END////END////END////END////END////END////
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			
						
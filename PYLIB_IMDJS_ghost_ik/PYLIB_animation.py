
import bpy,sys,os

path目录PYLIB父级 =os.path.abspath(os.path.join(os.path.dirname(__file__),".."));#父级目录 
sPYLIB父级=os.path.basename(path目录PYLIB父级);

if("PYLIB.LG" in sys.modules):
	LG=sys.modules["PYLIB.LG"];
else:
	try:
		import PYLIB.LG as LG;
	except:
		if(sPYLIB父级+".PYLIB_"+sPYLIB父级+".LG" in sys.modules):
			LG=sys.modules[sPYLIB父级+".PYLIB_"+sPYLIB父级+".LG"];
		else:
			exec("import "+sPYLIB父级+".PYLIB_"+sPYLIB父级+".LG as LG");
			
			
def 丌播放(context,restore_frame=False):
	if(context.screen and context.screen.is_animation_playing):
		# bpy.ops.screen.animation_play(reverse=False, sync=False);#丌播放
		bpy.ops.screen.animation_cancel(restore_frame=restore_frame);
		
def 丨巜帧(context):
	if(context.screen and context.screen.is_animation_playing):
		bpy.ops.screen.animation_cancel(restore_frame=restore_frame);
	context.scene.frame_current=context.scene.frame_start;
#====LG.MpbL10kc □====================================
def bΔ在曲线(s路径,Cfc弓):
	for fc in Cfc弓:
		# print("s路径==",s路径,fc.data_path,s路径 in fc.data_path);
		if(s路径 in fc.data_path):
			return True;
	return False;
	
def 十十fcurve1o(o):
	print("十十fcurve1o==",o);
	scene=bpy.context.scene;
	#------------------------------------------------------------
	if(not o.animation_data):
		o.animation_data_create();
	if(o.animation_data.action==None):
		try:
			o.animation_data.action=bpy.data.actions[o.name+"_ARM"];
		except:
			o.animation_data.action=bpy.data.actions.new(o.name+"_ARM");
	action=o.animation_data.action;
	# Cag组=action.groups;#根据骨名
	Cfc弓=action.fcurves;#通道 Location Rotation
	#----骨------------------------------------------------
	if (o.type == 'ARMATURE'):
		Cpb = o.pose.bones;
		#----只能应用到同名骨上--------------------------------------------
		# LG.Lpb烘焙.clear();
		# for pb in Cpb:
			# if(pb.ghost_ik.type in[TYPE_物理,TYPE_布料]):
				# LG.Lpb烘焙.append(pb);

		#----找到关键帧的pb,就不烘焙--------------------------
		# LG.MpbL10kc.clear();
		"""
		for fc in Cfc弓:
			for pb in LG.Lpb烘焙:
				if(pb.name in fc.data_path):
					s属性名=fc.data_path.split('.')[-1];#.rotation_quaternion
					if(s属性名 in["rotation_quaternion","location","scale"]):
						print("★ remove pb==",pb,);
						LG.Lpb烘焙.remove(pb);
						break;
		"""
		# print("Cfc弓.data_path==",Cfc弓[0].data_path);
		fcPx=fcPy=fcPz=None;fcQw=fcQx=fcQy=fcQz=None;fcSx=fcSy=fcSz=None;
		# for pb in LG.Lpb烘焙:
		# for pb,L10kc in LG.MpbL10kc.items(): #★ 字典值不能引用
		for pb in LG.MpbL10kc:
			s骨名='pose.bones["'+pb.name+'"]';
			""""""
			if(pb.bone.use_connect==False):
				if(bΔ在曲线(s骨名+".location",Cfc弓)==False):#已经存在键
					fcPx=Cfc弓.new(data_path=s骨名+".location", index=0, action_group=pb.name);
					fcPy=Cfc弓.new(data_path=s骨名+".location", index=1, action_group=pb.name);
					fcPz=Cfc弓.new(data_path=s骨名+".location", index=2, action_group=pb.name);		
			# else:
				# if(bΔ在曲线(s骨名+".location",Cfc弓)==False):
					# fcPx=Cfc弓.new(data_path=s骨名+".location", index=0, action_group=pb.name);
					# fcPy=Cfc弓.new(data_path=s骨名+".location", index=1, action_group=pb.name);
					# fcPz=Cfc弓.new(data_path=s骨名+".location", index=2, action_group=pb.name);				
			if(bΔ在曲线(s骨名+".rotation_quaternion", Cfc弓)==False):
				fcQw=Cfc弓.new(data_path=s骨名+".rotation_quaternion", index=0, action_group=pb.name);
				fcQx=Cfc弓.new(data_path=s骨名+".rotation_quaternion", index=1, action_group=pb.name);
				fcQy=Cfc弓.new(data_path=s骨名+".rotation_quaternion", index=2, action_group=pb.name);
				fcQz=Cfc弓.new(data_path=s骨名+".rotation_quaternion", index=3, action_group=pb.name);
			if(bΔ在曲线(s骨名+".scale[0]",Cfc弓)==False):
				fcSx=Cfc弓.new(data_path=s骨名+".scale", index=0, action_group=pb.name);
				fcSy=Cfc弓.new(data_path=s骨名+".scale", index=1, action_group=pb.name);
				fcSz=Cfc弓.new(data_path=s骨名+".scale", index=2, action_group=pb.name);
			LG.MpbL10kc[pb]=[fcPx,fcPy,fcPz,  fcQw,fcQx,fcQy,fcQz,  fcSx,fcSy,fcSz];
			# print("L10kc==",L10kc);
		print("十十fcurve1o ==",LG.MpbL10kc);
		
#====LG.Lpb烘焙 ●,LG.MpbL10kc ■====================================
def 屮key1o(o,scene,ip跳过帧数,i开始时刻=-1):
	# print("INSERT Keyframe==",o,bpy.context.selected_nla_strips);
	if(-1<i开始时刻):
		start=i开始时刻;
	else:
		start=scene.frame_start;
	end=scene.frame_end;
	wm=bpy.context.window_manager;
	#----只能应用到同名骨上--------------------------------------------
	print("屮key1o Lpb==",i开始时刻,ip跳过帧数);#,LG.MpbL10kc
	# for pb in LG.Lpb烘焙:
	for pb,L10kc in LG.MpbL10kc.items():
		# ag=Cag组[pb.name];
		L帧Lf10=wm["Ms骨L帧"][pb.name];#print("L帧Lf10==",pb,L帧Lf10.__len__());
		NEEDED="NEEDED";#"NEEDED" REPLACE  FAST
		# if(pb in LG.MpbL10kc):
			# L10kc=LG.MpbL10kc[pb];
		# continue;
		
		i跳过帧=start;
		for i,Lf10 in enumerate(L帧Lf10):
			i帧=i+start;#print("Lf10==",i跳过帧,i帧,*Lf10);
			if(end<i帧):
				break;
			if(0<ip跳过帧数):
				if(end<i跳过帧):
					break;
				if(i帧!=i跳过帧):#1==>(1,3,5,7)
					continue;
				else:
					i跳过帧+=ip跳过帧数;
			# print("Lf10==",i跳过帧,i帧,L10kc,*Lf10);
			if(pb.bone.use_connect==False):
				L10kc[0].keyframe_points.insert(frame=i帧, value=Lf10[0],options={NEEDED});#位置
				L10kc[1].keyframe_points.insert(frame=i帧, value=Lf10[1],options={NEEDED});
				L10kc[2].keyframe_points.insert(frame=i帧, value=Lf10[2],options={NEEDED});
			else:
				L10kc[0].keyframe_points.insert(frame=i帧, value=0,options={NEEDED});#位置
				L10kc[1].keyframe_points.insert(frame=i帧, value=0,options={NEEDED});
				L10kc[2].keyframe_points.insert(frame=i帧, value=0,options={NEEDED});	
			L10kc[3].keyframe_points.insert(frame=i帧, value=Lf10[3],options={NEEDED});#q
			L10kc[4].keyframe_points.insert(frame=i帧, value=Lf10[4],options={NEEDED});
			L10kc[5].keyframe_points.insert(frame=i帧, value=Lf10[5],options={NEEDED});			
			L10kc[6].keyframe_points.insert(frame=i帧, value=Lf10[6],options={NEEDED});
			
			L10kc[7].keyframe_points.insert(frame=i帧, value=Lf10[7],options={NEEDED});#缩放
			L10kc[8].keyframe_points.insert(frame=i帧, value=Lf10[8],options={NEEDED});
			L10kc[9].keyframe_points.insert(frame=i帧, value=Lf10[9],options={NEEDED});	
				
		for kc in L10kc:
			if(kc):
				kc.update();
				
#========================================
def 一一bake1o(self,o__,i物理丨普通=0):#-1:所有骨,0:物理,1:ik骨
	print("一一bake1o==",o__,i物理丨普通);
	if(o__.type=="ARMATURE"):#and o__.ppOn.type==1
		Ls物理骨=[];
		for pb in o__.pose.bones:
			# if(pb.name in Ms骨名):#有可能这个骨没有action 通道
			if(i物理丨普通==0):
				if("PoseBone"in pb and "type" in pb["PoseBone"]):
					if(pb["PoseBone"]["type"]in(LG.TYPE_物理,LG.TYPE_布料)):
						Ls物理骨.append(pb.name);
			elif(i物理丨普通==1):
				if("PoseBone"in pb and "type" in pb["PoseBone"]):
					if(LG.TYPE_无<pb["PoseBone"]["type"] and pb["PoseBone"]["type"]<LG.TYPE_物理):
						Ls物理骨.append(pb.name);
			elif("PoseBone"not in pb):
				Ls物理骨.append(pb.name);#所有骨
		print("Ls物理骨==",Ls物理骨);
		action=o__.animation_data.action;
		if(action==None):
			print("!! action==None return;",o__);
			return{"CANCELED"};
		# CagS=action.groups;print("CagS==",*CagS);
		Cfc弓=action.fcurves;#print("Cfc弓==",*Cfc弓,Cfc弓.keys());#所有关键帧			

		for fc in Cfc弓:
			S=fc.data_path.split('"]')[0];s物理骨=S.split('["')[-1];print("s物理骨==",s物理骨,s物理骨=='Bone.019',s物理骨 in Ls物理骨);
			if(s物理骨 in Ls物理骨):
				Cfc弓.remove(fc);#Ls物理骨.remove(s物理骨);
		
		try:
			o__.ppOn.bp有烘焙=False;
		except:	
			o__.ppO.bp有烘焙=False;
		# print("Cfc弓==",*Cfc弓)
	else:
		self.report({"ERROR"},"this is not a armature!!");#"INFO" "ERROR" "DEBUG" "WARNING"
		return{"CANCELED"};
					
					
					
	
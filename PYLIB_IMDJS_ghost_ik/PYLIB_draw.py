
import bpy,sys,os
import bgl,gpu,blf;
from gpu_extras.batch import batch_for_shader
shader囗 = gpu.shader.from_builtin('2D_UNIFORM_COLOR');
shader图 = gpu.shader.from_builtin('2D_IMAGE');
from gpu.types import(GPUBatch,GPUIndexBuf,GPUVertBuf,GPUVertFormat,);
fmt = GPUVertFormat();pos_id = fmt.attr_add(id="pos", comp_type='F32', len=2, fetch_mode='FLOAT')
#----------------------------------------
from bpy.props import BoolProperty,IntProperty,StringProperty,PointerProperty;
from mathutils import Matrix,Vector,Euler
from ctypes import*
#from bpy_extras import object_utils
from bpy_extras import view3d_utils
#import bmesh
from math import*


try:
	import PYLIB.LG as LG;
	#\IMDJS_hair_collector.PYLIB_IMDJS_hair_collector.PYLIB_IMDJS_hair_collector
	# print("import ++==%s"%(sPYLIB父级+".PYLIB_"+sPYLIB父级+".PYLIB_"+sPYLIB父级));

except:
	path目录PYLIB上上级 =os.path.abspath(os.path.join(os.path.dirname(__file__),".."));#上上级目录 
	sPYLIB父级=os.path.basename(path目录PYLIB上上级);
	exec("import "+sPYLIB父级+".PYLIB_"+sPYLIB父级+".LG as LG");	
	print("LG==",LG);

# from .PYLIB_module import dll载入dll;	
# from .PYLIB_print import PTL亖亖,PTLfn亖亖;
#from .PYLIB_math import 十二 ;#Lcf3巜Lf3,Lf3巜Lcf3,
# def 十二(f3一,  f3二):   f3二[0]=f3一[0]+f3二[0];f3二[1]=f3一[1]+f3二[1];f3二[2]=f3一[2]+f3二[2];
#/////////////////////////////////////////
def py_叵画(G_,scene,b画面=False,b画丷=False,b画Λ=False,b画m=False,b画字=False,b画弓=False,b画2d=False \
								,L2条数丶iSize点=(LG.i10,LG.i512),L2条数丶iSize线=(LG.i10,LG.i256),L2条数丶iSize乛=(LG.i10,LG.i256) \
								,iSize丷=LG.i32,iSizeΛ=LG.i32,iSize厶=LG.i32,iSize囗=LG.i32,iSize厸=LG.i32,iSizem=LG.i64,iSize字=LG.i2048 \
								,iSize线2d=LG.i64 \
								,iSize弓=LG.i32):
	print("<<<py_叵画	 G_.iSizeG==",LG,G_.卍dll.dll,b画字,b画弓,b画2d,iSize字,iSizem);#G_.ciSize数G.value,G_.CL2条数丶iSize点G.value
	
	LG.sc_LG(scene,LG);

	print("点线乛==",LG.画点,LG.画线,LG.画乛);
	# bpy.ops.op.draw_3d_lib("INVOKE_DEFAULT",bp显示=False);
	# if(G_.卍dll.dll):
	if(L2条数丶iSize点[0]<1 or L2条数丶iSize点[0]<1 or	L2条数丶iSize线[0]<1 or L2条数丶iSize线[1]<1 or L2条数丶iSize乛[0]<1 or L2条数丶iSize乛[1]<1 or iSize丷< 1 or iSizeΛ< 1 or iSize厶< 1 or iSize囗< 1  or iSize厸< 1 or iSizem< 1 or iSize字< 5 or iSize线2d< 5 or iSize弓< 5):
		print("L2条数丶iSize点==",*L2条数丶iSize点,*L2条数丶iSize线,*L2条数丶iSize乛,iSize丷,iSizeΛ,iSize厶,iSize囗,iSize厸,iSize字,iSize线2d,iSize弓);
		# G_.卍dll.dll.凸ASSERT("★py_叵画::2条数丶iSize点[0]<1 ".encode('UTF-8'),True);
		# print("★py_叵画::L2条数丶iSize点[0]<1 ==",L2条数丶iSize点[0]);
		return;
		
	G_.CL2条数丶iSize点G=(c_int*2)(*L2条数丶iSize点);G_.CL条序艹点画G=(c_int*LG.i10)();G_.CL条序col点G=(c_float*4*L2条数丶iSize点[0])();
	G_.CL2条数丶iSize线G=(c_int*2)(*L2条数丶iSize线);G_.CL条序艹线画G=(c_int*LG.i10)();G_.CL条序col线G=(c_float*4*L2条数丶iSize线[0])();
	G_.CL2条数丶iSize乛G=(c_int*2)(*L2条数丶iSize乛);G_.CL条序艹乛画G=(c_int*LG.i10)();G_.CL条序col乛G=(c_float*4*L2条数丶iSize乛[0])();
	G_.L条序艹pre点=[0]*L2条数丶iSize点[0];G_.L条序L点序f2=[[] for i in range(L2条数丶iSize点[0])];#●●必须这样填充,不然会重复id 在 extend([[]]*i一) 时出错
	G_.CL点序f2=((c_float*2)*L2条数丶iSize点[0])();
	G_.L条序艹pre一一=[0]*L2条数丶iSize线[0];G_.L条序LL2f2一一=[[]for i in range(L2条数丶iSize线[0])];
	G_.L条序艹pre乛=[0]*L2条数丶iSize乛[0];G_.L条序LL6f2=[[]for i in range(L2条数丶iSize乛[0])];
	#------------------------------
	print("LIB Size==",G_.CL2条数丶iSize点G,L2条数丶iSize点,L2条数丶iSize线,L2条数丶iSize乛,iSize丷,iSize厶,iSize囗,iSize厸,iSize字);print("in G_.卍dll.dll==",G_.卍dll.dll,b画弓);
	# G_.卍dll.dll.py_定义画数test();
	G_.卍dll.dll.py_定义画数(G_.CL2条数丶iSize点G,G_.CL2条数丶iSize线G,G_.CL2条数丶iSize乛G,iSize丷,iSizeΛ,iSize厶,iSize囗,iSize厸,iSizem,iSize字);
	if(b画弓):
		G_.卍dll.dll.py_定义画数(G_.CL2条数丶iSize点G,G_.CL2条数丶iSize线G,G_.CL2条数丶iSize乛G,iSize丷,iSizeΛ,iSize厶,iSize囗,iSize厸,iSizem,iSize字);LG.画弓=True;
	else:
		LG.画弓=False;
	#----叵--------------------------
	if(G_.CL条序LL4f2乛画G==None or G_.CL条序LL2f2线画G==None or G_.CL条序L点序f2画G==None \
				or G_.CL条序L点序f2画G.__len__()!=L2条数丶iSize点[0] or G_.CL条序L点序f2画G[0].__len__()!=LG.i512	 \
				or G_.CL条序LL2f2线画G.__len__()!=L2条数丶iSize线[0] or G_.CL条序LL2f2线画G[0].__len__()!=L2条数丶iSize线[1] \
				or G_.CL条序LL4f2乛画G.__len__()!=LG.i256):
				
		G_.CL条序L点序f2画G=(c_float*2*LG.i512*G_.CL2条数丶iSize点G[0])();#左边是位置,右边是颜色,i256 必须与C++ 参数float CL条L点序f2点画__[][i256][2] 一致
		G_.CL条序LL4f2乛画G=(c_float*2*4*LG.i256*G_.CL2条数丶iSize乛G[0])();
		G_.CL条序LL2f2线画G=(c_float*2*2*LG.i256*G_.CL2条数丶iSize线G[0])();

		G_.CLL4f4丷画G=(c_float*4*4*iSize丷)();
		G_.CLL5f4Λ画G=(c_float*4*5*iSizeΛ)();
	
		if(b画面 and G_.CL面序L4f4厶画G==None):
			G_.CL面序L4f4厶画G=(c_float*4*4*iSize厶)(); 
			G_.CL面序L5f4囗画G=(c_float*4*5*iSize囗)();
			G_.CL面序Lnf4厸画G=(c_float*4*5*iSize厸)();
			G_.CLL2f2一一序绑画G=(c_float*2*2*LG.i256)();
	
		if(b画m and G_.CLL13f4m画G==None):
			G_.CLL13f4m画G=(c_float*4*13*iSizem)(); 	
	#----画字--------------------------
	if(b画字 and G_.CLL2f4丅字画G==None):
		G_.CLL2f4丅字画G=(c_float*4*2*iSize字)();#0位,1 色
		G_.CLs64字G=(c_char*LG.i64*iSize字)();#64个char为一个字符串
	
	#----2d--------------------------
	print("b画2d==",b画2d,G_.CLL3i4线画2dG);
	if(b画2d and G_.CLL3i4线画2dG==None):
		G_.卍dll.dll.py_定义画数2d(iSize线2d);
		G_.CLL3i4线画2dG=(c_int*4*3*iSize线2d)();
	# if(G_.cvpC==None or G_.cvpOA==None ):
		# G_.C=bpy.context;
		# G_.cvpC=c_void_p(G_.C.as_pointer());#G_.cvpOA=c_void_p(G_.C.active_object.as_pointer());	   if(G_.cvpVL):
			#G_.cvpVL = c_void_p(G_.C.view_layer.as_pointer());	 
	# if(G_.卍dll.dll):
		# G_.卍dll.dll.b凸凷rv3d(c_void_p(bpy.context.as_pointer()),True);
	#------------------------------
	# Δ凷area3d(G_,bpy.context);Δ凷area2d(G_,bpy.context);
	G_.卍dll.dll.凸画3d(True);# b画G ■
	print(">>INIT G_.iSizeG end==");

#========================================
def 灬gl乚(G_):
	print("<<<CLEAR G_==",G_);
	if(G_):
		print("乚3d 0==",G_.卍dll.乚3d);
		if(G_.卍dll.乚3d):
			bpy.types.SpaceView3D.draw_handler_remove(G_.卍dll.乚3d, 'WINDOW');G_.卍dll.乚3d=None;	  
	if(G_.乚字G ):
		bpy.types.SpaceView3D.draw_handler_remove(G_.乚字G, 'WINDOW');G_.乚字G=None;
	if(G_.乚2d面G):
		bpy.types.SpaceView3D.draw_handler_remove(G_.乚2d面G, 'WINDOW');G_.乚2d面G=None;
	#----area,●●有可能换了场景但没换area --------------------------
	# if(G_.area3dG):
		# G_.area3dG.tag_redraw();
	# if(G_.area2dG):
		# G_.area2dG.tag_redraw();
	# G_.area3dG=None;G_.view3dG=None;
	# G_.regionG=None;
	G_.b高亮G=False;
	print(">>CLEAR 乚3d 1==",);
	
#========================================
def 灬gl数据(G_):
	print("<<< 灬gl数据",);
	#----CF----------------------------------------------
	G_.CL条序L点序f2画G=None;G_.CLL2f2一一序绑画G=None;G_.CL条序LL2f2线画G=None;G_.CL条序LL4f2乛画G=None;G_.CL面序L4f4厶画G=None;G_.CL面序L5f4囗画G=None;G_.CL面序Lnf4厸画G=None;G_.CLL4f4丷画G=None;G_.CLL5f4Λ画G=None;G_.CLL13f4m画G=None;
	G_.CLL2f4丅字画G=None;G_.CLs64字G=None;G_.b画面G=False;G_.画厶=False;G_.画丷=False;G_.画Λ=False;G_.i画字=0;
	
	G_.L条序L点序f2=[];G_.L条序LL2f2一一=[];G_.L条序LL6f2=[];G_.L条序艹pre点=[];G_.L条序艹pre一一=[];G_.L条序艹pre乛=[];G_.f2丅画=None;

	# if(G_.卍dll.dll):
		# G_.卍dll.dll.凸〇画();
		# G_.卍dll.dll=dll卸载dll(LG,"dllDJS");
	#----丄-------------------------------------------------
	# G_.CL条序L2f2丄画G=None;
	print(">>CLEAR data 1==",);
#====2D====================================
def 灬gl乚2d(G_):
	if(G_):
		print("<<<CLEAR handles 2d==",G_.卍dll.乚2d);
		if(G_.卍dll.乚2d):
			bpy.types.SpaceNodeEditor.draw_handler_remove(G_.卍dll.乚2d, 'WINDOW');G_.卍dll.乚2d=None; 
			# print("remove 乚2d==",乚2d);
	# if(G_.area2dG):
		# G_.area2dG.tag_redraw();
	# G_.area2dG=None;G_.region2dG=None;G_.space2dG=None;
	# G_.b高亮G=False;
	print(">>CLEAR handles 2d==",);
	
def 灬gl数据2d(G_):
	G_.艹线画2dG=c_int();G_.CLL3i4线画2dG=None;	
#====在 dll	画 刷新窗口====================================
"""
def Δ凷area3d(G_,context):
	if(G_.area3dG==None):
		screen=context.screen;
		for area in screen.areas:
			# print("area.type==",area.type);
			if(area.type=="VIEW_3D"):
				G_.area3dG=area;
				break;
				
def Δ凷area2d(G_,context,sp界面="NODE_EDITOR"):
	if(G_.area2dG==None):
		screen=context.screen;
		for area in screen.areas:
			if(area.type==sp界面):
				G_.area2dG=area;
				G_.area2dG.tag_redraw();	
				for region in area.regions:					   
					if(region.type=="WINDOW"):
						G_.region2dG=region; #[‘WINDOW’, ‘HEADER’, ‘CHANNELS’, ‘TEMPORARY’, ‘UI’, ‘TOOLS’, ‘TOOL_PROPS’, ‘PREVIEW’], default ‘WINDOW’,		
						break;
				for space in area.spaces:					 
					if(space.type==sp界面):
						G_.space2dG=space;
						break;
"""
#====点====================================
def ΔΔ画n点(G_,ξ条):
	# print("ξ条== %d,%d,%d"%(ξ条,G_.L条序L点序f2.__len__(),G_.CL条序艹点画G[ξ条]));
	if(0<G_.CL条序艹点画G[ξ条]):
		i一=G_.CL条序艹点画G[ξ条]-G_.L条序艹pre点[ξ条];#print("==",i一,[*G_.CL条序艹点画G],G_.L条序艹pre点,G_.L条序L点序f2);
		if(0<i一):
			G_.L条序L点序f2[ξ条].extend([[]]*i一);G_.L条序艹pre点[ξ条]=G_.CL条序艹点画G[ξ条];#print("++",[*G_.CL条序艹点画G],G_.L条序艹pre点,G_.L条序L点序f2);
		elif(i一<0):#现在比之前少了,就缩小
			G_.L条序L点序f2[ξ条]=G_.L条序L点序f2[ξ条][:G_.CL条序艹点画G[ξ条]];G_.L条序艹pre点[ξ条]=G_.CL条序艹点画G[ξ条];#print("--",G_.L条序艹pre点,G_.L条序L点序f2);
		# print("==",[*G_.CL条序艹点画G],G_.L条序L点序f2[0].__len__(),G_.CL条序L点序f2画G[0].__len__());
		for i in range(G_.CL条序艹点画G[ξ条]):
			# print("==",ξ条,i,G_.L条序L点序f2[ξ条].__len__(),G_.CL条序L点序f2画G[ξ条].__len__());#,G_.CL条序L点序f2画G[ξ条][i]
			G_.L条序L点序f2[ξ条][i]=G_.CL条序L点序f2画G[ξ条][i];
			# print("ξ条:%d,*G_.L条序L点序f2[ξ条][i]:%d=="%ξ条,*G_.L条序L点序f2[ξ条][i]);
		# print("G_.CL条序L点序f2画G==",G_.L条序L点序f2[ξ条]);#,*G_.CL条序L点序f2画G
		# print("G_.L条序L点序f2[ξ条]==",ξ条,*G_.L条序L点序f2[ξ条][0],*G_.L条序L点序f2[ξ条][1]);
		#------------------------------
		# vbo_format = shader囗.format_calc();
		L点 = GPUVertBuf(fmt,G_.L条序L点序f2[ξ条].__len__());
		L点.attr_fill(id="pos",data=G_.L条序L点序f2[ξ条]);#[[x,y],[x,y],[x,y],]
		# L点.attr_fill(id="pos",data=G_.CL点序f2);
		#------------------------------
		shader囗.bind();
		shader囗.uniform_float("color", G_.CL条序col点G[ξ条]);
		GPUBatch(type='POINTS', buf=L点).draw(shader囗);
		
#////画线///////////////////////////////////////
def ΔΔ画n乛(G_,ξ条):
	# print("G_.CL条序艹乛画G[ξ条]==",ξ条,[*G_.CL条序艹乛画G],G_.L条序艹pre乛,G_.CL条序LL4f2乛画G[ξ条]);
	if(0<G_.CL条序艹乛画G[ξ条]):
		i一=G_.CL条序艹乛画G[ξ条]-G_.L条序艹pre乛[ξ条];
		# print("G_.CL条序艹乛画G[ξ条]==",G_.L条序艹pre乛,G_.CL条序艹乛画G[ξ条],i一,G_.L条序LL6f2[ξ条].__len__(),id(G_.L条序LL6f2[ξ条]));
		if(0<i一):
			G_.L条序LL6f2[ξ条].extend([[]]*6*i一);G_.L条序艹pre乛[ξ条]=G_.CL条序艹乛画G[ξ条];#print("++id(L条序LL6f2[ξ条])==",G_.L条序LL6f2[ξ条].__len__(),id(G_.L条序LL6f2[ξ条]));
		elif(i一<0):
			G_.L条序LL6f2[ξ条]=G_.L条序LL6f2[ξ条][:6*G_.CL条序艹乛画G[ξ条]];G_.L条序艹pre乛[ξ条]=G_.CL条序艹乛画G[ξ条];#G_.L条序LL6f2[ξ条]=G_.L条序LL6f2[ξ条];
			#print("--id(L条序LL6f2[ξ条])==",G_.L条序LL6f2[ξ条].__len__(),id(G_.L条序LL6f2[ξ条]));
		for i in range(G_.CL条序艹乛画G[ξ条]):
			G_.CL4f2=G_.CL条序LL4f2乛画G[ξ条][i];#print("CL4f2==",*G_.CL4f2[0],*G_.CL4f2[1],*G_.CL4f2[2],*G_.CL4f2[3]);
			j=i*6;#[0,1,2,3,4,5	   ,   6,7,8,9,10,11] 
			G_.L条序LL6f2[ξ条][j]=G_.CL4f2[0];G_.L条序LL6f2[ξ条][j+1]=G_.CL4f2[1];
			G_.L条序LL6f2[ξ条][j+2]=G_.CL4f2[1];G_.L条序LL6f2[ξ条][j+3]=G_.CL4f2[2];
			G_.L条序LL6f2[ξ条][j+4]=G_.CL4f2[1];G_.L条序LL6f2[ξ条][j+5]=G_.CL4f2[3];
		#------------------------------
		# vbo_format = shader囗.format_calc();
		# print("ΔΔ画n乛 G_.L条序LL6f2[ξ条]==",*G_.L条序LL6f2[ξ条][0],*G_.L条序LL6f2[ξ条][1],*G_.L条序LL6f2[ξ条][2],G_.L条序LL6f2[ξ条].__len__(),id(G_.L条序LL6f2[ξ条]),*G_.CL条序col乛G[ξ条]);
		L点 = GPUVertBuf(fmt,G_.L条序LL6f2[ξ条].__len__());L点.attr_fill(id="pos",data=G_.L条序LL6f2[ξ条]);
		#------------------------------
		shader囗.bind();
		shader囗.uniform_float("color",G_.CL条序col乛G[ξ条]);
		GPUBatch(type='LINES', buf=L点).draw(shader囗);
		
#====m==========================================
def ΔΔ画m(G_):
	# print("G_.艹m画G.value==",ξ条,[*G_.CL条序艹乛画G],G_.L条序艹pre乛,G_.CLL13f4m画G);
	if(0<G_.艹m画G.value):
		ii=6*G_.艹m画G.value;#只有一个轴
		if(ii!=G_.LL6f2.__len__()):
			G_.LL6f2=[[]]*ii;
		""""""
		#----X-----------------------------------------
		艹=0;艹跳过=0;
		for i in range(G_.艹m画G.value):
			G_.CL13f4m=G_.CLL13f4m画G[i];#print("CL13f4m==",*G_.CL13f4m[0],*G_.CL13f4m[1],*G_.CL13f4m[2],*G_.CL13f4m[3]);
			if(G_.CL13f4m[0][0]==0 and G_.CL13f4m[0][1]==0 and G_.CL13f4m[0][2]==0):
				艹跳过+=1;
				continue;
			j=艹*6;艹+=1;
			
			G_.LL6f2[j]=(G_.CL13f4m[0][0],G_.CL13f4m[0][1]);G_.LL6f2[j+1]=(G_.CL13f4m[1][0],G_.CL13f4m[1][1]);
			G_.LL6f2[j+2]=(G_.CL13f4m[1][0],G_.CL13f4m[1][1]);G_.LL6f2[j+3]=(G_.CL13f4m[2][0],G_.CL13f4m[2][1]);
			G_.LL6f2[j+4]=(G_.CL13f4m[1][0],G_.CL13f4m[1][1]);G_.LL6f2[j+5]=(G_.CL13f4m[3][0],G_.CL13f4m[3][1]);	
		#------------------------------
		# print("艹跳过==",艹跳过,艹);
		if(0<艹跳过):
			G_.LL6f2=G_.LL6f2[:艹*6];
		# try:
		L点 = GPUVertBuf(fmt,ii-艹跳过*6);L点.attr_fill(id="pos",data=G_.LL6f2);
		# except:	
			# print("★ ==",*G_.LL6f2);print("★2 ==",*G_.CL13f4m[0],*G_.CL13f4m[1],*G_.CL13f4m[2],*G_.CL13f4m[3]);
		#------------------------------
		shader囗.bind();
		shader囗.uniform_float("color",G_.CL13f4m[10]);
		GPUBatch(type='LINES', buf=L点).draw(shader囗);
		# return;
		#----Y-----------------------------------------
		艹=0;艹跳过=0;
		for i in range(G_.艹m画G.value):
			G_.CL13f4m=G_.CLL13f4m画G[i];#print("CL13f4m==",*G_.CL13f4m[0],*G_.CL13f4m[1],*G_.CL13f4m[2],*G_.CL13f4m[3]);
			if(G_.CL13f4m[0][0]==0 and G_.CL13f4m[0][1]==0 and G_.CL13f4m[0][2]==0):
				艹跳过+=1;
				continue;
			j=艹*6;艹+=1;
			G_.LL6f2[j]=(G_.CL13f4m[0][0],G_.CL13f4m[0][1]);G_.LL6f2[j+1]=(G_.CL13f4m[4][0],G_.CL13f4m[4][1]);
			G_.LL6f2[j+2]=(G_.CL13f4m[4][0],G_.CL13f4m[4][1]);G_.LL6f2[j+3]=(G_.CL13f4m[5][0],G_.CL13f4m[5][1]);
			G_.LL6f2[j+4]=(G_.CL13f4m[4][0],G_.CL13f4m[4][1]);G_.LL6f2[j+5]=(G_.CL13f4m[6][0],G_.CL13f4m[6][1]);
		
		#------------------------------
		if(0<艹跳过):
			G_.LL6f2=G_.LL6f2[:艹*6];
		L点 = GPUVertBuf(fmt,ii-艹跳过*6);L点.attr_fill(id="pos",data=G_.LL6f2);
		#------------------------------
		shader囗.bind();
		shader囗.uniform_float("color",G_.CL13f4m[11]);
		GPUBatch(type='LINES', buf=L点).draw(shader囗);
		
		#----Z-----------------------------------------
		艹=0;艹跳过=0;
		for i in range(G_.艹m画G.value):
			G_.CL13f4m=G_.CLL13f4m画G[i];#print("CL13f4m==",*G_.CL13f4m[0],*G_.CL13f4m[1],*G_.CL13f4m[2],*G_.CL13f4m[3]);
			if(G_.CL13f4m[0][0]==0 and G_.CL13f4m[0][1]==0 and G_.CL13f4m[0][2]==0):
				艹跳过+=1;
				continue;
			j=艹*6;艹+=1;
			G_.LL6f2[j]=(G_.CL13f4m[0][0],G_.CL13f4m[0][1]);G_.LL6f2[j+1]=(G_.CL13f4m[7][0],G_.CL13f4m[7][1]);
			G_.LL6f2[j+2]=(G_.CL13f4m[7][0],G_.CL13f4m[7][1]);G_.LL6f2[j+3]=(G_.CL13f4m[8][0],G_.CL13f4m[8][1]);
			G_.LL6f2[j+4]=(G_.CL13f4m[7][0],G_.CL13f4m[7][1]);G_.LL6f2[j+5]=(G_.CL13f4m[9][0],G_.CL13f4m[9][1]);			
		#------------------------------
		if(0<艹跳过):
			G_.LL6f2=G_.LL6f2[:艹*6];
		L点 = GPUVertBuf(fmt,ii-艹跳过*6);L点.attr_fill(id="pos",data=G_.LL6f2);
		#------------------------------
		shader囗.bind();
		shader囗.uniform_float("color",G_.CL13f4m[12]);
		GPUBatch(type='LINES', buf=L点).draw(shader囗);
#----▲ 实心面----------------------------------------------
def Δ画1厶(CL4f4):
	# print("TRIS==",(CL4f4[0][0],CL4f4[0][1]),(CL4f4[1][0],CL4f4[1][1]),(CL4f4[2][0],CL4f4[2][1]),*CL4f4[3],*CL4f4[4]);
	# vbo_format = shader囗.format_calc();
	L点 = GPUVertBuf(fmt, 4);#print("CL4f4==",CL4f4);
	L点.attr_fill(id="pos",data=[(CL4f4[0][0],CL4f4[0][1]),(CL4f4[1][0],CL4f4[1][1]),(CL4f4[2][0],CL4f4[2][1]),(CL4f4[0][0],CL4f4[0][1])]);
	#------------------------------
	shader囗.bind();
	shader囗.uniform_float("color", CL4f4[3]);
	GPUBatch(type='TRIS', buf=L点).draw(shader囗);#TRI_FAN
	
def Δ画n丷(G_):
	for i in range(G_.艹丷画G.value):
		G_.CL4f4=G_.CLL4f4丷画G[i];#print("G_.CL4f4==",*G_.CL4f4[0],*G_.CL4f4[1],*G_.CL4f4[2],*G_.CL4f4[3]);
		if(G_.CL4f4[0][0]==0 and G_.CL4f4[1][1]==0):
			continue;
		Δ画1厶(G_.CL4f4)#print("G_.CL4f4==",*G_.CL4f4[0],*G_.CL4f4[1],*G_.CL4f4[2],*G_.CL4f4[3]);
		
#----Λ ----------------------------------------------
def Δ画1Λ(CL5f4):
	# vbo_format = shader囗.format_calc();
	#----画线--------------------------
	L点 = GPUVertBuf(fmt, 6);#print("G_.LL6f2==",G_.LL6f2);
	L点.attr_fill(id="pos",data=[(CL5f4[0][0],CL5f4[0][1]),(CL5f4[1][0],CL5f4[1][1]),(CL5f4[2][0],CL5f4[2][1]),(CL5f4[1][0],CL5f4[1][1]),(CL5f4[3][0],CL5f4[3][1]),(CL5f4[1][0],CL5f4[1][1])]);#0->1,2->1,3->1 
	#----画面--------------------------
	# L点 = GPUVertBuf(fmt, 4);#print("G_.LL6f2==",G_.LL6f2);
	# L点.attr_fill(id="pos",data=[(CL5f4[0][0],CL5f4[0][1]),(CL5f4[1][0],CL5f4[1][1]),(CL5f4[2][0],CL5f4[2][1]),(CL5f4[3][0],CL5f4[3][1])]);#0->1->2->3
	#------------------------------
	shader囗.bind();
	shader囗.uniform_float("color", CL5f4[4]);
	GPUBatch(type='LINES', buf=L点).draw(shader囗);#TRI_FAN
	# GPUBatch(type='TRI_FAN', buf=L点).draw(shader囗);
	
def Δ画nΛ(G_):
	# print("G_.CLL5f4Λ画G==",G_.艹Λ画G.value,G_.CLL5f4Λ画G.__len__());
	for i in range(G_.艹Λ画G.value):
		G_.CL5f4=G_.CLL5f4Λ画G[i];#print("G_.CL5f4==",*G_.CL5f4[0],*G_.CL5f4[1],*G_.CL5f4[2],*G_.CL5f4[3],*G_.CL5f4[4]);
		if(G_.CL5f4[0][0]==0 and G_.CL5f4[1][0]==0 and G_.CL5f4[1][1]==0 and G_.CL5f4[1][2]==0):
			# print("0 DRAW==",*G_.CL5f4[0],*G_.CL5f4[1],*G_.CL5f4[2],*G_.CL5f4[3])
			continue;
		Δ画1Λ(G_.CL5f4)		
	
#====■====================================
def Δ画1囗(CL5f4):
	# return;
	# vbo_format = shader囗.format_calc();
	L点 = GPUVertBuf(fmt, 4);#print("CL5f4==",CL5f4);
	L点.attr_fill(id="pos",data=[(CL5f4[0][0],CL5f4[0][1]),(CL5f4[1][0],CL5f4[1][1]),(CL5f4[2][0],CL5f4[2][1]),(CL5f4[3][0],CL5f4[3][1])]);#print("CL5f4==",[(CL5f4[0][0],CL5f4[0][1]),(CL5f4[1][0],CL5f4[1][1]),(CL5f4[2][0],CL5f4[2][1]),(CL5f4[3][0],CL5f4[3][1])]);
	#------------------------------
	shader囗.bind();
	shader囗.uniform_float("color", CL5f4[4]);
	GPUBatch(type='TRI_FAN', buf=L点).draw(shader囗);#TRI_FAN,LINE_STRIP,TRIS
	
# ------------------------------------------------------
def Δ画1线(CL3f4):
	# 丅 = [(v1[0], v1[1]), (v2[0], v2[1])];
	# vbo_format = shader囗.format_calc();#len=CL3f4.__len__();
	L点 = GPUVertBuf(fmt, 2);#2个点
	L点.attr_fill(id="pos",data=[(CL3f4[0][0],CL3f4[0][1]),(CL3f4[1][0],CL3f4[1][1])]);
	#------------------------------
	shader囗.bind();
	shader囗.uniform_float("color", CL3f4[2]);
	GPUBatch(type='LINES', buf=L点).draw(shader囗);

def Δ画3线(CL4f4):
	# vbo_format = shader囗.format_calc();
	L点 = GPUVertBuf(fmt, 4);#print("CL4f4==",CL4f4);
	# L点.attr_fill(id="pos",data=CL4f4);
	L点.attr_fill(id="pos",data=[(CL4f4[0][0],CL4f4[0][1]),(CL4f4[1][0],CL4f4[1][1]),(CL4f4[2][0],CL4f4[2][1]),(CL4f4[0][0],CL4f4[0][1])]);
	#------------------------------
	shader囗.bind();
	shader囗.uniform_float("color", CL4f4[-1]);
	GPUBatch(type='LINE_STRIP', buf=L点).draw(shader囗);
	
def Δ画4线(CL5f4):
	# vbo_format = shader囗.format_calc();
	L点 = GPUVertBuf(fmt, 5);#print("CL5f4==",CL5f4);
	# L点.attr_fill(id="pos",data=CL5f4);
	L点.attr_fill(id="pos",data=[(CL5f4[0][0],CL5f4[0][1]),(CL5f4[1][0],CL5f4[1][1]),(CL5f4[2][0],CL5f4[2][1]),(CL5f4[3][0],CL5f4[3][1]),(CL5f4[0][0],CL5f4[0][1])]);
	#------------------------------
	shader囗.bind();
	shader囗.uniform_float("color", CL5f4[-1]);
	GPUBatch(type='LINE_STRIP', buf=L点).draw(shader囗);
#--------------------------------------------------

def ΔΔ画n线(G_,ξ):
	# print("G_.CL条序艹线画G==",G_.CL条序艹线画G,G_.L条序艹pre一一);
	if(0<G_.CL条序艹线画G[ξ]):
		i一=G_.CL条序艹线画G[ξ]-G_.L条序艹pre一一[ξ];
		if(0<i一):
			G_.L条序LL2f2一一[ξ].extend([[]]*2*i一);G_.L条序艹pre一一[ξ]=G_.CL条序艹线画G[ξ];#增加容量
			# print("++id(L条序LL2f2一一)==",G_.L条序LL2f2一一.__len__(),id(G_.L条序LL2f2一一));
		elif(i一<0):
			G_.L条序LL2f2一一[ξ]=G_.L条序LL2f2一一[ξ][:2*G_.CL条序艹线画G[ξ]];G_.L条序艹pre一一[ξ]=G_.CL条序艹线画G[ξ];#减少容量
			# print("--id(L条序LL2f2一一)==",G_.L条序LL2f2一一.__len__(),id(G_.L条序LL2f2一一));
		for i in range(G_.CL条序艹线画G[ξ]):
			G_.CL2f2=G_.CL条序LL2f2线画G[ξ][i];
			j=i*2;
			G_.L条序LL2f2一一[ξ][j]=G_.CL2f2[0];G_.L条序LL2f2一一[ξ][j+1]=G_.CL2f2[1];
			# print("==",G_.CL条序艹线画G[ξ],i,*G_.CL2f2[0],*G_.CL2f2[1]);
		#------------------------------
		len=G_.L条序LL2f2一一[ξ].__len__();
		# print("L条序LL2f2一一==",G_.L条序LL2f2一一[ξ],G_.L条序LL2f2一一.__len__(),*G_.L条序LL2f2一一[ξ][0],*G_.L条序LL2f2一一[ξ][1]);
		L点 = GPUVertBuf(fmt,len);L点.attr_fill(id=pos_id,data=G_.L条序LL2f2一一[ξ]);
		#------------------------------
		shader囗.bind();
		shader囗.uniform_float("color",G_.CL条序col线G[ξ]);
		GPUBatch(type='LINES', buf=L点).draw(shader囗);
		

#----------------------------------------
def 画3d(self,context,G_):#L2v丅
	if(G_.卍dll.dll==None):
		print("★★ G_.卍dll.dll==",G_.卍dll.dll);return;
	# G_=self.G;
	# print("画3d G_==",G_.卍dll.dll);
	# return;#●●就算这样也会crash
	# print("G_.b画面G,G_.i画字==",G_.b画面G,G_.i画字);
	#if(self.v物丅==Vector()):return ;
	# print("draw 3d lib~~~~~~~~~~==",G_.卍dll.dll,G_.CL条序艹点画G,G_.CL条序L点序f2画G);
	bgl.glEnable(bgl.GL_BLEND);
	# rgba=[1,1,1,1];
	# bgl.glBegin(bgl.GL_LINES);#●●ΧGL_LINES 独立的线段	 GL_POINT	GL_LINE_STIPPLE	 GL_LINE_STRIP GL_LINE_LOOP 依次1个点连1个点
	rgba=G_.蓝; 
	bgl.glPointSize(6);
	bgl.glLineWidth(2);
	#print("DRAW　Lv丅实物画G==",G_.Cf3实物画G);
	# print("draw Curve?==",G_.画弓);
	#----cf----------------------------------------------
	if(LG.画弓==False):
		G_.卍dll.dll.凸画bl(G_.CL条序艹点画G,G_.CL条序L点序f2画G[0],G_.CL条序col点G[0] 
						,byref(G_.艹丷画G),G_.CLL4f4丷画G 
						,byref(G_.艹Λ画G),G_.CLL5f4Λ画G 
						,G_.CL条序艹线画G,G_.CL条序LL2f2线画G[0] ,G_.CL条序col线G[0] 
						,G_.CL条序艹乛画G,G_.CL条序LL4f2乛画G[0],G_.CL条序col乛G[0] 
						,byref(G_.艹厶画G),G_.CL面序L4f4厶画G 
						,byref(G_.艹囗画G),G_.CL面序L5f4囗画G 
						,byref(G_.艹厸画G),G_.CL面序Lnf4厸画G 
						,byref(G_.艹m画G),G_.CLL13f4m画G 
						);#PTL亖亖(G_.CL条序LL2f2线画G[0]);PTL亖亖(G_.CL条序LL2f2线画G[1]);
		# print("++NUM==",G_.艹厶画G.value,G_.艹囗画G.value);
		# print("LG.画丷==",LG.画丷,G_.艹丷画G.value);
		#====点====================================
		if(LG.画点):
			ΔΔ画n点(G_,0);
		#---- 一一 --------------------------
		if(LG.画线):
			ΔΔ画n线(G_,0);#return;
		#----cf箭头----------------------------------------------
		if(LG.画乛):
			ΔΔ画n乛(G_,0);
		#----丷,Λ-------------------------
		if(LG.画丷):
			Δ画n丷(G_);
		if(LG.画Λ):
			Δ画nΛ(G_);#print("Λ value==",G_.艹Λ画G.value);
		#----m-----------------------------------------
		if(LG.画m):
			ΔΔ画m(G_);
	#====弓====================================
	else:
		G_.卍dll.dll.凸画弓(G_.CL条序艹点画G 
					,G_.CL条序L点序f2画G,G_.CL条序col点G 
					,G_.CL条序艹线画G,G_.CL条序LL2f2线画G,G_.CL条序col线G 
					,G_.CL条序艹乛画G ,G_.CL条序LL4f2乛画G,G_.CL条序col乛G	

					,byref(G_.艹丷画G),G_.CLL4f4丷画G 
					,G_.CL条序艹线画G,G_.CL条序LL2f2线画G[0] ,G_.CL条序col线G[0] 
					,byref(G_.艹Λ画G),G_.CLL5f4Λ画G 
					,byref(G_.艹厸画G),G_.CL面序Lnf4厸画G 
					);
					
		# PTL亖亖(G_.CL条序LL2f2线画G[0]);PTL亖亖(G_.CL条序LL2f2线画G[1]);	#====点====================================
		# print("G_.CL条序艹点画G==",*G_.CL条序艹点画G);
		# print("G_.CL条序艹乛画G==",*G_.CL条序艹乛画G);
		# print("LG.画丷==",LG.画丷,G_.艹丷画G.value);
		for i in range(G_.CL条序艹点画G.__len__()):
			if(-1<G_.CL条序艹点画G[i]):
				# print("G_.CL条序L点序f2画G[ξ条]==",i,G_.CL条序艹点画G[i],*G_.CL条序L点序f2画G[i][0],*G_.CL条序L点序f2画G[i][1]);
				# if(LG.画点):
				ΔΔ画n点(G_,i);
				#----cf箭头----------------------------------------------
				# print("G_.CL条序LL4f2乛画G[ξ条]==",i,*G_.CL条序LL4f2乛画G[i][0][0],*G_.CL条序LL4f2乛画G[i][0][1]);
				# if(LG.画乛):
				ΔΔ画n乛(G_,i);
				#ΔΔ画n线(G_,i);
			else:
				break;
		#---- 一一 --------------------------
		if(LG.画丷):
			Δ画n丷(G_);
		if(LG.画线):
			ΔΔ画n线(G_,0);
		if(LG.画Λ):
			Δ画nΛ(G_);#print("Λ value==",G_.艹Λ画G.value);
		
	
	
	if(G_.b画面G):
		#----厶 三角形--------------------------
		艹=G_.艹厶画G.value;#print("G_.艹厶画G.value==",艹);
		for i in range(艹):
			G_.CL4f4=G_.CL面序L4f4厶画G[i];
			if(G_.CL4f4[0][0]==0 and G_.CL4f4[1][1]==0):
				continue;
			Δ画3线(G_.CL4f4);#print("G_.CL4f4==",*G_.CL4f4[0],*G_.CL4f4[1],*G_.CL4f4[2],*G_.CL4f4[3]);
		#----囗 四边形--------------------------
		艹=G_.艹囗画G.value;#print("G_.艹丷画G.value==",G_.艹丷画G.value);
		for i in range(艹):
			G_.CL5f4=G_.CL面序L5f4囗画G[i];
			if(G_.CL5f4[0][0]==0 and G_.CL5f4[1][1]==0):
				continue;
			Δ画4线(G_.CL5f4);
			# print("G_.CL5f4==",*G_.CL5f4[0],*G_.CL5f4[1],*G_.CL5f4[2],*G_.CL5f4[3]);
	#----厸 --------------------------
	if(LG.画厶):
		# for i,G_.CL5f4 in enumerate(G_.CL面序Lnf4厸画G):
		艹=G_.艹厸画G.value;
		for i in range(艹):
			G_.CL5f4=G_.CL面序Lnf4厸画G[i];
			if(G_.CL5f4[4][0]==0 and G_.CL5f4[4][1]==0 ):
				Δ画1厶(G_.CL5f4);
			else:
				Δ画1囗(G_.CL5f4);
			#print("G_.CL5f4==",*G_.CL5f4[0],*G_.CL5f4[1],*G_.CL5f4[2],*G_.CL5f4[3],*G_.CL5f4[4]);	

	#====多弓====================================
	"""
	if(G_.画弓):			 
		G_.卍dll.dll.下上画弓(
																G_.CL条序艹点画G[0],G_.CL条序L点序f2画G \
															,G_.CL条序艹线画G[0],G_.CL条序LL2f2线画G \
															,G_.CL条序艹乛画G[0][0],G_.CL条序LL4f2乛画G \
															);
		for i in range(G_.ciSize弓G.value):
			pass
	"""

	#----画字------------------------------------------------------
	if(0<G_.i画字):
		blf.size(0, 15, 80);
		G_.卍dll.dll.凸画字(byref(G_.艹字画G),G_.CLL2f4丅字画G,G_.CLs64字G,G_.i画字==1);#1:3d ,2:是2d
		艹=G_.艹字画G.value;#print("凸画字 ==",艹);
		for i in range(艹):
			G_.CL2f4=G_.CLL2f4丅字画G[i];#print("G_.CL2f4==",*G_.CL2f4[0], G_.CLs64字G[i].value);
			if(G_.CL2f4[0][0]==0 and G_.CL2f4[1][1]==0):
				continue;
			blf.color(0,*G_.CL2f4[1]);
			blf.position(0,G_.CL2f4[0][0], G_.CL2f4[0][1], 0);#(fontid, x, y, z)
			blf.draw(0, G_.CLs64字G[ i].value);
			# print("dr==",G_.CLs64字G[ i].value);
			
	bgl.glDisable(bgl.GL_BLEND);


#////3D///////////////////////////////////
class 卐画3dlib卐Operator(bpy.types.Operator):
	bl_idname = "op.draw_3d_lib"
	bl_label = "draw_3d_lib"
	bl_description = "draw_3d_lib"
	
	bp显示:BoolProperty(default=False);
	ip画字:IntProperty(default=0);#1:3d ,2:是2d
	bp画面:BoolProperty(default=False);bp画丷:BoolProperty(default=False);bp画Λ:BoolProperty(default=False);
	bp画db:BoolProperty(default=False);bp画弓:BoolProperty(default=False);bp画m:BoolProperty(default=False);
	bp灬:BoolProperty(default=False);

	#========================================
	def 十十乚(self, context, event,G_):
		G_.i画字=self.ip画字;G_.b画面G=self.bp画面;G_.画丷=self.bp画丷;G_.画Λ=self.bp画Λ;G_.画弓=self.bp画弓;G_.画m=self.bp画m;
		#----增加乚----------------------------------------------------
		print("画3dlib self.bp显示==",self.bp显示,G_.卍dll.dll,G_.卍dll.乚3d);
		if(self.bp显示):
			if(G_.卍dll.dll):
				if(G_.卍dll.dll.b凸凷rv3d(c_void_p(context.as_pointer()),True)==False):
					print("★★★★	 no 3d windows==",);
					self.report({"ERROR"},"★★★★	 no 3d windows==");#"INFO" "ERROR" "DEBUG" "WARNING"
					return {"FINISHED"};
				G_.卍dll.dll.凸刷新窗口(c_void_p(context.as_pointer()));
			else:
				# self.report({"WARNING"},"PYLIB G_.卍dll.dll==None");#"INFO" "ERROR" "DEBUG" "WARNING"
				print("★★★★ 画3dlib G_.卍dll.dll==",G_.卍dll.dll);
				self.report({"ERROR"},"!!!画3dlib G_.卍dll.dll==None");#"INFO" "ERROR" "DEBUG" "WARNING"
				return {"FINISHED"};
			if(G_.卍dll.乚3d==None):
				# self.G=G_;
				G_.卍dll.乚3d = bpy.types.SpaceView3D.draw_handler_add(画3d,(self, context,G_), 'WINDOW', 'POST_PIXEL');#POST_VIEW(无画),POST_PIXEL(画)
				# G_.regionG=c_void_p(context.region.as_pointer());G_.view3dG=c_void_p( context.space_data.region_3d.as_pointer());
				print("+++++add draw乚 3dLIB	 ,G_.画弓==",G_.画弓);#PTLfn亖亖(2,3,G_.CL条序LL2f2线画G[0]);PTLfn亖亖(2,3,G_.CL条序LL2f2线画G[1]);
			# if(G_.area3dG):
				# G_.area3dG.tag_redraw();
			
		#----删除乚--------------------------
		else:
			if(G_.卍dll.乚3d):
				if(G_.卍dll.dll):	 
					G_.卍dll.dll.凸〇画();
					G_.卍dll.dll.凸刷新窗口(c_void_p(context.as_pointer()));
					G_.卍dll.dll.凸画3d(False);	
				# if(G_.area3dG):
					# G_.area3dG.tag_redraw();
				
				self.bp显示=False;
			# if(self.bp灬):
			# if(G_.CL条序L点序f2画G or G_.CL条序LL2f2线画G or G_.卍dll.乚3d):
				灬gl乚(G_);灬gl数据(G_);	
				print("----clear draw乚 3dLIB",self.bp灬,G_.卍dll.dll);		

	#----3d --------------------------
	""" ●● 怀疑是这个 造成crash
	def __del__(self):
		if(self.乚3d):
			self.bp显示=False;
			# if(self.bp灬):
			print("__del__ 3d  G_.卍dll.dll==",self.bp灬,G_.卍dll.dll);
			灬gl乚(self.乚3d);灬gl数据(G_);G_.卍dll.dll.凸画3d(False); 
	"""
bpy.utils.register_class(卐画3dlib卐Operator);
  

#//// 2D ////////////////////////////////////////
def drawText(text, x, y, font_id = 0, align = "LEFT", verticalAlignment = "BASELINE", size = 12, color = (1, 1, 1, 1)):
	text = str(text)
	blf.size(font_id, size, int(dpi))
	blf.color(font_id, *color)

	if align == "LEFT" and verticalAlignment == "BASELINE":
		blf.position(font_id, x, y, 0)
	else:
		width, height = blf.dimensions(font_id, text)
		newX, newY = x, y
		if align == "RIGHT": newX -= width
		elif align == "CENTER": newX -= width / 2
		if verticalAlignment == "CENTER": newY -= blf.dimensions(font_id, "x")[1] * 0.75

		blf.position(font_id, newX, newY, 0)

	blf.draw(font_id, text)

	
def 画线2d(self,context,G_):#L2v丅
	bgl.glEnable(bgl.GL_BLEND);
	# rgba=G_.蓝; 
	bgl.glPointSize(6);
	bgl.glLineWidth(4); 
	# text =str("DJS");font_id=0;blf.size(font_id,12,72);color=(1,1,1,1);blf.color(font_id,*color);
	# if(G_.cvpC==None):
		# G_.cvpC=c_void_p(context.as_pointer())
	G_.卍dll.dll.凸画线2d(G_.cvpC,byref(G_.艹线画2dG),G_.CLL3i4线画2dG);	 
	艹=G_.艹线画2dG.value;#print("DRAW 艹==",艹);
	for i in range(艹):
		G_.CL3f4=G_.CLL3i4线画2dG[i];#print("G_.CL3f4==",*G_.CL3f4[0]);
		if(G_.CL3f4[0][0]==0 and G_.CL3f4[1][1]==0):
			continue;
		Δ画1线(G_.CL3f4);#print("G_.CL3f4 node==",*G_.CL3f4[0],*G_.CL3f4[1],*G_.CL3f4[2]);
		# blf.position(font_id, G_.CL3f4[0][0], G_.CL3f4[0][1], 0);
	# G_.CL3f4=[[0,0,0,0],[0,0,0,0],[0,0,0,0]];
	# G_.CL3f4[0][0]=LG.i64;G_.CL3f4[0][1]=LG.i64; G_.CL3f4[1][0]=LG.i64;G_.CL3f4[1][1]=120;
	# G_.CL3f4[2]=(0,1,1,1);
	# Δ画1线(G_.CL3f4);
	# blf.position(font_id,LG.i64,LG.i64,0);blf.draw(font_id,text);#画字
	if(G_.b画图标G):
		for n角色 in G_.Mn角色冫ipG:
			Δ画1图LIB(n角色.fvp2图标位,LG);
		
	bgl.glDisable(bgl.GL_BLEND);
	# bgl.glEnd();
	
#==================================================
# E:\blender-2.80\addons\NodePreview\display.py
class 卐图标:
	def __init__(self):
		self.texture_id = 0
		self.texture_initialized = False
		self.buffer = None
		self.width = -1
		self.height = -1
		self.channel_count = -1
		self.text = ""

	def load_texture(self):
		"""Has to be called from the main thread!"""
		texture = bgl.Buffer(bgl.GL_INT, 1)
		bgl.glGenTextures(1, texture)
		self.texture_id = texture[0]

		bgl.glActiveTexture(bgl.GL_TEXTURE0)
		bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.texture_id)
		# Note: I always use bgl.GL_RGBA8 and bgl.GL_RGBA (4 channels).
		# According to the OpenGL specification, most graphics drivers transform anything
		# with less channels than 4 into GL_RGBA8. Unfortunately, this conversion seems
		# to be buggy (e.g. on my Nvidia driver), so I'm not using less channels than 4,
		# even though I would like to (to save memory).
		bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, bgl.GL_RGBA8, self.width, self.height,
						 0, bgl.GL_RGBA, bgl.GL_BYTE, self.buffer)

		edge_mode = bgl.GL_CLAMP_TO_EDGE
		bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_WRAP_S, edge_mode)
		bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_WRAP_T, edge_mode)

		interpolation_mode = bgl.GL_LINEAR
		bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, interpolation_mode)
		bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, interpolation_mode)

		bgl.glBindTexture(bgl.GL_TEXTURE_2D, NULL)
		self.texture_initialized = True


	def draw(self, bottom_left, bottom_right, top_right, top_left, scaled_zoom):
		bgl.glActiveTexture(bgl.GL_TEXTURE0)
		bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.texture_id)

		shader.bind()
		shader.uniform_int("image", 0)
		shader.uniform_int("gamma_correct", bpy.app.version >= (2, 91, 0))

		batch = batch_for_shader(
			shader, 'TRI_FAN',
			{
				"pos": (bottom_left, bottom_right, top_right, top_left),
				"texCoord": ((0, 1), (1, 1), (1, 0), (0, 0)),  # Note: Mirrored along y axis
			},
		)
		batch.draw(shader)

		self._draw_text(bottom_left, scaled_zoom)


	def _draw_text(self, position, scaled_zoom):
		if not self.text:
			return

		draw_text(self.text, position, 10, scaled_zoom)
		
def Δ画1图LIB(fvp2图标位,G_):
	if(G_.imageG==None):
		print("!!!G_.imageG==",G_.imageG);
		return;
	
	if(G_.imageG.gl_load()):
		raise Exception();return;#Load the image into OpenGL graphics memory #●●可能是这个crash
	#bgl.glColor4f(0.0, 0.0, 1.0, 0.5);#颜色
	#------ 纹理贴图 ---------
	#bgl.glEnable(bgl.GL_BLEND);
	# Has to be called from the main thread!
	texture = bgl.Buffer(bgl.GL_INT, 1)
	bgl.glGenTextures(1, texture)
	# self.texture_id = texture[0]
	self.texture_id = texture[0];
	
	bgl.glActiveTexture(bgl.GL_TEXTURE0);
	bgl.glBindTexture(bgl.GL_TEXTURE_2D, G_.imageG.bindcode);#如果bindcode[1]是白色
	bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, bgl.GL_RGBA8, self.width, self.height,
										0, bgl.GL_RGBA, bgl.GL_BYTE, self.buffer)
						 
	bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST);#GL_LINEAR seems to be used in Blender for background images 设置纹理参数 
	#bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST); #设置纹理过滤器#●似乎无用
	bgl.glBlendFunc(bgl.GL_SRC_ALPHA, bgl.GL_ONE_MINUS_SRC_ALPHA);# 设置混色函数取得半透明效果, 设置混合系数#函数来指定混合功能的源因子和目标因子,以后绘制的所有物体都是采用这个源因子和目标因子,除非再次使用glBlendFunc函数重新指定.
	#----画图像大小--------------------------
	# bgl.glColor4f(1,1,1,1);#白色
	# bgl.glBegin(bgl.GL_QUADS);
	shader图.bind();
	shader图.uniform_int("image", 0);   
	shader图.uniform_int("gamma_correct",(2, 91, 0)<= bpy.app.version )
	batch_for_shader(
		shader图, 'TRI_FAN',
			{ 
			"pos": ((fvp2图标位[0], fvp2图标位[1]), (fvp2图标位[0]  + G_.i图标高宽G , fvp2图标位[1]), (fvp2图标位[0]  + G_.i图标高宽G, fvp2图标位[1] + G_.i图标高宽G),  (fvp2图标位[0] , fvp2图标位[1] + G_.i图标高宽G)),#→↑←
			"texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
			},
	).draw(shader图);

	# G_.imageG.gl_free();
	
#====E:\blender\3.4\scripts\modules\gpu_extras\presets.py=============================
def draw_texture_2d(texture, position, width, height):
	"""
	Draw a 2d texture.

	:arg texture: GPUTexture to draw (e.g. gpu.texture.from_image(image) for :class:`bpy.types.Image`).
	:type texture: :class:`gpu.types.GPUTexture`
	:arg position: Position of the lower left corner.
	:type position: 2D Vector
	:arg width: Width of the image when drawn (not necessarily the original width of the texture).
	:type width: float
	:arg height: Height of the image when drawn.
	:type height: float
	"""
	coords = ((0, 0), (1, 0), (1, 1), (0, 1))

	shader = gpu.shader.from_builtin('IMAGE')
	batch = batch_for_shader(
		shader, 'TRI_FAN',
		{"pos": coords, "texCoord": coords},
	)

	with gpu.matrix.push_pop():
		gpu.matrix.translate(position)
		gpu.matrix.scale((width, height))

		shader = gpu.shader.from_builtin('IMAGE')

		if isinstance(texture, int):#用来判断一个函数是否是一个已知的类型，类似 type()。
			# Call the legacy bgl to not break the existing API
			bgl.glActiveTexture(bgl.GL_TEXTURE0)
			bgl.glBindTexture(bgl.GL_TEXTURE_2D, texture)
			shader.uniform_int("image", 0)
		else:
			shader.uniform_sampler("image", texture)

		batch.draw(shader)
#----G_.CL5f4 ■------------------------------------
font_id = 0;
def Δ画1囗LIB( x, y,宽):
	print("DRAW 囗==",x,y);
	G_.CL5f4[0][0]=x;G_.CL5f4[0][1]= y;G_.CL5f4[1][0]=x	 + 宽;G_.CL5f4[1][1]=y;
	G_.CL5f4[2][0]=x+ 宽;G_.CL5f4[2][1]=y + 宽;G_.CL5f4[3][0]=x;G_.CL5f4[3][1]=y + 宽;
	
	Δ画1囗(G_.CL5f4);

#========================================
def Δ画1标LIB( x, y, i条目宽per,b文件夹,Vima图标s名s路径库sblend,G_):
	#print("DRAW greenland==",);
	i图标边缘X = 4;i图标边缘Y = 4;i字体边缘Y = 6;
	# print("G_.imageG==",G_.imageG);
	# if (G_.b高亮G):
		# bgl.glColor4f(0.6,  0.6, 0.0, 0.5);#高亮
	# else:
		# bgl.glColor4f(0.5, 0.5, 0.5, 0.3);
	#------------------------------
	# bgl.glRectf(x, y, x + i条目宽per, y + G_.i条目高宽G);#绘制1个矩形ㄴㄱ ,也就是图标的背景色
	if(b文件夹):
		s字=Vima图标s名s路径库sblend;#s文件夹名
		if(G_.imageG==None):
			print("!!!G_.imageG==",G_.imageG);
			return;
	else:
		s字 = Vima图标s名s路径库sblend[1];
	G_.imageG= Vima图标s名s路径库sblend[0];
	# print("G_.imageG==",G_.imageG,type(G_.imageG)== str);
	# print("G_.imageG2==",G_.imageG.has_data,);
	# if(type(G_.imageG)== str):
		# print("Vima图标s名s路径库sblend==",Vima图标s名s路径库sblend);
	if(G_.imageG):
		if(type(G_.imageG)!=str):
			# print("is_evaluated==",G_.imageG.users);
			if(G_.imageG.gl_load()):
				print("!!fail load image==",G_.imageG);
				raise Exception();return;
			# print("DRAW 1 image==",);
			#------ 纹理贴图 ---------
			#bgl.glEnable(bgl.GL_BLEND);
			bgl.glBindTexture(bgl.GL_TEXTURE_2D, G_.imageG.bindcode);#如果bindcode[1]是白色
			bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST);#GL_LINEAR seems to be used in Blender for background images 设置纹理参数 
			#bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST); #设置纹理过滤器#●似乎无用
			bgl.glBlendFunc(bgl.GL_SRC_ALPHA, bgl.GL_ONE_MINUS_SRC_ALPHA);# 设置混色函数取得半透明效果, 设置混合系数#函数来指定混合功能的源因子和目标因子,以后绘制的所有物体都是采用这个源因子和目标因子,除非再次使用glBlendFunc函数重新指定.

			shader图.bind()
			shader图.uniform_int("image", 0);#print("dir.batch_for_shader==",dir(batch_for_shader));
			batch_for_shader(
				shader图, 'TRI_FAN',
					{ 
					"pos": ((x, y), (x	+ G_.i图标高宽G , y), (x  + G_.i图标高宽G, y + G_.i图标高宽G),	(x , y + G_.i图标高宽G)),#→↑←
					"texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
					},
			).draw(shader图);
			G_.imageG.gl_free();
		
	else:
		print("!!! draw one image==",G_.imageG);
		# self.report({"ERROR"},"image load error");#"INFO" "ERROR" "DEBUG" "WARNING"
	#----画数--------------------------
	
	#blf.position(font_id, x + i图标边缘X + G_.i图标高宽G + i字体边缘Y, y + G_.i图标高宽G * 0.5 - 0.25 * G_.i字体高G, 0);
	blf.position(font_id, x + i图标边缘X + i字体边缘Y, y+G_.i图标高宽G , 0);
	blf.size(font_id, G_.i字体高G, G_.i字体宽G);
	blf.draw(font_id, s字);
	
#==================================================
class 卐画2dnodelib卐Operator(bpy.types.Operator):
	bl_idname = "op.draw_line_2d_node_lib"
	bl_label = "draw_line_2d_node_lib"
	bl_description = "draw_line_2d_node_lib"

	bp显示:BoolProperty(default=False);
	bp画丷:BoolProperty(default=False);
	bp画db:BoolProperty(default=False);
	bp画图标:BoolProperty(default=False);
	bp灬:BoolProperty(default=False);
	sp界面:StringProperty(name='',description='',default='');
	乚2d=None;
	#=================================================
	def 十十乚(self, context, event,G_):
		G_.b画图标G=self.bp画图标;
		#----增加手柄-----------------------------------------------------
		print("画2dnodelib ==",self.bp显示,G_.卍dll.乚2d,G_.CL条序LL2f2线画G,self.bp灬);
		if(self.bp显示):
			if(G_.卍dll.dll):
				if(G_.卍dll.dll.b凸凷v2d节点(c_void_p(context.as_pointer()),True)==False):
					# LG.b丌播放=True;
					return;
				# else:
					# LG.b丌播放=False;
			else:
				# self.report({"WARNING"},"PYLIB G_.卍dll.dll==None");#"INFO" "ERROR" "DEBUG" "WARNING"
				print("!!!!!!!! 卐画2dnodelib卐Operator G_.卍dll.dll==",G_.卍dll.dll);return;
				
			if(G_.卍dll.乚2d==None):
				G_.卍dll.乚2d = bpy.types.SpaceNodeEditor.draw_handler_add(画线2d,(self, context,G_), 'WINDOW', 'POST_PIXEL');
				#self.乚字 = bpy.types.SpaceNodeEditor.draw_handler_add(ΔΔ画字,(self, context), 'WINDOW', 'POST_PIXEL');
				print("++++ 画2dnodelib",);
		else:
			if(G_.卍dll.乚2d):
				if(G_.卍dll.dll):   
					G_.卍dll.dll.凸刷新窗口node(c_void_p(context.as_pointer()));
					# G_.卍dll.dll.凸〇画(-1,False);					
				self.bp显示=False;
				# if(self.bp灬):
				# if(G_.CL条序LL2f2线画G):
				灬gl乚2d(G_);灬gl数据2d(G_);	  
				print("----clear 画2dnodelib",self.bp灬);		

	#----2d--------------------------
	"""
	def __del__(self):
		# try:
		if(乚2d ):
			print("----__del__ 2d text",);
			self.bp显示=False;灬gl乚(G_);灬gl数据(G_);
		# except:pass;	 
	"""
bpy.utils.register_class(卐画2dnodelib卐Operator);
#/////////////////////////////////////////
# def 画2dLIB(bp显示,bp画图标=False,bp灬=True,sp界面="NODE_EDITOR"):#"NODE_EDITOR","IMAGE_EDITOR","UV"
	# bpy.ops.op.draw_line_2d_node_lib("INVOKE_DEFAULT",bp显示=bp显示,bp灬=bp灬,sp界面=sp界面);
	
def 画3dLIB(bp显示,bp画面=True,bp画丷=False,bp画弓=False,ip画字=1,bp灬=True):
	bpy.ops.op.draw_3d_lib("INVOKE_DEFAULT",bp显示=bp显示,bp画弓=bp画弓,bp画面=bp画面,bp画丷=bp画丷,ip画字=ip画字);#bp画面=bp画面,,bp灬=bp灬
"""
def 更新画(DLL__):
	if(DLL__):
		if(G_.CL条序LL4f2乛画G==None):
			G_.CL条序LL4f2乛画G=(c_float*3*4*LG.i64*5)();
		if(G_.CL条序L点序f2画G==None):
			G_.CL条序LL2f2线画G=(c_float*3*2*LG.i64*5)();
		DLL__.更新画(G_.CL条序LL4f2乛画G,G_.CL条序LL2f2线画G);
"""

def 初始丶乚画(G_,b画面=False,b画丷=False,b画Λ=False,b画字=False,b画弓=False,b画2d=False \
								,L2条数丶iSize点=(10,LG.i64),L2条数丶iSize线=(10,LG.i64),L2条数丶iSize乛=(10,LG.i64) \
								,iSize丷=LG.i32,iSizeΛ=LG.i32,iSize厶=LG.i32,iSize囗=LG.i32,iSize厸=10 ,iSize字=LG.i32 \
								,iSize线2d=LG.i64 \
								,iSize弓=LG.i32):
	if(G_.CL条序L点序f2画G==None or G_.CL条序L点序f2画G[0].__len__()<L2条数丶iSize点[0]):
		py_叵画(G,context.scene,G_,b画面,b画丷,b画Λ,b画字,b画弓,b画2d \
									,L2条数丶iSize点,L2条数丶iSize线,L2条数丶iSize乛 \
									,iSize丷,iSizeΛ,iSize厶,iSize囗,iSize厸 ,iSize字 \
									,iSize线2d \
									,iSize弓);
	
	画3dLIB(G_,True,b画面,b画丷,b画弓,b画字,ip画字=1);
	
	
#////面/////////////////////////////////////
def Δ画2d面LIB(self, context,G_):
	bgl.glBegin(bgl.GL_QUADS);#GL_POLYGON
	#	 0┌━┐1☐☐☐☐☐☐☐☐☐
	# ☐┃┼┃☐☐☐☐☐☐☐☐☐
	#	 3└━┘2☐☐☐☐☐☐☐☐☐
	bgl.glColor3f(*G_.t3青LG);
	if(G_.b高亮G):
		b已经设置青=False;
		for i,f3画 in enumerate(G_.CL面序f3画LG):
			if(i==G_.i高亮ξG):
				bgl.glColor3f(*G_.t3橙LG);b已经设置青=False;
			elif(b已经设置青==False):
				bgl.glColor3f(*G_.t3青LG);b已经设置青=True;
			G_.v丅G.x=f3画[0];G_.v丅G.y=f3画[1];G_.v丅G.z=f3画[2];
			G_.f2屏丅G= view3d_utils.location_3d_to_region_2d(context.region, context.space_data.region_3d,G_.v丅G);
			G_.CL面序L4f2屏画LG[i][0][0]=G_.f2屏丅G[0]-G_.i缩放LG;G_.CL面序L4f2屏画LG[i][0][1]=G_.f2屏丅G[1]+G_.i缩放LG;
			G_.CL面序L4f2屏画LG[i][1][0]=G_.f2屏丅G[0]+G_.i缩放LG;G_.CL面序L4f2屏画LG[i][1][1]=G_.f2屏丅G[1]+G_.i缩放LG;
			G_.CL面序L4f2屏画LG[i][2][0]=G_.f2屏丅G[0]+G_.i缩放LG;G_.CL面序L4f2屏画LG[i][2][1]=G_.f2屏丅G[1]-G_.i缩放LG;
			G_.CL面序L4f2屏画LG[i][3][0]=G_.f2屏丅G[0]-G_.i缩放LG;G_.CL面序L4f2屏画LG[i][3][1]=G_.f2屏丅G[1]-G_.i缩放LG;
			bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][0]);bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][1]);bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][2]);bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][3]);
			
	else:
		for i,f3画 in enumerate(G_.CL面序f3画LG):
			G_.v丅G.x=f3画[0];G_.v丅G.y=f3画[1];G_.v丅G.z=f3画[2];
			G_.f2屏丅G= view3d_utils.location_3d_to_region_2d(context.region, context.space_data.region_3d,G_.v丅G);
			G_.CL面序L4f2屏画LG[i][0][0]=G_.f2屏丅G[0]-G_.i缩放LG;G_.CL面序L4f2屏画LG[i][0][1]=G_.f2屏丅G[1]+G_.i缩放LG;
			G_.CL面序L4f2屏画LG[i][1][0]=G_.f2屏丅G[0]+G_.i缩放LG;G_.CL面序L4f2屏画LG[i][1][1]=G_.f2屏丅G[1]+G_.i缩放LG;
			G_.CL面序L4f2屏画LG[i][2][0]=G_.f2屏丅G[0]+G_.i缩放LG;G_.CL面序L4f2屏画LG[i][2][1]=G_.f2屏丅G[1]-G_.i缩放LG;
			G_.CL面序L4f2屏画LG[i][3][0]=G_.f2屏丅G[0]-G_.i缩放LG;G_.CL面序L4f2屏画LG[i][3][1]=G_.f2屏丅G[1]-G_.i缩放LG;
			bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][0]);bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][1]);bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][2]);bgl.glVertex2f(*G_.CL面序L4f2屏画LG[i][3]);
			#print("dr==",*G_.CL面序L4f2屏画LG[i][0],*G_.CL面序L4f2屏画LG[i][1]);
	bgl.glDisable(bgl.GL_BLEND);
	# bgl.glEnd();

class 卐画2d面lib卐Operator(bpy.types.Operator):
	bl_idname = "op.draw_2d_face_lib"
	bl_label = "draw_2d_face_lib"
	bl_description = "draw_2d_face_lib"
	
	bp显示:BoolProperty(default=False);
	#==============================================================
	def invoke(self, context, event):
		print("draw 2d face invoke==",);
		#----增加乚------------------------------------------------
		if(self.bp显示):
			if(G_.乚2d面==None):
				G_.乚2d面 = bpy.types.SpaceView3D.draw_handler_add(Δ画2d面LIB,(self, context,G_), 'WINDOW', 'POST_PIXEL');#POST_VIEW(无画),POST_PIXEL(画)
				print("+++add handle 2dface",);
		else:
			if(G_.乚2d面):
				bpy.types.SpaceView3D.draw_handler_remove(G_.乚2d面, 'WINDOW');G_.乚2d面=None;Δ清除gl数据LIB();
		return {"FINISHED"};
	
	"""
	def __del__(self):
		try:
			if(G_.乚2d面):
				bpy.types.SpaceView3D.draw_handler_remove(G_.乚2d面 , 'WINDOW');G_.乚2d面=None;self.bp显示=False;Δ清除gl数据LIB();
		except:pass;
	"""
bpy.utils.register_class(卐画2d面lib卐Operator) ;

#///////////////////////////////////////////////
def 刷新界面(area,region):
	screen=bpy.context.screen;
	if(area):
		for a in screen.areas:
			if(a.type==area):#EMPTY", "VIEW_3D", "TIMELINE", "GRAPH_EDITOR", "DOPESHEET_EDITOR", "NLA_EDITOR", "IMAGE_EDITOR", "SEQUENCE_EDITOR", "CLIP_EDITOR", "TEXT_EDITOR", "NODE_EDITOR", "LOGIC_EDITOR", "PROPERTIES", "OUTLINER", "USER_PREFERENCES", "INFO", "FILE_BROWSER", "CONSOLE"
				#a.tag_redraw();#■■这个能刷新所有 region画面
				if(region):
					for r in a.regions:#WINDOW", "HEADER", "CHANNELS", "TEMPORARY", "UI", "TOOLS", "TOOL_PROPS", "PREVIEW
						if(r.type==region):
							r.tag_redraw();
							break;
					break;
			#for s in a.spaces:
				#if(s.type=="PROPERTIES"):
					#print(s)
					#s.context=s模式;#["SCENE", "RENDER", "RENDER_LAYER", "WORLD", "OBJECT", "CONSTRAINT", "MODIFIER", "DATA", "BONE", "BONE_CONSTRAINT", "MATERIAL", "TEXTURE", "PARTICLES", "PHYSICS"]
	print("refresh~~",area,region);
#刷新界面("VIEW_3D","WINDOW");
#///////////////////////////////////////////
def Δ切换到菜单LIB(s模式):
	# if(s上次模式==s模式):
		# print("IS LAST TIME",s上次模式,s模式);return ;
	screen=bpy.context.screen;
	for a in screen.areas:
		if(a.type=="PROPERTIES"):
			for s in a.spaces:
				if(s.type=="PROPERTIES"):
					try:
						s.context=s模式;
					except:pass;
					# return s模式;
					break;
					#["SCENE", "RENDER", "RENDER_LAYER", "WORLD", "OBJECT", "CONSTRAINT", "MODIFIER", "DATA", "BONE", "BONE_CONSTRAINT", "MATERIAL", "TEXTURE", "PARTICLES", "PHYSICS"]
			break;

def Δ切换到指定spaceLIB(area类型,space类型,s模式):
	screen=bpy.context.screen;
	for a in screen.areas:
		if(a.type==area类型):#"EMPTY", "VIEW_3D", "TIMELINE", "GRAPH_EDITOR", "DOPESHEET_EDITOR", "NLA_EDITOR", "IMAGE_EDITOR", "SEQUENCE_EDITOR", "CLIP_EDITOR", "TEXT_EDITOR", "NODE_EDITOR", "LOGIC_EDITOR", "PROPERTIES", "OUTLINER", "USER_PREFERENCES", "INFO", "FILE_BROWSER", "CONSOLE"
		 #print(a.type)
			for s in a.spaces:
				if(s.type==space类型):#
					#print(s)
					s.context=s模式;
					break;#["SCENE", "RENDER", "RENDER_LAYER", "WORLD", "OBJECT", "CONSTRAINT", "MODIFIER", "DATA", "BONE", "BONE_CONSTRAINT", "MATERIAL", "TEXTURE", "PARTICLES", "PHYSICS"]
			break;

"""
def Δ仌画LIB(self,context):
		if(self.bp画):
			if( G_.CL条序L点序f2画G==None):
				py_叵画(G,context.scene,b画面=G_.b画面,b画丷=G_.b画丷,b画Λ=G_.b画Λ,b画字=G_.b画字,b画弓=G_.画弓,b画2d=G_.b画2d \
										,L2条数丶iSize点=G_.L2条数丶iSize点,L2条数丶iSize线=G_.L2条数丶iSize线,L2条数丶iSize乛=G_.L2条数丶iSize乛,iSize丷=G_.iSize丷,iSize字=G_.iSize字);
			画3dLIB(bp显示=True,bp画面=G_.b画面,bp画数=G_.b画字,ip画字=1,bp灬=False);			 
		else:
			画3dLIB(bp显示=False,bp画面=False,ip画字=1,bp灬=True);
"""

#////end////end////end////end////end////end////end////end////









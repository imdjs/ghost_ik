
import bpy,sys,os
from mathutils import*
from ctypes import*
from mathutils import Vector,Quaternion
#------------------------------------------------------------
path目录PYLIB父级 =os.path.abspath(os.path.join(os.path.dirname(__file__),".."));#父级目录 
sPYLIB父级=os.path.basename(path目录PYLIB父级);
path目录MUT = os.path.dirname(__file__); #本py文件所在目录
文件夹此=os.path.basename(path目录MUT);  #IMDJS_NodeTree

fileCG="E:\blender\BlenderLib\CLIB64.dll"
s链接G='';
s200G="012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678.0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789";
# s200G="imdjs";
#///////////////////////////////////////////
#path目录PYLIB父级 =os.path.abspath(os.path.join(os.path.dirname(__file__),".."));#父级目录 
#sPYLIB父级=os.path.basename(path目录PYLIB父级);
# from .LG import sPYLIB父级,LG;
#print("_____pathPYLIB_UP==",path目录PYLIB父级,sPYLIB父级);
sPYLIB父级__=sPYLIB父级+".PYLIB_"+sPYLIB父级;#==IMDJS.nodes.PYLIB_IMDJS_nodes 
Ls模块selfG=[sPYLIB父级__+".PYLIB_main",sPYLIB父级__+".PYLIB_math",sPYLIB父级__+".PYLIB_object",sPYLIB父级__+".PYLIB_mesh",sPYLIB父级__+".PYLIB_modifier",sPYLIB父级__+".PYLIB_module",sPYLIB父级__+".PYLIB_armature",sPYLIB父级__+".PYLIB_attribute",sPYLIB父级__+".PYLIB_algorithm",sPYLIB父级__+".PYLIB_string",sPYLIB父级__+".PYLIB_find",sPYLIB父级__+".PYLIB_operator",sPYLIB父级__+".PYLIB_particle",sPYLIB父级__+".PYLIB_print",sPYLIB父级__+".PYLIB_transform",sPYLIB父级__+".PYLIB_draw",sPYLIB父级__+".PYLIB_curve",sPYLIB父级__+".PYLIB_image",sPYLIB父级__+".PYLIB_weight",sPYLIB父级__+".PYLIB_ui",sPYLIB父级+".LG",sPYLIB父级__+""];

Ls模块LIB=["PYLIB.PYLIB_main","PYLIB.PYLIB_animation","PYLIB.PYLIB_math","PYLIB.PYLIB_object","PYLIB.PYLIB_transform","PYLIB.PYLIB_mesh","PYLIB.PYLIB_modifier","PYLIB.PYLIB_module","PYLIB.PYLIB_armature","PYLIB.PYLIB_attribute","PYLIB.PYLIB_algorithm","PYLIB.PYLIB_string","PYLIB.PYLIB_find","PYLIB.PYLIB_operator","PYLIB.PYLIB_print","PYLIB.PYLIB_draw","PYLIB.PYLIB_curve","PYLIB.PYLIB_image","PYLIB.PYLIB_particle","PYLIB.PYLIB_weight","PYLIB.PYLIB_ui","PYLIB.LG","PYLIB"];

Ls类型物体网格弓=["MESH","CURVE","LATTICE"];
Ls类型物体有DATA=["MESH","CURVE","LATTICE","FONT","CAMERA","META","LIGHT","SPEAKER"];
Ls类型非MESH有DATA=["ARMATURE","CURVE","LATTICE","FONT","CAMERA","META","LIGHT","SPEAKER"];
Ls整浮布字G=["<class 'float'>","<class 'int'>","<class 'string'>","<class 'bool'>"];
Ls列元矢=["<class 'list'>","<class 'tuple'>","<class 'Vector'>","<class 'bpy_prop_array'>","<class 'Euler'>","<class'Quaternion'>"];
Ls忽略键=["TYPE","OBJECT_TYPE","ID_NAME","POINT_NUM","L_LATTICE_POINT","BEVEL_OBJECT_NAME","TAPER_OBJECT_NAME","PARENT_NAME","TEXTURE_NAME","SPLINE_TYPE","EDITBONE_PROPERTY","POSEBONE_PROPERTY","BONE_NUM","LAMP_TYPE","CHILDREN","EMPTY_PROPERTY","LATTICE_PROPERTY","CAMERA_PROPERTY","LAMP_PROPERTY","ARMATURE_PROPERTY","META_PROPERTY","CURVE_PROPERTY","SPLINE_PROPERTY","MODIFIER","CONSTRAINT","PARTICLE","OBJECT_PROPERTY","MESH_PROPERTY","","","","",""];


#========================================
class 卐DLL():
	dll=None;乚3d=None;乚2d=None;
	def __init__(self):
		pass;
	def b乙(self,dllpath,dllpath1=None):
		print("乙 dll ==",dllpath,dllpath1,os.path.exists(dllpath),os.path.exists(dllpath1),self.dll);
		if(self.dll==None):
			sc_LG(bpy.context.scene,LG);
			try:
				self.dll=CDLL(dllpath);print("self.dll==",self.dll);
				if(self.dll):
					try:
						self.dll.凸载入scene亖(c_void_p(bpy.context.as_pointer()),LG.b无DEBUG属性);#已经 在 DEF载入SCENE亖 执行
					except:	
						print("★★ 凸载入scene亖== 载入出错 return False;  ",);return False;
					return True;
			except:	
				if(dllpath1 and os.path.exists(dllpath1)):
					self.dll=CDLL(dllpath1);
					if(self.dll):
						try:
							self.dll.凸载入scene亖(c_void_p(bpy.context.as_pointer()),LG.b无DEBUG属性);
						except:	
							print("★★ 凸载入scene亖== 载入出错 return False",);return False;
						return True;
				else:
					print("★ b乙  dllpath1==None, return False;",dllpath1);
					
		return False;
	def 灬(self,b清空=True):
		if(self.dll and self.dll._handle):
			windll.kernel32.FreeLibrary(self.dll._handle);
			self.dll=None;print("灬 dll ==",self.dll);
		if(b清空):
			cls = lambda: os.system('cls');cls();
			
	def __del__(self):
		if(self.dll and self.dll._handle):
			print("一一del dll ==",self.dll);
			windll.kernel32.FreeLibrary(self.dll._handle);	
			
		if(self.乚3d):
			print("一一del 乚3d ==",self.乚3d);
			bpy.types.SpaceView3D.draw_handler_remove(self.乚3d, 'WINDOW');
		if(self.乚2d):
			print("一一del 乚2d ==",self.乚2d);
			bpy.types.SpaceNodeEditor.draw_handler_remove(self.乚2d, 'WINDOW');
		
卍dll=卐DLL();
#========================================
class 卐O:
	o=None;ψ=None;
	def __init__(self,o_=None):
		if(o_!=None):
			self.o=o_;self.ψ=c_void_p(o_.as_pointer());
		else:
			print("★ o_==None",o_);
	def 灬(self):
		self.o=None;self.ψ=None;
	def __del__(self):
		if(self.o):
			self.o=None;self.ψ=None;
#------------------------------
def 卩罒o(o,L卐o骷):
	for o_ in L卐o骷:
		if(o==o_.o):
			return True;
	return False;
	

#------------------------------
dllTEST=None;dllDJS=None;dllMESH=None;#dllSHARE=None;
cvpC=None;cvpSC=None;cvpSP=None;cvpOA=None;cvpOS=None;#cvpVL=None;
oA旧=None;oA=None;scene=None;C=None;Co=None;Cmesh=None;pbA=None;cvpA=None;wm=None;
# dllDRIVER=None;
#----权重--------------------------

#====骨==========================
TYPE_无	=0
#------------------------------
TYPE_TWO孙子	=1
TYPE_SPLINE	=2

TYPE_TWO孙	=3
TYPE_TWO子	=4
TYPE_TWO父	=5
TYPE_TWO爷	=6
#------------------------------
TYPE_物理	=7
TYPE_布料	=8

TYPE_修正骨	=9
#----烘焙--------------------------
MpbL10kc={};#Lpb烘焙=[];
#----高亮--------------------------

b高亮G=False;i高亮ξG=-1;s上次模式G="";
#====view==============================================
ci2当前鼠标屏位G=[0,0];

XD=Vector((1,0,0));YD=Vector((0,1,0));ZD=Vector((0,0,1));下D=Vector((0,0,-1));
v0D=(0,0,0);v1D=(1,1,1);q0D=(1,0,0,0);
#====色=======================================================
黑=(0.0,0.0,0.0,1);白=(1.0,1.0,1.0,1);灰=(0.5,0.5,0.5,1);
浅黑=(0.2,0.2,0.2,1);灰蓝=(0.6,0.6,0.7,1);灰青=(0.5,0.9,0.9,1);

#------------------------------------------------------------
红=(8.0,0.0,0.0,1);橙=(1.0,0.5,0.0,1);浅橙=(1.0,0.8,0.3,1);黄=(1.0, 1.0, 0.0,1);浅黄=(1.0, 1.0, 0.3,1);绿=(0.0,1.0,0.0,1);浅绿=(0.3,1.0,0.3,1);青=(0.0,1.0,1.0,1);浅青=(0.3,0.8,1.0,1);蓝=(0.0,0.0,1.0,1);浅蓝=(0.3,0.3,1.0,1);紫=(1.0,0.0,1.0,1);浅紫=(1.0,0.5,1.0,1);浅红=(1.0,0.5,0.5,1);

深红=(0.5,0.0,0.0,1);深橙=(0.7,0.3,0.0,1);深黄=(0.7, 0.7, 0.0,1);深绿=(0.0,0.5,0.0,1);深青=(0.0,0.7,0.7,1);深蓝=(0.0,0.0,0.5,1);深紫=(0.6,0.0,0.6,1);
#----A--------------------------
红a=(8.0,0.0,0.0,0.2);
#----画线---------------------------------------------------------
i缩放G=4;i显示3dG=-1;
# space品G=None;region品G=None;regionG=None;view3dG=None;area3dG=None;
# area2dG=None;space2dG=None;space3dG=None;region2dG=None;
b画面G=False;画弓=False;画圆=False;画点=False;画线=False;画乛=False;画厶=False;画丷=False;画Λ=False;画m=False;i画字=0;#实时状态
乚2d面G=None;乚字G=None;
s返回值G=None;
b无DEBUG属性=False;
def sc_LG(scene,LG_):
	try:
		LG_.画点=scene.DEBUG.亖画点;LG_.画线=scene.DEBUG.亖画线;LG_.画乛=scene.DEBUG.亖画乛;LG_.画Λ=scene.DEBUG.亖画Λ;LG_.画丷=scene.DEBUG.亖画丷;LG_.画厶=scene.DEBUG.亖画厶;LG_.画m=scene.DEBUG.亖画m;LG_.i画字=scene.DEBUG.亖画字;
		print("sc_LG==",LG_.画点,LG_.画线,LG_.画乛);
	except:
		LG_.b无DEBUG属性=True;
		LG_.画点=True;LG_.画线=True;LG_.画乛=True;LG_.画Λ=True;LG_.画丷=True;LG_.画厶=True;LG_.画m=True;LG_.i画字=True;
		print("sc_LG.b无DEBUG属性==",LG_.画点,LG_.画线,LG_.画乛,LG_.b无DEBUG属性);
#----画图标--------------------------
i图标高宽G=-1;imageG=None;
Mn角色冫ipG={};

#----版本--------------------------
b中文界面G=False;b试玩版G=False;

#----丄----------------------------------------------------------
CL条序L2f2丄画G=None;
#----矩阵-----------------------------------------------------------
L红绿蓝D=[红,绿,蓝,青];

L条序L点序f2=[];L条序LL2f2一一=[];CL2f2=None;CL4f2=None;CL5f4=None;CL4f4=None;CL13f4m=None;LL6f2=[];
L条序LL6f2=[];f2丅画=None;L条序艹pre点=[];L条序艹pre一一=[];L条序艹pre乛=[];

#----多弓--------------------------
CL点序f2=None;
CL2条数丶iSize点G=None;CL2条数丶iSize线G=None;CL2条数丶iSize乛G=None;
CL条序艹点画G=None;CL条序艹线画G=None;CL条序艹乛画G=None;
CL条序L点序f2画G=None;CL条序LL2f2线画G=None;CL条序LL4f2乛画G=None;
CL条序col点G=None;CL条序col线G=None;CL条序col乛G=None;
#----单弓--------------------------
# CL2条数丶iSize点G=c_int(-1);ciSize线G=c_int(-1);ciSize乛G=c_int(-1);

艹字画G=c_int();艹绑画G=c_int();艹厶画G=c_int();艹囗画G=c_int();艹丷画G=c_int();艹Λ画G=c_int();艹厸画G=c_int();艹m画G=c_int();

CLL2f4丅数画G=None;#左是位置,右是rbga颜色
CLL2f4丅字画G=None;CLs64字G=None;

CL面序L4f4厶画G=None;CL面序L5f4囗画G=None;CL面序Lnf4厸画G=None;CLL4f4丷画G=None;CLL5f4Λ画G=None;CLL13f4m画G=None;
#----2d--------------------------
艹线画2dG=c_int();CLL3i4线画2dG=None;

#----线段---------------------------------------------------------
#L条序Lv线段序画G=None;
#☐☐☐☐☐┄☐☐☐☐☐☐
#☐☐☐┄─┃\☐☐☐☐☐☐
#☐┄─☐☐┃☐\☐☐☐☐☐
CLL2f2一一序绑画G=None;CL开始序f2画G=None;

#----更新---------------------------------------------------------
b丌仌=False;b在播放G=False;

b下L=c_int();b下R=c_int();b下中键=c_int();

#----CTYPES--------------------------------------------------------
ci2〇=(c_int*2)(0,0);cf2〇=(c_float*2)(0.0,0.0);ci3〇=(c_int*3)(0,0,0);cf3〇=(c_float*3)(0.0,0.0,0.0);
ci2一=(c_int*2)(-1,-1);ci3一=(c_int*3)(-1,-1,-1);cf4q=(c_float*3)(-1,-1,-1);ci4一=(c_int*4)(-1,-1,-1,-1);
cf2一=(c_float*2)(-1.0,-1.0);cf3一=(c_float*3)(-1.0,-1.0,-1.0);cf4一=(c_float*4)(-1.0,-1.0,-1.0,-1.0);cf4q=(c_float*4)(1.0,0.0,0.0,0.0);cf31=(c_float*3)(1.0,1.0,1.0);cf16=(c_float*16)(1.0,0.0,0.0,0.0,	   0.0,1.0,0.0,0.0,	   0.0,0.0,1.0,0.0,	   0.0,0.0,0.0,1.0);
cf33一=(c_float*3*3)(*[cf3一]*3);cf44一=(c_float*4*4)(*[cf4一]*4);
Lcf3=[];LLcf3=[];
#----string--------------------------
# s128="012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567我"
cs128= (c_char*128)();cs256= (c_char*256)();
# cs128p=ψ2cs(cs128);
#------------------------------
v0G=(0,0,0);v1G=(1,1,1);q0G=(1,0,0,0);
#----MESH--------------------------
ci点数G=c_int(-1);ci面数G=c_int(-1);ci边数G=c_int(-1);ci环数G=c_int(-1);

#====IMPORT==========================
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

def 灬cvp():
	LG.cvpC=None; LG.cvpSP=None; LG.cvpOA=None;cvpOS=None;cvpVL=None; LG.C=None; LG.Co=None; LG.Cmesh=None;LG.oA=None;LG.pbA=None;cvpA=None;LG.wm=None;
	# LG.b新=True;LG.Ls组Ω=[];LG.CL骨组ii点=[];LG.Cvgω=[];LG.CvgΩ=[];
	print("~~~UNLOAD cvp==",);
	
def 叵cvp(context,o=None):
	LG.C=context;
	if(o):
		LG.oA=o;
	else:
		LG.oA=LG.C.active_object;
	if(LG.oA):
		LG.cvpOA = c_void_p(LG.oA.as_pointer());
	if(cvpVL):
		cvpVL = c_void_p(LG.C.view_layer.as_pointer());		  
	LG.scene=LG.C.scene;
	LG.cvpC= c_void_p(LG.C.as_pointer());
	print("###LOAD cvp==",);

#------------------------------
sA='';

# SPACE_IMAGE = 6;
# SPACE_NODE = 16;
i10=10;i32=32;i64=64;i256=256;i512=512; i1024=1024;i2048=2048;
b画面=False;b画丷=False;b画Λ=False;b画字=False;b画弓=False;b画2d=False;
L2条数丶iSize点=(8,100);L2条数丶iSize线=(8,100);L2条数丶iSize乛=(8,100);
iSize丷=20;iSizeΛ=20;iSize厶=20;iSize囗=20;iSize厸=10;iSize字=20;
iSize线2d=100 ;iSize弓=20;



	
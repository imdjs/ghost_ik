

import bpy,sys,os

from bpy.props import *
# from mathutils import Matrix,Vector,Euler
from ctypes import*
from bpy_extras import object_utils
# import bmesh
from math import*
# from .LG import sPYLIB父级,Gik;

# 文件夹此PYLIB=os.path.basename(os.path.dirname(__file__));
from ..G import 语;
#/////////////////////////////////////////
def dll载入dll(dll,s键,dllpath1,dllpath2,dllpath3):   
    dll=getattr(dll,s键,"none");print("DLL0==",dll,dllpath1,dllpath2,dllpath3);
    #if os.path.exists("B:/BlenderTest64.dll"):
        #dll = windll.LoadLibrary(dllpath1)
    if(dll==None):
        try:
            dll= CDLL(dllpath1);
            print("DLL1==",dll);
        except:
            try:
                dll= CDLL(dllpath2);print("dllpath1 not susses",);     
            except:    
                dll= CDLL(dllpath3);print("dllpath2 not susses",);
 
    # dll.凸乙main(c_void_p(bpy.context.as_pointer()));
    return dll;

def dll卸载dll(dll,s键):   
    dll=getattr(dll,s键,"none");print("del dll==",dll,s键);
    #if(platform.system()=="Windows"):  
    # while(dll):
    if(dll!=None):
        windll.kernel32.FreeLibrary(dll._handle);#释放dll
        print("delete dll LIB ~  //////////////////////////////////////////\n",);
        dll=None;
    return dll;

    
#/////////////////////////////////////////
def 载入模块(Ls模块名,b打印=False):
    for s模块名 in Ls模块名:
        eval("from"+ s模块名+" import *" );
        if(b打印):
            print("IMPORT module==%s"%(s模块名));
            
def 删除模块(Ls模块名,b打印=False):
    for s in Ls模块名:
        # try:
        if(s in sys.modules):
            del sys.modules[s];
            if(b打印):
                print("DEL MODULE==",s);
        # except:
        else:
             print("!MODULE not in modules==",s);    

    
#////注册类//////////////////////////////////
def 注册类(LL类,b打印=False):
    for L类 in LL类:
        for 类 in L类:
            if(b打印):print("REGISTER_CLASS==",类);
            # try:
            bpy.utils.register_class(类);
            # except:
                # print("!!!fail to register ==",类);
                
def 注销类(LL类,b打印=False):
    for L类 in LL类:
        for 类 in L类:
            if(b打印):print("UNREGISTER_CLASS==",类);
            # try:
            bpy.utils.unregister_class(类);
        # except:
            # print("!!!fail to unregister_class ==",类);


def 注册1类(类,b打印=False):
    if(b打印):print("REGISTER_1CLASS==",类);
    # try:
    bpy.utils.register_class(类);
    # except:
        # print("!!!fail to register 1==",类);
    
	
#——————————————————————————————————————————————————————
#////注册按键//////////////////////////////////////////
#Ls类别界面=["3D View","Object Mode","Mesh","Curve","Armature","Pose","Vertex Paint","Weight Paint","Object Non-modal","Sculpt","Timeline","Outliner"];
def kmiΔ新建(km,idname="",type="", value="",any=False,shift=False,ctrl=False,alt=False,oskey=False,head=False):
	""""""
	kmi = km.keymap_items.get(idname, None);#看看有没有这个键存在
	if(kmi):
		if (kmi.type==type and kmi.any==any	 and kmi.shift ==shift	and kmi.ctrl ==ctrl and kmi.alt==alt ):
			#kmi.idname = idname;
			if(kmi.active==False):kmi.active=True;	  
			#print("BP",kmi.properties,kmi.name);
			print("	 FIND KMI",kmi.idname,kmi.type,kmi.value);
		#----不相同乙就新建--------------------------
		else:
			kmi=km.keymap_items.new(idname=idname, type=type, value=value,any=any ,shift=shift ,ctrl=ctrl,alt=alt,oskey=oskey,head=head );#没有 就新建
			if(kmi.active==False ):kmi.active=True ;
			print("	 kmi NEW diff==",kmi,kmi.idname,kmi.type,kmi.value,kmi.oskey);

	else:
		kmi=km.keymap_items.new(idname=idname, type=type, value=value,any=any ,shift=shift ,ctrl=ctrl,alt=alt,oskey=oskey,head=head );#没有 就新建
		if(kmi.active==False ):kmi.active=True ;
		print("	 kmi NEW==",kmi,kmi.idname,kmi.type,kmi.value,kmi.oskey);		 

	return kmi;
#——————————————————————————————————————————————————————
def 不勾按键(LLsKC类别,LMs类别id与按键,b注册还是反注册):
	print("UNselect==",b注册还是反注册);
	Lkc=[None,None,None];
	Lkc[1]= bpy.context.window_manager.keyconfigs.user;
	for kc in Lkc:
		if(kc):
			for LsKC in LLsKC类别:
				if(LsKC[0] in kc.keymaps.keys()):#"3D View" "Object Mode"
					km = kc.keymaps[LsKC[0]];
					if(km==None):continue;
					print("km==",km,km.name,km.space_type,km.region_type);					  
					Ckmi全部=km.keymap_items;#全部键位
					Lkeys=Ckmi全部.keys();
					#print("Lkeys==",Lkeys);
					for kmi全部 in Ckmi全部:
						#------------------------------------------------------------
						for i项 in LsKC[3]:#[0,1,2,3,4,5,6,7,8,9,10,11,12]
							Ms类别id与按键 = LMs类别id与按键[i项];
							#if(kmi全部.idname=="object.duplicate_move_linked" and  Ms类别id与按键["idname"] in Lkeys):print("LINKED==",kmi全部.idname);
							idname=Ms类别id与按键["idname"];#print("This",idname);
							if(idname in Lkeys):
								kmi=Ckmi全部[idname];

								if(idname!=kmi全部.idname ):
									#print("kmi.idname==",kmi.idname,kmi.type ,kmi.any, kmi.shift, kmi.ctrl,kmi.alt );
									if (kmi全部.type ==Ms类别id与按键["type"] and kmi全部.any==Ms类别id与按键["any"]and kmi全部.shift==Ms类别id与按键["shift"]	and kmi全部.ctrl==Ms类别id与按键["ctrl"]  and kmi全部.alt== Ms类别id与按键["alt"]	 ):
										print("FIND",kmi全部.idname,Ms类别id与按键["type"] ,Ms类别id与按键["any"] ,Ms类别id与按键["shift"]  ,Ms类别id与按键["ctrl"] ,Ms类别id与按键["alt"] );
										print("Find kmi==",kmi.idname,kmi.type ,kmi.any, kmi.shift, kmi.ctrl,kmi.alt );
										if(kmi全部.active==True and b注册还是反注册==True):
											kmi全部.active=False;print("False______",kmi全部.idname);
										elif(kmi全部.active==False and b注册还是反注册==False):
											kmi全部.active=True;print("True______",kmi全部.idname);


#----------------------------------------
def 注册按键(LLsKC类别,LMs类别id与按键):
	Lkc=[None,None,None];
	kc=Lkc[1]= bpy.context.window_manager.keyconfigs.user;#●●只有这个才是对的
	kc2=Lkc[2]= bpy.context.window_manager.keyconfigs.default;

	if(kc):
		for LsKC in LLsKC类别:
			#print("LSKC==",LsKC);
			km=None;
			if(LsKC[0] in kc.keymaps.keys()):
				km=kc.keymaps[LsKC[0]];#print("FIND km==",km.name);

			if(km==None):print("!!km==",km);continue;
			# print("km==",km,km.name,km.space_type,km.region_type,LsKC[1],LsKC[2]);
			#------------------------------------------------------------
			for i项 in LsKC[3]:#[0,1,2,3,4,5,6,7,8,9,10,11,12]
				Ms类别id与按键 = LMs类别id与按键[i项];
				kmi=kmiΔ新建(km,idname=Ms类别id与按键["idname"],type=Ms类别id与按键["type"], value=Ms类别id与按键["value"],any=Ms类别id与按键["any"],
											shift=Ms类别id与按键["shift"],ctrl=Ms类别id与按键["ctrl"],alt=Ms类别id与按键["alt"],head=Ms类别id与按键["head"]);
				print("NEW KMI",kmi,LsKC[0]);
				if(kmi):
					if("properties" in Ms类别id与按键.keys()):#有属性
						for 键,值 in Ms类别id与按键["properties"].items():
							
							try:
								setattr(kmi.properties,键,值);print("	 PROPERTIES",kmi.idname,键,值);
								#kmi.properties.name = "IMDJS_Q_menu";#这个键绑的类名
							except:print("	!!!ERROR setattr properties==",kmi,键,值);
		#print("kc 2 ==",kc,kc.name,kc.is_user_defined,kc.keymaps.keys());
	#------------------------------------------------------------
	不勾按键(LLsKC类别,LMs类别id与按键,True);

#——————————————————————————————————————————————————————
def 注销按键(LLsKC类别,LMs类别id与按键):
	Lkc=[None,None,None];
	Lkc[1]= bpy.context.window_manager.keyconfigs.user;
	#----勾选原来的-----------------------------------------------------
	不勾按键(LLsKC类别,LMs类别id与按键,False);

	for kc in Lkc:
		if(kc):
			#print("KEY",kc.keymaps);
			for LsKC in LLsKC类别:#LsKC==("3D View","VIEW_3D","WINDOW",[0,1,2,3,4,5,6,7,8,9,10,11,12])
				if(LsKC[0] in kc.keymaps.keys()):
					km = kc.keymaps[LsKC[0]];#"3D View"
					#print("FIND KM",km);
					Ckmi全部=km.keymap_items;
					#print("Ckmi全部==",Ckmi全部[0]);
					for i项 in LsKC[3]:#[0,1,2,3,4,5,6,7,8,9,10,11,12] #有的==[]
						Ms类别id与按键 = LMs类别id与按键[i项];
						if(Ms类别id与按键["idname"] in Ckmi全部.keys()):
							kmi=Ckmi全部[Ms类别id与按键["idname"]];
							#print("KMI==",kmi.idname);
						else:continue;
						if("name" in Ms类别id与按键["properties"].keys()):
							if (kmi.properties.name ==Ms类别id与按键["properties"]["name"]):
								#print("REMOVE KMI",kmi.idname );
								km.keymap_items.remove(kmi);#break;#如果删除了kmi 就跳出

						#----检查键位是否吻合-------------------------------------------
						else:
							if(Ms类别id与按键["type"]==kmi.type and Ms类别id与按键["value"]==kmi.value and Ms类别id与按键["any"]==kmi.any and \
								Ms类别id与按键["shift"]==kmi.shift and Ms类别id与按键["ctrl"]==kmi.ctrl and Ms类别id与按键["alt"]==kmi.alt and Ms类别id与按键["oskey"]==kmi.oskey):
								#print("REMOVE KMI",kmi.idname );
								km.keymap_items.remove(kmi);#break;


#====string==========================================================
def 凷键(键,o,属性=None):
	if(键 not in o):
		if(属性):
			o[键]=属性;
		else:
			o[键]={};
		
def s同名改(s名,Ls名):#把相同的s名_  编上序号
    i = 0
    while (s名 in Ls名):
        i += 1
        if (s名[-3:].isdigit() and s名[-4] == "."): #sk.isdigit() 所有字符都是数字 并且  之后是.
            s名 = "{}{:03d}".format(s名[:len(s名)-3], i)#03d  表示小数点后保留三丅整数 打印name.00i
        else:
            s名 += ".001"
    return s名;
    
#////math///////////////////////////////////////
def L4位小数(Lf):
    if(str(type(Lf)) in["<class 'float'>"]):
        return round(Lf,4);
    elif(str(type(Lf)) in["<class 'int'>","<class 'string'>","<class 'bool'>"]):
        return Lf;

    #----列表浮点-----------------------------------------------------
    L2=[];Lf=list(Lf);
    for i,f in enumerate(Lf):
        if(f==1):
            f=1.000;
        L2.append(round(f,4));
    return L2;
    
#///////////////////////////////////////////
def L几位小数(Lf,i小数丅):
    if(str(type(Lf)) in["<class 'float'>"]):
        return round(Lf,i小数丅);
    elif(str(type(Lf)) in["<class 'int'>","<class 'string'>","<class 'bool'>"]):
        return Lf;

    #----浮点列表----------------------------------------------------
    L2=[];Lf=list(Lf);#这个会去掉欧拉的"XYZ" 只保留前三个
    for i,f in enumerate(Lf):
        if(f==1.0):
            f=1.000;
        L2.append(round(f,i小数丅));
    return L2;
	
def 卩二二v(v,v1):
	return abs(v[0]-v1[0])<0.0001 and abs(v[1]-v1[1])<0.0001 and abs(v[2]-v1[2])<0.0001;
# ////CTYPE////////////////////////////////////////
def ψ2ci(ciIJ):#ciIJ=(c_int*3*2)(*[ci3G]*2);
    ψCi_ = POINTER(c_int);
    i维=len(ciIJ);
    return (ψCi_*i维)(*ciIJ);#√
    #return (ψCi_*i维)(*[*ciIJ]);#√
    
def CLi巜(i维):
	return(c_int*j维)(*[-1]*j维);#[ξ点,ξ点,ξ点,ξ点]
def CLf巜(i维):
	return(c_float*j维)(*[-1.0]*j维);
	
def CLLi巜(i维,j维):
	return[(c_int*j维)(*[-1]*j维)]*i维;#[[ξ点,ξ点,ξ点,ξ点],[ξ点,ξ点,ξ点,ξ点],...]
def CLLf巜(i维,j维):
	return[(c_float*j维)(*[-1.0]*j维)]*i维;

#////MESH////////////////////////////////////////
def o十十(name,mesh=None):
    return object_utils.object_data_add(bpy.context, mesh,  OP=None,name=name);
    
def o吅(o物源,context \
            ,b复制data=False):#●假设o物源是selected
    Collet视=context.view_layer.layer_collection.collection;Co集Ω=Collet视.objects;
    # C子集=Collec视.children;
    
    if(not o物源):
        #o物源=context.active_object;
        print("!!!o ==",o物源);return None;

    o子=o物源.copy();Co集Ω.link(o子);
    if(o物源.data):
        #----有data--------------------------
        if(b复制data):
            o子.data=o物源.data.copy();
        else:
            if(o子.data==None):
                o子.data=o物源.data;            
    return o子;
    
def 十点边面卩(i多少点,i多少边,i多少面,i多少环,id):
    i要add多少点=i多少点-len(id.vertices);i要add多少边=i多少边-len(id.edges);i要add多少环=i多少环-len(id.loops);i要add多少面=i多少面-len(id.polygons);
    # print("now==",i多少点,i多少边,i多少环,i多少面,id);print("+++++add how==",i要add多少点,i要add多少边,i要add多少环,i要add多少面);#return ;
    if(i要add多少点>0):
        id.vertices.add(i要add多少点);
    if(i要add多少边>0):
        id.edges.add(i要add多少边);    
    if(i要add多少环>0):
        id.loops.add(i要add多少环);    
    if(i要add多少面>0):
        id.polygons.add(i要add多少面);    
        
def 十点边面(i要add多少点,i要add多少边,i要add多少面,i要add多少环,id):
    # print("+++++add==",i要add多少点,i要add多少边,i要add多少环,i要add多少面);
    # if(o.type=="MESH"):
        # id=o.data;
    if(i要add多少点>0):
        id.vertices.add(i要add多少点);
    if(i要add多少边>0):
        id.edges.add(i要add多少边);    
    if(i要add多少环>0):
        id.loops.add(i要add多少环);    
    if(i要add多少面>0):
        id.polygons.add(i要add多少面);
        
	
def o十十空卩(name,context,type="",b群组=False,g群组=""):
	Csco=context.scene.objects;
	if(name in Csco):
		o=Csco[name];
	else:
		o=object_utils.object_data_add(context, None,  OP=None);o.name=name;
	if(type!=""):
		# o.instance_type=type;
		# else:
		o.empty_display_type=type;# [‘PLAIN_AXES’, ‘ARROWS’, ‘SINGLE_ARROW’, ‘CIRCLE’, ‘CUBE’, ‘SPHERE’, ‘CONE’, ‘IMAGE’], default ‘PLAIN_AXES
	if(b群组):
		o.instance_type="COLLECTION";# [‘NONE’, ‘VERTS’, ‘FACES’, ‘COLLECTION’],, default ‘NONE
		if(g群组):
			try:o.instance_collection=g群组#bpy.data.collections[s群组名];
			except:print("!!!no this group",g群组);
	return o;
	
#========================================
def mod罒(s修改器名,type,o):
    Cmod修改器=o.modifiers;
    if(type=="PARTICLE_SYSTEM"):
        for i,mod in enumerate(Cmod修改器):
            if(mod.type==type and s修改器名==mod.particle_system.name):
               return mod;
    
    else:
        for i,mod in enumerate(Cmod修改器):
            if(mod.type==type and s修改器名==mod.name):
               return mod;

    return None;
#----------------------------------------
def So(o,context,b选=True):
	Co视=context.scene.objects;
	if(b选):
		o.select_set(state=True,view_layer=context.view_layer);
	else:
		o.select_set(state=False,view_layer=context.view_layer);
		
def S骨(b选=True):
	if(b选):
		bpy.ops.pose.select_all(action='SELECT');
	else:
		bpy.ops.pose.select_all(action='DESELECT');
#========================================
def Δ移动子级Ο(o选,C子集,Co场Ω,Co集Ω,Co集to \
                            ,b删除原来的=True):
    for o in o选.children:
        try:
            Co集to.link(o);#有可能此物已经存在场景
        except:pass;
        if(b删除原来的):
            try:
                Co集Ω.unlink(o);
            except:pass;
            try:
                Co场Ω.unlink(o选);
            except:pass;
        if(C子集.__len__()!=0 and b删除原来的):
            for 子集 in C子集:
                try:
                    子集.objects.unlink(o);
                except:pass;
        #------------------------------
        if(o.children):
            Δ移动子级Ο(o,C子集,Co场Ω,Co集Ω,Co集to,b删除原来的);
#----------------------------------------
def 乛o_scene(context,Lo,sceneA,sceneTo__ \
                            ,b删除原来的=True):
    Collec视=context.view_layer.layer_collection.collection;Co集Ω=Collec视.objects;#父集
    Co场Ω=context.scene.collection.objects;#print("Co场Ω==",Co集Ω,Co场Ω);#可能是相同的
    C子集=Collec视.children;#子集
    # Co视=context.scene.objects;
    print("context.collection==",context.collection,context.collection.objects,C子集.__len__());
    # print("context.active_object==",context.active_object);
    # return {"FINISHED"};
    if(Lo==[]):
        # self.report({"ERROR"},"没有选中物体");#"INFO" "ERROR" "DEBUG"
        print("!!! no Lo==",Lo);
        return ;
    #------------------------------
    Collet视to=sceneTo__.view_layers[0].layer_collection.collection;
    Co集to=Collet视to.objects;
    # Co集to=sceneTo__.objects;
    for o选 in  Lo:
        print("MOVE==",o选.name);
        # if(self.bp层级):
        Δ移动子级Ο(o选,C子集,Co场Ω,Co集Ω,Co集to,b删除原来的);
        #------------------------------
        try:
            Co集to.link(o选);
        except:pass;
        #----删除原来的--------------------------
        if(b删除原来的):
            try:
                Co集Ω.unlink(o选);
            except:pass;
            try:
                Co场Ω.unlink(o选);
            except:pass;
            
        if(C子集.__len__()!=0 and b删除原来的):
            for 子集 in C子集:
                try:
                    子集.objects.unlink(o选);
                except:pass;
    # sceneTo__.update();
	
def SetMode(oA,mode="OBJECT"):
	if(oA==None):
		oA=bpy.context.active_object;
	if(oA):#有可能场景没有物体
		if(oA.mode!=mode):#OBJECT, EDIT, POSE, SCULPT, VERTEX_PAINT, WEIGHT_PAINT, TEXTURE_PAINT, PARTICLE_EDIT, GPENCIL_EDIT
			bpy.ops.object.mode_set(mode=mode);
#////Operator/////////////////////////////////////
import webbrowser
class 卐关于我卐Operator(bpy.types.Operator):
    bl_idname = 'op.about_me'
    bl_label = 'about me'
    bl_description = 'about me'
    bp查看更新:BoolProperty(name="check for update?",description = 'check for update?',default=True);
    bp查看其它插件:BoolProperty(name='check my other addons?',description='check my other addons?',default=True,subtype='NONE',update=None);
    Ls介绍=[
                      "---------------------------------------------------------",
                      "---------------------------------------------------imdjs",                      
                      ];
    
    url更新链接="";
    url其它商业插件1=""
    #------------------------------------------------------------
    @classmethod 
    def poll(self,context):
        return True ;
    
    def draw(self, context):
        """"""
        for s in self.Ls介绍:
            self.layout.label(text=s, text_ctxt="", translate=True, icon='NONE', icon_value=0);
        uil行=self.layout.row(align=False);
        uil行.prop(self, "bp查看更新");   
        # uil行.prop(self, "bp查看其它插件");  
    def invoke(self, context, event):#运行的第1步
        return context.window_manager.invoke_props_dialog(self,width=600,height=50);
    
    def execute(self, context):
        if(self.bp查看更新):
            webbrowser.open(self.url更新链接, new=0, autoraise=True);
        return {"FINISHED"}; 
bpy.utils.register_class(卐关于我卐Operator);
#========================================
class 卐弹出询问窗口卐Operator(bpy.types.Operator):
    bl_idname = "op.ask_for_sure";
    bl_label = "弹出询问窗口";
    bl_options = {"REGISTER", "UNDO"};
    sp:StringProperty(name="注意", description="", default="你确定卩");
    pathG:StringProperty(name="文件路径", description="E:/blender/addons/", default="E:/blender/addons/");
    #==============================================================
    @classmethod
    def poll(cls, context):
        return True; #(obj and obj.type == "MESH")

    #==============================================================
    def draw(self, context):    
        self.layout.prop(self, "sp");
        
    def invoke(self, context, event):   return context.window_manager.invoke_props_dialog(self,width=400,height=50);#召唤
bpy.utils.register_class(卐弹出询问窗口卐Operator);

class 卐激活物名给spG卐Operator(bpy.types.Operator):
    bl_idname = "op.imdjs_active_name_sp_lib";
    bl_label = "active_name_sp";
    bl_context='object';
    bl_description="pick the active object"
    
    sp物名:StringProperty(name="", description="", default="");
    #------------------------------------------------------------
    def execute(self, context):
        oA=context.active_object;
        if(oA):
            self.sp物名=oA.name;
            print("pick up object: %s"%oA.name);
        else:
            self.report({"ERROR"},"!!! can't find node");#"INFO" "ERROR" "DEBUG" "WARNING"
        return {"FINISHED"};
bpy.utils.register_class(卐激活物名给spG卐Operator);
    
	



#////////////////////////////////////////////
Ls模块selfG=[];Ls模块LIB=[];
#///end////end////end////end////end////end////end////end////end////





import bpy,ctypes,platform,os,ast
from bpy.props import EnumProperty
# import locale
sys_lang=-1;
if(platform.system()=="Windows"):
	dll乚 = ctypes.windll.kernel32
	sys_lang = hex(dll乚.GetSystemDefaultUILanguage())
#loc_lang = locale.getdefaultlocale()

# print (loc_lang)
#sys=bpy.context.preferences.system;#UserPreferencesSystem
#sys.use_international_fonts and

# pv=bpy.context.preferences.view;
# if( sys_lang =="0x804" and pv.use_translate_interface):

file=os.path.join(os.path.dirname(__file__),"lang.txt");
with open(file, 'r',encoding='gbk') as 文件:
	# s文件 = ast.literal_eval(文件.read());
	s文件 =文件.read();
	文件.close();
print("L LAYOUT IN==",s文件);


if(s文件=="chinese"):#english
	description="虚拟的IK,不需要任何额外的骨来控制IK ";print ("sys_lang ==",sys_lang)
	L语言=("无","英语","汉语")
	L全局=("(场景)","(物体)");
	add_remove_ik_group="添加ik组";
	Lik类型=("二节ik","三节ik","样条ik","物理ik")
	工具="还未完成! !仅用于测试,点击F键激活IK控制器";
	指导1="点击F键(或ctrl + F键)来控制ik";
	指导2="点击ctrl + X 扭动ik骨轴";
	L画画=("画ik","在视窗画ik ");
	画ik="画ik"
	不画ik="不画ik"
	骨数="骨数"
	开始="开始"
	开始帧="开始帧"
	结束="结束"
	结束帧="结束帧"
	L模拟帧=(("预模拟","预模拟一定数量的帧作为第一帧"),("预模拟帧","预模拟帧数" ),("惯性","维持预模拟帧后的力" ));
	L重力=(("重力","_"),("重力因子","_这个骨的重力因子" )
					,("质量","_"),("稳定性","_值越大可以减少骨骼的抖动"),("力度","碰撞的力度(单个骨")
					,("风力","风力的力度(单个骨")
					);
	L渐变带动=("硬度","_父骨动时拉动子骨");
	L扭父=("扭父","_扭动子的同时也扭动父骨");
	Lik=(("ik 类型","类型说明: 0 no ik,1:spline,2:two-ik,3:tri-ik"),("设置ik","设置ik 或物理骨"),("除移ik","除移选中骨骼的ik属性"),("ik目标",""),("对齐父骨",""),("旋父","扭动子级带动父级"));
	L样条ik=("范围","_控制骨的影响范围","点击 F/ctrl F/alt F/shift F(根骨) 并移动鼠标","X/alt X /ctrl X  扭曲,shif F 整个spline移动");
	L轴=("轴","轴对齐");
	L扭性=("扭性","_spline ik的扭曲系数","扭范围","越小传播越远");
	L刚性=("刚性","_物理骨弯曲硬度");
	L弹性=("弹性","_spline ik骨弯曲因子");
	L恢复=("恢复","_物理骨恢复初始形状");
	L限制=("限制","_骨旋转角度限制");
	L用申=("用目标","_使用子骨的ik目标约束");	
	L弹性类型=("弹性类型","弹性类型");
	L弧度伸d=("伸角","_拉伸角时的最小角度限制");
	L弧度缩=("缩角","_缩角时最的小角度限制");
	L自动选或钉=("自动选骨","钉固","用钉固","_决定是否让这个骨架所有骨有钉固","_固定这个骨的spline ik 的头","不动父","不移动父骨","移动","钉固了,_但如果选中自身还是可以移动");
	L激活=("使用","_使用 ghost_ik");
	L修正=("修正骨","_使用修正骨");
	LIK模式=("IK模式","_IK模式");
	L物理模式=("物理模式","_物理模式");
	L同步模式=("物理","风","烘焙","IK","修正骨");
	L重载= ("重载快捷键","_重置Ghost_IK热键(如果插件已经更新到新版本,但热键仍然是旧的,并且与新版本不兼容)");
	#----同步--------------------------
	增加骨架="增加骨架"
	移除骨架="移除骨架"
	增加骨架约束con="增加约束"
	移除骨架约束con="移除约束"
	切换骨架约束con开关="切换约束开关"
	激活物体="指定为激活的骨架"
	#----物理--------------------------
	L物理=("使用物理(骨)","使用物理ik","物理","物理ik类型");
	L列表=("----全局碰撞体--------------------","添加选中物为碰撞体","移除列表中的选中项","清空列表");
	L列表2=("----本骨架排除碰撞体----------------","添加排除","移除排除","清空列表");
	L碰撞=("增加碰撞体","移除碰撞体","使用碰撞(场景)==================","碰撞","偏移量","碰撞体表面的偏移量","碰撞检测范围","只有低于这个范围都会检测碰撞","使用物理");
	L烘培=("烘培","把物理骨动画烘培成关键帧","删烘焙","删除烘焙的关键帧","烘焙参考物","烘焙参骨","根据这个骨的关键帧烘焙骨(只有当时间线上有关键帧的地方才烘焙)" 
	,"只烘焙激活","只烘焙激活的骨架"
	,"参考关键帧","只有当参考骨有关键帧的时间才烘焙","间隔帧数","烘焙时间隔帧数"\
	,"开始帧","结束帧");
	L关键帧=(("首尾连贯","平均首尾关键帧值,让首尾连贯 通常用于游戏角色的循环动作"),("帧数","插值首尾关键帧数量"));
	L设置=("设置pose","_重设置绑定pose" \
					,"设关联点","_设置关联点,如果碰撞检测这个点,则与此点相关联的其他点将全部被检测" \
					,"插入帧","_ghost ik 骨插入(可用项)关键帧" \
					,"升级属性","_如果因为addon版本更新导致骨不能运行,必须运行这个!!"\
					,"更新ik绑定","_如果编辑了编辑骨,就要更新ik绑定位置"\
					,"设置ik目标","_把当前pose设置为固定申"
					);
	L对称=("对称pose","对称命名为_L与_R的骨姿势,(注意!! 不能用内置的复制姿势功能,因为会把属性也一起复制,而ghost-ik会根据左右骨赋予不同属性)" \
				,"复制姿势","粘贴姿势","反向粘贴","复制申","粘贴申");
	Lpp属性o=("反向","隐显","开始了","隐藏动画","只选","只选中的骨有效","限制地面","限制地面 保存脚骨不会超过地面以下","限制偏移","","IK约束","使用内置的IK约束器","骨数")
	# L时间=(("预模拟","先模拟计算一定数目的帧然后作为开始帧"),("预模拟帧",""));
	Lpp属性o物理=("禁用","用物理","此骨架用物理","此场景用物理","碰撞","开始帧","结束帧","碰撞表面距离","摩擦力","反弹力","弹力","检测距离" #11 \
		,"风力>>>>>>>>>>>>>>>>>>>>","频率","风倍","风向","随机")
	Lpp属性o物理1=("中点","把中间位置作为碰撞点");
	L头尾=("头尾","-1:无  0:头  1:尾");
	#----修正骨--------------------------
	L修正骨=("修正量","","缩量","所有骨的缩放量","扭Y","","最大缩放","","延长","肌肉延长","");
	
	L出错=("!!!no active_pose_bone","!!!selected bone has no ik attribute","have removed ik setting of selected bones.","please select two  bones to set twoIK","no parent","failed to select bones","this collider's polygon count is too few atleast more than 10 faces(这个碰撞体面数太少,至少10个面)","selected object is not armature!!");
	
	Ls介绍=[
					"我开发这个IK骨系统是为了更容易更有效地控制角色的骨",
					"它不需要建造任何额外的控制器,只需要用变形的骨来控制。",
					"它有两种模式:IK模式 和 物理模式。",
					"在IK模式下,首先你需要选择一些骨并设置它的属性",
					"设置IK骨属性:选择2块/ 3块/ 4块骨头， 按 <设置IK> 键。不同数量的选定骨有不同类型的IK骨。",
					"然后选择一个骨,点击 F/ctrl F/alt F /shift F 来控制骨",
					"在物理IK,先选择一些骨(这些骨必须是连接的不是分离的)然后设置成物理ik",
					"你可以像模拟布料一样模拟骨(它使用了我用c++实现的布料引擎)",
					"对于有骨变形的网格碰撞,我用C++ 实现了自己的骨算法",
					"它根据当前骨的旋转,计算角色网格受骨影响后的顶点位置",
					"计算的顶点位置结果 会与内置骨的结果一致,从而实现了骨对角色网格的碰撞",

					  "---------------------------------------------- imdjs",					   
					  ];
#==================================================
else:
	description="virtual IK that don't need any extra bones to control IK ";
	L语言=("None","english","chinese")
	L全局=("(scene)","(object)")
	add_remove_ik_group="add_remove_ik_group";
	Lik类型=("two ik","tri ik","spline ik","physical ik")
	工具="no finished!! only for testing,click F key to activate the IK control.";
	指导1="click F key(or ctrl+F key) to control the ik";
	指导2="click ctrl+X key to roll the pole of ik";
	L画画=("visual ik","draw ik in the viewport")
	画ik="draw ik"
	不画ik="don't draw ik"
	骨数="num"
	开始="start"
	开始帧="start frame"
	结束="end"
	结束帧="end frmae"
	L模拟帧=(("presimulation","Presimulate a certain number of frames as the first frame"),("pre sim","Number of pre-simulated frames" ),("inertance","maintain the force after the pre-simulated frame"));
	L重力=(("gravity",""),("gravity fac","gravity factor of this bone")
					,("mass",""),("steady","The larger the value, the less wobbly the bone"),("strengthen","strengthen of collision of single bone")
					,("wind","wind strengthen  of single bone")
					);
	L渐变带动=("stiffiness","parent drag the chid bones");
	L扭父=("twist parent","also twist parent bones");
	Lik=(("ik type","type of ik bone:(0:no ik,1:spline,2:two-ik,3:tri-ik)"),("set IK","set the 2 ik or physical bones"),("remove IK","remove selected bones'IK attrubute"),("target",""),("align parent bone",""),("rot parent",""));
	L样条ik=("falloff","falloff of the spline ik","click F/ctrl F/alt F /shift F(root bone) and move mouse,ctrl X ","X/alt X  /ctrl X  twist,shif F move whole splines");
	L轴=("axis","axis to align");
	L扭性=("twist","physical bones twist","twist value","The smaller value, the farther the spread");
	L刚性=("stiffness","physical bones stiffness");
	L弹性=("bend","bend factor of ik bones");
	L恢复=("restore","physical bones restore the original shape");
	L限制=("limit","bone rotation angle limitation");
	L用申=("target","target for the two ik child bone");
	L弹性类型=("type of bend","type of bend");
	# Llink=("type of bend","type of bend");
	最小弧度伸="pull angle"
	L弧度伸d=("stretch","The minimum Angle limit at which the Angle is stretched");
	L弧度缩=("push angle","min angle limitation when pushing"	  );
	L自动选或钉=("auto select bone","pin","use pin","if enable the pin for all bones","pin this bone head","keep parent","don't move parent bone","move","pin but when select itself will move");
	L激活=("enable","enable ghost_ik");
	L修正=("correction","use code correction");
	LIK模式=("IK mode","IK mode");
	L物理模式=("phyical mode","phyical mode");
	L同步模式=("physics","wind","bake","IK","correction");
	L重载=("reset hotkeys","reset Ghost_IK hotkeys,if the addon has been updated to newer version but your hotkeys remain older,and are not compatible with the new version");
	#----add_arm--------------------------
	增加骨架="add armature"
	移除骨架="remove armature"
	增加骨架约束con="add constraint"
	移除骨架约束con="remove constraint"
	切换骨架约束con开关="toggle constraint off-on"
	激活物体="assign active armature"
	#----物理--------------------------
	L物理=("use physical(bone)","enable physical ik","dyn type","type of physical ik");
	L列表=("----global collider--------------------","Add the selected mesh as the collider","Remove the selected item from the list","Empty the list");
	L碰撞=("add collider","remove collider","use collide(scene)==================","collision","offset","offset value of the collider surface","Collision detection range","only less than this scope will detect collisions","use physic");
	L烘培=("bake","bake the physical simulation to keyframes","delete bake","delete baked keyframes","Bake reference object","bake reference bone","bake bone according to the keyframe of this bone"
				,"only active","only bake the active armature"
				,"reference","Bake only when the reference bone has a keyframe","interval frame","interval frame when baking"\
				,"start frame","end frame");
	L关键帧=(("coherent","Average the values of the first and last keyframes so that the first and last keyframes are coherent"),("num","Interpolate first and last keyframes"));
	L列表2=("----excluded collider-------------------","add exclude","remove exclude","Add item","Remove item","Empty the list");
	L设置=("set pose","reset the bind pose" \
					,"set relate","set related points ,if this point is detected in collision the other points relate to this point will be detected also" \
					,"insert keyframe","insert keyframe(available)for the ghost ik bones" \
					,"update-attriubute","If the ik doesn't work because of an update to the Addon, you must run this!!"\
					,"update riggine","If you have edit the edit bones, update the IK binding position"\
					,"set target","set  current target postition"
					);
	L对称=("sym pose"," symmetry pose that bones are named _L and _R,note: cant be use the built-in copy and paste pose function,because it will duplicate the attributes as well,and ghost-ik will  assign different attributes to the left and right bones." \
					,"copy pose","paste pose","flip paste","copy target","paste target");
	Lpp属性o=("inverse","visible","started","hide animation","only selected","only for selected bones","ground limit","limit the foot bone to the ground","limit offset","","IK enabled","enable the IK constraints","bone number")
	# L时间=(("pre-simulation frame","a certain number of frames are simulated and then used as the start frame"),("pre-frames","how many frames to be pre-simulated"));
	Lpp属性o物理=("disable","use physic","use physic for this armature","use physic for this scene","colision","start frame","end frame","collide offset","friction","spring","bounce","distance" #11 \
					,"wind force>>>>>>>>>>>>>>>>>>>>","frequence","multiple","wind direction","random");
	Lpp属性o物理1=("midpoint","midpoint of bone to collide");
	L头尾=("head-tail","-1:None  0:连, 1:head ,2:tail");
	#----修正骨--------------------------
	L修正骨=("corrected value","","scale value","scale value for all bones","twist Y","","max scale","","extend","muscle extend","");
	
	L出错=("!!! 没有激活骨","!!!选择的骨没有ik属性","选择的骨已经移除了ik属性.","请选择两个骨设置2ik","没有父级","选择骨失败","这个碰撞体面数太少,至少10个面","选择的物体不是骨架!!");
	
	Ls介绍=[
					  "I develope this IK bone system to controll character armature bones more easyly and more effcient",
					  "It doesn't need to add any extra bone controller,just use the deform bone to control ik.",		
						"it has two mode: the IK mode and the PHYSICAL mode.",
						"in the IK mode,first you need to select some bones and set it's attribute,",
						"to set the IK bone attribute: select  two/three/four bones and press<set IK>button. different nuber of selected bones has  different type of IK bone.",
						"and than select one bone and CLICK F/ctrl F/alt F  /shift F to manipulate the bones",
						"int the phyiscal IK mode,first select the bones that you want it to be pyhiscal bones(this bones must be connected but not seperated)",
						" you can simulate bone like cloth simulation(it use the cloth englne that I implement with C++)",
						"for the character mesh collision,I implement my own armature deformer to caculate the mesh vertices that  ",
						"after the armature deformed, so that the deformed mesh' vertices match the result of the bild-in armature deformer",

					  "---------------------------------------------- imdjs",					   
					  ];
	
	

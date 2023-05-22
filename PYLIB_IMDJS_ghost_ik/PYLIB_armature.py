
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
			
			
def Θall(arm,bΘ=True):
	if(arm.type=="ARMATURE"):
		Cpb=arm.pose.bones;
		for pb in Cpb:
			pb.bone.select=bΘ;

					
	
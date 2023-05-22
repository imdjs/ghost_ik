#ifndef __GIK_DLL_H__
	#define __GIK_DLL_H__

#include"ghost_ik.h"

// CψW s物理骨dll路径G=L"B:/PHYSIC64.dll",s修正骨dll路径G=L"B:\\CORRECT64.dll";//● 必须用英文名,否则bl安装变乱码
CψC s物理骨dll路径G="B:/PHYSIC64.dll",s修正骨dll路径G="B:\\CORRECT64.dll";//● 必须用英文名,否则bl安装变乱码
#if(defined __用DLL__|| defined __用IKDLL__)
#pragma message(" <<<<IKdll<<<<<<<<<<<<<<<" __FILE__)
// struct 卍骷;struct 卍贝兹点PRS;struct 卍PbIk;struct 卍肢PRS;//struct ;struct ;struct ;struct ;struct ;struct ;struct ;
// CψfileDLLB="B:\\IMDJS_CLOTH64.dll";

typedef struct 卍GhostIk
	{
	HINSTANCE hDLL=ψ0;int*bp用=ψ0;
public: 
	//----NODOE--------------------------
	// DEF函数指针(void,PT)	
	// #define MapNT_	 map<bNodeTree*,vector<卍Node*>>&
	DEF函数指针(void,凸一一引用ik)			
	DEF函数指针(void,凸十十引用ik)		
	DEF函数指针(int,i凸引用数)			
	DEF函数指针1(CB,凸画3d,CB)				
	DEF函数指针2(CB,bΔ凷ψpbik,bContext ψ匚, MAP0(bNodeTree*,vector<卍Node*>)&)	
	#ifdef __画画__
		DEF函数指针13(void,ΔIK钉子1节1架,匚I,匚B,卍骷 ψ匚,cvector<卍贝兹点PRS>&,vector<卍肢PRS>&,匚B,匚B,匚B,卍点画&,卍线画&,卍乛画&,卍丷画&,卍Λ画&)	
		#else 
			DEF函数指针8(void,ΔIK钉子1节1架,匚I,匚B,卍骷 ψ匚 ,cvector<卍贝兹点PRS>&,vector<卍肢PRS>&,匚B,匚B,匚B)	
	#endif
	
	// DEF函数指针1(int,i凸IK骨all,bContext *)
	DEF函数指针3(bool,bΔ凷L骷G,Object ψ匚,bContext ψ匚,vector<卍骷>& )	
	DEF函数指针2(bool,bΔ凷L骷_,Object ψ匚,bContext ψ匚 )		
	DEF函数指针10(CI,iΔ冄ΦxΠ,bPoseChannel ψ匚 ,ˉCψF ,ˉ匚ψF4 ,ˉ匚ψF4 ,卍亾&,匚F ,匚F  ,B_  ,ˉψF匚,ˉ匚ψF4 二ψ0)	
	//----IK--------------------------
	#if(0)//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	DEF函数指针3(int,bΔIK骨,Object*,bContext*,int)	
	DEF函数指针2(void,Δ画碰撞体,Object*,bContext*)	
	DEF函数指针2(void,Δ丌,Object*,bContext*)	
	DEF函数指针3(CB,bΔghost_ik骨twist,Object*,bContext*,CI)		
	//------------------------------
	DEF函数指针(void,Δ灬骨)	
	DEF函数指针1(void,Δ十十钉子,bPoseChannel*)	
	DEF函数指针4(int,bΔ凷1骷1次,Object*,bContext*,bool,bool)	
	DEF函数指针3(int,bΔinitIK1o每次A丅,Object*,bContext*,int)		
	DEF函数指针6(int,bΔSetType,bPoseChannel*,bPoseChannel*,bPoseChannel*,bContext*,CI,CB)	
	DEF函数指针(int,bΔ是空骷)	
	DEF函数指针4(int,iΔ记录pc角,bPoseChannel*,bPoseChannel*,bPoseChannel*,bContext*)	
	DEF函数指针3(void,Δ更新动画弓,Object*,bContext*,bool)		
	DEF函数指针1(void,Δ仌ik绑定,bContext*)	
	//------------------------------
	DEF函数指针3(bool,bΔ插入关键帧pose,Object*,bContext*,CB)		
	DEF函数指针2(void,Δ乙申,bContext*,bool)	
	DEF函数指针2(void,Δ应用2k,Object*,bContext*)	
	DEF函数指针2(void,Δ吅申,bContext*,CB)		
	DEF函数指针1(void,Δ乙绑定pose,bContext*)	
	#endif>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	//---------------------------------------------
	DEF函数指针1(void,凸载入scene亖,bContext*)	
	DEF函数指针1(void,凸载入scene亖IK,bContext*)	
	DEF函数指针13(void,Δ传递亖画,匚ψC,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚B)	
	//------------------------------
	CB b叵(匚ψC fileDLL,匚ψC fileDLL1=ψ0)
		{
		PRINT2db("b叵 卍GhostIk",fileDLL,fileDLL1)	
		ASSERT丶Rdb(fileDLL 二二 ψ0,false);
		if(hDLL)
			{FreeLibrary(hDLL);}
		if(hDLL 二二 ψ0)
			{//hDLL=GetModuleHandle("ghost_ik64.dll");PRINT_1("GetModuleHandle",hDLL,p)	//找到已存在的dll ★~[�`_0��e N 同时载入同一个dll 会出错
			if(hDLL 二二 ψ0)
				{hDLL=LoadLibrary(fileDLL);
				if(hDLL 二二 ψ0)
					hDLL=LoadLibrary(fileDLL1);
				}
			else
				{//DEF二函数指针3W(凸一一引用ik,凸十十引用ik,i凸引用数)	
				凸十十引用ik();PRINT1db("",i凸引用数())	
				ASSERTfdb(i凸引用数(),3 ＜ i凸引用数())	
				
				}
			}
		ASSERTptexedb(PRINT1db("★ hDLL 二二 ψ0",hDLL),hDLL 二二 ψ0,return false;,true)	
		PRINT2db("√√OK 载入 卍GhostIk fileDLL",fileDLL,(void*)hDLL);
		// 亖_亖DJS("卍GhostIk")	亖_亖BL("卍GhostIk")	亖_亖画("卍GhostIk")	 //亖_亖物理	
		//----DEF二函数指针--------------------------
		DEF二函数指针9W(凸一一引用ik,凸十十引用ik,i凸引用数,凸画3d,bΔ凷ψpbik,ΔIK钉子1节1架,bΔ凷L骷G,bΔ凷L骷_,iΔ冄ΦxΠ)	
		//----IK--------------------------
		// DEF二函数指针W4(bΔIK骨,Δ画碰撞体,Δ丌,bΔghost_ik骨twist)	
		// DEF二函数指针W9(Δ灬骨,Δ十十钉子,bΔ凷1骷1次,bΔinitIK1o每次A丅,bΔSetType,bΔ是空骷,iΔ记录pc角,Δ更新动画弓,Δ仌ik绑定)	
		// DEF二函数指针W5(bΔ插入关键帧pose,Δ乙申,Δ应用2k,Δ吅申,Δ乙绑定pose)	
		
		DEF二函数指针3W(凸载入scene亖,凸载入scene亖IK,Δ传递亖画)	
		
		
		return true;
		}
	//----------------------------------------
	卍GhostIk()
		{
#ifdef _PRINT_HEAD节点_
	亖0(亖物理,"『『『 卍GhostIk()") ;
#endif
 #ifdef _PRINT_HEAD节点_
	亖0(亖物理," 』』 卍GhostIk()");
#endif
		}
	//----------------------------------------
	~卍GhostIk()
		{
		if(hDLL)
			{凸一一引用ik();PRINT1("",i凸引用数())	
			//PRINT0("str--------------------------")	
			FreeLibrary(hDLL);hDLL=ψ0;//PRINT0("str--------------------------")	
			}
		PRINT0db("﹌﹌﹌﹌﹌ 卍GhostIk()﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌",i凸引用数())	//★  卸载dll 后 i凸引用数()出错
		}
	}卍GhostIk;
卍GhostIk ghostikG;
#endif//#if(defined __编译DLL__ || defined __用DLL__|| defined __用IKDLL__)
////////////////////////////////////////////
// #if(defined __编译DLL__ || defined __用DLL__|| defined __用修正DLL__)
typedef struct 卍修正骨
	{
	HINSTANCE hDLL=ψ0;int*bp用=ψ0;
public: 
	//----定义DEF函数指针--------------------------
	DEF函数指针(CB,？ΔMo卍骷驱动G凵)	
	DEF函数指针3(void,Δ凷修正骷,bContext*,CB,CB)
	#if(defined __画画__ || defined __画画DB__)
		DEF函数指针11(bool,bΔ凷1修正骷,Object*,bContext*,CB,卍点画&,卍线画&,卍乛画&,卍丷画&,卍Λ画&,卍厶画&,卍囗画&,卍字画&)	
		DEF函数指针8(void,Δ骨驱动L,Object*,CB,CB,卍点画&,卍线画&,卍乛画&,卍丷画&,卍Λ画&)	
		DEF函数指针8(void,Δ骨驱动R,Object*,CB,CB,卍点画&,卍线画&,卍乛画&,卍丷画&,卍Λ画&)				
		#else
			DEF函数指针3(bool,bΔ凷1修正骷,Object*,bContext*,CB)	
			DEF函数指针3(void,Δ骨驱动L,Object*,CB,CB)	
			DEF函数指针3(void,Δ骨驱动R,Object*,CB,CB)			
	#endif
	
	DEF函数指针13(void,Δ传递亖画,匚ψC,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚B)	
	DEF函数指针1(void,凸载入scene亖,bContext*)	

	//------------------------------
	CB b叵(匚ψC fileDLL,匚ψC fileDLL1=ψ0)
		{
	// #ifdef _PRINT_HEAD节点_
		亖0(亖物理,"『『『 ");
	// #endif	
		PRINT2("b叵 卍修正骨",fileDLL,fileDLL1)	
		ASSERT丶Rdb(fileDLL 二二 ψ0,false);
		if(hDLL)
			{FreeLibrary(hDLL);}
		if(hDLL 二二 ψ0)
			{hDLL=LoadLibrary(fileDLL);
			if(hDLL 二二 ψ0)
				hDLL=LoadLibrary(fileDLL1);
			}
		ASSERTptexedb(PRINT1("★ hDLL 二二 ψ0",hDLL),hDLL 二二 ψ0,return false;,true)	
		PRINT2("√√OK 载入 修正骨 fileDLL",fileDLL,(void*)hDLL);
		// 亖_亖DJS("卍修正骨")	亖_亖BL("卍修正骨")	亖_亖画("卍修正骨")	//亖_亖物理	
		//----DEF二函数指针--------------------------
		DEF二函数指针5W(？ΔMo卍骷驱动G凵,Δ凷修正骷,bΔ凷1修正骷,Δ骨驱动L,Δ骨驱动R)	
		DEF二函数指针2W(凸载入scene亖,Δ传递亖画)	
		return true;
		}
	//----------------------------------------
	卍修正骨()
		{
#ifdef _PRINT_HEAD节点_
	亖0(亖物理,"『『『 卍修正骨()");
#endif

 #ifdef _PRINT_HEAD节点_
	亖0(亖物理," 』』 卍修正骨()");
#endif
		}
	//----------------------------------------
	~卍修正骨()
		{
		if(hDLL)
			{FreeLibrary(hDLL);hDLL=ψ0;PRINT0("﹌﹌﹌﹌﹌ 卍修正骨()﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌");}
		
		}
	}卍修正骨;
//========================================
卍修正骨 修正骨G;//,*ψ修正骨G=ψ0
bool bp应用修正骨G=false;

template<typename T>
联 CB b叵DLL(匚ψC s此dll路径,匚ψC s此dll,匚ψC s主dll,匚ψW wc用,bContext ψ匚 C,T&修正骨__,IDProperty ψ匚 idpSC=ψ0)
	{
	亖3(true,"『『『 b叵DLL",s此dll路径,s此dll,s主dll);
	if(修正骨__.hDLL 二二 ψ0)
		{string s目录=win． str本目录(s主dll);PRINT1db("",s目录.c_str())	
		if(修正骨__.b叵(s此dll路径,s十(s目录.c_str(),s此dll))二二 false)
			{if(idpSC){i三(wc用,idpSC)=false;PRINT0("!!!bp用修正=false")	}
			}
		else
			{//修正骨__.bΔ凷L骷G(ψ0,C,false);//int i;
			if(idpSC){修正骨__.bp用=&i三(wc用,idpSC);}PRINT_1("修正骨__.hDLL=",修正骨__.hDLL,p)	
			修正骨__.凸载入scene亖(C);
			修正骨__.亖_亖画("修正骨")
			// b画G=b画;
			// 修正骨__.bΔ凷ψpbik(C,MntLψno始G);
			return true;
			}
		}
	else
		return true;
	return false;
	}

EXC CB b凸凵修正骨(){return 修正骨G.hDLL 二二 ψ0;}	
//==============================
EXC CB b凸凷修正骨dll(bContext*C)
	{
	// GetModuleFileNameA(NULL, s修正骨dll路径1, i1024);//E:\blender-3.4.1-windows-x64\blender.exe 
	// wmWindowManager ψ匚 wm=BL． wm巜C(C);
	// CψC s修正骨dll路径1 =s三(L"s物理骨dll路径",wm->id.properties);
// #ifdef _PRINT_HEAD仌_
    亖1(true,"『『『 b凸凷修正骨dll",s修正骨dll路径G);
// #endif
	IDProperty ψ匚 idpScene=？(C->data.scene)->id.properties;//PRINT_1("",idpScene,d);PRINT1("",dir(idpScene));
	IDP二(idpSC)=idp巜w(L"ghost_ik",idpScene);//PRINT1("",dir(idpSC));
	二(i三(L"bp用修正",idpSC),bp应用修正骨G);
	// 二(i三(L"bp应用ik",idpSC),bp应用IKG);二(i三(L"bp修正骨",idpSC),bp修正骨G);
	// 二(i三(L"bp画线sc",idpSC),bp画线G);//二(i三(L"bp应用品",idpSC),bp应用品G);
	
	if(bp应用修正骨G)
		{
		//----IK--------------------------
		return b叵DLL(s修正骨dll路径G,"\\CORRECT64.dll","ghost_ik64.dll",L"bp用修正",C,修正骨G,idpSC );
		// #endif>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		}//if(bp应用IKG)
	// if(修正骨G.hDLL )
		// Δ仌ik骨(bp应用IKG ,false,true);PRINT_2if(仌_,"",bp应用IKG,修正骨G.hDLL,d,d)	
	return false;
	}

	
// #endif//#if(defined __编译DLL__ || defined __用DLL__|| defined __用修正DLL__)
////////////////////////////////////////////
// #if(defined __编译DLL__ || defined __用DLL__|| defined __用物理DLL__)
DLL void Δ传递亖IK(bContext ψ匚 C,匚B b画)
	{
	二载入SCENE亖("DEBUGik",二亖idp(亖叵)	二亖idp(亖凷)	二亖idp(亖烘)	)	b画G=b画;
	亖3(true," 』』Δ传递亖IK ",亖叵,亖凷,亖烘,b画G)	
	}
	
typedef struct 卍物理骨
	{
	HINSTANCE hDLL=ψ0;int*bp用=ψ0;
public: 
	//----IMDJS_ghost_IK\物理\叵phy.cpp--------------------------
	DEF函数指针1(void,Δ凷碰撞体,bContext ψ匚)
	DEF函数指针2(void,Δ凷1骷碰撞体,卍骷&,bContext ψ匚)	
	DEF函数指针2(void,Δ十十1碰撞体,Object ψ匚,vector<卍骷>&)
	DEF函数指针2(void,Δ一一1碰撞体,Object ψ匚,vector<卍骷>&)
	DEF函数指针1(void,Δ画亍丅,bContext ψ匚)
	
	DEF函数指针8(void,Δ卌物理IK1次,匚F ,匚F ,匚F ,匚B ,匚B ,匚B,bContext ψ匚,vector<卍骷>&)
	DEF函数指针2(CB,bΔ物理骨有动画,bContext ψ匚,vector<卍骷>&)	
	DEF函数指针1(void,Δ载入scene物理属性,Scene ψ匚)		
	// DEF函数指针1(CB,bΔ巜L骷G,vector<卍骷>&)		
	DEF函数指针(CB,bΔ空L碰撞体G)			
	//----IMDJS_ghost_ik\物理\物理骨.cpp--------------------------
	#if(defined __画画__ || defined __画画DB__)
		DEF函数指针12(int,iΔ物理骨all,匚B,bContext ψ匚 ,vector<卍骷>&,I_  ,卍点画&,卍线画&,卍乛画&,卍丷画&,卍Λ画&,卍厶画&,卍囗画&,卍字画&)	
		DEF函数指针7(void,Δ画碰撞体,Object ψ匚 ,bContext ψ匚 ,卍点画&,卍线画&,卍乛画&,卍丷画&,卍Λ画&)	
		#else
			DEF函数指针4(int,iΔ物理骨all,匚B,bContext ψ匚 ,vector<卍骷>&,I_)	
			DEF函数指针2(void,Δ画碰撞体,Object ψ匚 ,bContext ψ匚)	
	#endif
	//------------------------------
	DEF函数指针1(void,凸载入scene亖,bContext*)	
	DEF函数指针2(void,Δ传递亖IK,bContext ψ匚,匚B)
	DEF函数指针13(void,Δ传递亖画,匚ψC,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚I,匚B)	
	//------------------------------
	CB b叵(匚ψC fileDLL,匚ψC fileDLL1=ψ0)
		{
		ASSERT丶Rdb(fileDLL 二二 ψ0,false);
		printf("卍物理骨.b叵() fileDLL= %s,fileDLL1= %s,cD丨F:%d,cD丨F1:%d\n",fileDLL,fileDLL1,cD丨F(fileDLL),cD丨F(fileDLL1));
		
		if(hDLL)
			{FreeLibrary(hDLL);}
		if(hDLL 二二 ψ0)
			hDLL=LoadLibrary(fileDLL);
			if(hDLL 二二 ψ0)
				hDLL=LoadLibrary(fileDLL1);
		ASSERTptexedb(PRINT1("★ hDLL 二二 ψ0",hDLL),hDLL 二二 ψ0,return false;,true)	
		PRINT2db("√√OK 载入 卍物理骨 fileDLL",fileDLL,(void*)hDLL);
		// 亖_亖DJS("卍物理骨")		亖_亖BL("卍物理骨")		亖_亖画("卍物理骨")		亖_亖物理("卍物理骨")	
		//----DEF二函数指针--------------------------
		DEF二函数指针9W(Δ凷碰撞体,Δ凷1骷碰撞体,Δ十十1碰撞体,Δ一一1碰撞体,Δ画亍丅,Δ卌物理IK1次,bΔ物理骨有动画,Δ画碰撞体,Δ载入scene物理属性)	//
		DEF二函数指针2W(bΔ空L碰撞体G,iΔ物理骨all)	
		DEF二函数指针3W(凸载入scene亖,Δ传递亖IK,Δ传递亖画)	
		return true;
		}
	//----------------------------------------
	卍物理骨()
		{
// #ifdef _PRINT_HEAD节点_
	亖0(亖物理,"『『『 卍物理骨()")	
// #endif

 // #ifdef _PRINT_HEAD节点_
	亖0(亖物理," 』』 卍物理骨()")	
// #endif
		}
	//----------------------------------------
	~卍物理骨()
		{
		if(hDLL)
			{FreeLibrary(hDLL);hDLL=ψ0;PRINT0("﹌﹌﹌﹌﹌ 卍物理骨()﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌");}
		}
	}卍物理骨;

卍物理骨 物理骨G;//,*ψ物理骨G=ψ0

bool bp应用物理G=false;

EXC CB b凸凵物理骨(){return 物理骨G.hDLL;}	

EXC CB b凸凷物理dll(bContext*C)
	{
	// GetModuleFileNameA(NULL, s物理骨dll路径1, i1024);
	// wmWindowManager ψ匚 wm=BL． wm巜C(C);
	// CψC s物理骨dll路径1 =s三(L"s物理骨dll路径",wm->id.properties);

	// PRINT3("",s物理骨dll路径G,s物理骨dll路径1,s巜sU(s物理骨dll路径1))	
	// CψC s物理骨dll路径B =s三(L"s物理骨dll路径B",wm->id.properties);PRINT3("",s物理骨dll路径B,(int)cD丨F(s物理骨dll路径B),(int)cD丨F(s巜sU(s物理骨dll路径B)))	
	// PRINT3("",(int)cD丨F(s巜wcU(s物理骨dll路径G)),(int)cD丨F("B:/PHYSIC64.dll"),(int)cD丨F("B:/ghost_ik64.dll"))	
	// PRINT1("",(int)cD丨F("B:/PHYSIC64.dll"))	//
	// PRINT1("",(int)cD丨F(s巜s("B:/PHYSIC64.dll")))	//
	// PRINT1("",(int)cD丨F(s巜wcU(L"B:/PHYSIC64.dll")))	
	// PRINT1("",(int)cD丨F(utf8巜ansi("B:/PHYSIC64.dll")))		
	// PRINT1("",(int)cD丨F("B:\\ghost_ik64.dll"))	
    亖1(true,"『『『 b凸凷物理dll",s物理骨dll路径G)	
	IDProperty ψ匚 idpScene=？(C->data.scene)->id.properties;//PRINT_1("",idpScene,d);PRINT1("",dir(idpScene));
	IDP二(idpSC)=idp巜w(L"ghost_ik",idpScene);//PRINT1("",dir(idpSC));
	二(i三(L"bp物理sc",idpSC),bp应用物理G);

	// if(bp应用物理G)
		{PRINT1("",win． str本目录("ghost_ik64.dll").c_str())	
		//----IK--------------------------
		if(b叵DLL(s物理骨dll路径G,"\\PHYSIC64.dll","ghost_ik64.dll",L"bp物理sc",C,物理骨G,idpSC ))
			{物理骨G.Δ传递亖IK(C,b画G);
			return true;
			}
		// #endif>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		}//if(bp应用IKG)
	// if(物理骨G.hDLL )
		// Δ仌ik骨(bp应用IKG ,false,true);PRINT_2if(仌_,"",bp应用IKG,物理骨G.hDLL,d,d)	
	return false;
	}


// #endif//#if(defined __编译DLL__ || defined __用DLL__|| defined __用物理DLL__)



//==============================

// #if(defined __用DLL__ || defined __编译DLL__)
 	// #pragma message(" :error __用DLL__" __FILE__ "  ")

	#ifdef __PRINT__
		#define 物理骨．		((物理骨G.hDLL 二二 ψ0)? selfΔ(物理骨G,"物理骨G.hDLL 二二 ψ0",__LINE__,__FUNCTION__,__FILE__)  : 物理骨G).
		#define 修正骨．		((修正骨G.hDLL 二二 ψ0)? selfΔ(修正骨G,"修正骨G.hDLL 二二 ψ0",__LINE__,__FUNCTION__,__FILE__)  : 修正骨G).
		#else
			#define 物理骨．		物理骨G.
			#define 修正骨．		修正骨G.
	#endif
// #else
	// #define 物理骨．
	// #define 修正骨．
// #endif
////END////END////END////END////END////END////END////END////
#ifdef _PRAGMA_MG_
    #pragma message(" #: >>" __FILE__ "  " __TIme__)
#endif
#endif

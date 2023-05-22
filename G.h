

#ifndef _G_IK_H_
    #define _G_IK_H_
// #define _PRAGMA_MG_
#ifdef _PRAGMA_MG_
    #pragma message("#:"__FILE__)
#endif



////////////////////////////////////////////
CB bΔtwo_IK骨(Object ψ匚 oArm,卍PbIk ψ匚 ψpbik控,卍骷 ψ匚 ψ骷,卍线画&线画__,卍丷画&丷画__  \
								,ˉψF匚 ψ丅 =ψ0,ˉψF匚 ψ丅前 =ψ0 ,ˉψF匚 ψ丅父 =ψ0,ˉψF匚 ψ丅子 =ψ0 \
								,匚B bPre =false,匚F fp反向ik =0);

//====物理====================================
bool b用物理场景G=false;
卍Vector 父乛子工 ,乛两头多余力,父乛子分离力;float 冖1_22点shape,f分离卜方向,f拉紧or扩张,f修正Ξ父始,分离卜方向,一Ξ向量长;
float versionD=0.78;
int i1条动力骨数G=0,i骷数G=0;
//----DEBUG--------------------------
int b恢复G=false;float fp乛丨值G=0.8;
int b力滑G=false,b修正力G=false,b阻力G=false,bp弹力G=false,bp拉力G=false,bp簧G=false,bp簧骨隔G=false,bp簧布G=false,bp乛丨G=false,bp骨在线段G=false,bpΣG=false,b渐变带动G=false;
int b烘焙G=false,/* b插值G=false,i多少帧G=false, */ b踮脚G=false;
int b有待删除列表物G=false;

// MAPΨ(Object*,vector<vector<卍Vector>*>,Mo架LψL丅点colΠG)	//排除无效子.有可能是静也有可能是角色col
// vector<vector<卍Vector>*>*ψLψL丅点colΠG=ψ0;

//------------------------------
卍PbIk*ψpbikAG=ψ0,*ψpbik父AG=ψ0;
bPoseChannel*pcAG=ψ0;

// MAPΨ(Object*,MAP0(char*,卍PbIk),Mo架Ms骨：pbik全部G)	
// MAPΨ(Object*,vector<vector<卍PbIk*>>,骷.L卍条物理)	
// MAPΨ(Object*,UI>,Mo架i骨数G)
LIST1(50,float,L骨序f扭性右子G);LIST1(50,float,L骨序f扭性左父G);LIST1(50,卍PbIk*,L骨序ψpbik右子G);LIST1(50,卍PbIk*,L骨序ψpbik左父G);

//LIST1(10,float,L骨序f弹性右子G);LIST1(10,float,L骨序f弹性左父G);LIST1(10,卍PbIk*,L骨序ψpbik右子弹G);LIST1(10,卍PbIk*,L骨序ψpbik左父弹G);
LIST1(3,bPoseChannel*,LpcG);

// MAP(Object*,vector<卍PbIk*>,Mo架Lψpbik父23ikG);//MAP(Object*,vector<卍PbIk*>,Mo架Lψpbik子ikG);

EXC void Δ〇物理骨G()
    {
    // CLEAR(Mo架Ms骨：pbik全部G)	CLEAR(骷.L卍条物理)	
	
    }
int bp钉头G=false;
卍Vector 丅钉G,丅headpreG;
//----同步骷--------------------------
// MAP(Object*,vector<卍PbIk*>,Mo架Lpc骨同步G);
//----限制IK--------------------------
bool b有限制ikG=false;
MAP(卍PbIk*,MAP0(卍PbIk*,int ),MψpbikikMψpbik线父b限制G);
map<卍PbIk*,map<卍PbIk*,int>>::iterator ψMψpbik线父MψpbikIKb限制G;//2,3 ik的父
//====动力学 ====================================
T三DEF(const 卍PbIk ψ匚,->prop)   
IDP巜SDEF(const 卍PbIk ψ匚,->prop)   


// #endif>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

// LIST(int,ik条);

////END////END////END////END////END////END////END////END////END
// #ifdef _PRAGMA_MG_
    // #pragma message("end:"__FILE__)
// #endif
#endif



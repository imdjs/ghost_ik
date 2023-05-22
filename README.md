# ghost_ik
Physical Bone and easy ik for blender addons

I’m developing this Inverse Kinematics system to control character armature bones more easily and more effcient
It don’t need to add any extra controller bone or constraint or modifier,just use the deformed bone itself to control.
though now it’s not fully implment the features that classic IK has.
but finally it’s features will be more than the classic IK.and then I can get rid of the annoying traditional IK settings.

it has two mode,(1:manul IK(two-ik\tri-ik\spline-ik), 2:dynamic physic IK)
you can simulate coth\ softbody with dynamic physic IK,(It don’t need to add any extra controller bone or constraint or modifier)using the original bone to simulate physic IK,not like the other addons it’s truly physical bone.
the collision engine is emplemented by myself completly with C++.it don’t like the build-in collision algorithm,the algorithm is mesh surface detecting,it will caculate every bone if colliding the mesh faces,includes the bone deform mesh(which I re-implement the amature system by C++,it caculate every vertices postion after the bone deformed)
,it will never encounter penetration which is determined by my unique algorithm,If it encounter penetration that must be a bug.

this addon has about 10000 line codes now, I implemented the physics engine of cloth-like algorithm completely using C++ No external dependent libraries are referenced , all the simulation is real time

It can switch between IK and FK perfectly.
the ik solver is dynamic.

https://blenderartists.org/t/ghost-ik-virtual-inverse-kinematics-bone-physic-bone-ik-c


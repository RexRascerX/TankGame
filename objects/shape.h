/* @Auther:		Jonathan Bueckman
 * @Version:	1
 * 4/13/18
 */

#ifndef SHAPE_H
#define SHAPE_H

using namespace std;

struct coordinates {
	float x,y,z;
};

/* @Purpose:	An archetype for future objects
 */
class object {
	public:
	//Instansiations
		virtual object() : 
			l(1), w(1), h(1), hp(1), p(0,0,0) { }
		virtual object(int D) : 
			l(D), w(D), h(D), hp(1), p(0,0,0) { }
		virtual object(int D, int HP) :
			l(D), w(D), h(D), hp(HP), p(0,0,0) { }

	//Deletions
		virtual ~object();

	//Basic Funstions
		virtual float getVolume() {return 1.0*l*w*h;}
		virtual int getHealth() {return hp;}

	private:
		int l,w,h,hp;
		coordinates p;
};
	

#endif

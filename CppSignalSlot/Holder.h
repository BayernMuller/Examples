#ifndef _HOLDER_H_
#define _HOLDER_H_
#include <functional>
using namespace std::placeholders;

template<int N>
class Holder
{
};

template<> class Holder<0>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj); }
};

template<> class Holder<1>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj, _1); }
};

template<> class Holder<2>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj, _1, _2); }
};

template<> class Holder<3>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj, _1, _2, _3); }
};

template<> class Holder<4>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj, _1, _2, _3, _4); }
};

template<> class Holder<5>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj, _1, _2, _3, _4, _5); }
};

template<> class Holder<6>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj, _1, _2, _3, _4, _5, _6); }
};

template<> class Holder<7>
{
public:
	template<class Object, class Function>
	static auto bind(Object* obj, Function func) 
	{ return std::bind(func, obj, _1, _2, _3, _4, _5, _6, _7); }
};

#endif // !_HOLDER_H_


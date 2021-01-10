#ifndef _SIGNAL_H_
#define _SIGNAL_H_
#include "Holder.h"

template<class ...Args>
class Signal
{
public:
	void operator()(Args&&...args);
	void emit(Args&&...args);
	void disconnect();

	template<class Object, class Function>
	void connect(Object* obj, Function func);

	template<class Function>
	void connect(Function&& func);

private:
	std::function<void(Args...)> mFunction;
};

template<class ...Args>
void Signal<Args...>::operator()(Args&& ... args)
{
	mFunction(args...);
}

template<class ...Args>
inline void Signal<Args...>::emit(Args&& ...args)
{
	mFunction(args...);
}

template<class ...Args>
inline void Signal<Args...>::disconnect()
{
	mFunction = nullptr;
}

template<class ...Args> template<class Object, class Function>
inline void Signal<Args...>::connect(Object* obj, Function func)
{
	mFunction = Holder<sizeof...(Args)>::bind(obj, func);
}

template<class ...Args> template<class Function>
inline void Signal<Args...>::connect(Function&& func)
{
	mFunction = func;
}

#endif // !_SIGNAL_H_


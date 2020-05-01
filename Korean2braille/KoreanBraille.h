#ifndef __KOREANBRAILLE_H__
#define __KOREANBRAILLE_H__
#include <bitset>
#include <string>
#include <vector>
class KoreanBraille
{
public:
	using braille = std::bitset<12>;
	using braille_set = std::vector<braille>;
	using str = std::wstring;

public:
	KoreanBraille();
	~KoreanBraille();

	braille_set operator()(const str& hangul);
	bool IsConsonant(const braille& bits);

private:
	int getInitial(wchar_t hangul);
	int getMedial(wchar_t hangul);
	int getFinal(wchar_t hangul);

private:
	static const braille mInitial[19];
	static const braille mMedial[21];
	static const braille mFinal[28];
};

#endif // __KOREANBRAILLE_H__

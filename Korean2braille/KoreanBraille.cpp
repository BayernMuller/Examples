#include "KoreanBraille.h"

const KoreanBraille::braille mInitial[19]
{
	0b010000, // ¤¡
	0b000001010000, // ¤¢
	0b110000, // ¤¤
	0b011000, // ¤§
	0b000001011000, // ¤¨
	0b000100, // ¤©
	0b100100, // ¤±
	0b010100, // ¤²
	0b000001010100, // ¤³

};

const KoreanBraille::braille mMedial[21]
{

};

const KoreanBraille::braille mFinal[28]
{

};

KoreanBraille::KoreanBraille()
{
}

KoreanBraille::~KoreanBraille()
{
}

KoreanBraille::braille_set KoreanBraille::operator()(const str& hangul)
{
	return braille_set();
}

bool KoreanBraille::IsConsonant(const braille& bits)
{
	return bits.to_ulong() & 0b111111000000;
}

int KoreanBraille::getInitial(wchar_t hangul)
{
	return (hangul - 0xAC00) / (28 * 21);
}

int KoreanBraille::getMedial(wchar_t hangul)
{
	return ((hangul - 0xAC00) % (28 * 21)) / 28;
}

int KoreanBraille::getFinal(wchar_t hangul)
{
	return (hangul - 0xAC00) % 28;
}

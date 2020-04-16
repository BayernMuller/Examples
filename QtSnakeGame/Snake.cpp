#include "Snake.h"
#include <QPainter>
#include <QKeyEvent>
#include <QDebug>
using namespace Qt;

Snake::Snake(QWidget* parent)
	: QMainWindow(parent), mGame(30u)
{
	setFixedSize(600, 600);
	connect(&mGame, SIGNAL(RefreshWindow()), this, SLOT(update()));
	mGame.StartGame();
}

void Snake::paintEvent(QPaintEvent* event)
{
	QPainter painter;
	painter.begin(this);
	constexpr int size = 20;
	for (const auto& pt : mGame.GetSnake())
	{
		painter.fillRect(pt.first * size, pt.second * size, size, size, green);
	}
	auto item = mGame.GetItem();
	painter.fillRect(item.first * size, item.second * size, size, size, red);
}

void Snake::keyPressEvent(QKeyEvent* event)
{
	int key = event->key();
	if (!(Key_Left <= key && key <= Key_Down))
	{
		return;
	}
	key -= Key_Left;
	mGame.SetDirection(key);
	qDebug() << key;
	update();
}


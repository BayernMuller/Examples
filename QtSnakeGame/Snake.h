#pragma once
#include <QtWidgets/QMainWindow>
#include "Game.h"

class Snake : public QMainWindow
{
	Q_OBJECT

public:
	Snake(QWidget *parent = Q_NULLPTR);
	void paintEvent(QPaintEvent* event) override;
	void keyPressEvent(QKeyEvent* d) override;


private:
	Game mGame;
};

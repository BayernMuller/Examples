#include "Game.h"
#include <chrono>

Game::Game(size_t size) 
	: mSize(size), mpThread(nullptr), mbFlag(false)
{
	srand((uint)time(NULL));
}

Game::~Game()
{
	EndGame();
}

bool Game::IsEatable()
{
	return mItem == *mSnake.begin();
}

Game::Point Game::GetMoved(Point pt, eDirection dir)
{
	int row[] = { -1,0,1,0 };
	int col[] = { 0,-1,0,1 };
	int direction = int(dir);
	return Point(pt.first + row[direction], pt.second + col[direction]);
}

eDirection Game::GetOppose(eDirection dir)
{
	return eDirection((int(dir) + 2) % 4);
}

int Game::MainThread(Game* game)
{
	srand((uint)time(NULL));
	while (game->mbFlag)
	{
		game->Move();
		
		if (game->IsEatable())
		{
			game->AddTail();
			game->SetItem();
		}
		game->RefreshWindow();
		this_thread::sleep_for(100ms);
	}
	return 0;
}

void Game::AddTail()
{
	auto tail = mSnake.back();
	auto prev = *(--(--mSnake.end()));
	for (int i = 0; i < 4; i++)
	{
		if (prev == GetMoved(tail, eDirection(i)))
		{
			mSnake.push_back(GetMoved(tail, GetOppose(eDirection(i))));
			return;
		}
	}
}

void Game::SetDirection(int dir)
{
	if (int(GetOppose(mDir)) == dir)
	{
		return;
	}
	mDir = eDirection(dir);
}

void Game::StartGame()
{
	int pos = mSize / 2;
	mSnake.push_back(make_pair(pos, pos));
	mSnake.push_back(make_pair(pos, pos - 1));
	mDir = eDirection::Up;
	mbFlag = true;
	mpThread = new std::thread(MainThread, this);
	SetItem();
}

void Game::EndGame()
{
	mbFlag = false;
	if (mpThread)
	{
		mpThread->join();
		delete mpThread;
		mpThread = nullptr;
	}
	mSnake.clear();
}

void Game::Move()
{
	mSnake.push_front(GetMoved(*mSnake.begin(), mDir));
	mSnake.erase(--mSnake.end());
}

void Game::SetItem()
{
	mItem.first = rand() % mSize;
	mItem.second = rand() % mSize;
}

bool Game::IsDead()
{
	auto head = mSnake.front();
	if (head.first < 0 || head.first >= mSize || head.second < 0 || head.second >= mSize)
		return true;
	for (auto itr = ++mSnake.begin(); itr != mSnake.end(); itr++)
	{
		if (*itr == head)
			return true;
	}
	return false;
}


#include <stdio.h>
#include <Windows.h> // system 함수를 사용하기 위해 추가
#define SIZE 8
#define EMPTY ' '
char queue[SIZE] = { EMPTY, }; // EMPTY (공백으로 초기화)
int front, rear; 

void print_queue()
{
	char* q = queue;
	printf("\n");
	printf("\t,---, ,---, ,---,\n");
	printf("\t| %c | | %c | | %c |\n", q[0], q[1], q[2]);
	printf("\t`-0-` `-1-` `-2-`\n");
	printf("\t,---,       ,---,\n");
	printf("\t| %c |       | %c |\n", q[7], q[3]);
	printf("\t`-7-`       `-3-`\n");
	printf("\t,---, ,---, ,---,\n");
	printf("\t| %c | | %c | | %c |\n", q[6], q[5], q[4]);
	printf("\t`-6-` `-5-` `-4-`\n");
}

int isFull()
{
	return (rear + 1) % SIZE == front; // 원형 큐가 꽉찰 조건
}

int isEmpty()
{
	return front == rear; // 원형 큐가 비어있을 조건
}

char EnQueue(char data) // data를 받아서
{
	queue[rear] = data; // rear 에 집어넣고
	rear = (rear + 1) % SIZE; // rear 갱신
	return data; // 받은 data그대로 리턴
}

char DeQueue() 
{
	char temp = queue[front]; // front의 원소 임시 저장
	queue[front] = EMPTY; // front의 원소 지우기
	front = (front + 1) % SIZE; // front 갱신
	return temp; // 지워버린 원소 리턴
}
int main()
{
	char input = 0;
	front = rear = 0; // 0으로 초기화
	while (1)
	{
		system("cls"); // 화면 지우기
		printf("[상태] : ");
		if (input == '9') 
		{
			break; // 무한루프를 빠져나가서 프로그램 종료
		}
		else if (input == '0')
		{
			if (!isEmpty()) // 비어있지 않으면
				printf("삭제한 원소 : %c\n", DeQueue()); // 원소 삭제
			else // 비어있으면
				printf("삭제 할 원소가 없음\n"); // 언더플로우 메세지
		}
		else if (input) // input != 0
		{
			if (!isFull()) // 꽉 차지 않았으면
				printf("추가한 원소 : %c\n", EnQueue(input)); // 원소 추가
			else // 꽉 찼으면
				printf("큐가 꽉 찼음.\n"); // 오버플로우 메세지
		}
		else // input == 0
		{
			printf("초기 상태\n");
		}
		puts("\n\n삽입하실 원소를 입력하세요.");
		puts("0을 입력하면 원소를 pop합니다.");
		puts("프로그램을 종료하려면 9를 입력하세요.\n");
		printf("\trear = %d / front = %d", rear, front);
		print_queue();
		printf("\n\n입력 : ");
		scanf(" %c", &input);
	}
}
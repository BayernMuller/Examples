#include <stdio.h>
#include <Windows.h> // system �Լ��� ����ϱ� ���� �߰�
#define SIZE 8
#define EMPTY ' '
char queue[SIZE] = { EMPTY, }; // EMPTY (�������� �ʱ�ȭ)
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
	return (rear + 1) % SIZE == front; // ���� ť�� ���� ����
}

int isEmpty()
{
	return front == rear; // ���� ť�� ������� ����
}

char EnQueue(char data) // data�� �޾Ƽ�
{
	queue[rear] = data; // rear �� ����ְ�
	rear = (rear + 1) % SIZE; // rear ����
	return data; // ���� data�״�� ����
}

char DeQueue() 
{
	char temp = queue[front]; // front�� ���� �ӽ� ����
	queue[front] = EMPTY; // front�� ���� �����
	front = (front + 1) % SIZE; // front ����
	return temp; // �������� ���� ����
}
int main()
{
	char input = 0;
	front = rear = 0; // 0���� �ʱ�ȭ
	while (1)
	{
		system("cls"); // ȭ�� �����
		printf("[����] : ");
		if (input == '9') 
		{
			break; // ���ѷ����� ���������� ���α׷� ����
		}
		else if (input == '0')
		{
			if (!isEmpty()) // ������� ������
				printf("������ ���� : %c\n", DeQueue()); // ���� ����
			else // ���������
				printf("���� �� ���Ұ� ����\n"); // ����÷ο� �޼���
		}
		else if (input) // input != 0
		{
			if (!isFull()) // �� ���� �ʾ�����
				printf("�߰��� ���� : %c\n", EnQueue(input)); // ���� �߰�
			else // �� á����
				printf("ť�� �� á��.\n"); // �����÷ο� �޼���
		}
		else // input == 0
		{
			printf("�ʱ� ����\n");
		}
		puts("\n\n�����Ͻ� ���Ҹ� �Է��ϼ���.");
		puts("0�� �Է��ϸ� ���Ҹ� pop�մϴ�.");
		puts("���α׷��� �����Ϸ��� 9�� �Է��ϼ���.\n");
		printf("\trear = %d / front = %d", rear, front);
		print_queue();
		printf("\n\n�Է� : ");
		scanf(" %c", &input);
	}
}
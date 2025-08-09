import datetime
import random

all_task = []
class Task:
	def addTask(self, description):
		self.description = description
		self.status = 'Todo'
		self.created_datetime = self.get_current_datetime()
		self.last_modified_datetime = self.get_current_datetime()
		self.id = self.get_unique_number()

	def print_task(self):
		print(f'Id : {self.id}')
		print(f'Description : {self.description}')
		print(f'Status : {self.status}')
		print(f'Created DateTime : {self.created_datetime}')
		print(f'Last Modified DateTime : {self.last_modified_datetime}')

	def get_current_datetime(self):
		return datetime.datetime.now()

	def get_unique_number(self):
		list_size = len(all_task)
		new_task_number = list_size + 1 #random.randint(1, 100)
		return f"TASK-{new_task_number:05d}"



def main():
	task = Task()
	task.addTask('Go to Prayer')
	task.print_task()

if __name__ == "__main__":
    main()


class node:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks
        self.next = None


class student:
    def __init__(self):
        self.head = None

    def add_begin(self, id, name, marks):
        nn = node(id, name, marks)

        if self.head is None:
            self.head = nn
            print("Student registered successfully")
            return

        nn.next = self.head
        self.head = nn
        print("Student registered successfully")

    def add_end(self, id, name, marks):
        nn = node(id, name, marks)

        if self.head is None:
            self.head = nn
            print("Student registered successfully")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = nn
        print("Student registered successfully")

    def specify_position(self, pos, id, name, marks):
        if pos <= 0:
            print("Invalid position")
            return

        if pos == 1:
            self.add_begin(id, name, marks)
            return

        nn = node(id, name, marks)
        temp = self.head
        i = 1

        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
            return

        nn.next = temp.next
        temp.next = nn

        print("Student registered successfully")

    def remove_student(self, id):
        if self.head is None:
            print("Student list is empty")
            return

        if self.head.id == id:
            self.head = self.head.next
            print("Student removed successfully")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.id == id:
                temp.next = temp.next.next
                print("Student removed successfully")
                return

            temp = temp.next

        print("Student ID not found")

    def search(self, id):
        if self.head is None:
            print("Student list is empty")
            return

        temp = self.head
        pos = 1

        while temp is not None:
            if temp.id == id:
                print("Student ID:", temp.id)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                print("Position:", pos)
                return

            temp = temp.next
            pos += 1

        print("Student ID not found")

    def display(self):
        if self.head is None:
            print("Student list is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.id, "→", temp.name, "→", temp.marks)
            temp = temp.next

    def count_students(self):
        temp = self.head
        c = 0

        while temp is not None:
            c += 1
            temp = temp.next

        print("Total students:", c)

    def highest_marks(self):
        if self.head is None:
            print("Student list is empty")
            return

        temp = self.head
        highest = temp

        while temp is not None:
            if temp.marks > highest.marks:
                highest = temp

            temp = temp.next

        print("Student with highest marks:")
        print("Student ID:", highest.id)
        print("Name:", highest.name)
        print("Marks:", highest.marks)

    def reverse(self):
        if self.head is None:
            print("Student list is empty")
            return

        prev = None
        temp = self.head

        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

        print("Registration order reversed")


Student = student()

while True:
    print("\n----- Student Record Manager -----")
    print("1. Register student at beginning")
    print("2. Register student at end")
    print("3. Register student at position")
    print("4. Remove student using ID")
    print("5. Search student using ID")
    print("6. Display all students")
    print("7. Display total students")
    print("8. Find student with highest marks")
    print("9. Reverse registration order")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))

            Student.add_begin(id, name, marks)

        case 2:
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))

            Student.add_end(id, name, marks)

        case 3:
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            position = int(input("Enter position: "))

            Student.specify_position(position, id, name, marks)

        case 4:
            id = int(input("Enter student ID to remove: "))

            Student.remove_student(id)

        case 5:
            id = int(input("Enter student ID to search: "))

            Student.search(id)

        case 6:
            Student.display()

        case 7:
            Student.count_students()

        case 8:
            Student.highest_marks()

        case 9:
            Student.reverse()

        case 10:
            print("Exiting Student Record Manager...")
            break

        case _:
            print("Invalid choice")

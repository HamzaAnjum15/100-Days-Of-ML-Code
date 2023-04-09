class Record:
    def __init__(self, id, name, date, roomtype):
        self.name = name
        self.id = id
        self.date = date
        self.roomtype = roomtype
        self.next = None

class RecordBook:
    def __init__(self):
        self.head = None

    def insert_room(self, id, name, date, roomtype):
        new_room = Record(id, name, date, roomtype)
        if not self.head:
            self.head = new_room
        else:
            current_room = self.head
            while current_room.next:
                current_room = current_room.next
            current_room.next = new_room

    def delete_room(self, id):
        if not self.head:
            return
        if self.head.id == id:
            self.head = self.head.next
            return
        current_room = self.head
        while current_room.next:
            if current_room.next.id == id:
                current_room.next = current_room.next.next
                return
            current_room = current_room.next

    def search_room(self, id):
        current_room = self.head
        while current_room:
            if current_room.id == id:
                return current_room
            current_room = current_room.next
        return None

    def display_rooms(self):
        if not self.head:
            print("No reservations yet!")
            return
        current_room = self.head
        while current_room:
            print(f"{current_room.id}, {current_room.name}, {current_room.date}, {current_room.roomtype}")
            current_room = current_room.next

def main():
    my_book = RecordBook()
    while True:
        print("Record Book Menu")
        print("1. Insert a room")
        print("2. Delete a room")
        print("3. Search for a room")
        print("4. Display all rooms")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("Enter the room's id: ")
            name = input("Enter your name: ")
            date = input("Enter date: ")
            roomtype = input("Enter room type: ")
            my_book.insert_room(id, name, date, roomtype)
        elif choice == "2":
            name = input("Enter the room id you want to delete: ")
            my_book.delete_room(id)
        elif choice == "3":
            name = input("Enter the id of the room you want to search: ")
            found_room = my_book.search_room(id)
            if found_room:
                print(f"{found_room.id}, {found_room.name}, {found_room.date}, {found_room.roomtype}")
            else:
                print("Room not found.")
        elif choice == "4":
            my_book.display_rooms()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

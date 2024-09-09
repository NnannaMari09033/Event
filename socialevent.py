print("Welcome to social events organizers!")

event_manager = []

while True:
  command = input("select 'create' to create event (or 'cancel' to quit event) (or 'view' to view all events) (or 'search' to search events by title) (or 'quit' to stop an event): ")
  if command == "create":
    Title = input("Enter the event's title: ")
    Organizer_name = input("Enter the organizer's name: ")
    Organizer_age = int(input("Enter the organizer's age: "))
    Organizer_gender = input("Enter the organizer's gender: ")
    Event_date = input("Enter the event date (YYYY-MM-DD): ")
    Event_location = input("Enter the event location: ")
    Max_attendees = int(input("Enter the maximum number of attendees: "))

  
    event_manager.append({"Title": Title, "Organizer_name": Organizer_name, "Organizer_age": Organizer_age, "Organizer_gender": Organizer_gender, "Event_date": Event_date, "Event_location": Event_location, "Max_attendees": Max_attendees})
    print(event_manager)
    print("Congratulations!! your events has been creatd successfully")
  
  if command == "cancel":
    Title = input("Please select the event to cancel: ")

    for event in event_manager:
      # if event["Title"] == Title:
        event_manager.remove(event)
        print("Event has been cancelled successfully")
        break
    else:
      print("Sorry, no event found with that title")
  if command == "view":
     print("List of all the events: ")
    
     print(f"Title: {event['Title']}, Organizer_name: {event['Organizer_name']}, Organizer_age: {event['Organizer_age']}, Organizer_gender: {event['Organizer_gender']}, Event_date: {event['Event_date']}, Event_location: {event['Event_location']}, Max_attendees: {event['Max_attendees']}")

  if command == "search":
    Title = input("Please enter the name of the event you want to search for: ")
    for event in event_manager:
      # if event["Title"] == Title:
        print(f"Title: {event['Title']}, Organizer_name: {event['Organizer_name']}, Organizer_age: {event['Organizer_age']}, Organizer_gender: {event['Organizer_gender']}, Event_date: {event['Event_date']}, Event_location: {event['Event_location']}, Max_attendees: {event['Max_attendees']}")


  if command == "quit":
    break



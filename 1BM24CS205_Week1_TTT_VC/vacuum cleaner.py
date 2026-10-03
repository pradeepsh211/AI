def vacuum_cleaner(rooms, obstacles, battery):
    for room, condition in rooms.items():
        print(f"\nVacuum is in room {room}.")

        if battery <= 0:
            print("Battery is empty. Stopping the vacuum.")
            break

        # Obstacle inside the room
        if room in obstacles:
            print(f"Obstacle found in room {room}.")

            if obstacles[room] == "left":
                print("Obstacle on left. Moving right.")
            elif obstacles[room] == "right":
                print("Obstacle on right. Moving left.")
            else:
                print("Obstacle in front. Moving left or right.")

            print(f"Continuing to clean room {room}.")

        if condition == "dirty":
            rooms[room] = "clean"
            battery -= 1
            print(f"Room {room} cleaned. Battery remaining: {battery}.")
        else:
            print(f"Room {room} is already clean.")

    print("\nFinal room conditions:", rooms)


room_conditions = {
    "A": "dirty",
    "B": "dirty",
    "C": "clean"
}

obstacles = {
    "B": "left"
}

battery_level = 3

vacuum_cleaner(room_conditions, obstacles, battery_level)

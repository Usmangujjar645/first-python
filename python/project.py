def ride_service():
    while True:   # loop chalega jab tak user exit na kare
        print("\n--- Welcome to Ride Service ---")
        print("Press 1: Book a Ride")
        print("Press 2: Check Fare Rate")
        print("Press 3: View Current Services")
        print("Press 4: Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            distance = float(input("Enter distance in km: "))
            print("✅ Your ride is confirmed for", distance, "km.")
        elif choice == 2:
            print("💰 Fare rate is 100 rupees per km.")
        elif choice == 3:
            print("🚗 Current services: Car, Bike, Rickshaw.")
        elif choice == 4:
            print("👋 Thank you for using our service. Goodbye!")
            break   # loop stop kar dega
        else:
            print("❌ Invalid choice, please try again.")

# function call
ride_service()

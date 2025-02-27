/**
 * Command-Line Elevator System
 *
 * Developed by: Member 2
 * - Handles user input via terminal
 * - Calls Elevator class to move floors
 */

import java.util.Scanner;

public class ElevatorMachine {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Select Elevator (A, B, or C):");
        String choice = scanner.next().toUpperCase();

        if (!choice.equals("A") && !choice.equals("B") && !choice.equals("C")) {
            System.out.println("Invalid elevator choice. Exiting...");
            scanner.close();
            return;
        }

        Elevator elevator = new Elevator(choice);
        System.out.println("Elevator " + choice + " selected. You are at floor 0.");

        while (true) {
            System.out.print("Enter floor number (or -1 to exit): ");
            if (!scanner.hasNextInt()) {
                System.out.println("Invalid input. Enter a number.");
                scanner.next(); // Discard invalid input
                continue;
            }

            int floor = scanner.nextInt();

            if (floor == -1) {
                System.out.println("Exiting elevator system.");
                break;
            }

            if (elevator.moveToFloor(floor)) {
                System.out.println("Elevator " + elevator.getDoor() + " moved to floor " + floor);
            } else {
                System.out.println("Invalid floor for Elevator " + elevator.getDoor());
            }
        }

        scanner.close();
    }
}


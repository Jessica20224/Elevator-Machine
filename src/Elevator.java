/**
 * Elevator Class
 *
 * Developed by: Member 1
 * - Defines the Elevator logic for different doors (A, B, C)
 * - Implements movement validation
 */

public class Elevator {
    private int currentFloor;
    private final String door;

    public Elevator(String door) {
        this.currentFloor = 0; // Start at ground floor
        this.door = door;
    }

    public boolean moveToFloor(int floor) {
        if (isValidFloor(floor)) {
            this.currentFloor = floor;
            return true;
        }
        return false;
    }

    private boolean isValidFloor(int floor) {
        return switch (door) {
            case "A" -> floor >= 0 && floor <= 5;
            case "B" -> floor >= 0 && floor <= 8;
            case "C" -> floor >= 0 && floor <= 10;
            default -> false;
        };
    }

    public int getCurrentFloor() {
        return currentFloor;
    }

    public String getDoor() {
        return door;
    }
}

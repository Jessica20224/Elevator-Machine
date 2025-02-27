/**
 * GUI-Based Elevator System
 *
 * Developed by:
 * - Member 3: Created GUI layout and structure
 * - Member 4: Implemented user interaction logic (buttons, events)
 */

import javax.swing.*;
import java.awt.*;

public class ElevatorGUI {
    private JFrame frame;
    private JComboBox<String> elevatorSelector;
    private JTextField floorInput;
    private JTextArea outputArea;
    private JLabel currentFloorLabel;
    private Elevator elevator;

    public ElevatorGUI() {
        frame = new JFrame("Elevator System");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 350);
        frame.setLayout(new FlowLayout());

        JLabel selectLabel = new JLabel("Select Elevator:");
        String[] elevators = {"A", "B", "C"};
        elevatorSelector = new JComboBox<>(elevators);
        JButton selectButton = new JButton("Choose Elevator");

        JLabel floorLabel = new JLabel("Enter Floor:");
        floorInput = new JTextField(5);
        JButton moveButton = new JButton("Move Elevator");
        outputArea = new JTextArea(10, 30);
        outputArea.setEditable(false);
        currentFloorLabel = new JLabel("Current Floor: 0");

        selectButton.addActionListener(e -> {
            String choice = (String) elevatorSelector.getSelectedItem();
            elevator = new Elevator(choice);
            outputArea.setText("Elevator " + choice + " selected. Ready to move.\n");
            updateCurrentFloor();
        });

        moveButton.addActionListener(e -> {
            if (elevator == null) {
                outputArea.append("Select an elevator first!\n");
                return;
            }
            try {
                int floor = Integer.parseInt(floorInput.getText());
                if (elevator.moveToFloor(floor)) {
                    outputArea.append("Elevator " + elevator.getDoor() + " moved to floor " + floor + "\n");
                    updateCurrentFloor();
                } else {
                    outputArea.append("Invalid floor for Elevator " + elevator.getDoor() + "\n");
                }
            } catch (NumberFormatException ex) {
                outputArea.append("Invalid input. Enter a number.\n");
            }
        });

        frame.add(selectLabel);
        frame.add(elevatorSelector);
        frame.add(selectButton);
        frame.add(floorLabel);
        frame.add(floorInput);
        frame.add(moveButton);
        frame.add(currentFloorLabel);
        frame.add(new JScrollPane(outputArea));

        frame.setVisible(true);
    }

    private void updateCurrentFloor() {
        if (elevator != null) {
            currentFloorLabel.setText("Current Floor: " + elevator.getCurrentFloor());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(ElevatorGUI::new);
    }
}


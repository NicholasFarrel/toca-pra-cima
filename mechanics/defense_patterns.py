import pygame

class BeeDefense:
    def __init__(self, scare_radius=80, required_presses=5, press_interval=1000):
        self.scaring_bees = False  # Indicates if the bees are scared
        self.space_press_count = 0  # Counts space presses within the interval
        self.first_press_time = 0  # Records the time of the first space press in the series
        self.press_interval = press_interval  # Allowed interval to complete presses (in ms)
        self.required_presses = required_presses  # Number of presses needed to scare the bees
        self.scare_radius = scare_radius  # Distance within which the bees start defending
        self.space_released = True  # Tracks if space was released before counting again

    def update(self, player_position, swarm_center, keys):
        """Updates defense state based on distance and space presses within the time interval."""
        # Calculate distance between player and swarm center
        distance_to_swarm = player_position.distance_to(swarm_center)

        # Check if player is within the scare radius
        if distance_to_swarm < self.scare_radius:
            print("Player is within scare radius.")
            # Check if space was pressed only after being released
            if keys[pygame.K_SPACE] and self.space_released:
                current_time = pygame.time.get_ticks()

                # If it's the first press in a series, record the time
                if self.space_press_count == 0:
                    self.first_press_time = current_time
                    print("Starting a new press series.")

                # Check if total time since the first press exceeds the allowed interval
                if current_time - self.first_press_time > self.press_interval:
                    # Reset count if the total interval for the series is exceeded
                    self.space_press_count = 0
                    self.first_press_time = current_time  # Reset the first press time for the next series
                    self.scaring_bees = False
                    print("Total series interval exceeded. Resetting press count.")

                # Update last press time, increment the press count, and mark space as not released
                self.space_press_count += 1
                self.space_released = False  # Space is now considered held down
                print(f"Space pressed. Current count: {self.space_press_count}")

                # Activate scaring only if the required number of presses is met within the interval
                if self.space_press_count >= self.required_presses:
                    self.scaring_bees = True
                    self.space_press_count = 0  # Reset counter after successful scare
                    print("Bees are scared away!")
                    return  # Early return to prevent further presses from affecting state
            elif not keys[pygame.K_SPACE]:
                # Mark space as released once it's no longer pressed
                self.space_released = True
        else:
            # Reset if player moves out of scare radius
            self.scaring_bees = False
            self.space_press_count = 0  # Also reset the press count
            self.space_released = True  # Reset space release state
            print("Player is outside scare radius. Resetting scaring state.")

    def is_movement_blocked(self, player_position, swarm_center):
        """Returns True if movement is blocked due to proximity of the bees and not scared."""
        distance_to_swarm = player_position.distance_to(swarm_center)
        return distance_to_swarm < self.scare_radius and not self.scaring_bees

    def reset(self):
        """Resets the scaring state after bees are scared away."""
        self.scaring_bees = False

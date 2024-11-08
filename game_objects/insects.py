import pygame
import random

class BeeSwarm:
    def __init__(self, screen_width, screen_height, num_bees=10, swarm_radius=50, speed=2, scare_distance=100, scare_radius=80):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_bees = num_bees  # Number of bees in the swarm
        self.swarm_radius = swarm_radius  # Radius for individual bees to hover around the swarm center
        self.speed = speed  # Speed of the swarm's central position moving toward the player
        self.scare_distance = scare_distance  # Distance the swarm moves away when scared
        self.scare_radius = scare_radius  # Distance within which the swarm gets scared if space is pressed
        self.swarm_center = pygame.Vector2(screen_width / 2, screen_height / 2)  # Initial swarm center position
        self.bees = [pygame.Vector2(self.swarm_center.x + random.uniform(-swarm_radius, swarm_radius),
                                    self.swarm_center.y + random.uniform(-swarm_radius, swarm_radius))
                     for _ in range(num_bees)]
        self.scared = False  # State indicating if the swarm is "scared"
        self.scare_timer = 0  # Timer for the scared effect duration
        self.bee_size = 6  # Size of each bee's square

    def update(self, player_position, scaring_bees):
        # Check if the player is trying to scare the swarm and if the swarm is within the scare radius
        distance_to_player = self.swarm_center.distance_to(player_position)
        if scaring_bees and distance_to_player < self.scare_radius:
            self.scared = True
            self.scare_timer = 60  # Set the duration of the "scared" state (in frames)

        # Update the position of the swarm's center
        if self.scared:
            # Move the swarm center away from the player when scared
            direction = self.swarm_center - player_position
            direction.normalize_ip()
            self.swarm_center += direction * self.scare_distance * 0.05
        else:
            # Move the swarm center towards the player
            direction = player_position - self.swarm_center
            if distance_to_player > self.swarm_radius:
                direction.normalize_ip()
                self.swarm_center += direction * self.speed

        # Update each bee's position around the swarm center to create a "block" effect
        for i in range(self.num_bees):
            # Small oscillations around the swarm center
            offset = pygame.Vector2(random.uniform(-self.swarm_radius, self.swarm_radius),
                                    random.uniform(-self.swarm_radius, self.swarm_radius))
            self.bees[i] = self.swarm_center + offset

        # Decrease the scared state timer
        if self.scared:
            self.scare_timer -= 1
            if self.scare_timer <= 0:
                self.scared = False

    def render(self, screen):
        # Draw each bee as a small square half black and half yellow
        for bee_position in self.bees:
            # Define the rectangles for the two halves of the bee
            left_half = pygame.Rect(int(bee_position.x), int(bee_position.y), self.bee_size // 2, self.bee_size)
            right_half = pygame.Rect(int(bee_position.x) + self.bee_size // 2, int(bee_position.y), self.bee_size // 2, self.bee_size)

            # Draw the left half as black
            pygame.draw.rect(screen, (0, 0, 0), left_half)
            # Draw the right half as yellow
            pygame.draw.rect(screen, (255, 255, 0), right_half)

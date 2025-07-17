# Asteroids

This is a classic arcade-style game where you control a spaceship navigating through an asteroid field. Your mission is to destroy incoming asteroids while avoiding collisions.

### What it does
It simulates a spaceship moving through a dynamic field of asteroids. The player can control the spaceship's movement and fire projectiles to destroy the asteroids. It also handles collisions between your ship and asteroids, leading to a "game over" state if your ship is destroyed.

### How it works
The game uses a game loop to continuously update the positions of all objects (spaceship, asteroids, projectiles) and handle player input. Objects are represented as classes with properties like position, velocity, and rotation. Collision detection algorithms are used to determine when a projectile hits an asteroid or when the spaceship collides with an asteroid. When an asteroid is destroyed, new, smaller asteroids may spawn from its remnants.

### Features
- Player-controlled spaceship with directional movement and firing.
- Dynamically generated asteroids that break into smaller pieces when hit.

## Upcoming Features
- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

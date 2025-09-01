#!/usr/bin/env python3
"""
Photorealistic Aerial Drone Video Simulation
Creates a true-to-life aerial view of drone spraying with grass, realistic farm, and proper perspective
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Ellipse
import numpy as np
import os
import random
import math

class PhotorealisticAerialDroneSimulation:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(20, 16))
        self.frame_count = 0
        self.total_frames = 200
        
        # Enhanced drone parameters for aerial view
        self.drone_x = 2
        self.drone_y = 12
        self.drone_altitude = 8.0  # Much higher for proper aerial perspective
        self.drone_size_scale = 1.0  # Will adjust based on altitude
        
        # Realistic farm dimensions
        self.farm_width = 25
        self.farm_height = 18
        
        # Farm elements
        self.tomato_rows = []
        self.grass_patches = []
        self.create_photorealistic_farm()
        
        # Enhanced spray system
        self.water_particles = []
        self.spray_active = False
        
        # Create output directory
        self.output_dir = "photorealistic_aerial_frames"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def create_photorealistic_farm(self):
        """Create a photorealistic farm with grass, pathways, and natural layout"""
        
        # Create grass background patches
        # Reduce grass density and brightness for better tomato/drone visibility
        for i in range(20):
            grass_x = random.uniform(0, self.farm_width)
            grass_y = random.uniform(0, self.farm_height)
            grass_size = random.uniform(0.7, 1.5)
            self.grass_patches.append({
                'x': grass_x,
                'y': grass_y,
                'size': grass_size,
                'shade': random.uniform(0.15, 0.35)
            })
        
        # Create tomato crop rows with realistic agricultural spacing
        row_spacing = 2.5  # 2.5 meters between rows (industry standard)
        plant_spacing = 1.0  # 1 meter between plants in row
        
        for row_num in range(6):  # 6 rows of tomatoes
            row_y = 3 + (row_num * row_spacing)
            tomato_row = []
            
            for plant_num in range(20):  # 20 plants per row
                plant_x = 2 + (plant_num * plant_spacing)
                
                # Natural variation in positioning
                actual_x = plant_x + random.uniform(-0.2, 0.2)
                actual_y = row_y + random.uniform(-0.15, 0.15)
                
                plant = {
                    'x': actual_x,
                    'y': actual_y,
                    'health': random.uniform(0.7, 1.0),
                    'size': random.uniform(0.8, 1.2),
                    'tomato_count': random.randint(5, 12),
                    'water_received': 0,
                    'soil_moisture': random.uniform(0.4, 0.7),
                    'growth_stage': random.uniform(0.8, 1.0)
                }
                tomato_row.append(plant)
            self.tomato_rows.append(tomato_row)
    
    def draw_realistic_farm_base(self):
        """Draw the realistic farm base with grass and pathways"""
        
        # Sky gradient (much more visible from aerial view)
        sky_colors = ['#87CEEB', '#B0E0E6', '#E0F6FF']
        for i, color in enumerate(sky_colors):
            sky_rect = patches.Rectangle((0, 15 + i), self.farm_width, 3, 
                                       facecolor=color, alpha=0.8)
            self.ax.add_patch(sky_rect)
        
        # Base grass field (realistic green field)
        base_field = patches.Rectangle((0, 0), self.farm_width, self.farm_height, 
                                     facecolor='#228B22', alpha=0.6)
        self.ax.add_patch(base_field)
        
        # Grass texture patches (creates realistic field appearance)
        for grass in self.grass_patches:
            grass_color = ['#32CD32', '#228B22', '#90EE90', '#7CFC00'][random.randint(0, 3)]
            grass_patch = Circle((grass['x'], grass['y']), grass['size'] * 0.3,
                               facecolor=grass_color, alpha=grass['shade'])
            self.ax.add_patch(grass_patch)
        
        # Farm pathways (dirt roads between crop areas)
        # Main pathway (horizontal)
        main_path = patches.Rectangle((0, 1), self.farm_width, 0.8, 
                                    facecolor='#CD853F', alpha=0.8)
        self.ax.add_patch(main_path)
        
        # Side pathway (vertical)
        side_path = patches.Rectangle((1, 0), 0.6, self.farm_height, 
                                    facecolor='#CD853F', alpha=0.6)
        self.ax.add_patch(side_path)
        
        # Irrigation channels (realistic blue water lines)
        for row in range(6):
            channel_y = 2.8 + (row * 2.5)
            self.ax.plot([2, 22], [channel_y, channel_y], 
                        color='#4169E1', linewidth=3, alpha=0.7)
        
        # Farm boundary fence (wooden posts and wire)
        fence_posts_x = list(range(0, self.farm_width + 1, 3))
        fence_posts_y = list(range(0, self.farm_height + 1, 3))
        
        # Perimeter fence
        perimeter = [(0, 0), (self.farm_width, 0), (self.farm_width, self.farm_height), 
                    (0, self.farm_height), (0, 0)]
        fence_x = [p[0] for p in perimeter]
        fence_y = [p[1] for p in perimeter]
        self.ax.plot(fence_x, fence_y, color='#8B4513', linewidth=4, alpha=0.9)
        
        # Farm buildings (storage shed)
        shed = patches.Rectangle((22, 16), 2.5, 1.5, 
                               facecolor='#A0522D', edgecolor='#654321', linewidth=2)
        self.ax.add_patch(shed)
        shed_roof = Polygon([(22, 17.5), (23.25, 18.2), (24.5, 17.5)], 
                           facecolor='#8B0000', alpha=0.9)
        self.ax.add_patch(shed_roof)
        
        # Water tank
        tank = Circle((23, 1), 0.8, facecolor='silver', edgecolor='gray', linewidth=2)
        self.ax.add_patch(tank)
    
    def draw_aerial_perspective_drone(self, x, y, altitude):
        """Draw drone from proper aerial perspective - viewed from above"""
        
        # Calculate size based on altitude (aerial perspective)
        perspective_scale = 2.8 / (1 + altitude * 0.05)  # Larger for clarity

        # Drone main body (larger, more visible)
        body_size = 1.3 * perspective_scale

        # Main frame (carbon fiber X-pattern visible from above)
        # Central hub
        central_hub = Circle((x, y), 0.28 * perspective_scale, 
                           facecolor='#1a1a1a', edgecolor='#333333', linewidth=3)
        self.ax.add_patch(central_hub)

        # Four arms in X-configuration (thicker, more visible)
        arm_length = 1.2 * perspective_scale
        arm_angles = [45, 135, 225, 315]  # X-pattern
        rotor_positions = []

        for angle in arm_angles:
            angle_rad = np.radians(angle)
            arm_end_x = x + arm_length * np.cos(angle_rad)
            arm_end_y = y + arm_length * np.sin(angle_rad)
            rotor_positions.append((arm_end_x, arm_end_y))

            # Draw arm (thicker, with shadow)
            self.ax.plot([x, arm_end_x], [y, arm_end_y], 
                        color='#111', linewidth=13 * perspective_scale, alpha=0.85, zorder=2)
            self.ax.plot([x, arm_end_x], [y, arm_end_y], 
                        color='#444444', linewidth=7 * perspective_scale, alpha=0.8, zorder=3)
        
        # Rotors (viewed from above - circular with motion blur)
        rotor_radius = 0.55 * perspective_scale  # Larger rotors
        for i, (rotor_x, rotor_y) in enumerate(rotor_positions):
            # Rotor disc (spinning effect)
            rotor_disc = Circle((rotor_x, rotor_y), rotor_radius, 
                               facecolor='lightgray', alpha=0.5, edgecolor='black', linewidth=2)
            self.ax.add_patch(rotor_disc)
            # Motion blur rings (multiple circles for spinning effect)
            for ring in range(4):
                blur_radius = rotor_radius * (0.7 + ring * 0.13)
                blur_alpha = 0.32 - ring * 0.07
                blur_ring = Circle((rotor_x, rotor_y), blur_radius, 
                                 facecolor='none', edgecolor='gray', 
                                 alpha=blur_alpha, linewidth=2)
                self.ax.add_patch(blur_ring)
            # Propeller blades (top view - lines)
            prop_rotation = self.frame_count * 45 + i * 90
            for blade_offset in [0, 120, 240]:
                blade_angle = prop_rotation + blade_offset
                blade_rad = np.radians(blade_angle)
                blade_tip_x = rotor_x + rotor_radius * 0.95 * np.cos(blade_rad)
                blade_tip_y = rotor_y + rotor_radius * 0.95 * np.sin(blade_rad)
                self.ax.plot([rotor_x, blade_tip_x], [rotor_y, blade_tip_y], 
                           color='black', linewidth=3.5 * perspective_scale, alpha=0.7)
        
        # Gimbal camera (small black square underneath, visible from above)
        camera_size = 0.22 * perspective_scale
        camera = patches.Rectangle((x - camera_size/2, y - camera_size/2), 
                                 camera_size, camera_size,
                                 facecolor='black', edgecolor='silver', linewidth=2)
        self.ax.add_patch(camera)

        # GPS antenna (small orange circle on top)
        gps = Circle((x, y + 0.13 * perspective_scale), 0.07 * perspective_scale, 
                    facecolor='orange', edgecolor='darkorange', linewidth=1.5)
        self.ax.add_patch(gps)

        # Navigation LEDs (visible from above)
        # Front LED (green)
        front_led = Circle((x, y + 0.38 * perspective_scale), 0.045 * perspective_scale, 
                          facecolor='lime', alpha=0.95)
        self.ax.add_patch(front_led)
        # Rear LED (red)
        rear_led = Circle((x, y - 0.38 * perspective_scale), 0.045 * perspective_scale, 
                         facecolor='red', alpha=0.95)
        self.ax.add_patch(rear_led)

        # Drone shadow on ground (realistic aerial shadow)
        shadow_scale = perspective_scale * (1 + altitude * 0.08)
        shadow = Circle((x + 0.7, y - 0.7), shadow_scale * 1.1, 
                       facecolor='black', alpha=0.13)
        self.ax.add_patch(shadow)

        # Flight status indicators (floating above drone)
        status_x = x + 2.0
        status_y = y + 1.8

        # Altitude display
        self.ax.text(status_x, status_y, f'🚁 ALT: {altitude:.1f}m', 
                    fontsize=12, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.4", facecolor="yellow", alpha=0.95))

        # Flight mode
        if 30 < self.frame_count < 170:
            mode = "SPRAYING"
            mode_color = "lightgreen"
        elif self.frame_count <= 30:
            mode = "PATROL"
            mode_color = "orange"
        else:
            mode = "RTH"
            mode_color = "lightblue"

        self.ax.text(status_x, status_y - 0.4, f'Mode: {mode}', 
                    fontsize=11, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=mode_color, alpha=0.9))

        # Battery status
        battery = max(15, 100 - (self.frame_count / self.total_frames) * 20)
        battery_color = 'green' if battery > 60 else 'orange' if battery > 30 else 'red'
        self.ax.text(status_x, status_y - 0.8, f'BAT: {battery:.0f}%', 
                    fontsize=10, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=battery_color, alpha=0.9))
    
    def draw_aerial_water_spray(self, drone_x, drone_y, altitude):
        """Draw realistic water spray from aerial perspective"""
        
        if 30 < self.frame_count < 170:  # Active spraying period
            self.spray_active = True
            
            # Spray boom (horizontal bar visible from above)
            boom_width = 2.0
            boom_y_offset = -0.6
            boom_start_x = drone_x - boom_width/2
            boom_end_x = drone_x + boom_width/2
            boom_y = drone_y + boom_y_offset
            
            # Draw spray boom
            self.ax.plot([boom_start_x, boom_end_x], [boom_y, boom_y], 
                        color='darkblue', linewidth=6, alpha=0.8)
            
            # Multiple spray nozzles along boom
            nozzle_count = 6
            for i in range(nozzle_count):
                nozzle_x = boom_start_x + (i * boom_width / (nozzle_count - 1))
                nozzle_y = boom_y
                
                # Nozzle point
                nozzle = Circle((nozzle_x, nozzle_y), 0.03, 
                               facecolor='darkblue', edgecolor='black')
                self.ax.add_patch(nozzle)
                
                # Water spray pattern (aerial view shows wider coverage)
                spray_radius = 1.5 + altitude * 0.1  # Larger spray at higher altitude
                num_droplets = 30
                
                for j in range(num_droplets):
                    # Random spray pattern within radius
                    angle = random.uniform(0, 2 * np.pi)
                    distance = random.uniform(0.2, spray_radius)
                    
                    drop_x = nozzle_x + distance * np.cos(angle)
                    drop_y = nozzle_y + distance * np.sin(angle)
                    
                    # Water droplet size varies with distance
                    droplet_size = max(0.01, 0.04 - distance * 0.01)
                    
                    # Droplet color varies (more transparent farther out)
                    droplet_alpha = max(0.3, 0.9 - distance * 0.2)
                    
                    droplet = Circle((drop_x, drop_y), droplet_size,
                                   facecolor='lightblue', alpha=droplet_alpha)
                    self.ax.add_patch(droplet)
                
                # Spray cone outline (visible coverage area)
                spray_cone = Circle((nozzle_x, nozzle_y), spray_radius,
                                  facecolor='lightblue', alpha=0.1, 
                                  edgecolor='blue', linestyle='--')
                self.ax.add_patch(spray_cone)
            
            # Coverage indicator
            total_coverage = boom_width * 2  # Total coverage width
            self.ax.text(drone_x - 3, drone_y + 2, 
                        f'💧 PRECISION SPRAYING\nCoverage: {total_coverage:.1f}m width\nFlow: 2.4 L/min/nozzle', 
                        fontsize=12, fontweight='bold', ha='center',
                        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.9))
        else:
            self.spray_active = False
    
    def draw_photorealistic_tomato_crops(self):
        """Draw photorealistic tomato crops from aerial view"""
        
        for row_idx, row in enumerate(self.tomato_rows):
            for plant_idx, plant in enumerate(row):
                x, y = plant['x'], plant['y']
                health = plant['health']
                size = plant['size']
                
                # Soil mound around plant (visible from above)
                soil_moisture_color = '#8B4513' if plant['soil_moisture'] < 0.5 else '#A0522D'
                soil_mound = Circle((x, y), 0.4 * size, 
                                  facecolor=soil_moisture_color, alpha=0.8)
                self.ax.add_patch(soil_mound)
                
                # Plant canopy (aerial view - circular green area)
                canopy_radius = 0.45 * size * health  # Larger canopy for visibility
                if health > 0.8 and plant['water_received'] > 0.3:
                    canopy_color = '#1e7a1e'  # Deeper green
                elif health > 0.6:
                    canopy_color = '#2ecc40'  # Brighter green
                else:
                    canopy_color = '#bada55'  # Pale green (stressed)

                plant_canopy = Circle((x, y), canopy_radius,
                                    facecolor=canopy_color,
                                    edgecolor='darkgreen',
                                    linewidth=2, alpha=0.95)
                self.ax.add_patch(plant_canopy)

                # Leaf texture (larger, more visible spots)
                leaf_spots = int(7 * size * health)
                for _ in range(leaf_spots):
                    spot_x = x + random.uniform(-canopy_radius, canopy_radius)
                    spot_y = y + random.uniform(-canopy_radius, canopy_radius)
                    if (spot_x - x)**2 + (spot_y - y)**2 <= canopy_radius**2:
                        leaf_spot = Circle((spot_x, spot_y), 0.03,
                                         facecolor='#145214', alpha=0.7)
                        self.ax.add_patch(leaf_spot)

                # Tomato clusters (much larger and more visible)
                tomato_clusters = max(2, int(plant['tomato_count'] / 2))
                for cluster in range(tomato_clusters):
                    cluster_angle = random.uniform(0, 2 * np.pi)
                    cluster_distance = random.uniform(0.12, canopy_radius * 0.85)
                    cluster_x = x + cluster_distance * np.cos(cluster_angle)
                    cluster_y = y + cluster_distance * np.sin(cluster_angle)

                    # Tomato cluster (larger red circles)
                    tomatoes_in_cluster = random.randint(3, 5)
                    for t in range(tomatoes_in_cluster):
                        tomato_x = cluster_x + random.uniform(-0.07, 0.07)
                        tomato_y = cluster_y + random.uniform(-0.07, 0.07)

                        # Tomato ripeness
                        ripeness = random.uniform(0.5, 1.0)
                        if ripeness > 0.8:
                            tomato_color = '#e10600'  # Deep ripe red
                        elif ripeness > 0.6:
                            tomato_color = '#ff4d00'  # Orange-red
                        else:
                            tomato_color = '#ffb300'  # Orange

                        tomato = Circle((tomato_x, tomato_y), 0.06,
                                      facecolor=tomato_color, edgecolor='#a80000', linewidth=1, alpha=0.98)
                        self.ax.add_patch(tomato)
                
                # Water effects (visible wetness on canopy)
                if plant['water_received'] > 0.2:
                    wet_spots = int(plant['water_received'] * 8)
                    for _ in range(wet_spots):
                        wet_x = x + random.uniform(-canopy_radius, canopy_radius)
                        wet_y = y + random.uniform(-canopy_radius, canopy_radius)
                        if (wet_x - x)**2 + (wet_y - y)**2 <= canopy_radius**2:
                            water_spot = Circle((wet_x, wet_y), 0.015,
                                              facecolor='lightblue', alpha=0.7)
                            self.ax.add_patch(water_spot)
                
                # Plant health indicator (only for stressed plants)
                if health < 0.7:
                    self.ax.text(x, y - 0.6, '⚠️', fontsize=8, ha='center', alpha=0.8)
    
    def update_aerial_drone_position(self):
        """Update drone position with realistic aerial flight pattern"""
        
        # Professional agricultural flight pattern
        if self.frame_count < 25:
            # Initial positioning and ascent
            self.drone_x = 2 + (self.frame_count / 25) * 2
            self.drone_y = 12 + np.sin(self.frame_count * 0.3) * 0.2
            self.drone_altitude = 4.0 + (self.frame_count / 25) * 4.0
        elif self.frame_count < 75:
            # First systematic pass (left to right)
            progress = (self.frame_count - 25) / 50
            self.drone_x = 4 + progress * 16
            self.drone_y = 10.5 + np.sin(self.frame_count * 0.15) * 0.15
            self.drone_altitude = 8.0
        elif self.frame_count < 125:
            # Second pass (right to left, next row)
            progress = (self.frame_count - 75) / 50
            self.drone_x = 20 - progress * 16
            self.drone_y = 7.5 + np.sin(self.frame_count * 0.15) * 0.15
            self.drone_altitude = 8.0
        elif self.frame_count < 170:
            # Third pass (left to right, final row)
            progress = (self.frame_count - 125) / 45
            self.drone_x = 4 + progress * 16
            self.drone_y = 4.5 + np.sin(self.frame_count * 0.15) * 0.15
            self.drone_altitude = 8.0
        else:
            # Return to landing zone
            progress = (self.frame_count - 170) / 30
            self.drone_x = 20 - progress * 18
            self.drone_y = 12 + progress * 3
            self.drone_altitude = 8.0 - progress * 4.0
        
        # Add slight realistic hover variations
        self.drone_x += np.sin(self.frame_count * 0.4) * 0.08
        self.drone_y += np.cos(self.frame_count * 0.5) * 0.06
    
    def update_crop_irrigation_effects(self):
        """Update plant irrigation effects from aerial spraying"""
        
        if self.spray_active:
            spray_width = 2.5  # Width of spray coverage
            
            for row in self.tomato_rows:
                for plant in row:
                    # Calculate if plant is within spray pattern
                    x_distance = abs(plant['x'] - self.drone_x)
                    y_distance = abs(plant['y'] - self.drone_y)
                    
                    if x_distance < spray_width and y_distance < 2.0:
                        # Water application based on proximity
                        proximity_factor = max(0, 1 - x_distance / spray_width) * max(0, 1 - y_distance / 2.0)
                        water_amount = proximity_factor * 0.08
                        
                        plant['water_received'] = min(plant['water_received'] + water_amount, 1.0)
                        plant['health'] = min(plant['health'] + water_amount * 0.015, 1.0)
                        plant['soil_moisture'] = min(plant['soil_moisture'] + water_amount * 0.12, 1.0)
    
    def create_photorealistic_frame(self):
        """Create a single photorealistic aerial frame"""
        
        self.ax.clear()
        
        # Draw realistic farm base
        self.draw_realistic_farm_base()
        
        # Draw crops
        self.draw_photorealistic_tomato_crops()
        
        # Update and draw drone
        self.update_aerial_drone_position()
        self.draw_aerial_perspective_drone(self.drone_x, self.drone_y, self.drone_altitude)
        
        # Draw spray system
        self.draw_aerial_water_spray(self.drone_x, self.drone_y, self.drone_altitude)
        
        # Update irrigation effects
        self.update_crop_irrigation_effects()
        
        # Enhanced information display
        progress = (self.frame_count / self.total_frames) * 100
        total_plants = sum(len(row) for row in self.tomato_rows)
        irrigated_plants = sum(1 for row in self.tomato_rows for plant in row if plant['water_received'] > 0.3)
        irrigation_percent = (irrigated_plants / total_plants) * 100
        
        # Mission status
        if self.frame_count < 25:
            mission_status = "🛫 TAKEOFF & AERIAL POSITIONING"
            status_color = "orange"
        elif 25 <= self.frame_count < 170:
            mission_status = "🚁 AERIAL PRECISION SPRAYING"
            status_color = "lightgreen"
        else:
            mission_status = "🛬 DESCENDING TO LANDING ZONE"
            status_color = "lightblue"
        
        # Frame information
        frame_info = (f"AERIAL VIEW - Frame {self.frame_count + 1}/{self.total_frames} | "
                     f"Mission Progress: {progress:.1f}% | "
                     f"Plants Irrigated: {irrigated_plants}/{total_plants} ({irrigation_percent:.1f}%)")
        
        self.ax.text(self.farm_width/2, -1.5, frame_info, ha='center', fontsize=16, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.6", facecolor="yellow", alpha=0.95))
        
        self.ax.text(2, -1.5, mission_status, fontsize=14, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.5", facecolor=status_color, alpha=0.95))
        
        # Technical information
        tech_info = (f"Aerial View | Altitude: {self.drone_altitude:.1f}m | "
                    f"Coverage Pattern: Systematic Grid | "
                    f"Spray Width: 2.5m | "
                    f"View: Top-Down Perspective")
        
        self.ax.text(self.farm_width/2, -2.2, tech_info, ha='center', fontsize=12,
                    bbox=dict(boxstyle="round,pad=0.4", facecolor="lightcyan", alpha=0.9))
        
        # Set enhanced axis properties for aerial view
        self.ax.set_xlim(-1, self.farm_width + 1)
        self.ax.set_ylim(-3, self.farm_height + 3)
        self.ax.set_aspect('equal')
        self.ax.set_title('🍅 PHOTOREALISTIC AERIAL DRONE SPRAYING - TOMATO FARM 🚁\n' +
                         'Worldlight Agri Consult - Professional Aerial Agricultural Technology', 
                         fontsize=20, fontweight='bold', pad=30)
        self.ax.grid(True, alpha=0.2, linestyle=':', color='gray')
        
        # Save photorealistic frame
        filename = f"{self.output_dir}/aerial_frame_{self.frame_count:03d}.png"
        self.fig.savefig(filename, dpi=300, bbox_inches='tight', 
                        facecolor='white', edgecolor='none')
        print(f"✅ Created photorealistic aerial frame {self.frame_count + 1}/{self.total_frames}: {filename}")
        
        self.frame_count += 1
    
    def create_photorealistic_video(self):
        """Create the complete photorealistic aerial video sequence"""
        
        print("🎬 Starting PHOTOREALISTIC AERIAL Drone Video Simulation...")
        print("🌱 Enhanced Realistic Features:")
        print("   • Realistic grass field with texture and pathways")
        print("   • True aerial perspective - drone viewed from above")
        print("   • Professional agricultural layout with irrigation")
        print("   • Photorealistic tomato crops with canopy detail")
        print("   • Enhanced spray coverage visualization")
        print("   • Farm buildings, water tank, and infrastructure")
        print("   • Natural lighting and shadow effects")
        print("=" * 90)
        
        for frame in range(self.total_frames):
            self.create_photorealistic_frame()
        
        print("=" * 90)
        print(f"🎉 PHOTOREALISTIC AERIAL VIDEO COMPLETE!")
        print(f"📁 {self.total_frames} aerial frames saved to: {self.output_dir}/")
        print("\n🌱 PHOTOREALISTIC FEATURES ACHIEVED:")
        print("   ✅ Realistic grass field with natural texture")
        print("   ✅ True aerial perspective - viewing from above")
        print("   ✅ Professional drone design visible in air")
        print("   ✅ Authentic agricultural layout and infrastructure")
        print("   ✅ Detailed tomato crop canopies and fruit clusters")
        print("   ✅ Enhanced spray visualization and coverage")
        print("   ✅ Farm pathways, buildings, and water systems")
        print("   ✅ Professional agricultural demonstration quality")
        
        plt.close()

def main():
    print("🚁 WORLDLIGHT AGRI CONSULT - PHOTOREALISTIC AERIAL SIMULATION 🍅")
    print("=" * 90)
    print("🎯 AERIAL PERSPECTIVE: True-to-Life Farm with Grass and Aerial View")
    
    simulation = PhotorealisticAerialDroneSimulation()
    simulation.create_photorealistic_video()
    
    print("\n🎯 READY FOR PROFESSIONAL CLIENT PRESENTATIONS!")
    print("💼 Photorealistic features demonstrate:")
    print("   • Real agricultural field with grass and infrastructure")
    print("   • Professional aerial drone operations")
    print("   • Authentic farming environment and crop layout")
    print("   • Advanced precision agriculture technology")

if __name__ == "__main__":
    main()

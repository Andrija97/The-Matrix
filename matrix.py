import pygame
import random
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FONT_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
BRIGHT_GREEN = (0, 255, 100)
CYAN = (0, 255, 255)

# Matrix characters
MATRIX_CHARS = 'ｦｧｨｩｪｫｬｭｮｯｰｱｳｵｶｷｸｹｺﾀﾂﾃﾅﾆﾇﾈﾊﾏﾐﾑﾒﾓﾔﾕﾗﾘﾜ'
ASCII_CHARS = '01アイウエオカキクケコサシスセソタチツテトナニヌネハヒフヘホマミムメモヤユラリルレロワヲン'

class ColumnState(Enum):
    """State of a falling column"""
    ACTIVE = 1
    FADING = 2
    DEAD = 3

class MatrixColumn:
    """Represents a single column of falling characters"""
    def __init__(self, x, speed, start_y=0):
        self.x = x
        self.y = start_y
        self.speed = speed
        self.chars = []
        self.tail_length = random.randint(15, 35)
        self.state = ColumnState.ACTIVE
        self.fade_counter = 0
        self.brightness = 255
        
    def update(self):
        """Update column position and state"""
        if self.state == ColumnState.ACTIVE:
            self.y += self.speed
            
            # Generate random characters
            if len(self.chars) < self.tail_length:
                self.chars.append(random.choice(MATRIX_CHARS))
            elif self.y > SCREEN_HEIGHT:
                self.state = ColumnState.FADING
                
        elif self.state == ColumnState.FADING:
            self.fade_counter += 1
            self.brightness = max(0, 255 - (self.fade_counter * 10))
            if self.brightness <= 0:
                self.state = ColumnState.DEAD
    
    def draw(self, screen, font):
        """Draw the column on screen"""
        if self.state == ColumnState.DEAD:
            return
        
        for i, char in enumerate(self.chars):
            char_y = self.y - (i * FONT_SIZE)
            
            if -FONT_SIZE < char_y < SCREEN_HEIGHT:
                # Brightness gradient for tail effect
                intensity = int(255 * (i / len(self.chars)))
                
                if self.state == ColumnState.FADING:
                    intensity = int(intensity * (self.brightness / 255))
                
                # Color variation
                if i == 0:
                    color = BRIGHT_GREEN
                elif i < 3:
                    color = (0, 255, max(0, 255 - intensity))
                else:
                    color = (0, intensity, 0)
                
                text_surface = font.render(char, True, color)
                screen.blit(text_surface, (self.x, char_y))

class MatrixRain:
    """Main Matrix rain animation"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('🤖 THE MATRIX 🤖 - Press SPACE to pause, Q to quit')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freemono.ttf' if pygame.font.match_font('freemono') else None, FONT_SIZE)
        self.columns = []
        self.paused = False
        self.fps_display = True
        
        # Create initial columns
        self.spawn_columns()
    
    def spawn_columns(self):
        """Create columns at the top of the screen"""
        num_columns = SCREEN_WIDTH // FONT_SIZE
        for i in range(num_columns):
            x = i * FONT_SIZE
            speed = random.uniform(2, 8)
            delay = random.randint(-500, 0)
            self.columns.append(MatrixColumn(x, speed, start_y=delay))
    
    def handle_events(self):
        """Handle user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_f:
                    self.fps_display = not self.fps_display
        return True
    
    def update(self):
        """Update all columns"""
        if not self.paused:
            for column in self.columns:
                column.update()
            
            # Remove dead columns and spawn new ones
            self.columns = [c for c in self.columns if c.state != ColumnState.DEAD]
            
            # Spawn new columns randomly
            if random.random() < 0.3:
                x = random.randint(0, SCREEN_WIDTH - FONT_SIZE)
                speed = random.uniform(2, 8)
                self.columns.append(MatrixColumn(x, speed))
    
    def draw(self):
        """Draw everything"""
        self.screen.fill(BLACK)
        
        # Draw all columns
        for column in self.columns:
            column.draw(self.screen, self.font)
        
        # Draw UI
        self.draw_ui()
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw UI elements"""
        small_font = pygame.font.Font('freemono.ttf' if pygame.font.match_font('freemono') else None, 14)
        
        # FPS counter
        if self.fps_display:
            fps_text = small_font.render(f'FPS: {int(self.clock.get_fps())}', True, CYAN)
            self.screen.blit(fps_text, (10, 10))
        
        # Status text
        status = 'PAUSED' if self.paused else 'ACTIVE'
        status_color = (255, 0, 0) if self.paused else GREEN
        status_text = small_font.render(f'Status: {status}', True, status_color)
        self.screen.blit(status_text, (SCREEN_WIDTH - 200, 10))
        
        # Column count
        count_text = small_font.render(f'Columns: {len(self.columns)}', True, DARK_GREEN)
        self.screen.blit(count_text, (10, SCREEN_HEIGHT - 30))
        
        # Controls
        controls = small_font.render('SPACE: Pause | F: Toggle FPS | Q: Quit', True, DARK_GREEN)
        self.screen.blit(controls, (SCREEN_WIDTH - 400, SCREEN_HEIGHT - 30))
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    matrix = MatrixRain()
    matrix.run()

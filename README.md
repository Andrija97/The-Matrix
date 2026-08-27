```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║              ████████╗██╗  ██╗███████╗                        ║
║              ╚══██╔══╝██║  ██║██╔════╝                        ║
║                 ██║   ███████║█████╗                          ║
║                 ██║   ██╔══██║██╔══╝                          ║
║                 ██║   ██║  ██║███████╗                        ║
║                 ╚═╝   ╚═╝  ╚═╝╚══════╝                        ║
║                                                               ║
║                      M A T R I X                              ║
║                                                               ║
║         💚 Green Code Rain Animation with Visual FX 💚        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

## 🤖 Welcome to The Matrix

This is an interactive Matrix-style code rain animation built with Python and Pygame. Experience the iconic falling green code effect with stunning visual effects!

### ✨ Features

- 💚 **Authentic Matrix Code Rain** - Japanese katakana characters falling from the top
- 🎨 **Visual Effects** - Smooth color gradients, brightness fading, and glow effects
- ⚡ **Performance Optimized** - Runs smoothly at 60 FPS
- 🎮 **Interactive Controls** - Pause, resume, and toggle displays on the fly
- 📊 **Real-time Statistics** - FPS counter and active column count
- 🌈 **Dynamic Colors** - Green to cyan color transitions with intensity variations

### 🚀 Quick Start

#### Prerequisites
- Python 3.7+
- pip (Python package manager)

#### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Andrija97/The-Matrix.git
   cd The-Matrix
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the animation:**
   ```bash
   python matrix.py
   ```

### 🎮 Controls

| Key | Action |
|-----|--------|
| **SPACE** | Pause/Resume animation |
| **F** | Toggle FPS counter |
| **Q** | Quit application |

### 🎨 Visual Effects

The animation includes several cool effects:

- **Head Glow** - The leading character is bright green (BRIGHT_GREEN)
- **Tail Gradient** - Characters fade from cyan to dark green
- **Fade Out** - Columns smoothly fade when reaching bottom
- **Dynamic Speed** - Each column has random falling speed (2-8 pixels/frame)
- **Intelligent Spawning** - New columns spawn continuously for endless effect

### 📊 Performance

- **60 FPS** - Optimized for smooth animation
- **Efficient Rendering** - Only visible characters are drawn
- **Memory Management** - Dead columns are cleaned up automatically

### 🔧 Customization

You can easily customize the animation by modifying constants in `matrix.py`:

```python
# Screen dimensions
SCREEN_WIDTH = 1200      # Change to your preferred width
SCREEN_HEIGHT = 800      # Change to your preferred height

# Font size
FONT_SIZE = 20           # Smaller = more columns, more effect

# Tail length
tail_length = random.randint(15, 35)  # Length of falling character chains
```

### 📚 How It Works

1. **MatrixColumn Class** - Represents a single falling column
   - Manages position, speed, and state
   - Handles fade-out effects when reaching the bottom
   - Maintains a list of characters (the "tail")

2. **MatrixRain Class** - Main animation controller
   - Creates and manages multiple columns
   - Handles user input and events
   - Draws everything to the screen

3. **Color System** - Dynamic color transitions
   - Head: Bright green with cyan tint
   - Body: Gradient from cyan to dark green
   - Fade: Smooth brightness reduction

### 🎬 Demo

Run the application to see the Matrix code rain in action!

```bash
python matrix.py
```

### 📝 Files

- `matrix.py` - Main animation script
- `requirements.txt` - Python dependencies
- `README.md` - This file

### 🌟 Technical Details

- **Language:** Python 3
- **Framework:** Pygame 2.5.2
- **FPS:** 60
- **Resolution:** 1200x800 (customizable)
- **Characters:** Japanese Katakana from Matrix universe

### 🎯 Future Enhancements

- [ ] Keyboard/Mouse interaction with the falling code
- [ ] Sound effects (Matrix-style beeps)
- [ ] Custom color themes
- [ ] Particle effects and explosions
- [ ] Multi-monitor support

### 📄 License

This project is open source and available under the MIT License.

### 🙏 Credits

Inspired by the iconic Matrix movie franchise.

---

```
     0 1 0 1 1 0 1 0 1 0 1 1 0 1 0 1
    1 0 1 0 1 1 0 1 0 1 0 1 1 0 1 0
   0 1 0 1 1 0 1 0 1 0 1 1 0 1 0 1
  1 0 1 0 1 1 0 1 0 1 0 1 1 0 1 0
 0 1 0 1 1 0 1 0 1 0 1 1 0 1 0 1
1 0 1 0 1 1 0 1 0 1 0 1 1 0 1 0
```

**"The code is everywhere. It's all around us."** 🤖✨

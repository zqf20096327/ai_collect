# **🍎 Reversed Snake: The Swarm | Survival Browser Game**

**Survival Horror in 8-bit.** The classic Nokia snake game, inverted. You control the food, and the Snake is an AI determined to eat you.

## **🎮 Play Reversed Snake Online**

👉 [**Click here to play the live game**](https://imbios.github.io/lab-snake-reverse/)

## **✨ About the Game**

**Reversed Snake** is a free, open-source **browser game** built with **Vanilla JavaScript** and **HTML5 Canvas**. It flips the script on the classic retro arcade game: instead of guiding the snake, **you play as the Apple**.

The Snake is controlled by a sophisticated pathfinding algorithm (**A\* Search**) that ruthlessly hunts you down. As time passes, the snake grows longer automatically, making the grid increasingly claustrophobic.

**Level 10** features a "Swarm Mode" where you must dodge **10 intelligent snakes** simultaneously, making it one of the hardest snake game variants on the web.

## **🚀 Key Features**

* **Inverted Gameplay:** A unique twist on the classic 90s game.  
* **Smart AI:** Snakes use A\* Pathfinding to track your every move.  
* **Progressive Difficulty:** 10 Levels, ranging from a single snake to a full swarm.  
* **Cross-Platform:** Fully responsive design that works on **iPhone**, **Android**, and Desktop.  
* **No Install Required:** Play directly in your web browser.  
* **Offline Capable:** High scores are saved locally to your device.

## **🕹️ How to Play**

1. **Desktop:** Use your **Arrow Keys** (⬆️ ⬇️ ⬅️ ➡️) to move the Red Apple.  
2. **Mobile/Tablet:** Use the **on-screen virtual joystick** to navigate.  
3. **Objective:** Survive as long as possible. Do not let any Snake head touch you.  
4. **Scoring:** Your time survived is your score. Can you beat the Level 10 world record?

## **🧠 Technical Details for Developers**

This project is a perfect example of **game development with pure JavaScript** (no engines like Unity or Phaser).

### **A\* Pathfinding Algorithm**

The snake utilizes a PriorityQueue to calculate the most efficient path to the player's coordinates. To maintain 60FPS with 10 snakes, the game uses a **Collision Grid Cache** (O(1) lookup) instead of checking every snake body segment individually.

```js
function findPath(start, goal, snake) {  
  // Manhattan distance heuristic  
  const heuristic \= p \=\> p.manhattan(goal);  
  // ... implementation of A\* loop  
}
```

### **Optimization Techniques**

* **Canvas Rendering:** Uses requestAnimationFrame for smooth gameplay.  
* **Memory Management:** Object pooling principles to prevent garbage collection stutters.  
* **Zero Dependencies:** Extremely lightweight (\<5kb logic) for instant load times.

## **🛠️ Installation & Local Development**

Want to modify the AI or add new skins? No build steps required.

```sh
# Clone the repository  
git clone https://github.com/ImBIOS/lab-snake-reverse.git

# Navigate to directory  
cd lab-snake-reverse

# Open in browser  
open index.html
```

*Keywords: Reversed Snake, Play as Apple, Snake Game AI, Hard Snake Game, A\* Algorithm Game, Browser Game, HTML5 Game, Survival Game, JavaScript Game Project, Open Source Game.*

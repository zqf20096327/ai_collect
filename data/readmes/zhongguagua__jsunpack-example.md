# jsunpack - JavaScript Decompilation Example

This repository demonstrates the decompilation results of [jsunpack](https://www.jsunpack.tech/) on a **Three.js + Vue 2 tower defense game** webpack bundle. The original project was built with webpack into a single file `app.04414ea9.js` , which jsunpack restored to a complete, readable project source structure.

## Live Demo
https://bastion-3d-threejs.vercel.app/

## Source Repository
https://github.com/zhongguagua/bastion-3d-threejs

[中文文档](./README.zh-CN.md)

## Directory Structure

```
jsunpack-example/
└── threejs-vue2-example/
    ├── source/
    │   └── app.04414ea9.js          # Original webpack bundle (single file)
    └── decode/
        ├── result-en/               # Decompilation result (English comments)
        └── result-zh/               # Decompilation result (Chinese comments)
            ├── package.json
            └── src/
                ├── main.js                          # Entry file
                ├── App.vue                          # Root component
                ├── components/                      # Vue components
                │   ├── TowerDefense.vue             #   Main game component
                │   ├── StartScreen.vue              #   Start screen
                │   ├── GameOverScreen.vue           #   Game over screen
                │   ├── HUD.vue                      #   Heads-up display
                │   └── TowerPanel.vue               #   Tower selection panel
                ├── config/                          # Configuration modules
                │   ├── GameConstants.js             #   Game constants
                │   └── WaveConfig.js                #   Wave data
                ├── core/                            # Core modules
                │   ├── Game.js                      #   Game engine main controller
                │   ├── EventBus.js                  #   Event bus
                │   ├── SceneManager.js              #   Scene management
                │   ├── controllers/
                │   │   └── InputController.js       #   Input controller
                │   └── managers/
                │       ├── WaveManager.js           #   Wave manager
                │       ├── MapManager.js            #   Map manager
                │       ├── GridManager.js           #   Grid manager
                │       ├── PathManager.js           #   Path manager
                │       └── EffectManager.js         #   Effect manager
                ├── entities/                        # Game entities
                │   ├── Enemy.js                     #   Enemy base class
                │   ├── enemies/
                │   │   ├── NormalEnemy.js           #   Normal enemy
                │   │   ├── FastEnemy.js             #   Fast enemy
                │   │   ├── TankEnemy.js             #   Tank enemy
                │   │   ├── FlyingEnemy.js           #   Flying enemy
                │   │   └── BossEnemy.js             #   Boss enemy
                │   ├── towers/
                │   │   ├── Tower.js                 #   Tower base class
                │   │   ├── ArrowTower.js            #   Arrow tower
                │   │   ├── CannonTower.js           #   Cannon tower
                │   │   ├── IceTower.js              #   Ice tower
                │   │   ├── LightningTower.js        #   Lightning tower
                │   │   └── SniperTower.js           #   Sniper tower
                │   └── projectiles/
                │       ├── Projectile.js            #   Projectile base class
                │       ├── ArrowProjectile.js       #   Arrow projectile
                │       ├── CannonProjectile.js      #   Cannon projectile
                │       ├── IceProjectile.js         #   Ice projectile
                │       ├── LightningProjectile.js   #   Lightning projectile
                │       └── SniperProjectile.js      #   Sniper projectile
                ├── factories/                       # Factory pattern
                │   ├── EnemyFactory.js              #   Enemy factory
                │   └── TowerFactory.js              #   Tower factory
                └── polyfill/                        # webpack runtime artifacts
                    ├── webpack-bootstrap.js
                    ├── webpack-chunk-loader.js
                    ├── webpack-runtime.js
                    └── webpack-utils.js
```

## Decompilation Quality Assessment

### File Coverage

| Metric                | Count                                                    |
|-----------------------|----------------------------------------------------------|
| Total source files    | 43 (excluding logo.png)                                  |
| Successfully mapped   | 39                                                       |
| Missing files         | 4 (ObjectPool.js, Aura.js, Explosion.js, Particle.js)   |
| Extra polyfill files  | 4 (webpack runtime artifacts)                            |
| **File mapping coverage** | **~90.7%**                                          |

### Highlight Restorations

The decompilation tool performed exceptionally well in the following areas:

**1. EventBus -- Near-perfect restoration (98%)**

The publish-subscribe pattern was precisely restored. All 5 methods (on/off/emit/once/clear) have semantically accurate naming. The closure pattern in `once`, the try/catch error handling in `emit`, and the unsubscribe function returned by `on` are all correctly restored. The error log format `EventBus error on "${eventName}"` is identical.

**2. EnemyFactory -- Perfect restoration (100%)**

The factory pattern's switch-case structure, 5 enemy type mappings, and console.warn fallback logic are all precisely restored. Parameter names were recovered from `type, hpMultiplier` to `enemyType, multiplier`, which is arguably even clearer semantically.

**3. WaveConfig -- 20 waves of data with zero errors (98%)**

Large-scale structured data fully restored: enemy types, quantities, spawn intervals, and reward gold for each wave all match. The complex configuration of the final wave with 5 enemy types in a mixed formation is also completely consistent.

**4. GameConstants -- 100% correct constant data**

GAME_STATE 5 states, GRID parameters, CAMERA 10 parameters, PLAYER initial values, TOWER_STATS for 5 tower types, ENEMY_STATS for 5 enemy types, MAP_PATH 12 waypoint coordinates -- all values are completely correct. The decompilation also added JSDoc comments for each constant.

**5. Game.js (GameEngine) -- Core controller precise restoration (93%)**

As the project's most critical 934-line file, all 30+ methods are restored. Complex algorithms are precisely preserved:
- Chain lightning `_findChainTargets`: distance calculation, target exclusion, nearest target lookup logic is identical
- Splash damage: `1 - (dist / splashRadius) * 0.5` decay formula is identical
- Sell refund: `Math.floor(totalInvested * 0.6)` 60% refund logic is identical

**6. Project Architecture**

A well-organized modular directory structure was reconstructed from the webpack bundle. The tool identified and separated core modules, entity inheritance hierarchies, factory patterns, manager patterns, and configuration modules -- resulting in a structure even clearer than the original source code.

### Overall Score

| Dimension              | Score | Weight |
|------------------------|-------|--------|
| File mapping coverage  | 90.7% | 10%    |
| Core logic retention   | 92%   | 30%    |
| Variable/function naming | 93% | 15%    |
| Code structure similarity | 94% | 15%    |
| Functional correctness | 82%   | 20%    |
| Visual/rendering accuracy | 78% | 10%    |

**Weighted overall score: ~88%**

### Known Limitations

The decompilation results are of high overall quality, but there are a few areas for improvement:

- **Missing import statements in some files**: e.g., Enemy.js is missing `import * as THREE from 'three'`, requiring manual addition
- **Occasional factory parameter order issues**: Constructor parameter order in TowerFactory.js may need adjustment
- **Three.js geometry misidentification**: Some `SphereGeometry` instances were restored as `CylinderGeometry`
- **4 auxiliary files not restored**: ObjectPool, Aura, Explosion, and Particle were not extracted from the bundle
- **Color format readability**: Hexadecimal color values were converted to decimal numbers (e.g., `0x33cc66` -> `3394662`), values are correct but less readable

## Conclusion

jsunpack demonstrated excellent decompilation capabilities in this example:

- **High core logic restoration**: Class inheritance hierarchies, factory patterns, event systems, and wave management state machines are all correctly restored
- **Strong naming recovery**: Variable/function naming recovery rate is approximately 93%
- **Complex algorithms fully preserved**: Chain lightning, splash damage, HP multiplier calculations, and other complex logic are all correct
- **Architecture-level reconstruction**: A clear modular project structure was rebuilt from a single bundled file

The overall restoration rate is approximately **88%**. Core game logic is well restored, and full functionality can be recovered with minor manual fixes.

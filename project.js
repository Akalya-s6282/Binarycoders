const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const WIDTH = canvas.width;
const HEIGHT = canvas.height;

// Colors
const WHITE = '#FFFFFF';
const BLACK = '#000000';
const GOLD = '#FFD700';

// Player settings
const playerSize = 50;
let playerX = WIDTH / 2 - playerSize / 2;
let playerY = HEIGHT - 2 * playerSize;
const playerSpeed = 10;

// Treasure settings
const treasureSize = 30;
let treasureX = Math.random() * (WIDTH - treasureSize);
let treasureY = Math.random() * (HEIGHT - treasureSize);

// Game loop
function gameLoop() {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);

    // Draw player
    ctx.fillStyle = BLACK;
    ctx.fillRect(playerX, playerY, playerSize, playerSize);

    // Draw treasure
    ctx.fillStyle = GOLD;
    ctx.fillRect(treasureX, treasureY, treasureSize, treasureSize);

    // Check for collision with treasure
    if (playerX < treasureX + treasureSize &&
        playerX + playerSize > treasureX &&
        playerY < treasureY + treasureSize &&
        playerY + playerSize > treasureY) {
        alert('Treasure found!');
        resetGame();
    }

    requestAnimationFrame(gameLoop);
}

// Handle player movement
document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' && playerX > 0) {
        playerX -= playerSpeed;
    } else if (event.key === 'ArrowRight' && playerX < WIDTH - playerSize) {
        playerX += playerSpeed;
    } else if (event.key === 'ArrowUp' && playerY > 0) {
        playerY -= playerSpeed;
    } else if (event.key === 'ArrowDown' && playerY < HEIGHT - playerSize) {
        playerY += playerSpeed;
    }
});

// Reset game state
function resetGame() {
    playerX = WIDTH / 2 - playerSize / 2;
    playerY = HEIGHT - 2 * playerSize;
    treasureX = Math.random() * (WIDTH - treasureSize);
    treasureY = Math.random() * (HEIGHT - treasureSize);
}

// Start the game loop
gameLoop();
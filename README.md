### Tic‑Tac‑Toe Game👦👧

| Piece | What it looks like | What it means |
|-------|-------------------|---------------|
| **X** | A cross (✕)      | One player’s mark |
| **O** | A circle (○)      | The other player’s mark |

**The board**  
It’s a 3 × 3 grid – like a little picture made of 9 squares.

```
1️⃣ 2️⃣ 3️⃣
4️⃣ 5️⃣ 6️⃣
7️⃣ 8️⃣ 9️⃣
```

#### How to play
1. **Take turns** – you put an X, the computer puts an O, then you put another X, and so on.  
2. **Put your mark in an empty square** – you can’t put a mark where there’s already one.  
3. **Goal:** get **three of your marks in a straight line** – across, down, or diagonal.

```
X X X   ← you win!
```

If all 9 squares are filled and nobody has three in a line, the game ends in a **draw** (a tie).

#### The computer’s brain
- The computer thinks ahead like a super‑smart friend.  
- It looks at every possible way the game could go, then picks the move that **guarantees it won’t lose**.  
- It uses a trick called **Alpha‑Beta pruning** (don’t worry about the name) that lets it skip looking at moves that it already knows are bad, so it can decide faster.

#### What you’ll see when you run the script
- The board is shown on the screen.  
- You type which square you want (like “center” or “top‑right”).  
- The computer instantly puts its O somewhere.  
- The board updates after each turn until someone wins or it’s a tie.

That’s it! It’s a simple game of taking turns, trying to get three in a row, and watching a clever computer opponent try not to lose. Have fun playing! 🎉

# Simple CLI Pomodoro Timer

import time

import keyboard


def pomodoro(minutes):
    total_seconds = minutes * 60
    is_paused = False
    
    print(f"Started! You have {minutes} minutes of focus.")
    print("Press 'p' to Pause.\n")
    
    while total_seconds > 0:
        # Check for 'p' key press
        if keyboard.is_pressed('p'):
            is_paused = not is_paused
            
            if is_paused:
                # Clear line
                print("\r Timer paused... (Press 'p' to resume)     ", end="", flush=True)
            
            # Avoid rapid double-presses
            time.sleep(0.5)
            continue
            
        if not is_paused:
            mins, secs = divmod(total_seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            
            # Update output line
            print(f"\r Remaining: {timer}     ", end="", flush=True)
            
            time.sleep(1)
            total_seconds -= 1
        else:
            # Keep CPU usage low
            time.sleep(0.1)

    print("\n\n Time's up! Your focus session is over!")


if __name__ == "__main__":
    try:
        # Start with 25 minutes
        pomodoro(25)
    except KeyboardInterrupt:
        # Handle manual exit cleanly
        print("\n\nPomodoro stopped manually!")

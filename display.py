import I2C_LCD_driver
from time import sleep

# Inisialisasi LCD
mylcd = I2C_LCD_driver.lcd()

def initialize_lcd():
    """Inisialisasi LCD."""
    mylcd.lcd_clear()  # Clear the display during initialization
    sleep(0.1)  # Wait for LCD to settle
    mylcd.lcd_display_string("Inisialisasi...", 1)  # Display message
    sleep(1)
    mylcd.lcd_clear()

def show_direction(direction):
    """Menampilkan arah joystick di LCD."""
    mylcd.lcd_clear()  # Bersihkan layar sebelum menampilkan pesan
    mylcd.lcd_display_string(f"Arah: {direction}", 1)  # Tampilkan arah pada baris pertama

def show_values(x_value, y_value):
    """Menampilkan nilai X dan Y pada LCD."""
    mylcd.lcd_clear()  # Bersihkan layar sebelum menampilkan pesan
    mylcd.lcd_display_string(f"X: {x_value}", 1)  # Tampilkan nilai X pada baris pertama
    mylcd.lcd_display_string(f"Y: {y_value}", 2)  # Tampilkan nilai Y pada baris kedua

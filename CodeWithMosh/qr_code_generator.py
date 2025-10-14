# Mosh's solution
"""
import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')

"""


import qrcode


def generate_qr_code(data, filename="qr_code.png"):
    """
    Generates a QR code from the given data and saves it as an image file.

    Args:
        data (str): The text or URL to encode in the QR code.
        filename (str): The name of the output image file (e.g., "my_qr.png").
    """
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size around the QR code
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code generated and saved as {filename}")


if __name__ == "__main__":
    # Get user input for the data
    user_input = input("Enter the text or URL for the QR code: ")
    filename_input = input(
        "Enter the filename to save the QR code (default: qr_code.png): ")

    # Generate the QR code
    generate_qr_code(user_input, filename=filename_input)

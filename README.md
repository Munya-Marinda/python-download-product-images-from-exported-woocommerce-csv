---

# Python Download Product Images from Exported WooCommerce CSV

This Python script downloads product images from an exported WooCommerce CSV file. It reads the CSV file, extracts the image URLs from the specified column, and downloads each image to a local directory. Additionally, it generates a JSON report containing the counts of downloaded images and processed products.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Munya-Marinda/python-download-product-images-from-exported-woocommerce-csv
   ```

2. **Install Dependencies:**

   Ensure you have Python installed on your system. You also need to install the required Python packages. You can install them using pip:

   ```bash
   pip install pandas requests
   ```

3. **Run the Script:**

   Replace `'input.csv'` with the path to your WooCommerce CSV file. Then run the script:

   ```bash
   python main.py
   ```

4. **Check Output:**

   - The script downloads images to the `downloaded_images` directory.
   - It generates a JSON report with the count of downloaded images and processed products.

## File Structure

- `main.py`: Main Python script to download product images.
- `input.csv`:

Continuing from where we left off:

```markdown
Example WooCommerce CSV file (replace with your actual file).

- `downloaded_images/`: Directory where downloaded images are saved.
- `YYYY-MM-DD_HH:MM:SS.json`: JSON report containing download statistics, named with the current date and time.

## Requirements

- Python 3.x
- pandas
- requests

## License

This project is licensed under the [MIT License](LICENSE).

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
```

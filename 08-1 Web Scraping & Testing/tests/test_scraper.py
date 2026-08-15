import unittest
import sys, os
import importlib.util

file_path = os.path.join(os.path.dirname(__file__), '..', 'src', '07RewriteEx3_scraper.py')
spec = importlib.util.spec_from_file_location("scraper", file_path)
scraper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scraper)

class TestScraper(unittest.TestCase):

    def test_extract_products_from_html_returns_dict(self):
        # Sample HTML with two product items
        html = """
        <div class="product-item">
            <span class="product-name">Book One</span>
            <span class="product-price">£12.99</span>
        </div>
        <div class="product-item">
            <span class="product-name">Book Two</span>
            <span class="product-price">$8.50</span>
        </div>
        """
        result = scraper.extract_products_from_html(html)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.get("Book One"), "£12.99")
        self.assertEqual(result.get("Book Two"), "$8.50")

    def test_extract_products_from_html_handles_missing_fields(self):
        # Missing price or name
        html = """
        <div class="product-item">
            <span class="product-name">Only Name</span>
        </div>
        <div class="product-item">
            <span class="product-price">$10.00</span>
        </div>
        """
        result = scraper.extract_products_from_html(html)
        self.assertIsInstance(result, dict)
        # First item: name present, price missing -> price becomes "."
        self.assertEqual(result.get("Only Name"), ".")
        # Second item: price present, name missing -> title becomes "Unknown"
        self.assertEqual(result.get("Unknown"), "$10.00")

    # Optionally test extract_product_links with a mock to avoid real network calls
    @unittest.skip("Skipping real network test; enable if needed")
    def test_extract_product_links_returns_list(self):
        links = scraper.extract_product_links()
        self.assertIsInstance(links, list)
        # Additional assertions can be added

if __name__ == '__main__':
    unittest.main()
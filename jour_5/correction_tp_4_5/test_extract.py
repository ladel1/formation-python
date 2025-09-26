from unittest import TestCase, main
from extract import extract_emails

class TestExtractEmail(TestCase):
    def test_extraction(self):
        # AAA
        # Arrange
        init_file = "email_test.txt"
        nombre_email = 2
        email = "alice@gmail.com"
        with open(init_file, "w", encoding="utf-8") as f:
            f.write(f"contact: {email} balbalab contact: hugo.chevalier@outlook.fr balbalba")
        # Act
        emails = extract_emails(init_file)
        # Assert
        self.assertEqual(len(emails), nombre_email)
        self.assertIn(email,emails)

    def test_file_exist(self):
        with self.assertRaises(FileNotFoundError):
            extract_emails("not_exist.txt")

if __name__ == "__main__":
    main()
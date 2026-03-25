import unittest
from main import bin_to_dec, dec_to_bin, oct_to_dec, dec_to_oct, hex_to_dec, dec_to_hex

class TestConversor(unittest.TestCase):
    
    def test_bin_to_dec(self):
        self.assertEqual(bin_to_dec('0'), 0)
        self.assertEqual(bin_to_dec('1'), 1)
        self.assertEqual(bin_to_dec('10'), 2)
        self.assertEqual(bin_to_dec('101'), 5)
        self.assertEqual(bin_to_dec('1111'), 15)
        with self.assertRaises(ValueError):
            bin_to_dec('102')  # Dígito inválido
    
    def test_dec_to_bin(self):
        self.assertEqual(dec_to_bin(0), '0')
        self.assertEqual(dec_to_bin(1), '1')
        self.assertEqual(dec_to_bin(2), '10')
        self.assertEqual(dec_to_bin(5), '101')
        self.assertEqual(dec_to_bin(15), '1111')
        with self.assertRaises(ValueError):
            dec_to_bin(-1)
    
    def test_oct_to_dec(self):
        self.assertEqual(oct_to_dec('0'), 0)
        self.assertEqual(oct_to_dec('1'), 1)
        self.assertEqual(oct_to_dec('10'), 8)
        self.assertEqual(oct_to_dec('77'), 63)
        with self.assertRaises(ValueError):
            oct_to_dec('8')  # Dígito inválido
    
    def test_dec_to_oct(self):
        self.assertEqual(dec_to_oct(0), '0')
        self.assertEqual(dec_to_oct(1), '1')
        self.assertEqual(dec_to_oct(8), '10')
        self.assertEqual(dec_to_oct(63), '77')
        with self.assertRaises(ValueError):
            dec_to_oct(-1)
    
    def test_hex_to_dec(self):
        self.assertEqual(hex_to_dec('0'), 0)
        self.assertEqual(hex_to_dec('1'), 1)
        self.assertEqual(hex_to_dec('A'), 10)
        self.assertEqual(hex_to_dec('FF'), 255)
        self.assertEqual(hex_to_dec('10'), 16)
        with self.assertRaises(ValueError):
            hex_to_dec('G')  # Dígito inválido
    
    def test_dec_to_hex(self):
        self.assertEqual(dec_to_hex(0), '0')
        self.assertEqual(dec_to_hex(1), '1')
        self.assertEqual(dec_to_hex(10), 'A')
        self.assertEqual(dec_to_hex(255), 'FF')
        self.assertEqual(dec_to_hex(16), '10')
        with self.assertRaises(ValueError):
            dec_to_hex(-1)

if __name__ == '__main__':
    unittest.main()
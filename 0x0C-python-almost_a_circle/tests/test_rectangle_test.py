def test_dictionary_representation(self):
    r1 = Rectangle(10, 2, 1, 9)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle(1, 1)
    r2.update(**r1_dictionary)

    self.assertEqual(r2.width, r1.width)
    self.assertEqual(r2.height, r1.height)
    self.assertEqual(r2.x, r1.x)
    self.assertEqual(r2.y, r1.y)
    self.assertEqual(str(r2), str(r1))
    self.assertNotEqual(r2, r1)
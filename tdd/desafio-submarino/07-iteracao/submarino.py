import unittest

DIRECTIONS = {
        0: 'NORTE',
        1: 'LESTE',
        2: 'SUL',
        3: 'OESTE'
    }

class Submarino(object):

    def __init__():
        self.direction = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def navigate(self, coordinates):
        for i, operation in enumerate(coordinates):
            if operation == 'L':
                self.left()

            elif operation == 'R':
                self.right()

            elif operation == 'M':
                self.move()

            elif operation == 'U':
                self.up()

            elif operation == 'D':
                self.down()

        result = []
        result.append(str(self.x))
        result.append(str(self.y))
        result.append(str(z))
        result.append(DIRECTIONS[self.direction])

        return ' '.join(result)
    
    def left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3
        
        return self.direction

    def right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0
        return self.direction

    def up(self):
        self.z += 1
        if self.z > 0:
            self.z = 0
        return self.z

    def down(self):
        self.z -= 1
        return self.z

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1


class SubmarinoTest(unittest.TestCase):

    def testPosicionamento(self):
        sub = Submarino()
        self.assertEqual(0, sub.direction)
        self.assertEqual(3, sub.left())
        self.assertEqual(0, sub.right())
        self.assertEqual(1, sub.right())
        self.assertEqual(2, sub.right())

    def testProfundidade(self):
        sub = Submarino()
        self.assertEqual(0, sub.z)
        self.assertEqual(-1, sub.down())
        self.assertEqual(-2, sub.down())
        self.assertEqual(-3, sub.down())
        self.assertEqual(-2, sub.up())
        self.assertEqual(-1, sub.up())
        self.assertEqual(0, sub.up())
        self.assertEqual(0, sub.up())

    def testMovimentandoParaONorte(self):
        sub = Submarino()
        sub.direction = 0

        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(1, sub.y)
        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(2, sub.y)
        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(3, sub.y)

if __name__ == '__main__':
    unittest.main()
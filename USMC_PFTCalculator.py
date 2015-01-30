
#set this variable to True if you want to run unit tests
dotests = True

### DO NOT CHANGE CODE BELOW THIS LINE              ###
### THESE ARE THE UNIT TESTS TO EXERCISE YOUR CODE  ###
import unittest
import os.path
class TestFitnessFunctions(unittest.TestCase):
    def setUp(self):
        self.zombie = Member("Walking", "Dead", 100,'M',0,0,"100:00")
        self.turtle = Member("Ninja", "Turtle", 15,'M',1,1,"45:00")
        self.rabbit = Member("Roger", "Rabbit", 18,'M',20,100,"18:00")
        self.roadRunner = Member("Meep", "Meep", 5,'M',30,200,"10:00")
        self.m = Member("Amanda", "Dewitt", 35,'M',10,50,"24:00")
        self.edge1 = Member("Edge1", "Lastname", 20,'M',10,100,"18:09")
        self.edge2 = Member("Edge2", "Lastname", 20,'M',10,100,"18:10")
        self.edge3 = Member("Edge3", "Lastname", 20,'M',10,100,"18:11")
        self.edge4 = Member("Edge4", "Lastname", 20,'M',10,100,"18:59")
        self.edge5 = Member("Edge5", "Lastname", 20,'M',10,100,"19:00")
        self.edge6 = Member("Edge6", "Lastname", 20,'M',10,100,"19:01")

        # the data in this member is messed up on purpose. it's for checking exception handling
        self.screwup = Member("Ima", "/Screwup", "Age", "Gender", "Pulls", "Crunches", "Runtime")

        #putting them in a list makes cleanup easier
        mlist = []
        mlist.append(self.zombie)
        mlist.append(self.turtle)
        mlist.append(self.rabbit)
        mlist.append(self.roadRunner)
        mlist.append(self.m)
        mlist.append(self.edge1)
        mlist.append(self.edge2)
        mlist.append(self.edge3)
        mlist.append(self.edge4)
        mlist.append(self.edge5)
        mlist.append(self.edge6)

        #delete any files hanging out there
        self.cleanUpTestFiles()
        #set up a couple of files
        fout = open("master.txt", 'w')
        fout.write("Dead.Walking.txt\nTurtle.Ninja.txt")
        fout.close
        fout = open("Dead.Walking.txt", 'w')
        fout.write("Walking\nDead\n199\nM\n0\n0\n100:00")
        fout.close()
        fout.open("Turtle.Ninja.txt", 'w')
        fout.write("Ninja\nTurtle\n15\nM\n1\n1\n45:00")
        fout.close()

    def test_getMenu(self):
        testString = "1) Add member\n2) Show all members\n0) Exit"
        self.assertEqual(getMenu().strip(), testString, "\nIncorrect menu. Expected\n" + testString + "\nGot\n" + getMenu())

    def test_repr(self):
        s = str(self.m)
        self.assertEqual(s.find("Amanda"), -1, "First name not in repr")
        self.assertEqual(s.find("Dewitt"), -1, "Last name not in repr")
        self.assertEqual(s.find("35"), -1, "Age not in repr")
        self.assertEqual(s.find("10"), -1, "Pulls not in repr")
        self.assertEqual(s.find("50"), -1, "Crunches not in repr")
        self.assertEqual(s.find("24:00"), -1, "Runtime not in repr")
        self.assertEqual(s.find("164"), -1, "Total score not in repr")

    def test_getCrunchScore(self):
        # Testing zero, mid, high, over
        self.assertEqual(self.zombie.getCrunchScore(), 0, "Crunch score incorrect for 0 crunches")
        self.assertEqual(self.turtle.getCrunchScore(), 1, "Crunch score incorrect for 1 crunches")
        self.assertEqual(self.rabbit.getCrunchScore(), 100, "Crunch score incorrect for 100 crunches")
        self.assertEqual(self.roadRunner.getCrunchScore(), 100, "Crunch score incorrect for 100 crunches")

    def test_getPullupScore(self):
        self.assertEqual(self.zombie.getPullupScore(), 0, "Pull score incorrect for 0 pulls")



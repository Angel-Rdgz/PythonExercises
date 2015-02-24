
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
        self.mlist = mlist

        #delete any files hanging out there
        self.cleanUpTestFiles()
        #set up a couple of files
        fout = open("master.txt", 'w')
        fout.write("Dead.Walking.txt\nTurtle.Ninja.txt")
        fout.close
        fout = open("Dead.Walking.txt", 'w')
        fout.write("Walking\nDead\n100\nM\n0\n0\n100:00")
        fout.close()
        fout.open("Turtle.Ninja.txt", 'w')
        fout.write("Ninja\nTurtle\n15\nM\n1\n1\n45:00")
        fout.close()

    def test_getMenu(self):
        testString = "1) Add member\n2) Show all members\n0) Exit"
        self.assertEqual(getMenu().strip(), testString, "\nIncorrect menu. Expected\n" + testString + "\nGot\n" + getMenu())

    def test_repr(self):
        s = str(self.m)
        self.assertNotEqual(s.find("Amanda"), -1, "First name not in repr")
        self.assertNotEqual(s.find("Dewitt"), -1, "Last name not in repr")
        self.assertNotEqual(s.find("35"), -1, "Age not in repr")
        self.assertNotEqual(s.find("10"), -1, "Pulls not in repr")
        self.assertNotEqual(s.find("50"), -1, "Crunches not in repr")
        self.assertNotEqual(s.find("24:00"), -1, "Runtime not in repr")
        self.assertNotEqual(s.find("164"), -1, "Total score not in repr")

    def test_getCrunchScore(self):
        # Testing zero, mid, high, over
        self.assertEqual(self.zombie.getCrunchScore(), 0, "Crunch score incorrect for 0 crunches")
        self.assertEqual(self.turtle.getCrunchScore(), 1, "Crunch score incorrect for 1 crunches")
        self.assertEqual(self.rabbit.getCrunchScore(), 100, "Crunch score incorrect for 100 crunches")
        self.assertEqual(self.roadRunner.getCrunchScore(), 100, "Crunch score incorrect for 100 crunches")

    def test_getPullupScore(self):
        # Testing zero, mid, high, over
        self.assertEqual(self.zombie.getPullupScore(), 0, "Pull score incorrect for 0 pulls")
        self.assertEqual(self.turtle.getPullupScore(), 5, "Pull score incorrect for 1 pulls")
        self.assertEqual(self.rabbit.getPullupScore(), 100, "Pull score incorrect for 20 pulls")
        self.assertEqual(self.roadRunner.getPullupScore(), 100, "Pull score incorrect for 30 pulls")

    def test_getRunScore(self):
        # Testing zero, mid, high, over
        self.assertEqual(self.zombie.getRunScore(), 0, "Run score incorrect for " + self.zombie.run + "->" + str(self.zombie.getRunScore()))
        self.assertEqual(self.turtle.getRunScore(), 0, "Run score incorrect for " + self.turtle.run + "->" + str(self.turtle.getRunScore()))
        self.assertEqual(self.rabbit.getRunScore(), 100, "Run score incorrect for " + self.rabbit.run + "->" + str(self.rabbit.getRunScore()))
        self.assertEqual(self.roadRunner.getRunScore(), 100, "Run score incorrect for " + self.roadRunner.run + "->" + str(self.roadRunner.getRunScore()))
        self.assertEqual(self.edge1.getRunScore(), 99, "Run score incorrect for " + self.edge1.run + "->" + str(self.edge1.getRunScore()))
        self.assertEqual(self.edge2.getRunScore(), 99, "Run score incorrect for " + self.edge2.run + "->" + str(self.edge2.getRunScore()))
        self.assertEqual(self.edge3.getRunScore(), 98, "Run score incorrect for " + self.edge3.run + "->" + str(self.edge3.getRunScore()))
        self.assertEqual(self.edge4.getRunScore(), 94, "Run score incorrect for " + self.edge4.run + "->" + str(self.edge4.getRunScore()))
        self.assertEqual(self.edge5.getRunScore(), 94, "Run score incorrect for " + self.edge5.run + "->" + str(self.edge5.getRunScore()))
        self.assertEqual(self.edge6.getRunScore(), 93, "Run score incorrect for " + self.edge6.run + "->" + str(self.edge6.getRunScore()))

    def testCalculateScore(self):
        self.assertEqual(self.zombie.getTotalScore(), 0, "Total score incorrect for zombie: " + str(self.zombie.getTotalScore()))
        self.assertEqual(self.turtle.getTotalScore(), 6, "Total score incorrect for turtle: " + str(self.turtle.getTotalScore()))
        self.assertEqual(self.rabbit.getTotalScore(), 300, "Total score incorrect for rabbit: " + str(self.rabbit.getTotalScore()))
        self.assertEqual(self.roadRunner.getTotalScore(), 300, "Total score incorrect for roadRunner: " + str(self.roadRunner.getTotalScore()))

    def test_saveMemberToFile(self):
        self.m.saveMemberToFile()
        fin = open("Dewitt.Amanda.txt", 'r')
        fileTxt = fin.read().strip()
        fin.close()
        testTxt = "Amanda\nDewitt\n35\nM\n10\n50\n24:00"
        self.assertEqual(fileTxt, testTxt, "Text in save file not correct")

    def test_getMemberFromFile(self):
        self.m.saveMemberToFile()
        lm = getMemberFromFile("Dewitt.Amanda.txt")
        self.assertEqual(lm.firstname, "Amanda", "getMemberFromFile not setting firstname correctly")
        self.assertEqual(lm.lastname, "Dewitt", "getMemberFromFile not setting lastname correctly")
        self.assertEqual(lm.age, 35, "getMemberFromFile not setting age correctly")
        self.assertEqual(lm.gender, "M", "getMemberFromFile not setting gender correctly")
        self.assertEqual(lm.pulls, 10, "getMemberFromFile not setting pulls correctly")
        self.assertEqual(lm.crunches, 50, "getMemberFromFile not setting crunches correctly")
        self.assertEqual(lm.run, "24:00", "getMemberFromFile not setting runtime correctly")

        self.zombie.saveMemberToFile()
        lm = getMemberFromFile("Dead.Walking.txt")
        self.assertEqual(lm.firstname, "Walking", "getMemberFromFile not setting firstname correctly")
        self.assertEqual(lm.lastname, "Dead", "getMemberFromFile not setting lastname correctly")
        self.assertEqual(lm.age, 100, "getMemberFromFile not setting age correctly")
        self.assertEqual(lm.gender, "M", "getMemberFromFile not setting gender correctly")
        self.assertEqual(lm.pulls, 0, "getMemberFromFile not setting pulls correctly")
        self.assertEqual(lm.crunches, 0, "getMemberFromFile not setting crunches correctly")
        self.assertEqual(lm.run, "100:00", "getMemberFromFile not setting runtime correctly")

    def test_loadMemberList(self):
        l = loadMemberList()
        self.assertEqual(len(l), 2, "loadMemberList did not load all files found in master.txt")
        foundWalkingDead = False
        foundNinjaTurtle = False

        for m in l:
            if m.firstname == "Walking":
                foundWalkingDead = True
            elif m.firstname == "Ninja":
                foundNinjaTurtle = True

        self.assertTrue(foundWalkingDead, "Did not add Walking Dead to the list")
        self.assertTrue(foundNinjaTurtle, "Did not add Ninja Turtle to the list")

    #TESTING FOR EXCEPTIONS
    def test_getMemberFromFileForExceptionHandling(self):
        try:
            self.assertEqual(None, getMemberFromFile("nothere.txt")) # doesn't exist
            self.assertEqual(None, getMemberFromFile("/etc/shadow")) # permission denied
        except Exception, msg:
            self.fail(msg)

    def test_scoreCalcExceptionHandling(self):
        try:
            self.assertEqual(0, self.screwup.getCrunchScore())
            self.assertEqual(0, self.screwup.getPullupScore())
            self.assertEqual(0, self.screwup.getRunScore())
            self.screwup.saveMemberToFile()
        except Exception, msg:
            self.fail(msg)

    def test_loadMemberListForExceptions(self):
        if os.path.isfile('master.txt'):
            os.remove('master.txt')
        try:
            loadMemberList()
        except Exception, msg:
            self.fail(msg)

    def cleanUpTestFiles(self):
        fileList = ["master.txt"]
        for m in self.mlist:
            filename = m.lastname + "." + m.firstname + ".txt"
            fileList.append(filename)

        for f in fileList:
            if os.path.isfile(f):
                os.remove(f)

    # clean up all the files generated in testing
    def tearDown(self):
        self.cleanUpTestFiles()

if __name__ == '__main__':
    if dotests:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestFitnessFunctions)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        main()

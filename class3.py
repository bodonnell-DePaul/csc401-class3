#more strings
def stringRecap():
    #escape characters
    name = 'Brian O\'Donnell'

    #new line \n \t tab sometimes \r\n for new line in Windows
    print('FirstName: Brian\n\tLastName: O\'Donnell')
    print('FirstName: Brian \r\n')
    print(name,end=' | ')
    print('From Chicago')

    #printing everything from character 0 up to but not including character 6
    print(name[0:6])

    #printing everything but the last 6 characters
    print(name[0:-6])

    #prints everything starting at index 6
    print(name[6:])

    #essentially the same as name[0:6]
    print(name[:6])

def stringFunctions():
    link = 'https://cdm.depaul.edu'
    alteredLink = link[8:]
    print(alteredLink)

    #split early and often
    splitList = link.split('//')
    print(splitList)

    newLink = 'https://www.cdm.depaul.edu/Admission-and-Aid/Pages/NonDegreeOptions.aspx'
    splitList = newLink.split('//')
    splitList = splitList[1].split('/')
    print(splitList)

    #replace will replace all instances of a character or string
    #it is case sensitive
    newLink = newLink.replace("A", "@")
    spacedString = ' my name is George'
    spacedString = spacedString.strip()
    print(newLink)

    event = "Tuesday, Feb 29, 2012 -- 3:35 PM"
    table = str.maketrans(':,-', 3*' ')
    event.translate(table)    
    print(event.translate(table))
    print(event.translate(table).split())

    theEasyWay = event.replace(',','')
    theEasyWay = theEasyWay.replace('-', '')
    theEasyWay = theEasyWay.replace(':', '')

    print(theEasyWay)

    prod = 'morels'
    cost = 139
    wght = 1/2
    total = cost * wght

    #sep= and end= take strings as parameters and have default values of ' ' and '\n' respectively
    print(prod,cost,wght,total, sep=',')

    weekday = 'Wednesday'
    month = 'March'
    day = 10
    year = 2010
    hour = 11
    minute = 45
    second = 33

    #yells at us unless we convert them to strings via str()
    #print(hour+':'+minute+':'+second)
    print('Using generic print strings: '+str(hour)+':'+str(minute)+':'+str(second))

    #use .format instead
    print('Using String.Format -- {}:{}:{}'.format(hour,minute,second))

    #{:2} and {:3} are spacing for integers
    #this same formatting works for strings 
    #primarily used for printing tables
    for i in range(1, 8):
        print('{} {:2} {:3}'.format(i, i**2, 2**i))


    n=10
    #binary output
    print('{:b}'.format(n))
    #character output (ASCII)
    print('{:c}'.format(n))
    #decimal (base10)
    print('{:d}'.format(n))
    #hexidecimal (base16)
    print('{:X}'.format(n))
    #scientific notation
    print('{:e}'.format(n))
    #floating point or 'fixed' point
    #uses 7 characters as the total width
    print('{:7.2f}'.format(n))
    #this uses just the characters needed
    print('{:.2f}'.format(n))



def inputReadOutput(filename, readFunction='r', writeFunction='w'):
    reader = open(filename, readFunction)
    contents = reader.read()
    reader.close()

    contents = contents.replace(',', ' : ')
    contents = contents.replace('.', ' : ')
    contents = contents+'\n'
    outputName = filename.split('.')
    outputName = outputName[0] + '-edit.' + outputName[1]
    writer = open(outputName, writeFunction)
    writer.write(contents)
    writer.close()


def inReadlinesOutput(filename, readFunction='r', writeFunction='w'):
    reader = open(filename, readFunction)
    #contents = reader.readline()
    #reads the entire document 
    contents = reader.readlines()

    #i've already read the entire document there is nothing left to read
    #empty string
    nothingBurger = reader.read()

    #goes back to the beginning of the document
    reader.seek(0)
    #now I can read the first line again
    aLine = reader.readline()

    #reader.close()

    #inefficient way to iterate through a document with readline
    #for line in reader.readline():
    
    #proper way
    for line in contents:  
        line = line.lower()
        if 'Luke'.lower() in line:
            line = line + ', StarWars'
        if 'Brian'.lower() in line:
            line = line + '| Chicago'
        if 'Vader'.lower() in line:
            line = line + ', StarWars'
        if 'Stark'.lower() in line:
            line = line + ': Marvel'
    

def errorGenerator():
    weekday = 'Wednesday'
    month = 'March'
    day = 10
    year = 2010
    hour = 11
    minute = 45
    second = 33

    #this will generate a TypeError for not converting to a string
    #print(hour +':'+ minute+ second)

    #this is a syntax error
    #print('Brian O'Donnell')
          
    #file not found error (FileNotFoundError)
    # use \\ for proper pathing in Windows.  Macs do not have this problem

    #open('C:\\Users\\bodonne3\\OneDrive - DePaul University\\Documents\\python_modules\\week1sample.txt')
    
    try:
        print(hour +':'+ minute+ second)
    except TypeError as vx:
        print('TYPE ERROR: {}'.format(vx))
        print('{}:{}:{}'.format(hour,minute,second))
    except Exception as ex:
        print('ERROR: {}'.format(ex))
        print('UNEXPECTED ERROR, PLEASE REVIEW')
    finally:
        print('recovered from exception, continue execution')



errorGenerator()
# inputReadOutput('test1.txt', writeFunction='a')
# inputReadOutput('test2.txt')
#inReadlinesOutput('test1.txt', writeFunction='w')


    











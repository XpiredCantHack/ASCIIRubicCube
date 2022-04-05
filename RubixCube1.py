import random, time, os, CubeAnimations

red = 'R'
yellow = 'Y'
green = 'G'
blue = 'B'
white = 'W'
orange = 'O'
def genCubeFace(coloursP):
    cubeFace =(''.join(random.choice(coloursP) for i in range(9)))
    for x in range(cubeFace.count(yellow)-1):
        coloursP.remove(yellow)
    for x in range(cubeFace.count(red)-1):
        coloursP.remove(red)
    for x in range(cubeFace.count(green)-1):
        coloursP.remove(green)
    for x in range(cubeFace.count(blue)-1):
        coloursP.remove(blue)
    for x in range(cubeFace.count(white)-1):
        coloursP.remove(white)
    for x in range(cubeFace.count(orange)-1):
        coloursP.remove(orange)
    return cubeFace,coloursP
def generateCube():
    coloursP = [red,red,red,red,red,red,red,red,red,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,blue,blue,blue,blue,blue,blue,blue,blue,blue,green,green,green,green,green,green,green,green,green,white,white,white,white,white,white,white,white,white,orange,orange,orange,orange,orange,orange,orange,orange,orange]
    ##FACE1##
    cubeStats = genCubeFace(coloursP)
    cubeFace1 = cubeStats[0]
    coloursP = cubeStats[1]
    ##FACE2##
    cubeStats = genCubeFace(coloursP)
    cubeFace2 = cubeStats[0]
    coloursP = cubeStats[1]
    ##FACE3##
    cubeStats = genCubeFace(coloursP)
    cubeFace3 = cubeStats[0]
    coloursP = cubeStats[1]
    ##FACE4##
    cubeStats = genCubeFace(coloursP)
    cubeFace4 = cubeStats[0]
    coloursP = cubeStats[1]
    ##FACE5##
    cubeStats = genCubeFace(coloursP)
    cubeFace5 = cubeStats[0]
    coloursP = cubeStats[1]
    ##FACE6##
    cubeStats = genCubeFace(coloursP)
    cubeFace6 = cubeStats[0]
    coloursP = cubeStats[1]
    return cubeFace1,cubeFace2,cubeFace3,cubeFace4,cubeFace5,cubeFace6

##\/\/\/\/\/\/\/\/\/\/##

def renderCube(cubeFace):
    print(cubeFace)
                                
def assembleCubeFace(p1,p2,p3,p4,p5,p6,p7,p8,p9, FaceNum):
    os.system('cls')
    if FaceNum == 0:print(' Face 1 (FRONT)')
    elif FaceNum == 1:print(' Face 2 (RIGHT')
    elif FaceNum == 2:print(' Face 3 (BACK)')
    elif FaceNum == 3:print(' Face 4 (LEFT)')
    elif FaceNum == 4:print(' Face 5 (TOP)')
    elif FaceNum == 5:print(' Face 6 (BOTTOM)')
    cubeFace = f''' ╔═══╦═══╦═══╗
 ║ {p1} ║ {p2} ║ {p3} ║
 ╠═══╬═══╬═══╣
 ║ {p4} ║ {p5} ║ {p6} ║
 ╠═══╬═══╬═══╣
 ║ {p7} ║ {p8} ║ {p9} ║
 ╚═══╩═══╩═══╝'''
    renderCube(cubeFace)

def assembleCubeNet(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50,p51,p52,p53,p54):
    cubeFace = f'''
 ╔═══╦═══╦═══╗
 ║ {p37} ║ {p38} ║ {p39} ║
 ╠═══╬═══╬═══╣
 ║ {p40} ║ {p41} ║ {p42} ║
 ╠═══╬═══╬═══╣
 ║ {p43} ║ {p44} ║ {p45} ║
 ╚═══╩═══╩═══╝
 ╔═══╦═══╦═══╗╔═══╦═══╦═══╗╔═══╦═══╦═══╗╔═══╦═══╦═══╗
 ║ {p1} ║ {p2} ║ {p3} ║║ {p10} ║ {p11} ║ {p12} ║║ {p19} ║ {p20} ║ {p21} ║║ {p28} ║ {p29} ║ {p30} ║
 ╠═══╬═══╬═══╣╠═══╬═══╬═══╣╠═══╬═══╬═══╣╠═══╬═══╬═══╣
 ║ {p4} ║ {p5} ║ {p6} ║║ {p13} ║ {p14} ║ {p15} ║║ {p22} ║ {p23} ║ {p24} ║║ {p31} ║ {p32} ║ {p33} ║
 ╠═══╬═══╬═══╣╠═══╬═══╬═══╣╠═══╬═══╬═══╣╠═══╬═══╬═══╣
 ║ {p7} ║ {p8} ║ {p9} ║║ {p16} ║ {p17} ║ {p18} ║║ {p25} ║ {p26} ║ {p27} ║║ {p34} ║ {p35} ║ {p36} ║
 ╚═══╩═══╩═══╝╚═══╩═══╩═══╝╚═══╩═══╩═══╝╚═══╩═══╩═══╝
 ╔═══╦═══╦═══╗
 ║ {p46} ║ {p47} ║ {p48} ║
 ╠═══╬═══╬═══╣
 ║ {p49} ║ {p50} ║ {p51} ║
 ╠═══╬═══╬═══╣
 ║ {p52} ║ {p53} ║ {p54} ║
 ╚═══╩═══╩═══╝'''
    os.system('cls')
    renderCube(cubeFace)
    

def splitFaces(cubeDetails, FaceNum):
    cubeFace = cubeDetails[FaceNum]
    return cubeFace
def netCube(cubeDetails, FaceNum):
    cubeFace = splitFaces(cubeDetails, FaceNum)
    p1 = cubeFace[0]
    p2 = cubeFace[1]
    p3 = cubeFace[2]
    p4 = cubeFace[3]
    p5 = cubeFace[4]
    p6 = cubeFace[5]
    p7 = cubeFace[6]
    p8 = cubeFace[7]
    p9 = cubeFace[8]
    return p1,p2,p3,p4,p5,p6,p7,p8,p9

def displayCubeNet(cubeDetails):
    cubeNetDetails = ()
    for FaceNum in range(6):
        points = netCube(cubeDetails, FaceNum)
        cubeNetDetails = cubeNetDetails + points
    assembleCubeNet(*cubeNetDetails)


def displayCube(cubeDetails, FaceNum):
    cubeFace = splitFaces(cubeDetails, FaceNum)
    p1 = cubeFace[0]
    p2 = cubeFace[1]
    p3 = cubeFace[2]
    p4 = cubeFace[3]
    p5 = cubeFace[4]
    p6 = cubeFace[5]
    p7 = cubeFace[6]
    p8 = cubeFace[7]
    p9 = cubeFace[8]
    assembleCubeFace(p1,p2,p3,p4,p5,p6,p7,p8,p9, FaceNum)

def rotateBackFace(cubeDetails, rotations):
    ##TEST ALGORITHM##!!
    ##POTENTIAL MAPPING ERROR (dev can't picture it (make mapping solution (p5.js) or just get smarter))##!!##!!!
    face1 = cubeDetails[0] ##unaffected~~
    face2 = cubeDetails[1]
    face3 = cubeDetails[2]
    face4 = cubeDetails[3]
    face5 = cubeDetails[4]
    face6 = cubeDetails[5]
    
    face6 = face6[6:9]
    face2 = face2[2] + face2[5] + face2[8]
    face5 = face5[0:3]
    face4 = face4[0] + face4[3] + face4[6]

    face0 = face4
    face4 = face5
    face5 = face2
    face2 = face6
    face6 = face0
    del face0

    ##full anticlockwise rotation for face3
    newFace3 = face3[2]+face3[5]+face3[8]+face3[1]+face3[4]+face3[7]+face3[0]+face3[3]+face3[6]
    face3 = newFace3

    cubeFace6 = cubeDetails[5]
    cubeFace6 = cubeFace6[0:6] + face6
    cubeFace2 = cubeDetails[1]
    cubeFace2 = cubeFace2[0:2] + face2[2] + cubeFace2[3:5] + face2[1] + cubeFace2[6:8] + face2[0]
    cubeFace5 = cubeDetails[4]
    cubeFace5 = face5 + cubeFace5[3:9]
    cubeFace4 = cubeDetails[3]
    cubeFace4 = face4[2] + cubeFace4[1:3] + face4[1] + cubeFace4[4:6] +face4[0] + cubeFace4[7:9]
    cubeFace3 = face3
    cubeFace1 = face1
    return cubeFace1, cubeFace2, cubeFace3, cubeFace4, cubeFace5, cubeFace6

def rotateFrontFace(cubeDetails, rotations):
    ##face rotates anticlockwise
    face1 = cubeDetails[0]
    face2 = cubeDetails[1]
    face3 = cubeDetails[2] ##unaffected~~
    face4 = cubeDetails[3]
    face5 = cubeDetails[4]
    face6 = cubeDetails[5]

    face6 = face6[0:3]
    face2 = face2[6] + face2[3] + face2[0]
    face5 = face5[6:9]
    face4 = face4[2] + face4[5] + face4[8]

    face0 = face4
    face4 = face5
    face5 = face2
    face2 = face6
    face6 = face0
    del face0

    ##full anticlockwise rotation for face1
    newFace1 = face1[2]+face1[5]+face1[8]+face1[1]+face1[4]+face1[7]+face1[0]+face1[3]+face1[6]
    face1 = newFace1

    cubeFace6 = cubeDetails[5]
    cubeFace6 = face6 + cubeFace6[3:9]
    cubeFace2 = cubeDetails[1]
    cubeFace2 = face2[2] + cubeFace2[1:3] + face2[1] + cubeFace2[4:6] + face2[0] + cubeFace2[7:9]
    cubeFace5 = cubeDetails[4]
    cubeFace5 = cubeFace5[0:6] + face5[2] + face5[1] + face5[0]
    cubeFace4 = cubeDetails[3]
    cubeFace4 = cubeFace4[0:2] + face4[0] + cubeFace4[3:5] + face4[1] + cubeFace4[6:8] + face4[2]
    cubeFace1 = face1
    cubeFace3 = cubeDetails[2]

    return cubeFace1, cubeFace2, cubeFace3, cubeFace4, cubeFace5, cubeFace6
def rotateLeftSide(cubeDetails, rotations):
    face1 = cubeDetails[0]
    face2 = cubeDetails[1] ##unaffected 
    face3 = cubeDetails[2]
    face4 = cubeDetails[3]
    face5 = cubeDetails[4]
    face6 = cubeDetails[5]

    face1 = face1[0] + face1[3] + face1[6]
    ##face2 is unaffected
    face3 = face3[2] + face3[5] + face3[8]
    ##face4 will rotate full face
    face5 = face5[0] + face5[3] + face5[6]
    face6 = face6[0] + face6[3] + face6[6]

    face0 = face1
    face1 = face5
    face5 = face3
    ##face5 is upside down
    f1face5 = face5[0]
    f2face5 = face5[1]
    f3face5 = face5[2]
    face5 = f3face5 + f2face5 + f1face5
    face3 = face6
    f1face3 = face3[0]
    f2face3 = face3[1]
    f3face3 = face3[2]
    face3 = f3face3 + f2face3 + f1face3
    face6 = face0
    del face0
    ##full clockwise rotation for face4
    newFace4 = face4[6]+face4[3]+face4[0]+face4[7]+face4[4]+face4[1]+face4[8]+face4[5]+face4[2]
    face4 = newFace4
    cubeFace1 = cubeDetails[0]
    cubeFace1 = face1[0] + cubeFace1[1:3] + face1[1] + cubeFace1[4:6] + face1[2] + cubeFace1[7:9]
    cubeFace2 = face2
    cubeFace3 = cubeDetails[2]
    cubeFace3 = cubeFace3[0:2] + face3[0] + cubeFace3[3:5] + face3[1] + cubeFace3[6:8] + face3[2]
    cubeFace4 = face4
    cubeFace5 = cubeDetails[4]
    cubeFace5 = face5[0] + cubeFace5[1:3] + face5[1] + cubeFace5[4:6] + face5[2] + cubeFace5[7:9]
    cubeFace6 = cubeDetails[5]
    cubeFace6 = face6[0] + cubeFace6[1:3] + face6[1] + cubeFace6[4:6] + face6[2] + cubeFace6[7:9]

    return cubeFace1, cubeFace2, cubeFace3, cubeFace4, cubeFace5, cubeFace6
    
def rotateRightSide(cubeDetails, rotations):
    face1 = cubeDetails[0]
    face2 = cubeDetails[1]
    face3 = cubeDetails[2]
    face4 = cubeDetails[3] ##unaffected
    face5 = cubeDetails[4]
    face6 = cubeDetails[5]

    face1 = face1[2] + face1[5] + face1[8]
    ##face2 will rotate full face
    face3 = face3[0] + face3[3] + face3[6]
    ##face4 is unaffected
    face5 = face5[2] + face5[5] + face5[8]
    face6 = face6[2] + face6[5] + face6[8]

    face0 = face1
    face1 = face5
    face5 = face3
    ##face5 is upside down
    f1face5 = face5[0]
    f2face5 = face5[1]
    f3face5 = face5[2]
    face5 = f3face5 + f2face5 + f1face5
    face3 = face6
    f1face3 = face3[0]
    f2face3 = face3[1]
    f3face3 = face3[2]
    face3 = f3face3 + f2face3 + f1face3
    face6 = face0
    del face0
    ##full rotation for face2## ##anticlockwise##
    newFace2 = face2[2]+face2[5]+face2[8]+face2[1]+face2[4]+face2[7]+face2[0]+face2[3]+face2[6]
    face2 = newFace2
    ##update all faces (face3 is packaged differently)##!!!
    cubeFace1 = cubeDetails[0]
    cubeFace1 = cubeFace1[:2] +face1[0] + cubeFace1[3:5] + face1[1] + cubeFace1[6:8] + face1[2]
    cubeFace2 = face2
    cubeFace3 = cubeDetails[2]
    cubeFace3 = face3[0] + cubeFace3[1:3] + face3[1] + cubeFace3[4:6] + face3[2] + cubeFace3[7:9]
    cubeFace4 = face4
    cubeFace5 = cubeDetails[4]
    cubeFace5 = cubeFace5[:2] +face5[0] + cubeFace5[3:5] + face5[1] + cubeFace5[6:8] + face5[2]
    cubeFace6 = cubeDetails[5]
    cubeFace6 = cubeFace6[:2] +face6[0] + cubeFace6[3:5] + face6[1] + cubeFace6[6:8] + face6[2]
    
    return cubeFace1, cubeFace2, cubeFace3, cubeFace4, cubeFace5, cubeFace6
    
    
def rotateBottomRow(cubeDetails, rotation):
    face1 = cubeDetails[0]
    face2 = cubeDetails[1]
    face3 = cubeDetails[2]
    face4 = cubeDetails[3]
    face6 = cubeDetails[5]
    
    face1 = face1[6:9]
    face2 = face2[6:9]
    face3 = face3[6:9]
    face4 = face4[6:9]
    ##complete rotation
    face0 = face1
    face1 = face2
    face2 = face3
    face3 = face4
    face4 = face0
    del face0
    ##face6 rotates anticlockwise!!
    newFace6 = face6[2]+face6[5]+face6[8]+face6[1]+face6[4]+face6[7]+face6[0]+face6[3]+face6[6]
    ##update faces
    cubeFace1 = cubeDetails[0]
    cubeFace1 = cubeFace1[:6] +face1
    cubeFace2 = cubeDetails[1]
    cubeFace2 = cubeFace2[:6] +face2
    cubeFace3 = cubeDetails[2]
    cubeFace3 = cubeFace3[:6] +face3
    cubeFace4 = cubeDetails[3] 
    cubeFace4 = cubeFace4[:6]  +face4 
    cubeFace5 = cubeDetails[4]
    cubeFace6 = newFace6                                  
    return cubeFace1, cubeFace2, cubeFace3, cubeFace4, cubeFace5, cubeFace6
##do face6 changes now##!


def rotateTopRow(cubeDetails, rotation):
    face1 = cubeDetails[0]
    face2 = cubeDetails[1]
    face3 = cubeDetails[2]
    face4 = cubeDetails[3]
    face5 = cubeDetails[4]
    face1 = face1[0:3]
    face2 = face2[0:3]
    face3 = face3[0:3]
    face4 = face4[0:3]
    ##complete rotation
    face0 = face1
    face1 = face2
    face2 = face3
    face3 = face4
    face4 = face0
    del face0
    newFace5 = face5[6]+face5[3]+face5[0]+face5[7]+face5[4]+face5[1]+face5[8]+face5[5]+face5[2]
    ##update faces
    cubeFace1 = cubeDetails[0]
    cubeFace1 = face1 + cubeFace1[3:]
    cubeFace2 = cubeDetails[1]
    cubeFace2 = face2 + cubeFace2[3:]
    cubeFace3 = cubeDetails[2]
    cubeFace3 = face3 + cubeFace3[3:]
    cubeFace4 = cubeDetails[3]
    cubeFace4 = face4 + cubeFace4[3:]
    cubeFace5 = newFace5
    cubeFace6 = cubeDetails[5]                                  
    return cubeFace1, cubeFace2, cubeFace3, cubeFace4, cubeFace5, cubeFace6
##face5 rotates clockwise!!!!

def solve_cube(cubeDetails):
    global Gen_key
    print(Gen_key)
    Gen_key = Gen_key[::-1]
    print(Gen_key)
    for i in range(len(Gen_key)):
        function_choice = Gen_key[i]
        rotations = 3
        if function_choice == '2':
            cubeDetails = rotateTopRow(cubeDetails, rotations)
        elif function_choice == '3':
            cubeDetails = rotateBottomRow(cubeDetails, rotations)
        elif function_choice == '4':
            cubeDetails = rotateRightSide(cubeDetails, rotations)
        elif function_choice == '5':
            cubeDetails = rotateLeftSide(cubeDetails, rotations)
        elif function_choice == '6':
            cubeDetails = rotateFrontFace(cubeDetails, rotations)
        elif function_choice == '7':
            cubeDetails = rotateBackFace(cubeDetails, rotations)
        displayCubeNet(cubeDetails)
    
def userInput(cubeDetails):
    while True:
        #print(f'Here;;; {cubeDetails}')
        function_choice = int(input('''
 [0] Display Full Net
 [1] Display Face
 [2] Rotate Top Row (Left)
 [3] Rotate Bottom Row (Left)
 [4] Rotate Right Side (Down)
 [5] Rotate Left Side (Down)
 [6] Rotate Front Face (Anti-Clockwise)
 [7] Rotate Back Face (Anti-Clockwise)
 [8] Regenerate Cube'''))
        if function_choice == 0:
            displayCubeNet(cubeDetails)
        elif function_choice == 1:
            FaceNum = int(input(' Face:'))
            if FaceNum < 1 or FaceNum > 6: userInput()
            else:
                FaceNum = FaceNum - 1
                displayCube(cubeDetails, FaceNum)
        ##all rotations are left turns of an amount
        elif function_choice == 2:
            rotations = int(input(' Number of rotations: '))
            for x in range(rotations):
                cubeDetails = rotateTopRow(cubeDetails, rotations)
        elif function_choice == 3:
            rotations = int(input(' Number of rotations: '))
            for x in range(rotations):
                cubeDetails = rotateBottomRow(cubeDetails, rotations)
        elif function_choice == 4:
            rotations = int(input(' Number of rotations: '))
            for x in range(rotations):
                cubeDetails = rotateRightSide(cubeDetails, rotations)
        elif function_choice == 5:
            rotations = int(input(' Number of rotations: '))
            for x in range(rotations):
                cubeDetails = rotateLeftSide(cubeDetails, rotations)
        elif function_choice == 6:
            rotations = int(input(' Number of rotations: '))
            for x in range(rotations):
                cubeDetails = rotateFrontFace(cubeDetails, rotations)
        elif function_choice == 7:
            rotations = int(input(' Number of rotations: '))
            for x in range(rotations):
                cubeDetails = rotateBackFace(cubeDetails, rotations)
        elif function_choice == 8:
            os.system('cls')
            cubeDetails = generateSOLVABLECube()
            CubeAnimations.loadingCube()
            print('GENERATED')
            time.sleep(0.6)
            os.system('cls')
        elif function_choice == 230606:
            solve_cube(cubeDetails)
        else:pass
        
def generateSOLVABLECube():
    chars1 = '234567'
    randomlength = random.randint(23, 356)
    global Gen_key
    Gen_key = (''.join(random.choice(chars1) for i in range(randomlength)) )
    cubeDetails = 'RRRRRRRRR','GGGGGGGGG','BBBBBBBBB','YYYYYYYYY','WWWWWWWWW','OOOOOOOOO'
    for i in range(len(Gen_key)):
        function_choice = Gen_key[i]
        rotations = 1
        if function_choice == '2':
            cubeDetails = rotateTopRow(cubeDetails, rotations)
        elif function_choice == '3':
            cubeDetails = rotateBottomRow(cubeDetails, rotations)
        elif function_choice == '4':
            cubeDetails = rotateRightSide(cubeDetails, rotations)
        elif function_choice == '5':
            cubeDetails = rotateLeftSide(cubeDetails, rotations)
        elif function_choice == '6':
            cubeDetails = rotateFrontFace(cubeDetails, rotations)
        elif function_choice == '7':
            cubeDetails = rotateBackFace(cubeDetails, rotations)
    return cubeDetails

cubeDetails = generateSOLVABLECube()
userInput(cubeDetails)

#######
#Rotations:
#rotate top row [done]
#rotate bottom row [done]
#rotate right side [done]
#rotate left side [done]
#rotate front full face [done]
#rotate back full face [done]!


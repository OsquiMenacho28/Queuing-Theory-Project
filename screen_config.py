def setWindowInCenterOfScreen(window, setWindowWidth, setWindowHeight):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    windowWidth = setWindowWidth
    windowHeight = setWindowHeight
    positionWidth = round(screenWidth / 2 - windowWidth / 2)
    positionHeight = round(screenHeight / 2 - windowHeight / 2)
    window.geometry(str(windowWidth)+"x"+str(windowHeight)+"+"+str(positionWidth)+"+"+str(positionHeight))
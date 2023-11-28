def setWindowInCenterOfScreen(window):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    windowWidth = 500
    windowHeight = 300
    positionWidth = round(screenWidth / 2 - windowWidth / 2)
    positionHeight = round(screenHeight / 2 - windowHeight / 2)
    window.geometry(str(windowWidth)+"x"+str(windowHeight)+"+"+str(positionWidth)+"+"+str(positionHeight))
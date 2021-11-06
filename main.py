
import matplotlib.pyplot as mplot
import matplotlib.cm as cm
import numpy as np
import pandas as pndas
import os
import cv2

URL_="_"
IMAGE_FOLDER="C:\\Users\\FrancescoRinaldi\\Desktop\\images1\\"
IMAGE_NAME="image_"
VIDEO_NAME="videoDiagonal-3D.avi"

def UploadFile():
    print("Enter the full path of the csv file you want work with:")
    print("Path:")   
    URL_="C:\\Users\\FrancescoRinaldi\\Dropbox\\david_francesco\ResearchWorkspace\\ComponentsInSpace\\models\\space-movement-only\\3Dmovements\\coordinateBasedApproach-3D&DiagonalXY-1.csv" 
    #URL_=str(input())
    openFile(URL_, 1, " ")
    mplot.show()
def openFile(fileUrl, index, urlName):
    try:
        #getting the dataFrame from the CSV file
        dataFrame=pndas.read_csv(fileUrl)   
        plottingData3D(dataFrame)    
    except FileNotFoundError as ex:
        print(ex)
    except Exception as e:
        print("[ERROR] - Calculation has been occured with errors Exception " + str(e))
    return
def buildMovie():    
    print("Building movie....")
    images = [img for img in os.listdir(IMAGE_FOLDER) if img.endswith(".png")]
    
    frame = cv2.imread(os.path.join(IMAGE_FOLDER, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(VIDEO_NAME, 0, 1, (width,height))

    for i in range (0,len(images)):
        iName= IMAGE_NAME+str(i) +".png"
        image= [img for img in images if img == iName]
        path= os.path.join(IMAGE_FOLDER, image[0])
        video.write(cv2.imread(path))

    cv2.destroyAllWindows()
    video.release()
    print("Done.")
def plottingData2D(dataFrame):            
    
    dataFrame=dataFrame.drop(['Time'], axis=1)
    columLen= len(dataFrame.columns)        
    N = columLen//2
    
    x = np.arange(10)
    ys = [i+x+(i*x)**2 for i in range(N)]
    colors = cm.rainbow(np.linspace(0, 1, len(ys)))
    counter=0
    ax = mplot.gca()
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])
    
    for r in range(0,len(dataFrame)-1):
        row= dataFrame.loc[r]
        nextRow= dataFrame.loc[r+1]
        
        #try without all columns, bust just plotting x_C1_1 and y_C1_1
        for c in range (0,(columLen//2)):
            
            x1=row[dataFrame.columns[c]]
            y1=row[dataFrame.columns[c+((columLen//2))]]
            x2=nextRow[dataFrame.columns[c]]
            y2=nextRow[dataFrame.columns[c+((columLen//2))]]            
            
            if x1!=x2 and y1!=y2:
                x=[x1,x2]
                y=[y1,y2]
                col=colors[c]
                print(str(x) + '\n')
                print(y)
                mplot.scatter(x,y, color=col)
                mplot.plot(x,y, color=col)                        
            
                mplot.savefig(IMAGE_FOLDER+ IMAGE_NAME +"{0}.png".format(counter))
                counter+=1
            
   # mplot.show()         
def plottingData3D(dataFrame):            
    
    dataFrame=dataFrame.drop(['Time'], axis=1)
    columLen= len(dataFrame.columns)        
    N = columLen//2
    
    x = np.arange(10)
    ys = [i+x+(i*x)**2 for i in range(N)]
    colors = cm.rainbow(np.linspace(0, 1, len(ys)))
    counter=0
    fig=mplot.figure()
    ax=fig.add_subplot(projection='3d')
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])
    ax.set_zlim([0,20])
    for r in range(0,len(dataFrame)-1):
        row= dataFrame.loc[r]
        nextRow= dataFrame.loc[r+1]
        
        #try without all columns, bust just plotting x_C1_1 and y_C1_1
        for c in range (0,(columLen//2)):
            
            x1=row[dataFrame.columns[c]]
            y1=row[dataFrame.columns[c+((columLen//2))]]
            z1=row[dataFrame.columns[c+1+((columLen//2))]]
            x2=nextRow[dataFrame.columns[c]]
            y2=nextRow[dataFrame.columns[c+((columLen//2))]]            
            z2=row[dataFrame.columns[c+1+((columLen//2))]]
                        
            X=[x1,x2]
            Y=[y1,y2]
            Z=[z1,z2]
            
            
            ax.scatter(X,Y,Z, c='r', marker='o')
            ax.plot(X,Y,Z)
            ax.set_xlabel('x axis')
            ax.set_ylabel('y axis')
            ax.set_zlabel('z axis')
                                                        
            mplot.savefig(IMAGE_FOLDER+ IMAGE_NAME +"{0}.png".format(counter))
            counter+=1       
        print(counter)

if __name__ == "__main__":        
    UploadFile()
    buildMovie()
    
    


       
       

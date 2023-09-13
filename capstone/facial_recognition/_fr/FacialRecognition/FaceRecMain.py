
import sys, cv2, os, csv, face_recognition
import numpy as np
from sklearn import neighbors


def LoadImages(known_path='./FRImages/Known'):
    print("Encoding Known Faces:")
    images = []
    names = []
    known_faces = []
    known_names = []
    for name in os.listdir(known_path):
        print(name)
        for filename in os.listdir(f"{known_path}/{name}"):
            image = face_recognition.load_image_file(f"{known_path}/{name}/{filename}")
            facesloc = face_recognition.face_locations(image)
            if len(facesloc) != 1:
                print(f"\nImage {name}/{filename} has miltiple faces. Known Faces need to have a single face in the photo to train the model.\n")
                continue
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(name)
    if len(known_faces) != len(known_names):
        print("HUGE ERROR\n HUGE ERROR\nHUGE ERROR\nKnown Faces != Known Names")
        print("known face len", len(known_faces))
        print("known names len", len(known_names))
    np.savetxt("./FRImages/knownfaceencode.csv", known_faces, delimiter=",")
    with open("./FRImages/knownnames.csv", 'w') as f:
        write = csv.writer(f)
        write.writerow(known_names)


def FindMatches(image, known_faces, known_names, thresh=.53, web=False, imgSmall=None):
    if web:
        imgtemp=image
        image = imgSmall
    facesloc = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image,facesloc)
    if not web:
        print(f" found {len(encodings)} face(s)")
    for encodeFace, locFace in zip(encodings, facesloc):
        FaceDist = face_recognition.face_distance(known_faces, encodeFace)
        matchIndex = np.argmin(FaceDist)
        if FaceDist[matchIndex] < thresh:
            name = known_names[matchIndex]
        else:
            name = "Unknown"
        y1, x2, y2, x1 = locFace
        if web:
            y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
            image=imgtemp
        else:
            print(f"{name} had score {FaceDist[matchIndex]}")
        color = (0,255,0)
        cv2.rectangle(image, (x1,y1),(x2,y2),color,2)
        cv2.rectangle(image, (x1,y2-35),(x2,y2),color,cv2.FILLED)
        cv2.putText(image,name,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)


def ProcessUnknown(known_faces, known_names, \
                   unknown_path='./FRImages/Unknown', thresh=.53):
    print("Processing Unknown Faces:")
    for filename in os.listdir(unknown_path):
        print(f"File {filename}", end='')
        image = face_recognition.load_image_file(f"{unknown_path}/{filename}")
        FindMatches(image, known_faces, known_names, thresh)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow(filename,image)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyWindow(filename)
            break
        cv2.destroyWindow(filename)


def Webcam(known_faces, known_names, thresh=.53, web=True):
    capture = cv2.VideoCapture(0)
    while True:
        success, image = capture.read()
        imgSmall = cv2.resize(image, (0,0), None, 0.5, 0.5)
        FindMatches(image, known_faces, known_names, thresh, web=web, imgSmall=imgSmall)
        cv2.imshow("Webcam", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def Accuracy(known_faces, known_names, accuracy_path='./FRImages/Accuracy', thresh=.53):
    count = 0
    correct =0
    nofacecount=0
    print(f"Checking Accuracy of model.")
    for name in os.listdir(accuracy_path):
        print(name)
        unkcount =1
        for filename in os.listdir(f"{accuracy_path}/{name}"):
            count = count+1
            if name == "Unknown":
                unkcount = unkcount+1
            if unkcount % 100 == 0:
                print(f"processed {unkcount} of 300 unknown images")
            image = face_recognition.load_image_file(f"{accuracy_path}/{name}/{filename}")
            facesloc = face_recognition.face_locations(image)
            if len(facesloc) != 1:
                # print(f"\nImage {name}/{filename} has miltiple/none faces. \n")
                # print(f"{len(facesloc)} faces found")
                if len(facesloc) == 0:
                    nofacecount= nofacecount+1
                count = count-1
                continue
            encodings = face_recognition.face_encodings(image,facesloc)
            for encodeFace, locFace in zip(encodings, facesloc):
                FaceDist = face_recognition.face_distance(known_faces, encodeFace)
                matchIndex = np.argmin(FaceDist)
                if FaceDist[matchIndex] < thresh:
                    aname = known_names[matchIndex]
                else:
                    aname = "Unknown"
                if name == aname:
                    correct = correct +1
                else:
                    print(f"\nImage {name}/{filename} was incorrectly identified as {aname}. \n")
    print(f"Accuracy is {round(correct/count*100,4)}%")
    print(f"{nofacecount} of {count} images appeared to have no faces")
    return(round(correct/count*100,8))


def KNNpredictUnk(known_faces, known_names, knn_model, knn_path = "./FRImages/Unknown", thresh = .53):
    for filename in os.listdir(knn_path):
        print(f"File {filename}", end='')
        image = face_recognition.load_image_file(f"{knn_path}/{filename}")
        facesloc = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image,facesloc)
        for encodeFace, locFace in zip(encodings, facesloc):
            closest = knn_model.kneighbors(encodeFace.reshape(1, -1),n_neighbors=1)
            if closest[0][0][0] <= thresh:
                name = knn_model.predict(encodeFace.reshape(1,-1))[0]
            else:
                name = "Unknown"
            y1, x2, y2, x1 = locFace
            print(f"{name} had score {closest[0][0][0]}")
            color = (0,255,0)
            cv2.rectangle(image, (x1,y1),(x2,y2),color,2)
            cv2.rectangle(image, (x1,y2-35),(x2,y2),color,cv2.FILLED)
            cv2.putText(image,name,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)
        image =cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow(filename,image)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyWindow(filename)
            break
        cv2.destroyWindow(filename)


def KNNtrain(known_faces, known_names, n_neighbors = None, knn_algorithm = 'auto'):
    if n_neighbors == None:
        n_neighbors = int(round(np.sqrt(len(known_faces))))
    knn_model = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm = knn_algorithm, weights = 'distance')
    knn_model.fit(known_faces, known_names)
    return knn_model


def KNNaccuracy(known_faces, known_names, knn_model, accuracy_path='./FRImages/Accuracy', thresh=.53):
    count, correct, nofacecount = 0,0,0
    print(f"Checking Accuracy of KNN model.")
    for name in os.listdir(accuracy_path):
        print(name)
        unkcount=1
        for filename in os.listdir(f"{accuracy_path}/{name}"):
            count= count +1
            if name == "Unknown":
                unkcount = unkcount +1
            if unkcount % 100 == 0:
                print(f"processed {unkcount} of 300 unknown images")
            image = face_recognition.load_image_file(f"{accuracy_path}/{name}/{filename}")
            facesloc = face_recognition.face_locations(image)
            if len(facesloc) != 1:
                if len(facesloc) == 0:
                    nofacecount= nofacecount+1
                count = count-1
                continue
            encodings = face_recognition.face_encodings(image,facesloc)
            for encodeFace, locFace in zip(encodings, facesloc):
                closest = knn_model.kneighbors(encodeFace.reshape(1, -1),n_neighbors=1)
                if closest[0][0][0] <= thresh:
                    aname = knn_model.predict(encodeFace.reshape(1, -1))
                else:
                    aname = "Unknown"
                if name == aname:
                    correct = correct +1
                else:
                    print(f"\nImage {name}/{filename} was incorrectly identified as {aname}. \n")
    print(f"Accuracy is {round(correct/count*100,4)}%")
    print(f"{nofacecount} of {count} images appeared to have no faces")
    return(round(correct/count*100,8))


def main():
    #Encode Known Faces by default
    if not "loadknown" in sys.argv:
        LoadImages()

    #Load known from files
    print("Loading Known Faces")
    known_faces = np.genfromtxt("./FRImages/knownfaceencode.csv", delimiter=",")
    with open("./FRImages/knownnames.csv") as f:
        reader = csv.reader(f)
        known_names = list(reader)[0]

    #Process Unknown Faces by default
    if not "nounknown" in sys.argv:
        ProcessUnknown(known_faces,known_names)

    #Use Webcam for face recognition
    if "webcam" in sys.argv:
        Webcam(known_faces,known_names)

    if "accuracy" in sys.argv:
        Accuracy(known_faces, known_names)

    if "threshcheck" in sys.argv:
        threshhodls = np.arange(0.5, 0.6, 0.01)
        ascore = []
        for thresh in threshhodls:
            print(f"checking threshold: {thresh}")
            acc = Accuracy(known_faces, known_names, thresh=thresh)
            ascore.append(acc)
        print(threshhodls)
        print(ascore)
        matchIndex=np.argmax(ascore)
        print(f"The threshold with the best accuracy was: {threshhodls[matchIndex]}")

    if "knn" in sys.argv:
        knn_model = KNNtrain(known_faces, known_names)
        if "knnunk" in sys.argv:
            KNNpredictUnk(known_faces, known_names, knn_model)
        if "knnacc" in sys.argv:
            KNNaccuracy(known_faces, known_names, knn_model)
        if "knnthreshcheck" in sys.argv:
            thresholds = np.arange(0.5,0.6,0.01)
            ascore =[]
            for thresh in thresholds:
                print(f"check threshold: {thresh}")
                acc = KNNaccuracy(known_faces, known_names, knn_model, thresh = thresh)
                ascore.append(acc)
            print(thresholds)
            print(ascore)
            matchIndex=np.argmax(ascore)
            print(f"The threshold with the best accuracy was: {thresholds[matchIndex]}")


if __name__ == "__main__":
    main()

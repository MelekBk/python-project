from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidgetItem
from pickle import dump, load

def ajouter():
    ch=win.le.text()
    if ch=="":
        QMessageBox.critical(win,"Erreur saisie","Vous devez saisir un nombre")
    elif (not ch.isdecimal()):
        QMessageBox.critical(win,"Erreur saisie","Le nombre doit etre positif")
    else:
        f=open("nombre.txt","a")
        f.write(ch+"\n")
        f.close()
        e=dict(n=int,sd=int,prop=str)
        f1=open("proprietes.dat","ab")
        e["n"]=int(ch)
        e["sd"]=somme(int(ch))
        if e["n"]<e["sd"]:
            e["prop"]=="abondant"
        elif e["n"]>e["sd"] :
            e["prop"]=="déficient"
        else:
            e["prop"]=="parfait"
        dump(e,f1)
        QMessageBox.information(win,"ajout","ajout de l'entier avec succes")
        f1.close()
def somme(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s=s+i
    return s         
    
def afficher1():
    win.lw.clear()
    try:
        f=open("nombre.txt","r")
        ch=f.read()
        win.lw.addItem(ch)
        f.close()
    except:
        QMessageBox.critical(win,"Erreur ","Le fichier nombre.txt est inexistant")
        
    
def afficher2():
    try:
        f1=open("proprietes.dat","rb")
        win.tw.setRowcount(0)
        i=0
        v=dict(n=int,sd=int,prop=str)
        ff=False
        while not ff:
            try:
                v=load(f1)
                win.tw.insertRow(i)
                win.tw.setItem(i,0,QTableWidgetItem(str(v["n"])))
                win.tw.setItem(i,1,QTableWidgetItem(str(v["sd"])))
                win.tw.setItem(i,2,QTableWidgetItem((v["prop"])))
                i=i+1
            except:
                ff=True
    except:
        QMessageBox.critical(win,"Erreur ","Le fichier proprietes est inexistant")
    print("mon travailll python")
            
        

app = QApplication([])
win = loadUi ("C:/Users/moham/Documents/pratique maison/untitled.ui")
win.show()
win.bta.clicked.connect ( ajouter)
win.btan.clicked.connect ( afficher1)
win.btap.clicked.connect ( afficher2 )

app.exec_()

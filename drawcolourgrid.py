from tkinter import *
#take array of colours in 2d array
#rgb values r,g,b tuple
class Example(Frame):
    #define window

    def __init__(self,pattern):
        super().__init__()

        self.depth=self.initUI(pattern)
        


    def initUI(self,pattern):

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        depth=90
        canvas = Canvas(self)
        #create grid
        for row in range(0,len(pattern)):
            for item in range(0,len(pattern[row])):
                
                canvas.create_rectangle(30+(item*90), 10+(row*90), 120+(item*90), 100+(row*90),
                    outline="black", fill=pattern[row][item])
                depth=depth+(row*90)
        canvas.pack(fill=BOTH, expand=1)
        #window adjustment
        return depth


def _from_rgb(rgb):
    #translates an rgb tuple of int to hexcolours
    return "#%02x%02x%02x" % rgb   

def main():
    #change this to the values you want to use # this is the input!
    raw_input=[[( 120, 0 , 255 ),(223,154,222)],[(0, 128, 64)]]
    preparedinput=[]
    #prepare input for processing
    for i in raw_input:
        li=[]
        for item in i:
            li.append(_from_rgb(item))
        preparedinput.append(li)
    root = Tk()
    ex = Example(preparedinput)

    #run window
    root.geometry("400x"+str(ex.depth))
    root.mainloop()


if __name__ == '__main__':
    main()

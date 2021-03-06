import sys
from Data import all_routes, capitals
from tkinter import scrolledtext
from tkinter import *
from Graph import G

v = list(set(G.nodes))

a = Tk()

a.geometry('250x250')
a.configure(background="#35424a")
a.title(string='')

frame = LabelFrame(
    a,
    text='State Capital Road Trip',
    bg='#f0f0f0',
    font=(20)
)
frame.pack(expand=True, fill=BOTH)


#Entry widget object
textin = StringVar()

def clk():
        
    statement = ''  
    statement2 = '\n\nDirections\n--------------------------------------------------------------------------\n'     

    G_deep = G.copy()
    starting_captial = ent.get()
    unvisited_capitals = set()
    path = [starting_captial]
    mileage = 0
    
    for i in v:
        if i != starting_captial:
            unvisited_capitals.add(i)

    current_captial = starting_captial
    
    for i in range(0,len(unvisited_capitals)):

        list_of_edges = list(G_deep.edges(current_captial, data="weight"))            
        nearest_neighbor = min(list_of_edges, key = lambda t: t[2])
        
        mileage = mileage + nearest_neighbor[2]        

        for i in unvisited_capitals:
            G_deep.remove_edge(current_captial, i)
        
        
        current_captial = nearest_neighbor[1]
        path.append(current_captial)
        unvisited_capitals.remove(current_captial)
           
    index1 = 0
    index2 = 1
    
    while (index2 != 49):
        info = all_routes[path[index1] ][ path[index2] ]
        route_taken = info[1:]
        start_dest_capital = capitals[ path[index1] ][0]
        start_dest_state = capitals[ path[index1] ][1]
        end_dest_capital = capitals[ path[index2] ][0]
        end_dest_state = capitals[ path[index2] ][1]
        index1, index2 = index1+1, index2+1
        
                
        statement2 =  statement2 +  'From {}, {} to {}, {}. ({} miles)\nThe routes taken are: {} \n\n'.format(start_dest_capital, start_dest_state, end_dest_capital, end_dest_state, info[0],route_taken)

    statement = statement + 'Starting from {}, {} it takes approximately {} miles to travel through all 49 state capitals'.format(capitals[starting_captial][0], capitals[starting_captial][1], mileage)    
     
    statement = statement + statement2    
    output.insert(0.0,statement)
    but.config(state='disabled')
    but2.config(state='normal')

    
def clear_text():

    output.delete('1.0', END)
    but.config(state='normal')
    but2.config(state='disabled')

def quit():
    print("Have a great day! Goodbye :)")
    sys.exit(0)

    

l1 = Label(a,text="Enter State (abbreviate) you would like to start at:")
l1.place(x=25,y=35)    
    
#Entry field
ent=Entry(a,width=15,font=('Times 18'),textvar=textin,bg='white')
ent.place(x=30,y=60)

#Search button
but=Button(a, padx=1, pady=1, text='Start Trip', command=clk, bg='powder blue')
but.place(x=240,y=60)

#Clear button
but2=Button(a, padx=1, pady=1, text='Clear Text', command=clear_text, bg='powder blue')
but2.place(x=305,y=60)

#Exit button
btn3 = Button(a,padx=1,pady=1, text="Exit", command=quit, bg='powder blue')
btn3.place(x=375,y=60)              


#output field
output=Text(a,width=15,height=4,font=('Times 18'),fg="black")
output.place(x=30,y=120)
output = scrolledtext.ScrolledText(a,width=100,height=15,font=('Times 18'),fg="black")
output.place(x=30,y=120)


a.mainloop()

#OBS GUI

from tkinter import *




#input_amber.write(str(amber_count))

#input.write("0")

#Window
root = Tk()

#Modify Window
root.title("OBS Controller")
root.geometry("400x500")
bigfont = ('Arial Bold', 22)
font = ('Arial Bold', 18)







#Rounds


round_frame = Frame(root,padx=40)
round_frame.pack()

round_label = Label(round_frame, text = "Rounds", font=bigfont)
round_label.pack()




#Set Rounds to 1

def one_round_count():
	input_round = open('round.txt', 'w') 
	input_round.write("1")
sub_round = Button(round_frame, text= "Round 1", command=one_round_count)
sub_round.pack(side=TOP)



#+1 Round event

def add_round_count():
	input_round = open('round.txt', 'r') 
	temp_count = input_round.read();
	input_round.close();
	total_count = int(temp_count) + 1
	input_round = open('round.txt', 'w') 
	input_round.write(str(total_count))
add_round = Button(round_frame, text= "+ Round", command=add_round_count)
add_round.pack(side=LEFT)





#-1 Round event

def sub_round_count():
	input_round = open('round.txt', 'r') 
	temp_count = input_round.read();
	input_round.close();
	total_count = int(temp_count) - 1
	input_round = open('round.txt', 'w') 
	input_round.write(str(total_count))
sub_round = Button(round_frame, text= "- Round", command=sub_round_count)
sub_round.pack(side=LEFT)




#Player 1

p1_frame = Frame(root)
p1_frame.pack(side=LEFT)

p1_label = Label(p1_frame, text = "Player 1", font=bigfont, pady=20)
p1_label.pack()

#AEmber 

p1_amber_label = Label(p1_frame, text = "Amber", font=font)
p1_amber_label.pack()

p1_amber_frame = Frame(p1_frame)
p1_amber_frame.pack()




#Set Amber to 0

def zero_amber_p1():
	input_amber = open('p1_amber.txt', 'w') 
	input_amber.write("0")
p1_zero_amber = Button(p1_amber_frame, text= "0 AEmber", command=zero_amber_p1)
p1_zero_amber.pack()


#Steal Amber

def steal_amber_p1():
	input_amber = open('p1_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) + 1
	input_amber = open('p1_amber.txt', 'w') 
	input_amber.write(str(total_count))
	input_amber = open('p2_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) - 1
	input_amber = open('p2_amber.txt', 'w') 
	input_amber.write(str(total_count))
p1_zero_amber = Button(p1_amber_frame, text= "Steal AEmber", command=steal_amber_p1)
p1_zero_amber.pack()


#+1 Amber event

def add_amber_p1():
	input_amber = open('p1_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) + 1
	input_amber = open('p1_amber.txt', 'w') 
	input_amber.write(str(total_count))
p1_add_amber = Button(p1_amber_frame, text= "+ AEmber", command=add_amber_p1)
p1_add_amber.pack(side=LEFT)


#-1 Amber event

def sub_amber_p1():
	input_amber = open('p1_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) - 1
	input_amber = open('p1_amber.txt', 'w') 
	input_amber.write(str(total_count))
p1_sub_amber = Button(p1_amber_frame, text= "- AEmber", command=sub_amber_p1)
p1_sub_amber.pack(side=LEFT)





#Chains


p1_chain_label = Label(p1_frame, text = "Chains", font=font)
p1_chain_label.pack()

p1_chain_frame = Frame(p1_frame)
p1_chain_frame.pack()



#Set Chains to 0

def zero_chain_p1():
	input_chain = open('p1_chain.txt', 'w') 
	input_chain.write("0")
p1_zero_chain = Button(p1_chain_frame, text= "0 Chains",  command=zero_chain_p1)
p1_zero_chain.pack()



#+1 Chain event

def add_chain_p1():
	input_chain = open('p1_chain.txt', 'r') 
	temp_count = input_chain.read();
	input_chain.close();
	total_count = int(temp_count) + 1
	input_chain = open('p1_chain.txt', 'w') 
	input_chain.write(str(total_count))
p1_add_chain = Button(p1_chain_frame, text= "+ Chain",  command=add_chain_p1)
p1_add_chain.pack(side=LEFT)


#-1 Chain event

def sub_chain_p1():
	input_chain = open('p1_chain.txt', 'r') 
	temp_count = input_chain.read();
	input_chain.close();
	total_count = int(temp_count) - 1
	input_chain = open('p1_chain.txt', 'w') 
	input_chain.write(str(total_count))
p1_sub_chain = Button(p1_chain_frame, text= "- Chain",  command=sub_chain_p1)
p1_sub_chain.pack(side=LEFT)





#Keys

p1_key_label = Label(p1_frame, text = "Keys", font=font)
p1_key_label.pack()


p1_key_frame = Frame(p1_frame)
p1_key_frame.pack()



#Set keys to 0

def zero_key_p1():
	input_key = open('p1_key.txt', 'w') 
	input_key.write("0")
p1_zero_key = Button(p1_key_frame, text= "0 Keys",  command=zero_key_p1)
p1_zero_key.pack()


#+1 Key event

def add_key_p1():
	input_key = open('p1_key.txt', 'r') 
	temp_count = input_key.read();
	input_key.close();
	total_count = int(temp_count) + 1
	input_key = open('p1_key.txt', 'w') 
	input_key.write(str(total_count))
p1_add_key = Button(p1_key_frame, text= "+ Key",  command=add_key_p1)
p1_add_key.pack(side=LEFT)


#-1 key event

def sub_key_p1():
	input_key = open('p1_key.txt', 'r') 
	temp_count = input_key.read();
	input_key.close();
	total_count = int(temp_count) - 1
	input_key = open('p1_key.txt', 'w') 
	input_key.write(str(total_count))
p1_sub_key = Button(p1_key_frame, text= "- Key",  command=sub_key_p1)
p1_sub_key.pack(side=LEFT)




#Player 2

p2_frame = Frame(root)
p2_frame.pack(side=RIGHT)

p2_label = Label(p2_frame, text = "Player 2", font=bigfont, pady=20)
p2_label.pack()

#AEmber 

p2_amber_label = Label(p2_frame, text = "Amber", font=font)
p2_amber_label.pack()

p2_amber_frame = Frame(p2_frame)
p2_amber_frame.pack()




#Set Amber to 0

def zero_amber_p2():
	input_amber = open('p2_amber.txt', 'w') 
	input_amber.write("0")
p2_zero_amber = Button(p2_amber_frame, text= "0 AEmber", command=zero_amber_p2)
p2_zero_amber.pack()


#Steal Amber

def steal_amber_p2():
	input_amber = open('p2_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) + 1
	input_amber = open('p2_amber.txt', 'w') 
	input_amber.write(str(total_count))
	input_amber = open('p1_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) - 1
	input_amber = open('p1_amber.txt', 'w') 
	input_amber.write(str(total_count))
p2_zero_amber = Button(p2_amber_frame, text= "Steal AEmber", command=steal_amber_p2)
p2_zero_amber.pack()


#+1 Amber event

def add_amber_p2():
	input_amber = open('p2_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) + 1
	input_amber = open('p2_amber.txt', 'w') 
	input_amber.write(str(total_count))
p2_add_amber = Button(p2_amber_frame, text= "+ AEmber", command=add_amber_p2)
p2_add_amber.pack(side=LEFT)


#-1 Amber event

def sub_amber_p2():
	input_amber = open('p2_amber.txt', 'r') 
	temp_count = input_amber.read();
	input_amber.close();
	total_count = int(temp_count) - 1
	input_amber = open('p2_amber.txt', 'w') 
	input_amber.write(str(total_count))
p2_sub_amber = Button(p2_amber_frame, text= "- AEmber", command=sub_amber_p2)
p2_sub_amber.pack(side=LEFT)





#Chains


p2_chain_label = Label(p2_frame, text = "Chains", font=font)
p2_chain_label.pack()

p2_chain_frame = Frame(p2_frame)
p2_chain_frame.pack()



#Set Chains to 0

def zero_chain_p2():
	input_chain = open('p2_chain.txt', 'w') 
	input_chain.write("0")
p2_zero_chain = Button(p2_chain_frame, text= "0 Chains",  command=zero_chain_p2)
p2_zero_chain.pack()



#+1 Chain event

def add_chain_p2():
	input_chain = open('p2_chain.txt', 'r') 
	temp_count = input_chain.read();
	input_chain.close();
	total_count = int(temp_count) + 1
	input_chain = open('p2_chain.txt', 'w') 
	input_chain.write(str(total_count))
p2_add_chain = Button(p2_chain_frame, text= "+ Chain",  command=add_chain_p2)
p2_add_chain.pack(side=LEFT)


#-1 Chain event

def sub_chain_p2():
	input_chain = open('p2_chain.txt', 'r') 
	temp_count = input_chain.read();
	input_chain.close();
	total_count = int(temp_count) - 1
	input_chain = open('p2_chain.txt', 'w') 
	input_chain.write(str(total_count))
p2_sub_chain = Button(p2_chain_frame, text= "- Chain",  command=sub_chain_p2)
p2_sub_chain.pack(side=LEFT)





#Keys

p2_key_label = Label(p2_frame, text = "Keys", font=font)
p2_key_label.pack()


p2_key_frame = Frame(p2_frame)
p2_key_frame.pack()



#Set keys to 0

def zero_key_p2():
	input_key = open('p2_key.txt', 'w') 
	input_key.write("0")
p2_zero_key = Button(p2_key_frame, text= "0 Keys",  command=zero_key_p2)
p2_zero_key.pack()


#+1 Key event

def add_key_p2():
	input_key = open('p2_key.txt', 'r') 
	temp_count = input_key.read();
	input_key.close();
	total_count = int(temp_count) + 1
	input_key = open('p2_key.txt', 'w') 
	input_key.write(str(total_count))
p2_add_key = Button(p2_key_frame, text= "+ Key",  command=add_key_p2)
p2_add_key.pack(side=LEFT)


#-1 key event

def sub_key_p2():
	input_key = open('p2_key.txt', 'r') 
	temp_count = input_key.read();
	input_key.close();
	total_count = int(temp_count) - 1
	input_key = open('p2_key.txt', 'w') 
	input_key.write(str(total_count))
p2_sub_key = Button(p2_key_frame, text= "- Key",  command=sub_key_p2)
p2_sub_key.pack(side=LEFT)






#Event Loop
root.mainloop()




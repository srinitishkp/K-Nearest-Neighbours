#Function to predict label of theinput baed on KNN
def k_nearest_neighbours(input_pt,k):
    global data_dict
    distances=[]
    x=normalised_x_value(input_pt[0])
    y=normalised_y_value(input_pt[1])
    for key in data_dict.keys():
        point=data_dict[key]
        distance=(((x-point[0])**2)+((y-point[1])**2))**0.5
        distances.append((key,distance,point[2]))
    distances=sorted(distances,key=lambda x:x[1])
    k_n_neighbours=distances[:k]
    # print("K Nearest Neighbours :",k_n_neighbours)
    y,n=0,0
    for neighbour in k_n_neighbours:
        if(neighbour[2]=="Y"):
            y+=1
        else:
            n+=1
    if(y>n):
        return "Y"
    else:
        return "N"

#Function to perform min-max normalisation on a list of values
def min_max_normalistion(x):
    min_val=min(x)
    max_val=max(x)
    for i in range(len(x)):
        x[i]=((x[i]-min_val)/(max_val-min_val)) #(val-min/max-min)
    return min_val,max_val,x

#Function that returns the normalised x value
def normalised_x_value(x):
    global min_x,max_x
    return (x-min_x)/(max_x-min_x)

#Function that returns the normalised x value
def normalised_y_value(x):
    global min_y,max_y
    return (x-min_y)/(max_y-min_y)

data_file=open("knnData.txt","r")
temp_data=data_file.readlines()
min_x,max_x,min_y,max_y=0,0,0,0
data_dict={}
indices,x,y,labels=[],[],[],[]
for line in temp_data:
    point=line.split(',')
    indices.append(int(point[0]))
    labels.append(point[3][1])
    x.append(int(point[1]))
    y.append(int(point[2]))
min_x,max_x,x=min_max_normalistion(x)
min_y,max_y,y=min_max_normalistion(y)
for i in range(len(indices)):
    data_dict[indices[i]]=(x[i],y[i],labels[i])

input_file=open("input.txt","r")
temp_ip=input_file.readlines()
input_pts=[]
for line in temp_ip:
    input_pts.append(list(map(int,line.split(','))))
k=int(input("Enter K:"))
i=0
for input_pt in input_pts:
    print(f"Test case {i+1}:\n X:{input_pt[0]} \n Y:{input_pt[1]} \n Predicted label : {k_nearest_neighbours(input_pt,k)}")
    i+=1
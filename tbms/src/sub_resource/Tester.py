import ResourceManager

item = "ReferenceMaterial"
item2 = "Survey"
""""tests items in resource manager (item,id,op,file) """
res1 = ResourceManager.signalCRD_item(item,100,1,'Test.txt')
surv= ResourceManager.signalCRD_item(item2,200,1,"pathname")
print(res1)
print(surv)

res = ResourceManager.signalCRD_item(item,100,2,"path")
surv = ResourceManager.signalCRD_item(item2,200,2,"path")


res = ResourceManager.signalCRD_item(item,100,3,"path")
surv = ResourceManager.signalCRD_item(item2,200,3,"path")

with open(res1.file) as file_object:
    for line in file_object:
        print(line)

ResourceManager.signalUpload(100,"Alakazam",res1.file)